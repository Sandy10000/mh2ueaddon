# <pep8-80 compliant>


import bpy

from . import operators
from . import panels
from . import properties
from .translation import jajp


bl_info = {
    "name": "mh2ue add-on",
    "author": "Sandy",
    "version": (2021, 2, 10),
    "blender": (2, 91, 0),
    "location": "View3D > Sidebar",
    "description":
        "Convert characters created with makehuman for Unreal Engine",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "https://github.com/Sandy10000/mh2ueaddon/wiki",
    "tracker_url": "https://github.com/Sandy10000/mh2ueaddon/issues",
    "category": "MakeHuman"
}


translation_dict = {
    "ja_JP": jajp.dic,
}


class MH2UE_PT_Panel(bpy.types.Panel):
    bl_label = "mh2ue ver. %d.%d.%d" % bl_info["version"]
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "mh2ue"

    def draw(self, context):
        layout = self.layout


classes = [
    operators.MH2UE_OT_Import,
    operators.MH2UE_OT_Bone,
    operators.MH2UE_OT_UEeye,
    operators.MH2UE_OT_Export,
    MH2UE_PT_Panel,
    panels.MH2UE_PT_Import,
    panels.MH2UE_PT_Bone,
    panels.MH2UE_PT_UEeye,
    panels.MH2UE_PT_Export,
    properties.MH2UE_Property,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.Scene.mh2ue_prop = bpy.props.PointerProperty(
        type=properties.MH2UE_Property)
    bpy.app.translations.register(__name__, translation_dict)


def unregister():
    bpy.app.translations.unregister(__name__)
    del bpy.types.Scene.mh2ue_prop
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == '__main__':
    register()
