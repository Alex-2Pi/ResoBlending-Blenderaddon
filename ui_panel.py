import bpy


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
