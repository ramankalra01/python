import start_chat
from spy_details import spy, Spy

question = "Continue as guest Y/N"
existing = raw_input(question)

if existing.upper() == "Y":
    print "Welcome %s %s age %s rating %f" %(spy.salutation,spy.name,spy.age,spy.rating)
    if spy.is_online == True:
        print "you are online"
        start_chat.start_chat(spy)
    else:
        print "You are currently offline"


else:
    spy.name = raw_input("Welcome to spy chat, enter your name: ")

    if len(spy.name) > 0:
    # Start writing from here now. See how this is under the if statement?


        print 'Welcome ' + spy.name + '. Glad to have you back with us.'

        spy.salutation = raw_input("Should I call you Mister or Miss?: ")

        spy.name = spy.salutation + " " + spy.name

        print "Alright " + spy.name + ". I'd like to know a little bit more about you before we proceed..."




        #some new variables
        spy.age = 0
        spy.rating = 0.0
        spy.is_online = False

        spy.age = int(raw_input("what is your age?"))

        print int(spy.age)

        spy.age = int(spy.age)

        # Age cannot be less than 12 and no spies greater than 50 are allowed to exist
        # Nested if
        if spy.age > 12 and spy.age < 50:

            spy.rating = raw_input("What is your spy rating?")
            spy.rating = float(spy.rating)

            if spy.rating > 4.5:
                print 'Great ace!'
            elif spy.rating > 3.5 and spy.rating <= 4.5:
                print 'You are one of the good ones.'
            elif spy.rating >= 2.5 and spy.rating <= 3.5:
                print 'You can always do better'
            else:
                print 'We can always use somebody to help in the office.'

            spy.is_online = True
            print "Authentication complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"
        else:
            print 'Sorry you are not of the correct age to be a spy'
    else:
        print "A spy needs to have a valid name. Try again please."