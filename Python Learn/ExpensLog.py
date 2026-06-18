import csv 

def ReadCSV(_filePath = "ExpensLog.csv"):
    try:
        with open(_filePath, "r") as file:
            return csv.reader(file)
    except FileNotFoundError:
        print(f"Files:  {_filePath} doesn't exist")
        
def WriteCSV(_filePath = "ExpensLog.csv"):
    try:
        with open(_filePath, "a") as file:
            return csv.writer(file)
    except FileNotFoundError:
        print(f"Files:  {_filePath} doesn't exist")

def SplitCSV(file):    
    for row in file:
        print(row)

def MenuChoise():
   
    while True:
        print("Choose a menu betwen :")
        print("Write | Read | Quit")
        choose = input("Your choice : ").split().lower()
        
        if choose == "write" or choose == "read" or choose == "Quit":
            return choose
        else :
            print("Please enter Write or Read or Quit")

def main():
    
    while True:
        menu = MenuChoise()
        
        if menu == "quit":
            break
        elif menu == "write":
            content = WriteCSV()
            if content is not None:
                ...
        else:
            content = ReadCSV()
            if content is not None:
                SplitCSV(content)

    
    
if __name__ == "__main__":
    main()