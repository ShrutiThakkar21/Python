lst = [] #empty list
print(lst)

language = ['java', 'python', 'c', 'c++', 'android', 'php'] #with items item
print(language)

print(len(language)) #length find

first_item = language[0]
print(first_item) #first index
middle_index = int(len(language)/2)
print(language[middle_index]) #middle index
last_language= len(language)-1 
last_index = language[last_language]
print(last_index) #last index

mixed_data_type = ['Shruti', '18', 'CE eng', '5.2','bhavnagar']
print(mixed_data_type) #mixed data types

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] #declare
print(it_companies) #print list
print(len(it_companies)) #length of list

first_company = it_companies[0]
print(first_company) #first company
middle_company = int(len(it_companies)/2)
print(it_companies[middle_company]) #middle company
last_index_company = len(it_companies)-1
last_company = it_companies[last_index_company]
print(last_company)  #last company

it_companies[0] = 'Meta' 
print(it_companies) #modify list

it_companies.append('infosys')
print(it_companies) #insert an item
new_item = ["byju's"]
new_list = new_item + it_companies #insert an item with operator
print(new_list)

middle_company = (len(it_companies)/2)
print(middle_company) #find middle index
it_companies.insert(5,'sky')
print(it_companies) #insert item in middle

index_to_convert = 0
it_companies[index_to_convert] = it_companies[index_to_convert].upper()
print(it_companies) #convert 0 index in uper case

new_lst = ['#;']
new_print_lst = it_companies + new_lst
print(new_print_lst) #insert '#'

company_to_check = "Microsoft"
# Check if the company exists in the list
if company_to_check in it_companies:
    print(f"{company_to_check} is in the list of IT companies.")
else:
    print(f"{company_to_check} is not in the list of IT companies.")

it_companies.sort() #sort the list
print(it_companies)

it_companies.reverse() #reverse the list
print(it_companies)

all_company = it_companies[0:3] #slice first 3 companies
print(all_company)

all_company_reverse = it_companies[-3:] #slice last 3 companies
print(all_company_reverse) 

middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    middle_companies = it_companies[middle_index - 1 : middle_index + 1]
else:
    middle_companies = [it_companies[middle_index]]
print (middle_companies) #slice middle company

it_companies.pop(0)
print(it_companies) #remove first company
#or
#it_companies.remove('sky')
#print(it_companies)

it_companies.remove('IBM')
print(it_companies) #remove middle company

del it_companies[-1]
print(it_companies) #remove last company

del it_companies[0:] 
print(it_companies) #remove all items
#or
#del it_companies[-6:]

#it_companies.clear()
del it_companies #clear all item as well as list

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end #join two list
print(full_stack) 

full_stack.extend(['python','sql'])
print(full_stack) #insert python and sql

#exercise 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
sorted_age= sorted(ages)
print(sorted_age) #sort list
max_age = sorted_age[-1]
print(max_age)    #max age
min_age = sorted_age[0]
print(min_age)    #min age

ages.append(max_age)
ages.append(min_age)
print(ages) #append min and max age

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] #median age
sorted_ages = sorted(ages)
length = len(sorted_ages)
if length % 2 == 0:
    middle1 = sorted_ages[length // 2 - 1]
    middle2 = sorted_ages[length // 2]
    median = (middle1 + middle2) / 2
else:
    median = sorted_ages[length // 2]
print(median)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] #average age
average_age = sum(ages) / len(ages)
print(average_age)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] #range of  age
age_range = max(ages) - min(ages)
print( age_range)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] #compare minavg and maxavg
average_age = sum(ages) / len(ages)
min_difference = abs(min(ages) - average_age)
max_difference = abs(max(ages) - average_age)
print(min_difference)
print(max_difference)

countries = ["USA", "Canada", "Brazil", "India", "China", "Russia", "Australia", "France"]
length = len(countries)
if length % 2 == 0:
    middle1 = countries[length // 2 - 1]
    middle2 = countries[length // 2]
    middle_countries = [middle1, middle2]
else:
    middle_countries = [countries[length // 2]]
print(middle_countries) #middle company

countries = ["USA", "Canada", "Brazil", "India", "China", "Russia", "Australia", "France"]
length = len(countries)
if length % 2 == 0:
    first_half = countries[:length // 2]
    second_half = countries[length // 2:]
else:
    first_half = countries[:length // 2 + 1]
    second_half = countries[length // 2 + 1:]
print(first_half)
print(second_half) #divide countries in two sub part

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_three, *scandic_countries = countries[:3], countries[3:]
print(first_three)
print(scandic_countries) #Unpack the first three countries and the rest as scandic countries.

