'''
Input

Pesho-Java-84
Gosho-C#-70
Gosho-C#-84
Annabel-C#-84
Kiro-C#-94
exam finished

Output

Results:
Kiro | 94
Gosho | 84
Pesho | 84
Submissions:
C# - 3
Java - 1

'''


class Student:
    def __init__(self, name):
        self.name = name
        self.results = {}

    # add his language and/or update points, only if the current pints are lower than the new value.
    def add_results(self, language_new, points_new):
        if language_new not in self.results:
            self.results[language_new] = points_new
        elif self.results[language_new] < points_new:
            self.results[language_new] = points_new

    def get_total_points(self):
        result = sum(self.results.values())
        return result

    #to do - get number of submisions
    def get_language(self):
        result = sum(self.results.keys())
        return result

    def print_self(self):
        print(f"{self.name} | {str(self.get_total_points())}")

    def print_submissions(self):
        print(f"{str(self.get_language())}")



students = {}

line = input()
while line != 'exam finished':
    tokens = [x for x in line.split('-')]
    if len(tokens) == 3:
        name = tokens[0]
        language = tokens[1]
        points = int(tokens[2])
        if name not in students:  # add the student if he is not present
            students[name] = Student(name)
            # to do - add language and points
        students[name].add_results(language, points)
    else:
        name_banned = tokens[0]

    line = input()


sorted_students = dict(sorted(
    students.items(), key=lambda kvp: (-kvp[1].get_total_points(), kvp[0])))

print("Results:")
for student in sorted_students.values():
    student.print_self()

'''
for student in sorted_students.values():
    student.print_submissions()
'''


'''
Problem 4 – SoftUni Exam Results
Judge statistics on the last Programing Fundamentals exam was not working correctly, so you have the task to take all the submissions and analyze them properly. You should collect all the submission and print the final results and statistics about each language that the participants submitted their solutions in.
You will be receiving lines in the following format: "{username}-{language}-{points}" until you receive "exam finished". You should store each username and his submissions and points. 
You can receive a command to ban a user for cheating in the following format: "{username}-banned". In that case, you should remove the user from the contest, but preserve his submissions in the total count of submissions for each language.
After receiving "exam finished" print each of the participants, ordered descending by their max points, then by username, in the following format:
Results:
{username} | {points}
…
After that print each language, used in the exam, ordered descending by total submission count and then by language name, in the following format:
Submissions:
{language} – {submissionsCount}
…
Input / Constraints
Until you receive "exam finished" you will be receiving participant submissions in the following format: 
"{username}-{language}-{points}".
You can receive a ban command -> "{username}-banned"
The points of the participant will always be a valid integer in the range [0-100];
Output
•	Print the exam results for each participant, ordered descending by max points and then by username, 
in the following format: 
Results:
{username} | {points}
…
•	After that print each language, ordered descending by total submissions and then by language name, 
in the following format:
Submissions:
{language} – {submissionsCount}

Input 2

Pesho-Java-91
Gosho-C#-84
Kiro-JavaScript-90
Kiro-C#-50
Kiro-banned
exam finished

Output 2

Results:
Pesho | 91
Gosho | 84
Submissions:
C# - 2
Java - 1
JavaScript - 1



'''
