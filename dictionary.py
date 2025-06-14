#Dictionary
# its in key : Value  format like Objects
# dictionary is  an unordered list

stud_info = {
    'name' : "Rohit",
    'age' : 25,
    "add" : "NA"
    }
print(stud_info)

print(stud_info["age"])
stud_info["gender"] = "Male"
print(stud_info)

for keys in stud_info.keys():
    if keys  == "age":
        stud_info[keys] = 50
print(stud_info)