'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

unsorted_list = [('first_element', 4),('fourth_element', 1), ('second_element', 2), ('third_element', 6)]
sorted_list = []

#while we still have values in the unsorted list
while len(unsorted_list) > 0:
    print("ale")
    #loop through the unsorted list to find the minimum value

    #the first items inthe list are default, fixed and forms a basis of reference
    current_value = unsorted_list[0][1]
    min_value = unsorted_list[0][1]
    index = 0
    for tuple_ in unsorted_list:
        #save the minimum value to use outside of this for loop
        if tuple_[1] <= min_value:
            min_value = tuple_[1]
            min_index = index #the index of the tuple being scrutinized, the index of the next tuple will be plus 1, this will assist in indetifying the tuple with minimum value to be popped from the list
        index += 1

    #push the minimum value onto the sorted list
    sorted_list.append(unsorted_list.pop(min_index))
    print("unsorted list is " + str(unsorted_list))

print(sorted_list)


# the logical thinking is;
# two lists , an empty sorted list, an unordered list with tuples

# we loop through the entire list
# declared the first item on the list ( the first tuple) as a reference point. ( The current value, minimum value)
# we then loop through the tuples to compare each tuple with the fixed tuple
# it's only the minimum value that will be elimniated from the unsorted list and appended to the new list