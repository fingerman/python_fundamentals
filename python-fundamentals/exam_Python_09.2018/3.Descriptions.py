'''
Problem 3. Descriptions
Input / Constraints
You will receive descriptions of people. For each in a single row. Your role will be to decide if the description contains valid information or not, If contains you should store the data in the database.
When you receive the command "make migrations" you should print all info you have stored.
A valid person's information in a description will contain the following:
•	a string "name is" after which a single space and a name (first name and last name), separated by single space. Both names should start with capital letter.
•	single space before and after that two digits representing the person's age after which we have single space and the word "years". A valid age is between >9 and age<100
•	birthday date - before the date we should have the word "on" after that single space and then date in exact format dd-mm-yyyy (months will be digits and the date should be separated with "-" {dd-mm-yyyy})
•	Every description should end with '.'(dot) after the date of birth.

If one of this requirements is not valid DO NOT include any of the information for the person in the database.
Output
After the command "make migrations" you should print the info in the following format:
“Name of the person: {person's name}.”
“Age of the person: {age of the person}.”
“Birthdate of the person: {Birthdate of the person}.”
If date base is empty print:
"DB is empty"

Hello,everyone my name is Maria Mariova. I am 22 years old. was born on 22-06-1994.


Examples
Input	Output	Comments
Hello,everyone my name is Maria Mariova. I am 22 years old. was born on 22-06-1994.
Hello,everyone my name is Yan Familiov. I am 10 years old. was born on 22-06-2008.
make migrations
	Name of the person: Maria Mariova.
Age of the person: 22.
Birthdate of the person: 22-06-1994.
Name of the person: Yan Familiov.
Age of the person: 10.
Birthdate of the person: 22-06-2008.
	Because the first example is valid we add the person information to our data base.
The second example is also valid so we add the info to the data base
Input	Output	Comments
Hello,everyone my name is Py Thon. I am 18 years old. was born on 16-10-2000.
Hello,everyone my name is Ja Va. I am 20 years old. was born on kogato si iskam.
make migrations
	Name of the person: Py Thon.
Age of the person: 18.
Birthdate of the person: 16-10-2000.
	First row is valid so we add it to the datebase
Second example is not valid, because the birthday is not in the requested format.

'''