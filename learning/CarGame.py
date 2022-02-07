
play = True
started = False
while play:
    action = input(">").lower()
    if action == 'help':
        print(" start - to start the car \n stop - to stop the car \n quit - to exit")
    elif action == 'start':
        if started:
            print("Car is already started, WHAT ARE YOU DOING???")
        else:
            started = True
            print("Car started, ready to go")
    elif action == 'stop':
        if not started:
            print("Car is already stopped, WHAT ARE YOU DOING")
        else:
            started = False
            print("Car Stopped")
    elif action == 'quit':
        print("Thank you for playing")
        break
    else:
        print("I don't understand that")


