def greet():
    name = input("Enter your name: ")
    time = int(input("Enter the time (0-23): "))

    if 0 <= time <= 12:
        print(f"Good morning, {name}!")
    elif 13 <= time <= 17:
        print(f"Good afternoon, {name}!")
    elif 18 <= time <= 23:
        print(f"Good evening, {name}!")

greet()
