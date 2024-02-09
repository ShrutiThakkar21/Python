String = "Shruti"
print(String) #String
reverse_string = String[::-1]
print(reverse_string) #reverse string

original_string = "you and me, me and you"
new_string = original_string.replace("you", "me")
print("Original string:", original_string)
print("Modified string:", new_string) #replace

String_new= "Thakkar"
Merge_string= String+String_new
print(Merge_string) #merge string

#find the character is present in string or not
char_to_find = 'S'
index = String.find(char_to_find)
if index != -1:
    print("The character '{}' is present in the string at index {}.".format(char_to_find, index))
else:
    print("The character '{}' is not present in the string.".format(char_to_find))

#split in to words
org_string = "Shruti Thakkar"
words = org_string.split()
print("Words:", words)

#split in to characters
characters = list(org_string)
print("Characters:", characters)

#b)
# Create a sample dictionary
my_dict = {
    'arpita': 12,
    'binal': 21,
    'chamak': 31,
    'disha': 41
}
#update dictionary
my_dict.update({'binal': 20, 'isha': 5})
print("After Update:", my_dict)
#delete dictionary
del my_dict['arpita']
print("After Delete:", my_dict)
#clear dictionary
my_dict.clear()
print("After Clear:", my_dict)
#create new dictionary
my_dict = {
    'abhi': 1,
    'barbie': 2,
    'catey': 3,
    'dev': 4
}
#popitem
item = my_dict.popitem()
print("Popped Item:", item)
print("After popitem:", my_dict)
#pop value
value = my_dict.pop('barbie')
print("Popped Value:", value)
print("After pop('barbie'):", my_dict) 

print("Get value for 'catey':", my_dict.get('catey'))
print("Get value for 'x' with default value 0:", my_dict.get('x', 0))
#key value
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())

dict1 = {'first_name': 'shruti', 'last_name': 'thakkar'}
dict2 = {'class': 'CE', 'div': 2}
dict3 = {'institute': 'cspit', 'gender': 'female'}

# Merging dictionaries using the update() method
merged_dict = {}
merged_dict.update(dict1)
merged_dict.update(dict2)
merged_dict.update(dict3)

print("Merged Dictionary:", merged_dict)
