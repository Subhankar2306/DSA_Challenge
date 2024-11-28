'''
Problem Statement : 
Given an array arr[] consisting of n integers, the task is to find all the array elements which occurs more than floor(n/3) times.
Note: The returned array of majority elements should be sorted.

Examples:

Input: arr[] = {2, 2, 3, 1, 3, 2, 1, 1}
Output: {1, 2}
Explanation: The frequency of 1 and 2 is 3, which is more than floor n/3 (8/3 = 2).

Input: arr[] = {-5, 3, -5}
Output: {-5}
Explanation: The frequency of -5 is 2, which is more than floor n/3 (3/3 = 1).

Input: arr[] = {3, 2, 2, 4, 1, 4}
Output: { }
Explanation: There is no majority element.
'''

# Python program for finding out majority element in an array
# using hash map

def findMajority(arr):
    n = len(arr)
    freq = {}
    res = []

    # find frequency of each number
    for ele in arr:
        freq[ele] = freq.get(ele, 0) + 1

    # Iterate over each key-value pair in the hash map
    for ele, cnt in freq.items():
        
        # Add the element to the result, if its frequency
        # is greater than floor(n/3)
        if cnt > n // 3:
            res.append(ele)

    if len(res) == 2 and res[0] > res[1]:
        res[0], res[1] = res[1], res[0]
    return res

if __name__ == "__main__":
    arr = [2, 2, 3, 1, 3, 2, 1, 1]
    res = findMajority(arr)
    for ele in res:
        print(ele, end=" ")