# <pep8-80 compliant>

import bpy


def fbx_import(filepath, global_scale):
    bpy.ops.import_scene.fbx(
        filepath=filepath,
        directory="",
        filter_glob="*.fbx",
        ui_tab='MAIN',
        use_manual_orientation=False,
        global_scale=global_scale,
        bake_space_transform=False,
        use_custom_normals=True,
        use_image_search=True,
        use_alpha_decals=False,
        decal_offset=0.0,
        use_anim=True,
        anim_offset=1.0,
        use_subsurf=False,
        use_custom_props=True,
        use_custom_props_enum_as_string=True,
        ignore_leaf_bones=False,
        force_connect_children=False,
        automatic_bone_orientation=False,
        primary_bone_axis='Y',
        secondary_bone_axis='X',
        use_prepost_rot=True,
        axis_forward='-Z',
        axis_up='Y'
    )
    return


def fbx_export(filepath, use_selection):
    bpy.ops.export_scene.fbx(
        filepath=filepath,
        check_existing=True,
        filter_glob='*.fbx',
        use_selection=use_selection,
        use_active_collection=False,
        global_scale=1.0,
        apply_unit_scale=True,
        apply_scale_options='FBX_SCALE_NONE',
        bake_space_transform=False,
        object_types={'ARMATURE', 'MESH'},
        use_mesh_modifiers=True,
        use_mesh_modifiers_render=True,
        mesh_smooth_type="FACE",
        use_subsurf=False,
        use_mesh_edges=False,
        use_tspace=False,
        use_custom_props=False,
        add_leaf_bones=False,
        primary_bone_axis='X',
        secondary_bone_axis='-Z',
        use_armature_deform_only=False,
        armature_nodetype='NULL',
        bake_anim=False,
        bake_anim_use_all_bones=True,
        bake_anim_use_nla_strips=True,
        bake_anim_use_all_actions=True,
        bake_anim_force_startend_keying=True,
        bake_anim_step=1.0,
        bake_anim_simplify_factor=1.0,
        path_mode='AUTO',
        embed_textures=False,
        batch_mode='OFF',
        use_batch_own_dir=True,
        use_metadata=True,
        axis_forward='-Z',
        axis_up='Y'
    )
    return
