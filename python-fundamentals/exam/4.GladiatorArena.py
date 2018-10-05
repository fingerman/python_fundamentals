'''

Gladius -> Heal -> 200
Gladius -> Support -> 250
Gladius -> Shield -> 250
Pesho -> BattleCry -> 400
Gladius -> Heal -> 250
Ave Cesar
'''


class Gladiator:
    def __init__(self, name):
        self.name = name
        self.techniques = {}

# add his technique or update his skill, only if the current technique skill is lower than the new value.
    def add_skill(self, technique_new, skill_new):
        if technique_new not in self.techniques:
            self.techniques[technique_new] = skill_new
        elif self.techniques[technique_new] < skill_new:
            self.techniques[technique_new] = skill_new

    def get_all_techniques(self):
        result = list(self.techniques.keys())
        return result

    def get_total_skills(self):
        result = sum(self.techniques.values())
        return result

    def print_self(self):
        print(f"{self.name}: {str(self.get_total_skills())} skill")

# sort the techniques first by skill(value of the dict) in descending order and then by name in ascending order
        sorted_techniques = dict(
            sorted(self.techniques.items(), key=lambda kvp: (-kvp[1], kvp[0])))

        for tech in sorted_techniques:
            print(f"- {tech} <!> {self.techniques[tech]}")


gladiators = {}
line = input()

while line != "Ave Cesar":
    tokens = [x.strip() for x in line.split()]
    if len(tokens) == 5:
        name = tokens[0]
        technique = tokens[2]
        skill = int(tokens[4])
        if name not in gladiators:  # add the gladiator if he is not present
            gladiators[name] = Gladiator(name)
        gladiators[name].add_skill(technique, skill)
    else:
        first_name = tokens[0]
        second_name = tokens[2]

        if first_name in gladiators and second_name in gladiators:
            first_tech = gladiators[first_name].get_all_techniques()
            second_tech = gladiators[second_name].get_all_techniques()
            # check for duplicates
            common_tech = list(set(first_tech) & set(second_tech))

            if common_tech:
                first_skills = gladiators[first_name].get_total_skills()
                second_skills = gladiators[second_name].get_total_skills()

                if first_skills > second_skills:
                    gladiators.pop(second_name)
                elif first_skills < second_skills:
                    gladiators.pop(first_name)

    line = input()

# ordered by total skill in desecending order,
# then ordered by name of the technique (key of the dict) in ascending order.
sorted_gladiators = dict(sorted(
    gladiators.items(), key=lambda kvp: (-kvp[1].get_total_skills(), kvp[0])))


for gladiator in sorted_gladiators.values():
    gladiator.print_self()

'''
Problem 4 – Arena Tier
Pesho is a pro gladiator, he is struggling to become master of the Arena. 
You will receive several input lines in one of the following formats:
"{gladiator} -> {technique} -> {skill}"
"{gladiator} vs {gladiator}"
The gladiator and technique are strings, the given skill will be an integer number. 
You need to keep track of every gladiator. 

When you receive a gladiator and his technique and skill, add him to the gladiator pool, if he isn`t present, 
else add his technique or update his skill, only if the current technique skill is lower than the new value.

If you receive "{gladiator} vs {gladiator}" and both gladiators exist in the tier, they duel with the following rules:
Compare their techniques, if they got at least one in common, 
the gladiator with better total skill points wins and the other is demoted from the tier -> remove him.

If they don`t have techniques in common, the duel isn`t happening and both continue in the Season.
You should end your program when you receive the command "Ave Cesar".
 
At that point you should print the gladiators, ordered by total skill in desecending order, 
then ordered by name in ascending order. 
Foreach gladiator print their technique and skill, ordered desecending, 
then ordered by technique name in ascending order


Input / Constraints
You will receive input on several lines.
•	The input comes in the form of commands in one of the formats specified above.
•	Gladiator and technique will always be one word string, containing no whitespaces.
•	Skill will be an integer in the range [0, 1000].
•	There will be no invalid input lines.
•	The programm ends when you receive the command "Ave Cesar".

Output
•	The output format for each gladiator is:
"{gladiator}: {totalSkill} skill"
"- {technique} <!> {skill}"

Input
Pesho -> BattleCry -> 400
Gosho -> PowerPunch -> 300
Stamat -> Duck -> 200
Stamat -> Tiger -> 250
Ave Cesar

Output
Stamat: 450 skill
- Tiger <!> 250
- Duck <!> 200
Pesho: 400 skill
- BattleCry <!> 400
Gosho: 300 skill
- PowerPunch <!> 300

Input
Pesho -> Duck -> 400
Julius -> Shield -> 150
Gladius -> Heal -> 200
Gladius -> Support -> 250
Gladius -> Shield -> 250
Pesho vs Gladius
Gladius vs Julius
Gladius vs Gosho
Ave Cesar


Output
Gladius: 700 skill
- Support <!> 250
- Shield <!> 250
- Heal <!> 200
Pesho: 400 skill
- Duck <!> 400

----------
Gladius -> Heal -> 200
Gladius -> Support -> 250
Gladius -> Shield -> 250
Gladius -> Heal -> 250
Ave Cesar

Pesho -> Duck -> 400
Julius -> Shield -> 150
Gladius -> Heal -> 200
Ave Cesar


'''
