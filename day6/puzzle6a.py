fin = open('input.txt')
answers = fin.read().split('\n\n')

count = 0
for answer in answers:
    individual = answer.split('\n')
    yes_questions = set()
    for line in individual:
        for char in line:
            yes_questions.add(char)
    count += len(yes_questions)

print(count)
