dictionary={}

while True:
    try:
        input2=input("Give me a word\n")
        if input2 in dictionary.keys():
            print(dictionary[input2])
        else:
            dictionary[input2]=input("I don't know this word, please give me the meaning of it\n")
    except EOFError as e:
        break
