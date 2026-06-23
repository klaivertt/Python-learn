import time
import threading

def DisplayLine(text):
    print(f"\r{text:<40}", end="", flush=True)

def GetFloat(_str):
    while True:
        try:
            nb = float(input(_str))
            
            if nb > 0:
                return nb
            else:
                print("Please enter an float greater than 0")
        except ValueError : 
            print("Please enter an valid float")

def StopWatchLoop(_stopEvent):
    
    times = float(0)
    start = time.time()
    while not _stopEvent.is_set():
        current = time.time()
        elapsed = current - start
        times += elapsed
        start = current
        DisplayLine(f"Time : {times:.2f} seconds")

def main():
    choice = ""
    while True:    
        choice = input("Choice between, 'timer' or 'stopwatch' : ")
        
        if choice == "timer" or choice == "stopwatch" :
            break
        else :
            print("Please enter 'timer' or 'stopwatch'")    
    
    if choice == "timer":
        times = GetFloat("Enter time remaining : ")
        start = time.time()
        
        while True:
            current = time.time()
            elapsed = current - start
            times -= elapsed
            start = current
            
            time.sleep(0.01)
            
            if times <= 0:
                DisplayLine("Finished")
                print()
                break
            else:
                DisplayLine(f"Time remaining : {times:.2f} seconds")
    
    
    if choice == "stopwatch":
        times = 0
        
        stopEvent = threading.Event()
        thread = threading.Thread(target=StopWatchLoop, args=(stopEvent,))
        thread.start()
        
        while True:
            
            print("Type 'stop' : ")
            choice = input("")
            
            if choice != "stop" :
                print("Please enter stop")
            else :
                stopEvent.set()
                thread.join()
                break
        

if __name__ == "__main__":
    main()