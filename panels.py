# <pep8-80 compliant>


import bpy

from . import operators


class MH2UE_PT_Import(bpy.types.Panel):
    bl_label = "Import"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "mh2ue"

    def draw(self, context):
        layout = self.layout
        props = context.scene.mh2ue_prop

        layout.prop(
            props,
            "bool1",
            text="Delete all objects")
        layout.prop(
            props,
            "bool2",
            text="Set the unit scale to 0.01")
        layout.prop(
            props,
            "bool3",
            text="Set Blender unit equals of makehuman add-on to Centimeter")
        layout.prop(
            props,
            "bool4",
            text="Press the Import human button on makehuman add-on")
        layout.prop(
            props,
            "bool5",
            text="Press the Separate Eyes button on makehuman add-on")
        layout.prop(
            props,
            "bool6",
            text="Changed the object name of armature to \"Armature\"")
        layout.prop(
            props,
            "bool7",
            text="Change bone vector for Unreal Engine")
        layout.operator(
            operators.MH2UE_OT_Import.bl_idname,
            text=bpy.app.translations.pgettext("Import"))


class MH2UE_PT_UEeye(bpy.types.Panel):
    bl_label = "Use Unreal Engine eyes"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "mh2ue"

    def draw(self, context):
        layout = self.layout
        props = context.scene.mh2ue_prop

        layout.prop(
            props,
            "str1",
            text="File path")
        layout.prop(
            props,
            "float1",
            text="Scale")
        layout.label(text="Bone to apply weight")
        layout.prop(
            props,
            "str2",
            text="Left eye")
        layout.prop(
            props,
            "str3",
            text="Right eye")
        layout.prop(
            props,
            "bool8",
            text="Delete makehuman eyes")
        layout.operator(
            operators.MH2UE_OT_UEeye.bl_idname,
            text=bpy.app.translations.pgettext("Use Unreal Engine eyes"))


class MH2UE_PT_Export(bpy.types.Panel):
    bl_label = "Export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "mh2ue"

    def draw(self, context):
        layout = self.layout
        props = context.scene.mh2ue_prop

        layout.prop(
            props,
            "str4",
            text="Folder")
        layout.prop(
            props,
            "str5",
            text="File name")
        layout.prop(
            props,
            "bool9",
            text="Limit to selected objects")
        layout.operator(
            operators.MH2UE_OT_Export.bl_idname,
            text=bpy.app.translations.pgettext("Export in FBX format"))
