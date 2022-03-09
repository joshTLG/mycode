class Weapon:  
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon Objects.")
        
    def __str__(self):
        return "{}+{} STR ".format(self.name, self.damage)
      
class Rock(Weapon):
    def __init__(self):
        self.name="Rock"
        self.description= "A fist-sized rock, suitable for bludgening."
        self.damage=5
        self.value= 1
class Dagger(Weapon):
    def __init__(self):
        self.name="Dagger"
        self.description="a small dagger with some rust."\
                         "Somewhere more dangerous than a rock"
        self.damage=10
        self.value= 20
# \ means to continue on another line but consider same line in coding

class WoodmansAxe(Weapon):
    def __init__(self):
        self.name="Woodman's Axe"
        self.description= "This sword is showing its age,"\
                          "but still has some fight in it"
        self.damage=15
        self.value= 100

class HuntingSpear(Weapon):
    def __init__(self):
        self.name="Hunting Spear"
        self.description= "This sword is showing its age,"\
                          "but still has some fight in it"
        self.damage=20
        self.value= 250
        
class SilverSword(Weapon):
    def __init__(self):
        self.name="Silver sword"
        self.description= "This sword is showing its age,"\
                          "but still has some fight in it"
        self.damage=30
        self.value= 150
        
class DoomHammer(Weapon):
    def __init__(self):
        self.name="Doom Hammer"
        self.description= "A powerful hammer that was crafted long ago,"\
                          "forged in a pool of elemental lava"
        self.damage=40
        self.value= 100        

class Consumable:
    def __init__ (self):
        raise NotImplementedError ("Do not create raw Consumable Objects")
    
    def __str__(self):
        return "{}+{}HP".format(self.name, self.healing_value)
        
class HardTack(Consumable):
    def __init__ (self):
        self.name = "Moldy Bread"
        self.healing_value = 15 
        self.value= 15

class LesserHealingPotion(Consumable):
    def __init__(self):
        self.name = " Lesser Healing Potion"
        self.healing_value = 50
        self.value = 60 

class GreaterHealingPotion(Consumable):
    def __init__(self):
        self.name = " Greater Healing Potion"
        self.healing_value = 100
        self.value = 150    

class bug: 
    def __init__(self):
        raise NotImplementedError("Do not create raw bug Objects.")
        
    def __str__(self):
        return "{} ".format(self.name)
        
class BoneDoll(bug):
    def __init__(self):
        self.name = " Bone Doll"
        self.value = 7700    
        
class BoneFlute(bug):
    def __init__(self):
        self.name = " Bone Flute "
        self.value = 5600  
        
class BoneCrown(bug):        
     def __init__(self):
        self.name = " Bone Crown "   
        self.value = 6300  

class BoneHarp(bug):        
     def __init__(self):
        self.name = " Bone Harp "   
        self.value = 3000      
