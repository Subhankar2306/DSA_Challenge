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