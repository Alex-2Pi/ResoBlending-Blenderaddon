# ui_panel.py
import bpy


class VIEW3D_PT_reso_connection(bpy.types.Panel):
    bl_label = "Resonite Connection"
    bl_idname = "VIEW3D_PT_reso_connection"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ResoBlending'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        col = layout.column()
        col.enabled = not scene.socket_connected
        col.prop(scene, "socket_host")
        col.prop(scene, "socket_port")

        if scene.socket_connected:
            layout.operator("reso.disconnect", icon='CANCEL')
        else:
            layout.operator("reso.connect", icon='LINKED')

        box = layout.box()
        icon = 'CHECKMARK' if scene.socket_connected else 'ERROR'
        box.label(text=scene.socket_status, icon=icon)
