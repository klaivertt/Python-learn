def LetterCounter(_str) :
    letterDic = {}
    if (_str != "") :
        for letter in str(_str) :
            if not letter.isspace() :     
                if letter in letterDic :
                    letterDic[letter] += 1
                else :
                    letterDic[letter] = 1
        
    return letterDic


def main():
    string = input("Write a sentence :")
    
    dictionary = LetterCounter(string)
    
    for letter in dictionary :
        print(letter, dictionary[letter])
            
main()