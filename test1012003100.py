def GetPlayRecord():
    f = open('hangman_play_record.txt', 'r')
    for i in f:
        lst = i.strip().split(',')
    f.close()
    return lst

ans = GetPlayRecord()
print(ans)
