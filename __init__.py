# <pep8-80 compliant>

import bpy
from bpy.props import (
    BoolProperty,
    StringProperty,
)

from . import mh2ueaddon
from . import fbxexport
from .translation import jajp


bl_info = {
    "name": "mh2ue add-on",
    "author": "Sandy",
    "version": (2021, 1, 10),
    "blender": (2, 90, 0),
    "location": "View3D > Sidebar",
    "description":
        "Convert characters created with makehuman for Unreal Engine",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "https://github.com/Sandy10000/mh2ueaddon",
    "tracker_url": "https://github.com/Sandy10000/mh2ueaddon/issues",
    "category": "MakeHuman"
}


translation_dict = {
    "ja_JP": jajp.dic,
}


class MH2UE_OT_Run(bpy.types.Operator):
    bl_idname = "mh2ue.run"
    bl_label = "mh2ue.run"
    bl_description = "run"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        scene = context.scene
        if scene.mh2ue_prop_bool1:
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.delete()
        if scene.mh2ue_prop_bool2:
            scene.unit_settings.scale_length = 0.01
        if scene.mh2ue_prop_bool3:
            scene.MhScaleMode = "CENTIMETER"
        if scene.mh2ue_prop_bool4:
            bpy.ops.mh_community.import_body()
        if scene.mh2ue_prop_bool5:
            bpy.data.objects["human"].name = "Armature"
        if scene.mh2ue_prop_bool6:
            mh2ueaddon.mh2ue()
        if scene.mh2ue_prop_bool7:
            filepath = scene.mh2ue_prop_str1\
                     + scene.mh2ue_prop_str2\
                     + ".fbx"
            fbxexport.fbx_export(filepath, scene.mh2ue_prop_bool8)
        return {"FINISHED"}


class MH2UE_PT_Panel(bpy.types.Panel):
    bl_label = "mh2ue ver. %d.%d.%d" % bl_info["version"]
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "mh2ue"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(
            scene,
            "mh2ue_prop_bool1",
            text="Delete all objects")
        layout.prop(
            scene,
            "mh2ue_prop_bool2",
            text="Set the unit scale to 0.01")
        layout.prop(
            scene,
            "mh2ue_prop_bool3",
            text="Set Blender unit equals of makehuman add-on to Centimeter")
        layout.prop(
            scene,
            "mh2ue_prop_bool4",
            text="Press the Import human button on makehuman add-on")
        layout.prop(
            scene,
            "mh2ue_prop_bool5",
            text="Changed the object name of Armature to \"Armature\"")
        layout.prop(
            scene,
            "mh2ue_prop_bool6",
            text="Change bone vector for Unreal Engine")
        layout.prop(
            scene,
            "mh2ue_prop_bool7",
            text="Export in FBX format")
        row = layout.row()
        box = row.box()
        box_row = box.row()
        box_column = box_row.column()
        box_column.prop(
            scene,
            "mh2ue_prop_str1",
            text="Folder")
        box_column.separator()
        box_column.prop(
            scene,
            "mh2ue_prop_str2",
            text="File name")
        box_column.separator()
        box_column.prop(
            scene,
            "mh2ue_prop_bool8",
            text="Limit to selected objects")
        layout.operator(
            MH2UE_OT_Run.bl_idname,
            text=bpy.app.translations.pgettext("run"))


def init_props():
    scene = bpy.types.Scene
    scene.mh2ue_prop_bool1 = BoolProperty(
        default=True)
    scene.mh2ue_prop_bool2 = BoolProperty(
        default=True)
    scene.mh2ue_prop_bool3 = BoolProperty(
        default=True)
    scene.mh2ue_prop_bool4 = BoolProperty(
        default=True)
    scene.mh2ue_prop_bool5 = BoolProperty(
        default=True)
    scene.mh2ue_prop_bool6 = BoolProperty(
        default=True)
    scene.mh2ue_prop_bool7 = BoolProperty(
        default=True)
    scene.mh2ue_prop_bool8 = BoolProperty(
        default=False)
    scene.mh2ue_prop_str1 = StringProperty(
        subtype='DIR_PATH')
    scene.mh2ue_prop_str2 = StringProperty(
        default="SK_Makehuman")


def clear_props():
    scene = bpy.types.Scene
    del scene.mh2ue_prop_bool1
    del scene.mh2ue_prop_bool2
    del scene.mh2ue_prop_bool3
    del scene.mh2ue_prop_bool4
    del scene.mh2ue_prop_bool5
    del scene.mh2ue_prop_bool6
    del scene.mh2ue_prop_bool7
    del scene.mh2ue_prop_bool8
    del scene.mh2ue_prop_str1
    del scene.mh2ue_prop_str2


classes = [
    MH2UE_OT_Run,
    MH2UE_PT_Panel,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    init_props()
    bpy.app.translations.register(__name__, translation_dict)


def unregister():
    bpy.app.translations.unregister(__name__)
    clear_props()
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == '__main__':
    register()
