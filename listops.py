integers = [9, 5, 3, 2, 11, 13, 7, 10, 15, 19]
def print_list(integers):
    print("The list is:" , integers)

def print_sum(integers):
    total = sum(integers)
    print("The sum of all elements in list is:" , total)

def print_largest(integers):
    largest = max(integers)
    print("The largest element in list is:" , largest)

def print_smallest(integers):
    smallest = min(integers)
    print("The smallest element in list is:" , smallest)

def print_reverse(integers):
    reversed_list = integers[::-1]
    print("The list in reverse order is:" , reversed_list)



print_list(integers)
print_sum(integers)
print_largest(integers)
print_smallest(integers)
print_reverse(integers)
