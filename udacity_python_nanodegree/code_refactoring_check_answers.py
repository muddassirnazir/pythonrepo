def check_answers(my_answers, answers):

# Checks the five answers provided to a multiple choice quiz and returns the results.
    results = [None, None, None, None, None]
    for i in range(len(my_answers)):
    #    print(my_answers[i])
    #    print(answers[i])
    #    print(results[i])
        if my_answers[i] == answers[i]:
            results[i] = True
        else:
            results[i] = False
    #    print(results[i])

    count_correct = 0
    count_incorrect = 0
    for result in results:
        if result == True:
            count_correct += 1
        if result != True:
            count_incorrect += 1
    if count_correct / 5 > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect / 5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."

print (check_answers([1,2,3,4,5],["badger","badger","badger","badger","badger"]))

"""
def check_answer(my_answer, answer):
    if my_answer == answer:
        return True
    else:
        return False

def check_answers(my_answers,answers):
    #Checks the five answers provided to a multiple choice quiz and returns the results.
    results = []
    for i in range(len(my_answers)):
        results.append(check_answer(my_answers[i], answers[i]))
    count_correct = 0

    for result in results:
        if result:
            count_correct += 1

    if count_correct/len(results) > 0.7:
        return "Congratulations, you passed the test!"
    elif (len(results) - count_correct)/len(results) >= 0.3:
        return "Unfortunately, you did not pass."
"""
