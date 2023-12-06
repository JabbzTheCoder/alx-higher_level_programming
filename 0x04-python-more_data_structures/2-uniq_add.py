#!/usr/bin/python3

def uniq_add(my_list=[]):
    num_to_add = []
    results = 0

    for i in range(len(my_list)):
        if (my_list[i] not in num_to_add):
            num_to_add.append(my_list[i])

    
    for i in num_to_add:
        results += i;

    return(results)
