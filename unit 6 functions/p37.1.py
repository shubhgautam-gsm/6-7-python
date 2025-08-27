
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        

class Horse:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
        

# dog={}
# cat={}
# horse={}
dog = Dog("Tommy", "German Shepherd")
cat = Cat("Minu", "Persian")
horse = Horse("Champion", "Arabian")

# dog={
#     name:'Tommy',
#     breed:'German sheprad'
# }

# cat={
#     name:'Minu',
#     breed:'Persian'
# }

print(dog.name, "-", dog.breed)   # Tommy - German Shepherd
print(cat.name, "-", cat.breed)   # Kitty - Persian
print(horse.name, "-", horse.breed) # Champion - Arabian
