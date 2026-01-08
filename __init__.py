# __init__.py
bl_info = {
    "name": "ResoBlending",
    "author": "Alex_2Pi",
    "version": (0, 1, 0),
    "blender": (3, 6, 0),
    "category": "3D View",
}

import bpy
from . import properties, operators, ui_panel

classes = (
    operators.RESO_OT_connect,
    operators.RESO_OT_disconnect,
    ui_panel.VIEW3D_PT_reso_connection,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    properties.register_properties()


def unregister():
    properties.unregister_properties()
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
