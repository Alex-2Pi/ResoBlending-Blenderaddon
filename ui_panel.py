import bpy

# ------------------ PROPERTIES ------------------

def register_properties():
    bpy.types.Scene.socket_host = bpy.props.StringProperty(
        name="Host",
        default="127.0.0.1"
    )

    bpy.types.Scene.socket_port = bpy.props.IntProperty(
        name="Port",
        default=5000,
        min=1,
        max=65535
    )

    bpy.types.Scene.socket_connected = bpy.props.BoolProperty(
        name="Connected",
        default=False
    )

    bpy.types.Scene.socket_status = bpy.props.StringProperty(
        name="Status",
        default="Disconnected"
    )

# ------------------ OPERATORS ------------------

class MY_OT_connect(bpy.types.Operator):
    bl_idname = "my.socket_connect"
    bl_label = "Connect"

    def execute(self, context):
        scene = context.scene
        scene.socket_connected = True
        scene.socket_status = "Connected"
        return {'FINISHED'}


class MY_OT_disconnect(bpy.types.Operator):
    bl_idname = "my.socket_disconnect"
    bl_label = "Disconnect"

    def execute(self, context):
        scene = context.scene
        scene.socket_connected = False
        scene.socket_status = "Disconnected"
        return {'FINISHED'}

# ------------------ PANEL ------------------

class VIEW3D_PT_socket_ui(bpy.types.Panel):
    bl_label = "Resonite_Connection"
    bl_idname = "VIEW3D_PT_socket_ui"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ResoBlending'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(scene, "socket_host")
        layout.prop(scene, "socket_port")

        if scene.socket_connected:
            layout.operator("my.socket_disconnect", icon='CANCEL')
        else:
            layout.operator("my.socket_connect", icon='LINKED')

        box = layout.box()
        icon = 'CHECKMARK' if scene.socket_connected else 'ERROR'
        box.label(text=scene.socket_status, icon=icon)

# ------------------ REGISTER ------------------

classes = (
    MY_OT_connect,
    MY_OT_disconnect,
    VIEW3D_PT_socket_ui,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    register_properties()

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.socket_host
    del bpy.types.Scene.socket_port
    del bpy.types.Scene.socket_connected
    del bpy.types.Scene.socket_status


if __name__ == "__main__":
    register()
