# --- 1. DICTIONARY BASICS DEMO ---
# creation
student = {"Name" : "satya" , "Branch":"IT", "Year" : "4th"}
# Access
print(student["Name"])
print(student.get("grade"))
# Update & Add
student["Branch"] = "CS"
student["Grade"] = "C"
print(student)
# Delete
del student["Grade"]
student_branch = student.pop("Branch")
print (student)
# view Methods
print(student.keys())
print(student.values())
print(student.items())