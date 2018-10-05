class Exercise:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = [*problems]

    def get_info(self):
        info = f'{self.topic}\n' \
               f'Problems for exercises and homework for the "{self.course_name}" course @ SoftUni.' \
               f'\nCheck your solutions here: {self.judge_contest_link}\n'

        for p in range(len(self.problems)):
            if p == len(self.problems) - 1:
                info += f'{p + 1}. {self.problems[p]}'
            else:
                info += f'{p + 1}. {self.problems[p]}\n'
        return info


line = input()
exercises = []
while line != 'go go go':
    inp1, inp2, inp3, list_inp = line.split(' -> ')
    list_inp = list_inp.split(', ')
    exercises.append(Exercise(inp1, inp2, inp3, list_inp))
    line = input()

for exercise in exercises:
    print(exercise.get_info())


'''
ObjectsAndSimpleClasses -> ProgrammingFundamentalsExtended -> https://judge.softuni.bg/Contests/439 -> Exercises, OptimizedBankingSystem, Animals, Websites, Boxes, BoxIntersection, Messages
go go go


'''