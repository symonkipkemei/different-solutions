'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6), ('fourth_element', 2)]
sorted_list = []

#abstract the values from the tuples and store them in a list
value_list = []
for tuple_ in unsorted_list:
    value_list.append(tuple_[1])

#sort the list in ascending order
print(value_list)
value_list.sort()

# loop through the ordered value matching the value to the tuple, if it matches append it to sorted list and delete the value from the unsorted list
for value in value_list:
    for tuple_ in unsorted_list:
        if tuple_[1] == value:
            sorted_list.append(tuple_)
            unsorted_list.remove(tuple_)
            break

print(sorted_list)
