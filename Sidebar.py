import bpy


class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the View3D > Sidebar"""
    bl_label = "Mój Panel"
    bl_idname = "VIEW3D_PT_my_custom_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'MyTools'  # nazwa zakładki w N-panelu

    def draw(self, context):
        layout = self.layout
        layout.label(text="Hello Blender!")
        layout.operator("mesh.primitive_cube_add", text="Dodaj Cube")
        
        obj = context.object

        row = layout.row()
        row.label(text="Hello world!", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")

        row = layout.row()
        row.operator("mesh.primitive_cube_add")


def register():
    bpy.utils.register_class(HelloWorldPanel)


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)


if __name__ == "__main__":
    register()
