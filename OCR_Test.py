# # Python program showing  
# # use of json package 
  
import json 
import demjson
import requests 
import csv
# # {key:value mapping} 
# a ={"name":"John", 
#    "age":31, 
#     "Salary":25000} 
  
# # conversion to JSON done by dumps() function 
# b = json.dumps(a) 
  
# # printing the output 
# print(b) 
# # list conversion to Array 
# print(json.dumps(['Welcome', "to", "GeeksforGeeks"])) 
  
# # tuple conversion to Array 
# print(json.dumps(("Welcome", "to", "GeeksforGeeks"))) 
  
# # string conversion to String 
# print(json.dumps("Hi")) 
  
# # int conversion to Number 
# print(json.dumps(123)) 
  
# # float conversion to Number 
# print(json.dumps(23.572)) 
  
# # Boolean conversion to their respective values 
# print(json.dumps(True)) 
# print(json.dumps(False)) 
  
# # None value to null 
# print(json.dumps(None)) 

# var = {  
#       "Subjects": { 
#                   "Maths":85, 
#                   "Physics":90
#                    } 
#       } 
# with open("Sample.json", "w") as p:
#     json.dump(var, p) 

# with open("Sample.json", "r") as read_it: 
#     data = json.load(read_it) 

# json_var =""" 
# { 
#     "Country": { 
#         "name": "INDIA", 
#         "Languages_spoken": [ 
#             { 
#                 "names": ["Hindi", "English", "Bengali", "Telugu"] 
#             } 
#         ] 
#     } 
# } 
# """
# var = json.loads(json_var) 

# # storing marks of 3 subjects 
# var = [{"Math": 50, "physics":60, "Chemistry":70}] 
# print(demjson.encode(var)) 
# var = '{"a":0, "b":1, "c":2, "d":3, "e":4}'
# text = demjson.decode(var) 
# print(text)
# # Other Method of Encoding 
# json.JSONEncoder().encode({"foo": ["bar"]}) 
# '{"foo": ["bar"]}'
 
# var = {'age':31, 'height': 6} 
# x = json.dumps(var) 
# y = json.loads(x) 
# print(x) 
# print(y) 
  
# # when performing from a file in disk 
# with open("C:/Users/asus/Desktop/Optical_Character_Reccognition-master/edited_slide-1-638.json", "r") as readit: 
#     x = json.load(readit) 
# print(x)

# # Now we have to request our JSON data through 
# # the API package 
# res = requests.get("https://jsonplaceholder.typicode.com / todos") 
# var = json.loads(res.text) 
  
# # To view your Json data, type var and hit enter 
# var 
  
# # Now our Goal is to find the User who have  
# # maximum completed their task !! 
# # i.e we would count the True value of a  
# # User in completed key. 
# # { 
#     # "userId": 1, 
#     # "id": 1, 
#     # "title": "Hey", 
#     # "completed": false,  # we will count 
#                            # this for a user. 
# # } 
  
# # Note that there are multiple users with  
# # unique id, and their task have respective 
# # Boolean Values. 
  
# def find(todo): 
#     check = todo["completed"] 
#     max_var = todo["userId"] in users 
#     return check and max_var 
  
# # To find the values. 
  
# Value = list(filter(find, todos)) 
  
# # To write these value to your disk 
  
# with open("sample.json", "w") as data: 
#     Value = list(filter(keep, todos)) 
#     json.dump(Value, data, indent = 2) 

# Opening JSON file and loading the data 
# into the variable data 
with open('C:/Users/asus/Desktop/Optical_Character_Reccognition-master/edited_slide-1-638.json') as json_file: 
    data = json.load(json_file) 
  
employee_data = data['emp_details'] 
  
# now we will open a file for writing 
data_file = open('data_file.csv', 'w') 
  
# create the csv writer object 
csv_writer = csv.writer(data_file) 
  
# Counter variable used for writing  
# headers to the CSV file 
count = 0
  
for emp in employee_data: 
    if count == 0: 
  
        # Writing headers of CSV file 
        header = emp.keys() 
        csv_writer.writerow(header) 
        count += 1
  
    # Writing data of CSV file 
    csv_writer.writerow(emp.values()) 
  
data_file.close() 