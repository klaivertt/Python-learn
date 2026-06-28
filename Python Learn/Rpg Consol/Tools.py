def GetInt(_str, _min = 0, _max = 10):
    while True:
        try:
            nb = int(input(_str))
            
            if _min < nb < _max:
                return nb
            else:
                print(f"Please enter en int between {_min} and {_max}")
        
        except ValueError:
            print("Please enter an valid int")