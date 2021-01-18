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
        if props.bool1:
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.delete()
        if props.bool2:
            scene.unit_settings.scale_length = 0.01
        if props.bool3:
            scene.MhScaleMode = "CENTIMETER"
        if props.bool4:
            bpy.ops.mh_community.import_body()
        if props.bool5:
            bpy.ops.mh_community.separate_eyes()
        if props.bool6:
            bpy.data.objects["human"].name = "Armature"
        if props.bool7:
            mh2ueaddon.mh2ue()
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
        fbx.fbx_import(props.str1, props.float1)
        bpy.context.view_layer.objects.active = bpy.data.objects[ue_eye_L]
        index = bpy.data.collections.find("human") + 1
        bpy.ops.object.move_to_collection(collection_index=index)
        bpy.ops.object.duplicate()
        loc_eye_l = bpy.data.objects[mh_eye_L].location\
            + mathutils.Vector((0, 0.3 * scale.y, 0))
        loc_eye_r = loc_eye_l * mathutils.Vector((-1, 1, 1))
        MH2UE_OT_UEeye._seteye(
            self, loc_eye_l, scale * props.float1, ue_eye_L, props.str2)
        MH2UE_OT_UEeye._seteye(
            self, loc_eye_r, scale * props.float1, ue_eye_R, props.str3)
        if props.bool8:
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
        filepath = props.str4 + props.str5 + ".fbx"
        fbx.fbx_export(filepath, props.bool9)
        return {"FINISHED"}
