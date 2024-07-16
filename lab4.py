# Implementing stack using List
my_list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
my_stack = []

# Adding elements to the stack
print("-----Adding values in Stack-----\n")
for day in my_list:
    my_stack.append(day)
    print(my_stack)

# Removing elements from the stack
print("----Removing values from stack----\n")
while my_stack:
    my_stack.pop()
    print(my_stack)

# Updating elements in a stack
my_stack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]

def update_stack(location, value):
    if location < len(my_stack):
        my_stack[location] = value
    else:
        print(f"Index {location} is out of range for the stack!!!")

update_stack(5, 50)
print(my_stack)

# Implementing stack using Arrays
import array as myarray
my_stack_array = myarray.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Reading the stack elements
print("\nReading stack elements from array:")
for item in my_stack_array:
    print(item, end=' ')
print("\n")

# Inserting elements into the stack
my_stack_array.append(11)
print("After inserting 11 into array stack:")
for item in my_stack_array:
    print(item, end=' ')
print("\n")

# Deleting elements from the stack
print("Deleting elements from array stack:")
while my_stack_array:
    my_stack_array.pop()
    for item in my_stack_array:
        print(item, end=' ')
    print("\n")

# Updating elements in a stack implemented using array
stack_array = myarray.array('i', [1, 2, 3, 4, 5])

def update_array(data, value):
    ind = stack_array.index(data)
    stack_array[ind] = value
    for item in stack_array:
        print(item, end=" ")

update_array(5, 30)
print("\n")

# Implementing stack using deque from the collections package
from collections import deque

my_stack_deque = deque()
my_list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

# Inserting elements into the stack using deque
print("Inserting elements into deque stack:")
for day in my_list:
    my_stack_deque.append(day)
    print(my_stack_deque)
print("\n")

# Deleting elements from the stack using deque
print("Deleting elements from deque stack:")
while my_stack_deque:
    my_stack_deque.pop()
    print(my_stack_deque)
print("\n")

# Updating elements in the stack using deque
stack_deque = deque([1, 2, 3, 4, 5])

def update_deque(data, value):
    ind = stack_deque.index(data)
    stack_deque[ind] = value
    return stack_deque

update_deque(4, 44)
print(stack_deque)

# Sorting the stack implemented using deque
stack_deq = deque([5, 3, 1, 16, 22, 33, 12, 10, 2, 15])

def sort_deq():
    sorted_stack = sorted(stack_deq)
    return deque(sorted_stack)

sorted_stack = sort_deq()
print("\n----After sorting Stack deque elements----\n")
print(sorted_stack)

# Binary Search Function
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # If target is not present in array
    return -1

# Example usage of binary search:
sorted_array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target_value = 12
result_index = binary_search(sorted_array, target_value)

if result_index != -1:
    print(f"\nTarget {target_value} found at index {result_index}.")
else:
    print(f"\nTarget {target_value} not found in the array.")
