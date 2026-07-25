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