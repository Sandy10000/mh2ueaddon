# Does not meet PEP8 requirements


import bpy


class MH2UE_Property(bpy.types.PropertyGroup):
    bool1: bpy.props.BoolProperty(default=True)
    bool2: bpy.props.BoolProperty(default=True)
    bool3: bpy.props.BoolProperty(default=True)
    bool4: bpy.props.BoolProperty(default=True)
    bool5: bpy.props.BoolProperty(default=False)
    bool6: bpy.props.BoolProperty(default=True)
    bool7: bpy.props.BoolProperty(default=True)
    bool8: bpy.props.BoolProperty(default=True)
    bool9: bpy.props.BoolProperty(default=False)
    float1: bpy.props.FloatProperty(default=0.1)
    str1: bpy.props.StringProperty(subtype='FILE_PATH')
    str2: bpy.props.StringProperty(default="head")
    str3: bpy.props.StringProperty(default="head")
    str4: bpy.props.StringProperty(subtype='DIR_PATH')
    str5: bpy.props.StringProperty(default="SK_Makehuman")
