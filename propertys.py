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
