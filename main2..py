command = ""
started = False
while command != "quit":
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is started!!!")
        else:
            started = True
            print("Car is already started!!")
    elif command == "stop":
        if not started:
            print("Car is stopped!")
        else:
            started = False
            print("Car is already stopped")
    elif command == "help":
        print('''
start -to start the car
stop - to stop the car
quit - to exit 
        ''')
    elif command == "quit":
        break
    else:
        print("Sorry! I don't understand that")