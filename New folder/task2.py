single_dim_array = [1, 2, 3, 4, 5,]
two_dim_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

def display_single_dim_array(arr):
    print("single-dimensional array")
    for element in arr:
        print(element)

def display_two_dim_array(arr):
    print("two-dimensional array elements:")
    for sublist in arr:
        print(sublist)

choice = input("which array you want to display? (1 for single and 2 for two-dimensional)")

if choice == "1":
    display_single_dim_array(single_dim_array)
elif choice =="2":
    display_two_dim_array(two_dim_array)
else:
    print("error")