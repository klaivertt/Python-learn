def IsPalindrome(_str):
    reversedWord = ""
    
    for letter in reversed(_str):
        reversedWord += letter
    
    if reversedWord != _str:
            return False
    else :
        return True

def main():
    
    word = input("Enter a unique word : ").strip().lower()
    
    if (IsPalindrome(word)):
        print("This word is a palindrome")
    else :
        print("This word isn't a palindrome")

main()