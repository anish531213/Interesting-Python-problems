def count_seven(y, i):
    x = y % 10
    y = y//10
    if y!=0:
        if x == 7:
            i += 1
            count_seven(y, i)
        else:
            count_seven(y, i)
    else:
        print(i)
        
    
count_seven(77, 0)
    

        

        
        
  
    
        
