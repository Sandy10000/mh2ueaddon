# <pep8-80 compliant>


import bpy
import mathutils

from . import mh2ueaddon
from . import fbx


class MH2UE_OT_Import(bpy.types.Operator):
    bl_idname = "mh2ue.import"
    bl_label = "mh2ue.import"
    bl_description = "import"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        scene = context.scene
        props = scene.mh2ue_prop
        if props.import_b1:
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.delete()
        if props.import_b2:
            scene.unit_settings.scale_length = 0.01
        if props.import_b3:
            scene.MhScaleMode = "CENTIMETER"
        if props.import_b4:
            bpy.ops.mh_community.import_body()
        if props.import_b5:
            bpy.context.view_layer.objects.active\
                = bpy.data.objects["human.HighPolyEyes"]
            bpy.ops.mh_community.separate_eyes()
        if props.import_b6:
            bpy.data.objects["human"].name = "Armature"
        if props.import_b7:
            mh2ueaddon.mh2ue()
        bpy.context.scene.cursor.location = (0, 0, 0)
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.view_layer.objects.active = bpy.data.objects["Armature"]
        bpy.data.objects["Armature"].select_set(True)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        return {"FINISHED"}


class MH2UE_OT_Bone(bpy.types.Operator):
    bl_idname = "mh2ue.bone"
    bl_label = "mh2ue.bone"
    bl_description = "Add bone"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.view_layer.objects.active = bpy.data.objects["Armature"]
        bpy.ops.object.mode_set(mode='EDIT')

        props = context.scene.mh2ue_prop
        if props.bone_tw_ll:
            MH2UE_OT_Bone._addbone(self, 0)
        if props.bone_tw_ul:
            MH2UE_OT_Bone._addbone(self, 1)
        if props.bone_tw_lr:
            MH2UE_OT_Bone._addbone(self, 2)
        if props.bone_tw_ur:
            MH2UE_OT_Bone._addbone(self, 3)
        if props.bone_tw_cl:
            MH2UE_OT_Bone._addbone(self, 4)
        if props.bone_tw_tl:
            MH2UE_OT_Bone._addbone(self, 5)
        if props.bone_tw_cr:
            MH2UE_OT_Bone._addbone(self, 6)
        if props.bone_tw_tr:
            MH2UE_OT_Bone._addbone(self, 7)
        if props.bone_ik_froot:
            MH2UE_OT_Bone._addbone(self, 8)
        if props.bone_ik_fl:
            MH2UE_OT_Bone._addbone(self, 9)
        if props.bone_ik_fr:
            MH2UE_OT_Bone._addbone(self, 10)
        if props.bone_ik_hroot:
            MH2UE_OT_Bone._addbone(self, 11)
        if props.bone_ik_hg:
            MH2UE_OT_Bone._addbone(self, 12)
        if props.bone_ik_hl:
            MH2UE_OT_Bone._addbone(self, 13)
        if props.bone_ik_hr:
            MH2UE_OT_Bone._addbone(self, 14)
        bpy.ops.object.mode_set(mode='OBJECT')
        return {"FINISHED"}

    def _addbone(self, index):
        bones = [
            ("lowerarm_twist_01_l",
                "lowerarm_l",
                (47.3235, 5.903, 118.782),
                0.1000,
                (51.958, 24.1038, 110.5971),
                0.0500,
                0.6921,
                20.4876,
                0.2500),
            ("upperarm_twist_01_l",
                "upperarm_l",
                (18.0226, 9.7473, 149.1498),
                0.1000,
                (16.9733, 25.1207, 149.7254),
                0.0500,
                0.8667,
                15.4200,
                0.2500),
            ("lowerarm_twist_01_r",
                "lowerarm_r",
                (-47.3235, 5.903, 118.7821),
                0.1000,
                (-45.9653, -11.0129, 130.2603),
                0.0500,
                0.9821,
                20.4876,
                0.2500),
            ("upperarm_twist_01_r",
                "upperarm_r",
                (-18.0226, 9.7472, 149.1499),
                0.1000,
                (-23.0146, -4.5578, 152.0177),
                0.0500,
                -1.2448,
                15.4200,
                0.2500),
            ("calf_twist_01_l",
                "calf_l",
                (15.674, 4.9968, 32.8937),
                0.1000,
                (13.5435, 34.8359, 37.9342),
                0.0500,
                -1.6509,
                30.3367,
                0.2500),
            ("thigh_twist_01_l",
                "thigh_l",
                (11.7108, 1.1901, 73.3817),
                0.1000,
                (9.9577, 33.466, 74.1692),
                0.0500,
                -1.6942,
                32.3331,
                0.2500),
            ("calf_twist_01_r",
                "calf_r",
                (-15.674, 4.9968, 32.8935),
                0.1000,
                (-17.8044, -24.8424, 27.853),
                0.0500,
                -0.8511,
                30.3369,
                0.2500),
            ("thigh_twist_01_r",
                "thigh_r",
                (-11.7108, 1.19, 73.3819),
                0.1000,
                (-13.4638, -31.086, 72.5944),
                0.0500,
                0.6029,
                32.3333,
                0.2500),
            ("ik_foot_root",
                "Root",
                (0.0, 0.0, 0.0),
                0.1000,
                (0.0, 23.1966, 0.0),
                0.0500,
                0.0000,
                23.1966,
                0.2500),
            ("ik_foot_l",
                "ik_foot_root",
                (17.0763, 8.0721, 13.4657),
                0.1000,
                (16.0163, 31.2428, 13.7466),
                0.0500,
                -1.5859,
                23.1966,
                0.2500),
            ("ik_foot_r",
                "ik_foot_root",
                (-17.0763, 8.0721, 13.4656),
                0.1000,
                (-18.1363, -15.0985, 13.1848),
                0.0500,
                1.0377,
                23.1966,
                0.2500),
            ("ik_hand_root",
                "Root",
                (0.0, 0.0, 0.0),
                0.1000,
                (0.0, 125.2248, 0.0),
                0.0500,
                0.0000,
                125.2248,
                0.2500),
            ("ik_hand_gun",
                "ik_hand_root",
                (-56.6461, 0.3354, 111.6797),
                0.1000,
                (-91.4471, -3.562, 156.2047),
                0.0500,
                -0.2042,
                56.6460,
                0.2500),
            ("ik_hand_l",
                "ik_hand_gun",
                (56.646, 0.3355, 111.6797),
                0.1000,
                (21.8451, 4.2329, 67.1546),
                0.0500,
                1.1227,
                56.6461,
                0.2500),
            ("ik_hand_r",
                "ik_hand_gun",
                (-56.6461, 0.3354, 111.6797),
                0.1000,
                (-91.4471, -3.562, 156.2047),
                0.0500,
                -0.2042,
                56.6460,
                0.2500),
        ]
        bone = bpy.context.object.data.edit_bones.new(bones[index][0])
        bone.parent = bpy.context.object.data.edit_bones[bones[index][1]]
        bone.head = bones[index][2]
        bone.head_radius = bones[index][3]
        bone.tail = bones[index][4]
        bone.tail_radius = bones[index][5]
        bone.roll = bones[index][6]
        bone.length = bones[index][7]
        bone.envelope_distance = bones[index][8]
        return {"FINISHED"}


class MH2UE_OT_UEeye(bpy.types.Operator):
    bl_idname = "mh2ue.ueeye"
    bl_label = "mh2ue.ueeye"
    bl_description = "ueeye"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT')
        props = context.scene.mh2ue_prop
        mh_eye_L = "human.HighPolyEyes_L"
        mh_eye_R = "human.HighPolyEyes_R"
        ue_eye_L = "SKM_Eye_00"
        ue_eye_R = "SKM_Eye_00.001"
        default_dimensions = mathutils.Vector(
            (3.090881824493408, 2.3374056816101074, 2.9753799438476562))
        dimensions = bpy.data.objects[mh_eye_L].dimensions
        scale = mathutils.Vector()
        scale.x = dimensions.x / default_dimensions.x
        scale.y = dimensions.y / default_dimensions.y
        scale.z = dimensions.z / default_dimensions.z
        fbx.fbx_import(props.eye_s1, props.eye_f1)
        bpy.context.view_layer.objects.active = bpy.data.objects[ue_eye_L]
        index = bpy.data.collections.find("human") + 1
        bpy.ops.object.move_to_collection(collection_index=index)
        bpy.ops.object.duplicate()
        loc_eye_l = bpy.data.objects[mh_eye_L].location\
            + mathutils.Vector((0, 0.3 * scale.y, 0))
        loc_eye_r = loc_eye_l * mathutils.Vector((-1, 1, 1))
        MH2UE_OT_UEeye._seteye(
            self, loc_eye_l, scale * props.eye_f1, ue_eye_L, props.eye_s2)
        MH2UE_OT_UEeye._seteye(
            self, loc_eye_r, scale * props.eye_f1, ue_eye_R, props.eye_s3)
        if props.eye_b1:
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects[mh_eye_L].select_set(True)
            bpy.data.objects[mh_eye_R].select_set(True)
            bpy.ops.object.delete(use_global=True)
        return {"FINISHED"}

    def _seteye(self, loc_eye, scale, ueeye, bone):
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[ueeye].location = loc_eye
        bpy.data.objects[ueeye].scale = scale
        bpy.context.view_layer.objects.active = bpy.data.objects["Armature"]
        bpy.data.objects[ueeye].select_set(True)
        bpy.ops.object.parent_set(type='ARMATURE_NAME')
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.view_layer.objects.active = bpy.data.objects[ueeye]
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        index = bpy.data.objects[ueeye].vertex_groups[bone].index
        bpy.data.objects[ueeye].vertex_groups.active_index = index
        bpy.ops.object.vertex_group_assign()
        bpy.ops.object.vertex_group_lock(action='LOCK', mask='SELECTED')
        bpy.ops.object.vertex_group_remove(all_unlocked=True)
        bpy.ops.object.mode_set(mode='OBJECT')
        return {"FINISHED"}


class MH2UE_OT_Export(bpy.types.Operator):
    bl_idname = "mh2ue.export"
    bl_label = "mh2ue.export"
    bl_description = "export"
    bl_options = {"REGISTER"}

    def execute(self, context):
        props = context.scene.mh2ue_prop
        filepath = props.export_s1 + props.export_s2 + ".fbx"
        fbx.fbx_export(filepath, props.export_b1)
        return {"FINISHED"}
