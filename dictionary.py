dog = {} #empty dictionary
print(dog)

#Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name':'ticen',
    'color':'white',
    'breed':'gemen',
    'legs':'4',
    'age':'12'
}
print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'shruti', 'last_name':'Thakkar', 'gender':'Female', 'age':'18', 'marital_status':'single', 'skills':'dance', 'country':'India', 'city':'bhavnagar', 'address':{'street':'sardarnagar',
        'zipcode':'364002'}
}
print(student)

#get the length
length = len(student)
print(length)

print(student['skills']) #get the value of skills
type = type('skills') #get the datatype of skills
print(type)

student['skills']='singing' #modify  by addind new skills
print(student)

values = student.values() #get the dictionary value as list
print(values)

key = student.keys() #get the dictionary key as list
print(key)

print(student.items()) #Change the dictionary to a list of tuples using items() method

del student['age'] #Delete one of the items in the dictionary
print(student)

del student #delete the dictionary






