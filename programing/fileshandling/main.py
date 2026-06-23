# txt_file = "i like you "
# employees =["ram","akhi","rupi","nikhil"]
# import json
# employe={
#     "name": "ram",
#     "age":25,
#     "job":"Fisher Man"
# }
import csv
employees=[["Name","Age","job"],
         ["ram",25,"fisherMan"],
         ["rupi",24,"Farmer"],
         ["akhi",24,"unemployed"]]
# file_path= "c:/Users/HP/OneDrive/Desktop/output1.txt"
# file_path= "c:/Users/HP/OneDrive/Desktop/output1.json"
file_path= "c:/Users/HP/OneDrive/Desktop/output1.csv"
# with open(file_path,"w") as file:
#     file.write(txt_file)
#     print(f"text file is created with  {file_path}")
try:
    with open(file_path,"w") as file:
        writer = csv.writer(file)
        for employe in employees:
            writer.writerow(employe)
            # json.dump(employe,file,indent=4)
            # file.write("\n"+"Employee Name :"+ employe.capitalize())
            print(f"CSV file is created with  {file_path}")
except FileExistsError:
    print("the file is alred exist idiot")