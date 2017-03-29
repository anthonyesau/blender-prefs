bl_info = {
    "name": "AE Blender Preferences",
    "description": "A simple add-on to update Anthony's preferences for Blender settings.",
    "author": "Anthony Esau",
    "version": (0, 0, 1),
    "blender": (2, 78, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "System"}

import bpy
import os
from sys import platform


url = "https://github.com/anthonyesau/blender-prefs/archive/master.zip"

script_file = os.path.realpath(__file__)
directory = os.path.dirname(script_file)

user_path = bpy.utils.resource_path('USER')
config_path = os.path.join(user_path, "config")


class downloadAEPrefs(bpy.types.Operator):
    "Download and install AE Blender Preferences. Restart Blender when it's done"
    bl_idname='ae_prefs.get'
    bl_label='Install AE Preferences'

    def execute(self,context):

        print (directory)

        print (user_path)
        print (config_path)

        return {'FINISHED'}



class ThisAddonPreferences(bpy.types.AddonPreferences):
    # this must match the addon name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __name__

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        row = col.row()
        row.scale_y=1.5
        row.alignment = 'CENTER'
        row.operator('ae_prefs.get', icon='FILE_REFRESH')
        row = col.row()
        row.alignment = 'CENTER'
        row.label("Please restart Blender when it's done")


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
