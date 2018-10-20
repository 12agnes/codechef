
def Whats_in_name():

    mystr = 'Mohndas KaramChand gandhi'
    wordList = mystr.split()

    if len(wordList)>3:
        print("not valid name")
    elif len(wordList) == 3:
        capitalized =  [x[0].upper() for x in wordList]
        print(capitalized)


        for list, string_list in zip(mystr, capitalized):
            print(list, string_list)

    # new_mystr = ' '.join("'{}'".format(word) for word in mystr.split(' '))
    # print(new_mystr)
    result = []
    for i in range(0, len(wordList)):
        splited = mystr.split()
        result.append(wordList[:3])
    print(result[0])


if __name__ == "__main__":
    Whats_in_name()
