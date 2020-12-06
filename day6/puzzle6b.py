fin = open('input.txt')
answers = fin.read().split('\n\n')

count = 0
for answer in answers:
    individual = answer.split('\n')
    yes_questions = set('abcdefghijklmnopqrstuvwxyz')
    for line in individual:
        line_yes = set()
        for char in line:
            line_yes.add(char)
        yes_questions = yes_questions.intersection(line_yes)
    count += len(yes_questions)

print(count)
