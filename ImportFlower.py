import maya.cmds as mc
import os
import AdvancedRigging
reload(AdvancedRigging)

"""
Create the bulb by importing a bulb type from default lib
path : "/Users/christyye/Documents/maya/projects/Advanced_Rigging/bulb_default.fbx "
"""


def createBulb(path):

    mc.file(path, i=True)

    # create a locator for bulb
    dir_path = os.path.basename(os.path.normpath(path)).split(".")[0]

    # Assign the locator as a controller to the bulb
    obj = mc.ls(dir_path)
    AdvancedRigging.createCenterLocatorController(obj, orient=False)


"""
Create a single petal by importing a petal type from default lib
testing default is : "/Users/christyye/Documents/maya/projects/Advanced_Rigging/petal_default.fbx "
"""


def createPetal(path):

    mc.file(path, i=True)

    # find the petal in the scene
    dir_path = os.path.basename(os.path.normpath(path)).split(".")[0]
    obj = mc.ls(dir_path)

    # get all the meshes and joints in the petal
    children = mc.listRelatives(obj, ad=True)[:-1]

    joints = []
    meshes = []

    # separate the children into meshes and joints. Rename them as their respective categories
    for i in range(len(children)):

        if mc.objectType(children[i]) == "joint":
            mc.rename(children[i], "petal_joint_" + str(i))
            joints.append(children[i])
        elif mc.objectType(children[i]) == "mesh":
            mc.rename(children[i], "petal_geo" + str(i))
            meshes.append(children[i])

    return joints, meshes
