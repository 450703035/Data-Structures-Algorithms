'''
Problem Statement:

Given an integer array, find and return all the subsets of the array.
The order of subsets in the output array is not important. 
However the order of elements in a particular subset should remain the
same as in the input array.

Note: An empty set will be represented by an empty list

Example 1:
arr = [9]
output = [[]
          [9]]

Example 2:
arr = [9, 12, 15]
output =  [[],
           [15],
           [12],
           [12, 15],
           [9],
           [9, 15],
           [9, 12],
           [9, 12, 15]]
'''

import pdb

def subsets(arr):
    if len(arr) < 1:
        return [[]]
    
    else:
        output = list()
        output.append(arr)
        
        for i in range(len(arr)):
            temp_arr = arr.copy()
            temp_arr.pop(i)
            output.extend(subsets(temp_arr))
        
        #pdb.set_trace()
        
        results_mod = []
        for i, item in enumerate(output):
            if i == output.index(item):  # Case detected is the one we are
                results_mod.append(item)
        
        return results_mod

#
#def subsets(arr):
#    """
#    :param: arr - input integer array
#    Return - list of lists (two dimensional array) where each list represents a subset
#    """
#
#    if len(arr) <= 1:
#        return [arr]
#
#    else:
#        results = list()
#        results.append(arr)
#
#        for i_pos in range(len(arr)):
#            temp_arr = arr.copy()
#            temp_arr.pop(i_pos)
#            results.extend(subsets(temp_arr))
#
#        results_mod = []
#        for i, item in enumerate(results):
#            if i == results.index(item):  # Case detected is the one we are
#                results_mod.append(item)
#            else:
#                pass
#        
#        results_mod.append([])
#        return results_mod

#def subsets(arr):
#    return return_subsets(arr, 0)
#
#
#def return_subsets(arr, index):
#    if index >= len(arr):
#        return [[]]
#
#    small_output = return_subsets(arr, index + 1)
#    output = list()
#
#    for element in small_output:
#        output.append(element)
#
#    for element in small_output:
#        current = list()
#        current.append(arr[index])
#        current.extend(element)
#        output.append(current)
#
#    return output


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = subsets(arr)
    pdb.set_trace()
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")    


#arr = [9]
#solution = [[], [9]]
#test_case = [arr, solution]
#test_function(test_case)


arr = [5, 7]
solution = [[], [7], [5], [5, 7]]
test_case = [arr, solution]
test_function(test_case)


#arr = [9, 12, 15]
#solution = [[], [15], [12], [12, 15], [9], [9, 15], [9, 12], [9, 12, 15]]
#test_case = [arr, solution]
#test_function(test_case)


#arr = [9, 8, 9, 8]
#solution = [[],
#[8],
#[9],
#[9, 8],
#[8],
#[8, 8],
#[8, 9],
#[8, 9, 8],
#[9],
#[9, 8],
#[9, 9],
#[9, 9, 8],
#[9, 8],
#[9, 8, 8],
#[9, 8, 9],
#[9, 8, 9, 8]]
#
#test_case = [arr, solution]
#test_function(test_case)