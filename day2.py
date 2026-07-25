 #Dictionaries
student = {
    "name": "Adithayn",
    "age": 22,
    "course": "BCA",
    "Is_developer": True
}

print(student)
print(student["name"])
print(student["age"])

# Add new key
student["city"] = "Bangalore"
 
#Loop through dictionary
for key, value in student.items():
    print(key, ":", value)

#OOP - Classes and Objects
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print("Hi, I am", self.name, "studying", self.course)

    def is_adult(self):
        if self.age >= 18:
            print(self.name, "is an adult")
        else:
            print(self.name, "is a minor")

# Create objects
student1 = Student("Adithyan", 22, "BCA")
student2 = Student("Rahul", 17, "BSc")

student1.introduce()
student2.introduce()
student1.is_adult()
student2.is_adult()