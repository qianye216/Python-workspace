import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certern'
    elif answerNumber == 2:
        return 'Yes'


r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
