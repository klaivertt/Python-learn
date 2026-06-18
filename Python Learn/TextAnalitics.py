def ReadTextFile(_filePath="Ligne.txt"):
    try:
        with open(_filePath, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Le fichier '{_filePath}' est introuvable.")
        return None

def Count(_files):
    carateres = 0
    ligneCount = 0
    words = 0
    
    word = ""
    
    for char in _files :
        carateres += 1
        word += char
        if str(char).isspace() and word != "" :
            words += 1
            word = ""
        
        if str(char) == "\n":
            ligneCount += 1
            
    
    print("Number of charactere :", carateres)
    print("Number of word:", words)
    print("Number of ligne :", ligneCount)
        

def main():
    content = ReadTextFile()
    
    if content is not None:
        Count(content)
    


if __name__ == "__main__":
    main()