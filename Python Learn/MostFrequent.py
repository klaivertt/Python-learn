def WordCounter(_str):
    wordRegistered =  []
    
    word = ""
    for letter in str(_str) : 
        if letter.isspace():
            wordRegistered.append(word)
            word = ""
        else :
            word += letter
    
    if word != "":
        wordRegistered.append(word)
    
    wordDictionary = {}
    
    for word in wordRegistered:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else :
            wordDictionary[word] = 1
    
    return wordDictionary

def main():
    
    dictionary = WordCounter("hello world hello test hello")
    
    key = ""
    for word in dictionary:
        if key == "" :
            key = word
        elif dictionary[word] > dictionary[key] :
            key = word
        
        print(word, dictionary[word])

    print("Most common world", key, dictionary[key])
    
main()