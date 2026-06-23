# # --- 1. DICTIONARY BASICS DEMO ---
# # creation
# student = {"Name" : "satya" , "Branch":"IT", "Year" : "4th"}
# # Access
# print(student["Name"])
# print(student.get("grade"))
# # Update & Add
# student["Branch"] = "CS"
# student["Grade"] = "C"
# print(student)
# # Delete
# del student["Grade"]
# student_branch = student.pop("Branch")
# print (student)
# # view Methods
# print(student.keys())
# print(student.values())
# print(student.items())

capitals = {"india":"new delhi",
            "china":"beljiam",
            "russia":"mascow",
            "USA":"whashington DC"}
# print(capitals.get("india"))
capitals.update({"germany":"berlin"})
capitals.update({"USA":"dc"})
capitals.pop("USA")
capitals.popitem()
print(capitals)

for value in capitals.values():
    print(value)

for key in capitals.items():
    print(key)