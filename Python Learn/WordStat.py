def WordCounter(_str):
    wordRegistre = []

    word = ""

    for letter in str(_str):
        if letter.isspace():
            wordRegistre.append(word)
            word = ""
        else:
            word += letter.lower()

    if word != "":
        wordRegistre.append(word)

    dictionary = {}

    for word in wordRegistre:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return dictionary


def main():

    dictionary = WordCounter("Hello world hello test hello")

    key = ""
    nbWord = 0
    for word in dictionary:
        if key == "":
            key = word
        elif dictionary[word] > dictionary[key]:
            key = word

        nbWord += 1

        print(word, dictionary[word])

    print("number of word :", len(nbWord))
    print("unique word :", len(dictionary))
    print("most frequent world :", key)


main()
