# <pep8-80 compliant>

import bpy
import mathutils


def mh2ue():
    bpy.ops.outliner.orphans_purge()

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = bpy.data.objects["Armature"]

    bpy.ops.object.mode_set(mode='EDIT')
    bones = [
        ("Root", (3.14, 0.0, 0.0), 1.57),
        ("pelvis", (0.0, -0.0355, 9.7054), 1.204043940106203e-07),
        ("spine_01", (0.0, -2.4676, 19.0955), 1.2043376784731663e-07),
        ("spine_02", (0.0, 1.5651, 13.3223), 1.2037928343033855e-07),
        ("spine_03", (0.0, 2.3111, 13.8404), 1.2036994689879066e-07),
        ("clavicle_l", (13.9182, 6.9506, -2.671), 1.6761107444763184),
        ("upperarm_l", (9.9434, 1.1179, -11.7326), 2.410767078399658),
        ("lowerarm_l", (14.7201, -8.7915, -11.2146), 2.0401418209075928),
        ("hand_l", (7.4183, -4.7717, -6.2159), 0.7742447257041931),
        ("index_01_l", (1.6298, -1.3284, -3.7365), 1.688023328781128),
        ("index_02_l", (0.7641, -0.6676, -3.2386), 1.9376062154769897),
        ("index_03_l", (1.1548, -1.0154, -3.0254), 1.7928578853607178),
        ("middle_01_l", (2.0408, -1.2455, -3.9771), 1.37657630443573),
        ("middle_02_l", (0.9041, -0.8173, -3.4393), 1.6097930669784546),
        ("middle_03_l", (1.8408, -0.8, -3.0472), 1.26283860206604),
        ("pinky_01_l", (1.9121, -0.2855, -3.0024), 0.8965443968772888),
        ("pinky_02_l", (1.0753, -0.228, -2.7759), 1.1303706169128418),
        ("pinky_03_l", (1.0301, -0.4317, -2.7689), 1.1524299383163452),
        ("ring_01_l", (2.0167, -0.8928, -3.8422), 1.0971653461456299),
        ("ring_02_l", (0.8418, -0.5747, -3.3239), 1.3844847679138184),
        ("ring_03_l", (1.5493, -0.785, -3.0117), 1.1123979091644287),
        ("thumb_01_l", (0.1295, -3.2002, -2.1717), -2.6270177364349365),
        ("thumb_02_l", (0.1767, -2.4893, -3.2052), -2.6139678955078125),
        ("thumb_03_l", (-0.3584, -2.9914, -2.7248), -2.2586119174957275),
        ("clavicle_r", (13.9182, -6.9506, 2.671), -1.8446810245513916),
        ("upperarm_r", (9.9435, -1.1179, 11.7327), -2.4663352966308594),
        ("lowerarm_r", (14.7202, 8.7916, 11.2146), -2.40354061126709),
        ("hand_r", (7.4183, 4.7717, 6.2159), 2.52095627784729),
        ("index_01_r", (1.6298, 1.3285, 3.7367), 2.510608673095703),
        ("index_02_r", (0.7641, 0.6676, 3.2386), 2.400984048843384),
        ("index_03_r", (1.1548, 1.0154, 3.0254), 2.5221238136291504),
        ("middle_01_r", (2.0409, 1.2455, 3.9772), 2.3247838020324707),
        ("middle_02_r", (0.9042, 0.8173, 3.4393), 2.1239285469055176),
        ("middle_03_r", (1.8408, 0.8, 3.0473), 2.3496832847595215),
        ("pinky_01_r", (1.9122, 0.2855, 3.0024), 2.030719757080078),
        ("pinky_02_r", (1.0752, 0.228, 2.7757), 1.8695118427276611),
        ("pinky_03_r", (1.03, 0.4316, 2.7686), 1.8647516965866089),
        ("ring_01_r", (2.0165, 0.8928, 3.8419), 2.0638554096221924),
        ("ring_02_r", (0.8418, 0.5747, 3.3239), 1.8805898427963257),
        ("ring_03_r", (1.5493, 0.785, 3.0117), 2.062621593475342),
        ("thumb_01_r", (0.1295, 3.2001, 2.1717), -2.507920503616333),
        ("thumb_02_r", (0.1767, 2.4893, 3.2052), -2.5038182735443115),
        ("thumb_03_r", (-0.3584, 2.9914, 2.7248), -2.5201525688171387),
        ("neck_01", (0.0, -2.2521, 9.0137), 1.2046517383623723e-07),
        ("head", (0.0, 0.2141, 9.2883), 1.203985817710418e-07),
        ("thigh_l", (-3.9585, -0.9659, 32.0754), 0.022982334718108177),
        ("calf_l", (-2.1573, -4.7335, 29.8874), -0.019580373540520668),
        ("foot_l", (-0.2906, -0.2511, 19.5951), 0.030697213485836983),
        ("ball_l", (0.9077, -19.5579, -0.8815), -1.5856081247329712),
        ("thigh_r", (-3.9585, 0.9659, -32.0755), 0.268565833568573),
        ("calf_r", (-2.1573, 4.7335, -29.8876), 0.12452912330627441),
        ("foot_r", (-0.2906, 0.2511, -19.595), 0.060352873057127),
        ("ball_r", (0.9077, 19.5579, 0.8815), 0.014443517662584782),
    ]
    arm = bpy.data.armatures[0]
    for bone in bones:
        arm.edit_bones[bone[0]].tail\
            = arm.edit_bones[bone[0]].head\
            + mathutils.Vector(bone[1])
        arm.edit_bones[bone[0]].roll = bone[2]

    bpy.ops.object.mode_set(mode='OBJECT')
