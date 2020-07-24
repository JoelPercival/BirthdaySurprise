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
        if ans is True: # start of the game
            print("The first code is hidden with your guilty pleasure... get your hands off they are mine!!") # first location is with the nuggets
            code1 = input("input the first code: ").lower()
            if code_1 == "catbirdewstar":
            	print("congratulations! you have got one step closer to the key!")
            	print("The next clue wont be so easy.. you're going to have to study for this one...") # second location in grad photo
            	code_2 = input("input the second code: ").lower()
            	if code_2 == "lishgotthemsmarts":
            		print("You are making this look far too easy...")
            		print("For this next one we are going to shake it up a bit!")
            		code_3 = input("input the third code: ").lower() # third location is in the cocktail shaker
            	else:
            		print("try, again!") # ensure this looped to offer multiple tries	
            else:
            	print("try again!") # ensure this looped to offer multiple tries
        else:
            print("urgh, greys anatomy it is then!!")
    else:
        print("oh.... thats rude....")
else:
    print("Unlucky, this game is for Lisha")

