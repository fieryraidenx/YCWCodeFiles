'''Warmup 1: Lists and Dictionaries Error Analysis'''

# Objective 1: Print "Jack" to the screen
students = ["Jack", "Vladimir", "Zachary", "Corey"]
print(students[2])

# Objective 2: Correct the syntax error
students = ["Jack", "Vladimir', "Zachary", "Corey"]

# Objective 3: Correct the runtime error in the if statement
students = ["Jack", "Vladimir", "Zachary", "Corey"]
if "Vladmir" in students:
	print("Found him!")
else:
	print("Keep looking for him!")

# Objective 4: Correct the syntax error
programming_languages = {
	"python": "good",
	"html": "good",
	"lisp": "no"
}

print("Python Review: " + str(programing_languaes["python"]))