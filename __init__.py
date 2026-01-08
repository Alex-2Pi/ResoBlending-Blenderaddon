bl_info = {
    "name": "ResoBlending",
    "author": "Alex_2Pi",
    "version": (0, 1, 0),
    "blender": (4, 0, 0),
    "category": "3D View",
}

import bpy

# Import modules explicitly
from . import properties
from . import operators
from . import ui_panel

classes = (
    operators.RESO_OT_connect,
    operators.RESO_OT_disconnect,
    ui_panel.VIEW3D_PT_reso_connection,
)


def register():
    properties.register_properties()

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    properties.unregister_properties()
