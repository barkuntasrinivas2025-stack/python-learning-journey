# def testLogin():
#     print("your shit always")
# def testLogoff():
#     print("LOGOFFED")
# def testCAl():
#     assert 2+2==7
# import json

# contact_book = {
#         "ID":1234,
#         "firstname":"hero",
#         "lastname":"alayala",
#         "age":48,
#         "field":"farmer"
# }
# contact1= contact_book()
# file_path ="c:/Users/HP/OneDrive/Desktop/contact.json"
# try:
#     with open(file_path,"w")as file:
#         for contact in contact_book:
#             json.dump(contact,file)
#             print(f"json file is create at location{file_path}")
# except FileExistsError:
#     print("the file is alred exist idiot")
# def testExist():
#     print("the file alredy exist")
# def testLoginDetailes():
#     print(f"they are existed with {contact1.ID}")
# def testCall():
#     assert contact1.ID ==1234
import json
import pytest
import os

contact_book = {
        "ID":1234,
        "firstname":"hero",
        "lastname":"alayala",
        "age":48,
        "field":"farmer"
}
# contact1= contact_book()
file_path ="c:/Users/HP/OneDrive/Desktop/contact.json"
@pytest.fixture(autouse=True)
def setup_and_teardown():
        with open(file_path,"w")as file:
             json.dump(contact_book,file,indent=4)
        yield
        if os.path.exists(file_path):
             os.remove(file_path)

# try:
#     with open(file_path,"w")as file:
#         for contact in contact_book:
#             json.dump(contact,file)
#             print(f"json file is create at location{file_path}")
# except FileExistsError:
#     print("the file is alred exist idiot")
def test_exist():
    # print("the file alredy exist")
    assert os.path.exists(file_path)is True
def testLoginDetailes():
    with open(file_path,"r")as file:
        data =json.load(file)
        assert data["firstname"] == "hero"
        assert data["field"] == "farmer" 
        # print(f"they are existed with {contact1.ID}")
def testCall():
    with open(file_path,"r")as file:
        data1=json.load(file)
        assert data1["ID"]  == 1234