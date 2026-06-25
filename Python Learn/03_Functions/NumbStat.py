import random 

def LoadNumber(_nb):
    
    nb = []
    
    for _ in range(_nb):
        rng = random.randint(0 , 200)
        nb.append(rng)
        
    return nb

def GetInt(_str, _min = 4):
    while True:
        try:
            nb = int(input(_str))
            if _min < nb :
                return nb
            else:
                print(f"Enter a int upper than {_min}")
        except ValueError:
            print("Please enter an valid int")
        
def DictionaryNumber(_nb):
    
    dicNb = {}
    
    for nb in _nb:
        if nb in dicNb:
            dicNb[nb] += 1
        else:
            dicNb[nb] = 1
    
    return dicNb

def main():
    
    nb = GetInt("Choose the number of digits you want : ")
    
    table = LoadNumber(nb)
    
    dictionary = DictionaryNumber(table)
    
    minNbs = []
    minNb = 201
    maxNbs = []
    maxNb = 0
    median = 0
    totalnb = len(table)
    total = 0
    
    for number in dictionary:
        print(number, " : ", dictionary[number])
        
        if (dictionary[number] < minNb):
            minNb = dictionary[number]
            minNbs = [number]
        elif (dictionary[number] == minNb):
            minNbs.append(number)
            
        if (dictionary[number] > maxNb):
            maxNb = dictionary[number]
            maxNbs = [number]
        elif (dictionary[number] == maxNb):
            maxNbs.append(number)
            
        
        total += number
    
    median = total % totalnb
    
    print("Min number:")
    
    for numb in minNbs:
        print (numb,"Total :", dictionary[numb])
    
    print("Max Number:")
    for numb in maxNbs:
        print (numb, "Total :",dictionary[numb])
    
    print(f"Median : {median}")
    
    print(f"Total : {total}")
    
main()           
    