def MovingAverage(i, avg):
    new_num = float(input("what's your number: "))
    avg = (i * avg +  new_num)/ (i+1)
    i += 1
    print("Moving Avergae is: ", avg)
    MovingAverage(i, avg)

MovingAverage(0, 0)
    
