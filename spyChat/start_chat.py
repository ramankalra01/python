from steganography.steganography import Steganography
from datetime import datetime
#datetime.datetime.now shows current date and time
from spy_details import Spy,ChatMessages,friends
from termcolor import colored

current_time= datetime.now()
print current_time.strftime("%a, %d %b %Y %H:%M:%S")
now = datetime.now()




STATUS_DEFAULTS = ['My name is Pablo', 'Pablo Escobar', 'Hijo de Puta', 'Drug Lord']
#Enabling a function to start chat
def start_chat (spy):
    print "Authentication complete ! Welcome %s of age %d.You have spy rating of%.2f" %(spy.name,spy.age,spy.rating)

    status_rn = None
    show_menu = True
    while show_menu:
        menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
        menu_choices = raw_input(menu_choices)
        menu_choice = int(menu_choices)

        if menu_choice == 1:
            print "Update status"
            status_rn = update_status(status_rn)
        elif menu_choice == 2:
            print 'Add friend'
            add_friend()
        elif menu_choice == 3:
            print 'Send a secret message'
            send_message()
        elif menu_choice == 4:
            print  'Read a secret message'
            read_message()
        elif menu_choice == 5:
            print 'Read a chat history'
            read_existing_chat()
        elif menu_choice == 6:
            show_menu = False
#Enabling a function to update status
def update_status(status_rn):
    updated_status_msg = None

    if status_rn != None:
        print "Your current status message is: %s" %(status_rn) + "\n"
    else:
        print 'you don\'t have message currently \n'

    default = raw_input("Do you want to select status from defaults? Y/N")
    if default.upper() == "N":
        while True:
            new_status_msg = raw_input("Enter your status")
            if len(new_status_msg) < 25:
                break
            else:
                print "Status should not be more than 25 words"
        if len(new_status_msg) < 25:
            updated_status_msg = new_status_msg
            STATUS_DEFAULTS.append(new_status_msg)

    elif default.upper() == "Y":
        item_position = 1
        for message in STATUS_DEFAULTS:
            print "%d.%s"%(item_position,message)
            item_position = item_position+1

        select_status = int(raw_input("Select number corresponding to the status you want to use"))
        if len(STATUS_DEFAULTS) > select_status:
                updated_status_msg =  STATUS_DEFAULTS[select_status-1]

    else:
        print 'Please enter Y or N !'

    return(updated_status_msg)

#Enabling a function to add friend in the list
def add_friend():
    new_friend = Spy('','',0,0.0)
    while True:
        new_friend.name = raw_input("Enter friends name")
        if len(new_friend.name) > 0:
            break
        else:
            print "Enter Valid Name"
    new_friend.salutation = raw_input("Are they Mr. or Ms.?:")


    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    new_friend.chats = []

    if len(new_friend.name) >0 and new_friend.age >12:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry.We can\'t add spy with details you provided'

        return len(friends)

#Enabling a function to select a friend from the list
def select_friend():
    item_number = 0

    for friend in friends:
        print '%d.%s of %d age has %.2f rating' %(item_number+1,friend.name,friend.age,friend.rating)

        item_number = item_number+1

        friend_choice = int (raw_input('Select number corresponding to friend you want to select'))

        friend_choice_position = friend_choice-1

        return (friend_choice_position)

#Enabling a function to send message
def send_message():
    friend_chosen = select_friend()
    print "Image is all set to image.jpg"
    image_path = 'image.jpg'
    output_path = 'output.jpg'
    secret_push = raw_input('Enter message you want to encode')
    #steganography used for purpose of hiding the message
    Steganography.encode(image_path, output_path,secret_push)
    #push function helps in encoding message

    new_chat = ChatMessages(secret_push, True)

    friends[friend_chosen].chats.append(new_chat)
    print "Your secret message is ready!"

#Enabling a function to read message
def read_message():
    sender = select_friend()
    output_path = raw_input('What is the name of the file?')
    #pull functions helps in decoding message
    secret_pull = Steganography.decode(output_path)
    print secret_pull

    new_chat = ChatMessages(secret_pull,False)

    friends[sender].chats.append(new_chat)
    print "Your secret message has been saved"
#Enabling a function to read existing message
def read_existing_chat():
    read_for = select_friend()
    print '\n6'
    for chat in friends[read_for].chats:
        if chat.was_sent_by_me:
            # print colored('text','red', attrs=['bold'])

            print colored("[%s]", "blue") %(chat.time.strftime("%d %B %Y")), colored("you said", "red")
            print chat.message
        else:
            print colored("[%s]", "blue") %(chat.time.strftime("%d %B %Y")), colored(friends[read_for].name +" said", "red")
            print chat.message

