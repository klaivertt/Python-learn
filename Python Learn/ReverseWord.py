def main():
    word = input("Write a word : ").strip()
    
    reversedWord = ""
    for letter in reversed(word) :
        reversedWord += letter
    
    
    print(reversedWord)
        
main()