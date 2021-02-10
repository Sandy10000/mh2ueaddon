# <pep8-80 compliant>


import bpy

from . import operators


class MH2UE_PT:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "mh2ue"


class MH2UE_PT_Import(MH2UE_PT, bpy.types.Panel):
    bl_label = "Import"

    def draw(self, context):
        layout = self.layout
        props = context.scene.mh2ue_prop

        layout.prop(
            props,
            "import_b1",
            text="Delete all objects")
        layout.prop(
            props,
            "import_b2",
            text="Set the unit scale to 0.01")
        layout.prop(
            props,
            "import_b3",
            text="Set Blender unit equals of makehuman add-on to Centimeter")
        layout.prop(
            props,
            "import_b4",
            text="Press the Import human button on makehuman add-on")
        layout.prop(
            props,
            "import_b5",
            text="Press the Separate Eyes button on makehuman add-on")
        layout.prop(
            props,
            "import_b6",
            text="Changed the object name of armature to \"Armature\"")
        layout.prop(
            props,
            "import_b7",
            text="Change bone vector for Unreal Engine")
        layout.label(text="Collections")
        layout.prop(
            props,
            "import_s1",
            text="armature")
        layout.prop(
            props,
            "import_s2",
            text="mesh")
        layout.operator(
            operators.MH2UE_OT_Import.bl_idname,
            text=bpy.app.translations.pgettext("Import"))


class MH2UE_PT_Bone(MH2UE_PT, bpy.types.Panel):
    bl_label = "Add bones"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        props = context.scene.mh2ue_prop

        layout.prop(
            props,
            "bone_tw_ll",
            text="lowerarm_twist_01_l")
        layout.prop(
            props,
            "bone_tw_ul",
            text="upperarm_twist_01_l")
        layout.prop(
            props,
            "bone_tw_lr",
            text="lowerarm_twist_01_r")
        layout.prop(
            props,
            "bone_tw_ur",
            text="upperarm_twist_01_r")
        layout.prop(
            props,
            "bone_tw_cl",
            text="calf_twist_01_l")
        layout.prop(
            props,
            "bone_tw_tl",
            text="thigh_twist_01_l")
        layout.prop(
            props,
            "bone_tw_cr",
            text="calf_twist_01_r")
        layout.prop(
            props,
            "bone_tw_tr",
            text="thigh_twist_01_r")
        layout.prop(
            props,
            "bone_ik_froot",
            text="ik_foot_root")
        row = layout.row()
        row.separator()
        row.prop(
            props,
            "bone_ik_fl",
            text="ik_foot_l")
        row = layout.row()
        row.separator()
        row.prop(
            props,
            "bone_ik_fr",
            text="ik_foot_r")
        layout.prop(
            props,
            "bone_ik_hroot",
            text="ik_hand_root")
        row = layout.row()
        row.separator()
        row.prop(
            props,
            "bone_ik_hg",
            text="ik_hand_gun")
        row = layout.row()
        row.separator(factor=3)
        row.prop(
            props,
            "bone_ik_hl",
            text="ik_hand_l")
        row = layout.row()
        row.separator(factor=3)
        row.prop(
            props,
            "bone_ik_hr",
            text="ik_hand_r")
        layout.operator(
            operators.MH2UE_OT_Bone.bl_idname,
            text=bpy.app.translations.pgettext("Add bones"))


class MH2UE_PT_UEeye(MH2UE_PT, bpy.types.Panel):
    bl_label = "Use Unreal Engine eyes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        props = context.scene.mh2ue_prop

        layout.prop(
            props,
            "eye_s1",
            text="File path")
        layout.prop(
            props,
            "eye_f1",
            text="Scale")
        layout.label(text="Bone to apply weight")
        layout.prop(
            props,
            "eye_s2",
            text="Left eye")
        layout.prop(
            props,
            "eye_s3",
            text="Right eye")
        layout.prop(
            props,
            "eye_b1",
            text="Delete makehuman eyes")
        layout.operator(
            operators.MH2UE_OT_UEeye.bl_idname,
            text=bpy.app.translations.pgettext("Use Unreal Engine eyes"))


class MH2UE_PT_Export(MH2UE_PT, bpy.types.Panel):
    bl_label = "Export"

    def draw(self, context):
        layout = self.layout
        props = context.scene.mh2ue_prop

        layout.prop(
            props,
            "export_s1",
            text="Folder")
        layout.prop(
            props,
            "export_s2",
            text="File name")
        layout.prop(
            props,
            "export_b1",
            text="Limit to selected objects")
        layout.operator(
            operators.MH2UE_OT_Export.bl_idname,
            text=bpy.app.translations.pgettext("Export in FBX format"))
