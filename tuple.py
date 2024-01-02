empty_tuple = () #empty tupple

sister_tuple = ('pooja','jhanvi','dhara','dipu') #create tuple 
brother_tuple = ('avi','sanket','darshan','ashish')

siblings = sister_tuple + brother_tuple #join two tuple
print(siblings)

total_siblings = len(siblings) #total siblings
print(total_siblings)

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
mom_dad = ('urvashi', 'rajendra') 
family = siblings + mom_dad
print(family)

unpacking = mom_dad, *siblings #unpacking
print(unpacking)

fruit = ('mango','banana') #create three tuple
vegetable = ('potato','tomato')
animmal = ('dog','cat')

#assign it to a variable called food_stuff_tp.
food_stuff_tp = fruit+vegetable+animmal
print(food_stuff_tp)

food_stuff_lp = list(food_stuff_tp) #convert tuple in list
print(food_stuff_lp)

slicing = food_stuff_lp[2:-3] #slicing middle element
print(slicing)

first_three = food_stuff_lp[:-3] #slice first three
print(first_three)
last_three = food_stuff_lp[-3:] #slice last three
print(last_three)

del food_stuff_tp #deleting food_stuff_tp tuple

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)  #Check if 'Estonia' is a nordic country
print('Iceland' in nordic_countries) #check if 'Iceland' is a nordic country