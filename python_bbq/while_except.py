import random
import operator


while True:
    try:
        inp = input('Write number of tasks: ')
        int(inp)
        break

    except:
        print('That is not an integer !')


ops = {'added to': operator.add,
       'minus': operator.sub,
       'dividied by': operator.truediv,
       'multiplied by': operator.mul}
correct = 0
int_input = int(inp)
for i in range(0, int_input):
    num1 = random.randint(-15, 15)
    num2 = random.randint(-15, 15)
    while num2 == 0:
        num2 = random.randint(-15, 15)
    op_name, op = random.choice(list(ops.items()))
    answer = op(num1, num2)
    answer = round(answer, 2)
    tried = 3
    for t in range(0, 3):
        print('What is {} {} {}?'.format(num1, op_name, num2))
        user_answer = float(input('Result is: (integer or float, with max 1 place after the decimal) '))
        #print(answer)
        if user_answer == answer:
            correct += 1
            print("Correct ! It makes ", answer)
            break
        else:
            tried -= 1
            if tried == 0:
                print("No, the correct answer is", answer)
            else:
                print("No, try again. You have ", tried, "more tries left")
print()
print('Game Over !')
print("You were asked {} questions and answered {} of them correctly".format(inp, correct))
