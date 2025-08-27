class Details:
 age = 22
 name = "Phill"
details = Details()

print('The roll is:', setattr(details,"rollno", 55))
print('The age is:', details.age)
print(details.rollno)


# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
