def WordCounter(_str):
    wordRegistered = []
    word = ""
    for letter in str(_str):
        if letter.isspace():
           if word != "":
                wordRegistered.append(word)
                word = ""
        else :
            word += letter
    
    if word != "":
        wordRegistered.append(word)
        
    wordDic = {}
    for word in wordRegistered:
        if word in wordDic:
            wordDic[word] += 1        
        else:
            wordDic[word] = 1
    
    return wordDic
        
        
        
        

def main():
    nbWorld = 0
    sentences = input("Write a text :").strip().lower()
    
    dictionary =  WordCounter(sentences)

    for word in dictionary:
        print(word, dictionary[word])

main()