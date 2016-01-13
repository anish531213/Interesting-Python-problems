import urllib
def proof_read():
    text = open("/home/anish/Desktop/anish.txt")
    text_content = text.read()
    print(text_content)
    text.close()
    check_proof(text_content)
def check_proof(text_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_check)
    output = connection.read()
    if "true" in output:
        print("There is fowl word")
    else:
        print("There is no fowl words")
    connection.close()
    
proof_read()
    
