def rev_sentence(sentence):
    sent = ""
    a = ""
    for letters in sentence:
        if letters == " ":
            sent = sent + a
            a = ""
        else:
            a = a + letters
    print(sent)
rev_sentence("my name is")
        
        
