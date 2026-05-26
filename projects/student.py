student ={
    "name" : "mahesh",
    "branch" : "IT",
    "grade" : [20,30,40,55,78],
    "address":{
        "street" : "hanuman gally",
        "h-no" : "6-889/276",
        "zip-code":"567890"
    }
}
print(student["name"])
print(student["grade"][0])
print(student["address"]["h-no"])
student["address"]["street"] = "ambethkar gully"
student["grade"].append(95)


grade_list = student["grade"]
total_score = sum(grade_list)
num_of_subjects = len(grade_list)
average_grade = total_score/num_of_subjects

print(f"Updated Grades: {student['grade']}")
print(f"Average Grade: {average_grade:.2f}")
print(f"New City: {student['address']['street']}")