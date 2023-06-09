def show_question(questions, examples, answer):
    options = ['a', 'b', 'c', 'd']
    our_answer = []
    for x in range(0, len(questions)):
        print(questions[x])
        print(examples[x])
        option = input('choose a answer type: a, b, c or d: ')
        our_answer.append(option)
    return check_question(our_answer, answer)


def check_question(our_answer, answer):
    result = 0
    for x in range(0, len(answer)):
        if our_answer[x] == answer[x]:
            result += 1
    return count_good_answer(result)


def count_good_answer(result):
    if result >= 2:
        return 'Good job! You pass the exam, you got ' + str(result/4*100)+'%'
    else:
        return 'Unfortunately, you dont pass the exam, you got ' + str(result/2*100)+'%'


# questions
questions = ['1. Who developed Python Programming Language?', '2. Which type of Programming does Python support?',
             '3. Is Python case sensitive when dealing with identifiers?', '4. Which of the following is the correct extension of the Python file?']

examples = ['''a) Wick van Rossum
b) Rasmus Lerdorf
c) Guido van Rossum
d) Niene Stom''',
            '''a) object-oriented programming'
b) structured programming
c) functional programming
d) all of the mentioned''',
            '''a) no
b) yes
c) machine dependent
d) none of the mentioned''',
            '''a) .python
b) .pl
c) .py
d) .p''']

answer = ['c', 'b', 'd', 'c']

print(show_question(questions, examples, answer))
