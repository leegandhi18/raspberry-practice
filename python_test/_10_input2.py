try:
    while True:
        userInput = input(">>>")
        print("You entered", userInput)
        if userInput == "quit()":
            print("bye...")
            break
except KeyboardInterrupt:
    pass
