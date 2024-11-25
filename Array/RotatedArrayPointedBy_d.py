'''
Problem Statement: - 

Given an array of integers arr[] of size n, the task is to rotate the array elements to the left by d positions.

Examples:

Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
Output: {3, 4, 5, 6, 1, 2}
Explanation: After first left rotation, arr[] becomes {2, 3, 4, 5, 6, 1} and after the second rotation, arr[] becomes {3, 4, 5, 6, 1, 2}

Input: arr[] = {1, 2, 3}, d = 4
Output: {2, 3, 1}
Explanation: The array is rotated as follows:

After first left rotation, arr[] = {2, 3, 1}
After second left rotation, arr[] = {3, 1, 2}
After third left rotation, arr[] = {1, 2, 3}
After fourth left rotation, arr[] = {2, 3, 1}
'''

# Python Program to left rotate the array by d positions
# using temporary array

# Function to rotate array
def rotateArr(arr, d):
    n = len(arr)

    # Handle case when d > n
    d %= n
    
    # Storing rotated version of array
    temp = [0] * n

    # Copy last n - d elements to the front of temp
    for i in range(n - d):
        temp[i] = arr[d + i]

    # Copy the first d elements to the back of temp
    for i in range(d):
        temp[n - d + i] = arr[i]

    # Copying the elements of temp in arr
    # to get the final rotated array
    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
    arr = list(map(int, input("Enter space-separated integers: ").split()))
    d = int(input("Enter the position from where want to rotated: "))

    rotateArr(arr, d)
    print(f"After rotating the array by {d} positions:")
    # Print the rotated array
    for i in range(len(arr)):
        print(arr[i], end=" ")