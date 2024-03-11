# Practical task 1
# helloWorld.py

# Defining the main function.
def main():
	# Printing out the message.
    print("Git is awesome!")

# Executing the main function if the script is running directly.
if __name__ == "__main__":
    main()

# Practical task 2 

# This line of code prompts the user to enter their name.
user_input = input("Enter your name:")

#This line of code prints out the entered data.
print("Hello,", user_input)

# Practical task 3.

# Constants.
# Defining a constant message to be printed.
MESSAGE = "Git is awesome!" 

# Function to print the message.
def print_message():
	# Print the predefined message.
	print(MESSAGE)

# Main function.
def main():
	# Entry point of the program.
	try:
		# Calling the function to print the message. 
		print_message()
	except Exception as e:
		# Handling any exceptions that occur. 
		print("An error occured:".e)

# Execute the main function if the script is running directly.
if __name__ == "__main__":
	# Caling the main function to start the program.
	main()



