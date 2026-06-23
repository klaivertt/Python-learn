import csv 

def GetInt(_str):
    while True:
        try:
            return int(input(_str))
        except ValueError:
            print("Please enter an valid int")
        
def AskLigne(_str):
    print(_str)

    categorie = input("Catégorie de la dépense : ").strip()
    montant = GetInt("Montant de la dépense : ")

    return [categorie, montant]

def SaveFile(_fileName):
    expense = AskLigne("What you want to write in your ExpensLog ?")
    with open(_fileName, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(expense)

def ReadFiles(_fileName):
    with open(_fileName, "r") as file:
        read = csv.reader(file)
        
             
        total = 0
        for row in read:
            print(f"Category {row[0]}: {row[1]}")   
            total += float(row[1])    

        print(f"Total des dépenses : {total}")
        
        

def MenuChoise():
    while True:
        print("Choose a menu betwen :")
        print("Write | Read | Quit")
        choisse = input("Your choice : ").strip().lower()
        
        if choisse == "write" or choisse == "read" or choisse == "quit":
            return choisse
        else :
            print("Please enter Write or Read or Quit")
            

def main():
    filePath = "ExpensLog.csv"
    while True:
        menu = MenuChoise()
        
        if menu == "quit":
            break
        elif menu == "write":
            SaveFile(filePath)
        else:
            ReadFiles(filePath)
                

    
    
if __name__ == "__main__":
    main()