#Birthday Hide and Seek Game
print("welcome to my first game!")

name = input("What is your name? ").lower()
is_birthday = bool(input("Is today your birthday? (True/False) "))

if name == "lisha" and is_birthday is True:
    print("ITS YOUR BIRTHDAY!!")
    print("Hi Lisha, welcome to your birthday game!")
    print("in order to get your present you will need to find 5 codes which are hidden throughout our flat.")
    ans = input("Are you ready to play? (yes/no) ").lower()
    if ans == "yes":
        print("The rules are simple, each time you find a code it will give you a hint for how to find the next one.")
        print("when you have found the final code it will lead you to the key to open the lock box!")
        ans = bool(input("ready to proceed? "))
        if ans is True:
            print("The first code is hidden with your guilty pleasure... get your hands off they are mine!!")
            code1 = input("input the first code: ").lower()
            if code1 == "catbirdewstar"
        else:
            print("urgh, greys anatomy it is then!!")
    else:
        print("oh.... thats rude....")
else:
    print("Unlucky, this game is for Lisha")

