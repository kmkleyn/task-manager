# The purpose of this program is to help a small business manage tasks assigned to each member of its team.

# First, the datetime and sys modules are imported so that later we can get the current date and be able to exit the program via command.
import datetime
import sys

# We initialise correct login and admin login as false. It will be set to true if the user's username and password match and are on file.
# We also create an empty list to store the tasks in.
# An empty dictionary is created to see if passwords match usernames.
correct_login = False
admin_login = False
task_list = []
credentials = {}

# To avoid repeating ourselves, we create a number of functions to perform different actions.
# This function displays options available to admin and returns the user's choice.
def adminOptions():
	options = input('''Please select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
s - statistics
e - exit
Enter your selection: ''')
	return options

# This function displays options available to others and returns the user's choice.
def normalOptions():
	options = input('''Please select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
Enter your selection: ''')
	return options

# This function allows the user to register a new user.
def registerUser():
	new_user = input("Enter a new username: ")
	new_password = input("Enter a new password: ")
	confirm_password = input("Confirm the new password: ")
	while new_password != confirm_password: # The new password and confirmed password need to match.
		print("The passwords do not match. Please try again.")
		new_password = input("Enter a new password: ")
		confirm_password = input("Confirm the new password: ")
	else: # If the passwords match, the username and password will be add to the user file.
		with open('user.txt', 'a') as user_f: # The file is opened in append so that the original contents don't get written over.
			user_f.write(f"\n{new_user}, {new_password}")

# This function allows the user to add a new task.
def addTasks():
    task_username = input("Enter a username to assign the task to: ")
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter the task description: ")
    task_assigned = datetime.datetime.now().strftime("%d/%m/%Y") # This gets the current date.
    task_duedate = input("Enter the date the task is due: ")
    task_complete = "No" # New tasks are automatically set as uncompleted.
    with open('tasks.txt', 'a') as tasks_f: # This writes the new task to the tasks file without overwriting the original contents.
    	tasks_f.write(task_username + "\n" + task_title + "\n" + task_description + "\n"
                		+ task_duedate + "\n" + task_assigned + "\n" + task_complete + "\n")

# This function allows the user to view all the tasks in the tasks file.
def viewAll():
	with open('tasks.txt', 'r') as tasks_f:
		for line in tasks_f:
			task_list.append(line.strip("\n")) # The task elements are added to a list for ease of use.
		for count in range(0, len(task_list), 6): # This code will run for every 6 items in the task list.
			print(f"Task username: {task_list[count]}")
			print(f"Task title: {task_list[count + 1]}")
			print(f"Task description: {task_list[count + 2]}")
			print(f"Date assigned: {task_list[count + 3]}")
			print(f"Due date: {task_list[count + 4]}")
			print(f"Complete: {task_list[count + 5]}")

# This function allows the user to view the tasks assigned to their username.
def viewMy():
	with open('tasks.txt', 'r') as tasks_f:
		for line in tasks_f:
			if username in line: # The 6 lines containing the task details will only be printed out if the task begins with the user's username.
				print(f"Task username: {line}", end = "")
				print(f"Task title: {next(tasks_f)}", end = "")
				print(f"Task description: {next(tasks_f)}", end = "")
				print(f"Date assigned: {next(tasks_f)}", end = "")
				print(f"Due date: {next(tasks_f)}", end = "")
				print(f"Complete: {next(tasks_f)}")

# This function allows the user to view the number of tasks and users currently in each of the respective files.
def statView():
	num_tasks = 0 # The number of tasks and users is initialised to 0.
	num_users = 0
	with open('tasks.txt', 'r') as tasks_f:
		for line in tasks_f: # For each line in the tasks file, the tasks count increases by 1.
			num_tasks += 1
		num_tasks /= 6 # The result is divided by 6 as 6 lines comprise a task.
	with open('user.txt', 'r') as user_f:
		for line in user_f: # For each line in the user file, the users count increases by 1.
			num_users += 1
	# The results are printed to the user.
	print(f"The total number of tasks is: {int(num_tasks)}")
	print(f"The total number of users is: {num_users}")

# This code fills the credentials dictionary with the login information.
# Each key in the dictionary is the username and each password is the value.
with open('user.txt', 'r') as user_f:
	for line in user_f:
		user, pwd = line.strip().split(',')
		credentials[user] = pwd.strip(" ")

# This code gets a username and password from the user.
username = input("Enter username: ")
password = input("Enter password: ")

# This checks if the username and password belong to admin.
if username == "admin":
	while password != credentials[username]:
		if password != credentials[username]: # If the password does not match the admin's password, the user must try again.
			print("Incorrect password. Please try again.")
			password = input("Enter password: ")
		else: # If the admin username and password match, admin login is set to True.
			print("Admin login successful.")
	admin_login = True

# This code allows other users to login.
else:
	# First the username is checked to see if it is in the user file.
	while username not in credentials:
		if username not in credentials: # If the username entered in not in the user file, the user must try again.
			print("Username incorrect. Please try again.")
			username = input("Enter username: ")
		else: # If the username is in the user file, the password is checked.
			print("Username correct.")

	# This code checks if the password entered matches the username entered.
	while password != credentials[username]:
		if credentials[username] != password: # If the password does not match the username, the user must try again.
			print("Password incorrect. Please try again.")
			password = input("Enter password: ")
		else: # If the password matches the valid username, correct login is set to True.
			print("Password correct.")
	correct_login = True

# This code will run if admin logs in.
if admin_login == True:
	options = adminOptions()

	# If a valid option is not selected, the user will see an error code and be prompted to try again.
	while options != "r" and options != "a" and options != "va" and options != "vm" and options != "s" and options != "e":
		print("ERROR: Invalid selection. Please try again.")
		options = adminOptions()

	# The following code will run based on the user's choice given the options menu.
	# It makes use of the functions defined earlier.
	if options == "r":
		registerUser()

	elif options == "a":
		addTasks()
		new_task = input("Would you like to add another task? 1 = 'Yes', 2 = 'No': ") # The user is given the choice to add another task.
		while new_task == "1":
			addTasks()
			new_task = input("Would you like to add another task? 1 = 'Yes', 2 = 'No': ") # As long as the user selects yes, they will be able to add a new task.

	elif options == "va":
		viewAll()

	elif options == "vm":
		viewMy()

	elif options == "s":
		statView()

	# If the user selects 'e', the program will exit.
	else:
		sys.exit()            



# If the username and password match and are in user.txt, the options menu will be displayed.
if correct_login == True:
    options = normalOptions()

    #This code will run if the user selects an invalid option.
    while options != "a" and options != "va" and options != "vm" and options != "e":
        print("ERROR: Invalid selection. Please try again.")
        options = normalOptions()
                
    # The following code will run based on the user's choice given the options menu.
	# It makes use of the functions defined earlier.
    if options == "a":
        addTasks()
        new_task = input("Would you like to add another task? 1 = 'Yes', 2 = 'No': ") #This gives the user the opportunity to add another task.

        while new_task == "1":
            addTasks()
            new_task = input("Would you like to add another task? 1 = 'Yes', 2 = 'No': ")

    elif options == "va":
        viewAll()
            
    elif options == "vm":
        viewMy()

    else:
        sys.exit()