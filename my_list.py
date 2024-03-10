my_list = [] # Create an empty list to store the numbers.

nums = (10, 20, 30, 40) # Create a list of numbers.

for x in nums:  #Iterates through the list of numbers.
    my_list.append(x) #Adds the numbers to the list one by one.

my_list.insert(1, 15) #Insert number 15 at index 1 which is the second position 

more_nums = [60, 50, 70]
my_list.extend(more_nums) # Add a second list of numbers to my_list.

my_list.remove(my_list[-1])

my_list.sort()# Sort the list in ascending order.

print(my_list.index(30)) # Print the list.
