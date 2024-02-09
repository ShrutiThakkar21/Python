#a)
lst = ['Thakkar','patel','joshi','dave']
print(lst) #list

lst.append('pandya') #append list
print(lst) 

lst.reverse()
print(lst)

lst.extend('jasani')
print(lst)

asceding_order = sorted(lst)
print(asceding_order)

descending_order = sorted(lst, reverse=True)
print(descending_order)

#b)
List1 = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana", 
"orange"]]
print(List1)
get_orange = List1[-1][-1]
print(get_orange)

get_python = List1[4][0]
print(get_python)

repeat_list = [List1]*5
print(repeat_list)

#c)
list_new = ['shruti','mahi','pooja']
print(list_new)
slice = list_new[0:3]
print(slice)

#d)
tpl = (2,3,4)
sum_tpl = sum(tpl)
print(sum_tpl)

max_tpl = max(tpl)
print(max_tpl)

min_tpl = min(tpl)
print(min_tpl)

