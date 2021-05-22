done = False
while not done:
    print("Menu")
    print("E1 - Example 1")
    print("Q - Quit")
    choice = input("Choice: ")
    if choice == "E1":
        print("Example 1")
        for x in range(2,11,2):
            print(x)
    elif choice == "Q":
        print("Exiting Game!")
        done = True