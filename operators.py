# operators.py
# Blender logic layer
import bpy
from . import socket_client


def socket_timer():
    scene = bpy.context.scene
    msg = socket_client.pop_message()

    if msg:
        scene.socket_status = f"Received: {msg}"

    return 0.2


class RESO_OT_connect(bpy.types.Operator):
    bl_idname = "reso.connect"
    bl_label = "Connect"

    def execute(self, context):
        scene = context.scene

        socket_client.start_client(
            scene.socket_host,
            scene.socket_port
        )

        scene.socket_connected = True
        scene.socket_status = "Connecting..."

        bpy.app.timers.register(socket_timer)
        return {'FINISHED'}


class RESO_OT_disconnect(bpy.types.Operator):
    bl_idname = "reso.disconnect"
    bl_label = "Disconnect"

    def execute(self, context):
        socket_client.stop_client()

        scene = context.scene
        scene.socket_connected = False
        scene.socket_status = "Disconnected"
        return {'FINISHED'}

