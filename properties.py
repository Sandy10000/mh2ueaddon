# Does not meet PEP8 requirements


import bpy


class MH2UE_Property(bpy.types.PropertyGroup):
    import_b1: bpy.props.BoolProperty(default=True)
    import_b2: bpy.props.BoolProperty(default=True)
    import_b3: bpy.props.BoolProperty(default=True)
    import_b4: bpy.props.BoolProperty(default=True)
    import_b5: bpy.props.BoolProperty(default=False)
    import_b6: bpy.props.BoolProperty(default=True)
    import_b7: bpy.props.BoolProperty(default=True)
    bone_tw_ll: bpy.props.BoolProperty(default=True)
    bone_tw_ul: bpy.props.BoolProperty(default=True)
    bone_tw_lr: bpy.props.BoolProperty(default=True)
    bone_tw_ur: bpy.props.BoolProperty(default=True)
    bone_tw_cl: bpy.props.BoolProperty(default=True)
    bone_tw_tl: bpy.props.BoolProperty(default=True)
    bone_tw_cr: bpy.props.BoolProperty(default=True)
    bone_tw_tr: bpy.props.BoolProperty(default=True)
    bone_ik_froot: bpy.props.BoolProperty(default=True)
    bone_ik_fl: bpy.props.BoolProperty(default=True)
    bone_ik_fr: bpy.props.BoolProperty(default=True)
    bone_ik_hroot: bpy.props.BoolProperty(default=True)
    bone_ik_hg: bpy.props.BoolProperty(default=True)
    bone_ik_hl: bpy.props.BoolProperty(default=True)
    bone_ik_hr: bpy.props.BoolProperty(default=True)
    eye_b1: bpy.props.BoolProperty(default=True)
    eye_f1: bpy.props.FloatProperty(default=0.1)
    eye_s1: bpy.props.StringProperty(subtype='FILE_PATH')
    eye_s2: bpy.props.StringProperty(default="head")
    eye_s3: bpy.props.StringProperty(default="head")
    export_b1: bpy.props.BoolProperty(default=False)
    export_s1: bpy.props.StringProperty(subtype='DIR_PATH')
    export_s2: bpy.props.StringProperty(default="SK_Makehuman")
