def GetInt(_str, _min = 0):
    while True:
        try:
            nb = int(input(_str))
            if nb > _min :
                return nb
            else :
                print(f"enter a int upper than {_min}")
        except ValueError:
            print("enter an valide int")

def GetCandidate(_str ,_nb):
    nb = _nb
    candidate = []
    while nb > 0:
        name = input(_str)
        if not name in candidate:
            candidate.append(name)
            nb -= 1
        else :
            print(f"This candidate: {name} already present in the list")
    
    return candidate       
    
def DisplayCanditate(_str ,_candidates):
    print(_str)
    for candidate in _candidates:
        print(candidate + " | ", end="")
    
    print()
    
def ChoiseCandidate(_str , _candidates):
    while True:
        name = input(_str)
        
        if name in _candidates:
            return name
        else :
            print("Enter an valid Name ")
            
def DisplayCurentVote(_vote):
      for candidate in _vote:        
        print(candidate, _vote[candidate])


def main():
    nbCandidate = GetInt("Enter number of candidate : ")
    nb = GetInt("Enter number of voting : ")
    candidates = GetCandidate("Enter Your candidate name : ", nbCandidate)
    vote = {}
    
    while nb > 0:
        
        DisplayCanditate("\nList of candidates : ", candidates)
        currentVote = ChoiseCandidate("Enter name of a Candidate to vote : ", candidates)
        if currentVote in vote:
            vote[currentVote] += 1
        else:
            vote[currentVote] = 1
        
        nb -= 1
        DisplayCurentVote(vote)
        
    maxVote = 0
    winners = []
    
    for candidate in vote:
        if vote[candidate] >  maxVote: 
            maxVote = vote[candidate]
            winners = [candidate]
        if vote[candidate] == maxVote:            
            winners.append(candidate)
            
    if len(winners) == 1 :
        print(f"the winner is : {winners[0]}, with : {vote[winners[0]]} of vote")
    else :
        print("Draw between")
        for winner in winners:
            print(winner)
        print(f"With {maxVote} votes")

    

main()
