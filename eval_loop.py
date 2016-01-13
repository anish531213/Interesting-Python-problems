def eval_loop():
    a = ''
    while a != 'done':
        answer = input(' something to evaluate or enter done ')
        answer = answer.lower()
        if answer == 'done':
            a = answer
        elif answer != 'done':
            z = eval(answer)
            print (z)
    return (z)
eval_loop()
