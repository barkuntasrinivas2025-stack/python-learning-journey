list_one = [1,2,2,3,4,5]
list_two = [4,5,5,6,7,8]

set_one = set(list_one)
set_two = set(list_two)
print(set_one) 
print(set_two)
comman_set = set_one.intersection(set_two)
comman_elements = list(comman_set)
print(comman_elements)
