from Question import Question
questionPrompts = [
    "1. What is the color of Apple? \n (a) Red \n (b) Green \n (c) Yellow",
    "2. What is the color of Pomegranate? \n (a) Red \n (b) Green \n (c) Black",
    "3. What is the color of Orange? \n (a) Red \n (b) Orange \n (c) Yellow"
]

questions = [
    Question(questionPrompts[0], 'a'),
    Question(questionPrompts[1], 'a'),
    Question(questionPrompts[2], 'b'),
]

def MCQ(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt + "\n")
        if answer == question.answer:
            score+=1
    print("Your score is " + str(score) + '/' + str(len(questions)))

MCQ(questions)