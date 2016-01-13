def WaterCollected(l):
    start = l[0]
    mid = l[0]
    count = 0
    answer = 0
    temp = 0
    count2 = 0
    for i in range(1, len(l)):
        if l[i] >= start:
            temp = (start-mid)*count
            start = l[i]
            mid = start
            count = 0
            answer += temp
            temp = 0
        else:
            if l[i] < l[i-1]:
                temp += (mid -l[i])
                count += 1
                count2 += 1
            else:
                mid = l[i]
                temp -= (start-mid)*count2
                answer += temp
                count2 = 0
                count += 1
            print(temp)
    return answer
                        
print(WaterCollected([7, 2, 3, 4, 6, 5, 4, 2, 1, 8]))
                          
            
            
        
