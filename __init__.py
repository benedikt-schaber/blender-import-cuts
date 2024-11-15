import bpy
import os
import math

from bpy.props import StringProperty, FloatProperty
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator

bl_info = {
    "name": "Import SVG Cuts Directory",
    "description": "Import object based on a directory of SVG cuts",
    "author": "Benedikt Schaber",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "location": "File > Import > SVG Cuts Directory",
    "category": "Import-Export",
}


class IMPORT_OT_svg_cuts_directory(Operator, ImportHelper):
    """Import object based on a directory of SVG cuts"""

    bl_idname = "import_files.svg_cuts_directory"
    bl_label = "Import SVG Cuts Directory"
    bl_options = {"REGISTER", "UNDO"}

    filter_glob: StringProperty(default="*.svg;*.SVG", options={"HIDDEN"})

    distance: FloatProperty(
        name="Distance Between Cuts",
        description="Distance between successive cuts",
        default=0.1,
        precision=2,
    )
    extrude: FloatProperty(
        name="Extrusion Distance",
        description="Extrusion depth of each cut, usually 0.5 * distance",
        default=0.05,
        precision=2,
    )

    directory: StringProperty(
        name="Folder Path", description="Select Folder", default="", subtype="DIR_PATH"
    )

    def execute(self, context):
        folder_path = self.directory
        print(folder_path)

        if not os.path.isdir(folder_path):
            self.report({"ERROR"}, "Invalid folder path")
            return {"CANCELLED"}

        svg_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".svg")]

        if not svg_files:
            self.report({"INFO"}, "No SVG files found in directory")
            return {"FINISHED"}

        svg_files.sort()

        print(f"Found {len(svg_files)} SVG files: {svg_files}")

        for i, svg_file in enumerate(svg_files):
            svg_path = os.path.join(folder_path, svg_file)
            print(f"Importing SVG: {svg_path}")

            existing_objects = set(bpy.data.objects)
            bpy.ops.import_curve.svg(filepath=svg_path)
            new_objects = set(bpy.data.objects) - existing_objects

            if len(new_objects) == 0:
                continue

            bpy.ops.object.select_all(action="DESELECT")
            new_objects = list(new_objects)
            aobj = new_objects[0]
            for obj in new_objects:
                obj.select_set(True)
            context.view_layer.objects.active = aobj
            bpy.ops.object.join()
            bpy.ops.object.select_all(action="DESELECT")

            aobj.location = (i * self.distance, 0.0, 0.0)
            aobj.rotation_euler = (math.pi / 2, 0.0, math.pi / 2)
            aobj.data.extrude = self.extrude

        context.view_layer.update()
        return {"FINISHED"}


def menu_func_import(self, context):
    self.layout.operator(
        IMPORT_OT_svg_cuts_directory.bl_idname, text="SVG Cuts Directory (*.svg)"
    )


def register():
    bpy.utils.register_class(IMPORT_OT_svg_cuts_directory)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    bpy.utils.unregister_class(IMPORT_OT_svg_cuts_directory)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
    register()
