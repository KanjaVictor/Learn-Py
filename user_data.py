user_data = {} #Create an empty dictionary to store user data.

key = ('name', 'age') #Create a tuple to store the keys for the dictionary. Its used for iteration with the for loop.

for x in key: #Iterates through the tuple, for a key in tuple the block of code below is run.
    value = input("Enter your "+ x + ": ") #Prompts the user to enter data. Its temporarily stored in value.
    user_data[x] = value #Stores the data in the dictionary it couples data entered with the key which is in (x).

#if you don't store in dictionary, the loop will run again and the previous data in value will be overwritten.

print(user_data)
