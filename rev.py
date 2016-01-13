def reverse_sent(sentence):
    sumn = ""
    a = ""
    for letters in sentence:
        if letters == " ":
            sumn = a + sumn
            a = ""
        else:
            a = a + letters
    print(sumn)
 
reverse_sent("anish adhikari")
