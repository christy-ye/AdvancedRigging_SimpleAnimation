import ImportFlower
reload(ImportFlower)
import FlowerAnimation
reload(FlowerAnimation)
from Flower import Flower
import os

print "In main.py"

#Step 1: Load the models
def StepOne(bulb="bulb_default", petal="petal_default"):

    """find the relative paths to the models and load them"""
    current_dir = os.path.dirname(__file__)
    bulb_path = os.path.join(current_dir, "Assets", bulb + ".fbx")

    petal_path = os.path.join(current_dir, "Assets", petal + ".fbx")

    """load the models found"""
    ImportFlower.createBulb(bulb_path)
    ImportFlower.createPetal(petal_path)

#Step 2: Move Petals in place. Specify name of the parent petal joint, petal geo name, and bulb locator name in this order
def StepTwo(petal_name, bulb_name, petal_rows=1, base_petals=3):

    """create an Flower instance so each flower as a unique set attributes"""
    lotus_flower = Flower(petal=petal_name, bulb=bulb_name, rows=petal_rows, base_petals=base_petals)

    """build the flower using the traits assigned to instance"""
    lotus_flower.organiseFlowerPetals()
    lotus_flower.movePetalsAroundBulb(offset=1)

    return lotus_flower

#Step 3: Rig and Animation petal joints in Flower. Select the petal groups to animate
def StepThree():
    FlowerAnimation.animatePetals()


#Optional: Edit the form and animations of a created Flower object. Specify the flower object
# to change and the type edit
def editPetals(flower, edit):
    switcher = {
        "adjustPetalRowTransform": flower.adjustPetalRowTransform(),
        "adjustSinglePetalTransform": flower.adjustSinglePetalTransform(),
        "changeRowAnimation": FlowerAnimation.changeRowAnimation(flower)
    }

    return switcher[edit]

