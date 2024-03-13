sum_list = []  # Create an empty list to store the numbers.

while True:
    num = input("Enter a number (or 'q' to quit): ")
    
    if num.lower() == 'q': #Converts input to lowercase and checks if it is 'q'
        break  # Exit the loop if 'Q or q' is entered. 
    
    try:
        nums = float(num)  # Convert the input to a float.
        sum_list.append(nums)  # Add the number to the list.
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")  # Prints an error message if you enter a non-numeric value.

# Compute the sum of all the integers in the list
total = sum(sum_list)

# Prints the list
print("Here is the list of numbers entered: ", sum_list)

#Prints the sum of the integers
print("The sum of the integers is:", total)


