#!/usr/bin/python3

# Import Python Libraries
import random, sys, getopt
from os import system, name

# Import script modules
import contacts, quote

def logo():
    print('''
#####################################################################
#
# Motivator Bot
# It's a Bot Time to Get Motivated! [VERSION 1.1]
# CODED BY: ANDREW STURM
# CREATED ON: 2020-04-20
#
#####################################################################

''')

def clear():
    # Clear command for Windows
    if name == 'nt':
        _ = system('cls')

    # Clear command for Mac/*nix
    else:
        _ = system('clear')

def quotes():
    try:
        print(quote.messages[random.randint(0,len(quote.messages) - 1)])

    except KeyboardInterrupt:
        print("Keyboard interrupt signal detected.\nExiting...")
        sys.exit()

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hn:qv",["help","notify","quotes","version"])
        for opt, arg in opts:
            if opt in ("-h","--help"):
                logo()
                exit()
            elif opt in ("-n","--notify"):
                notify(arg)
            elif opt in ("-q","--quotes"):
                print('You currently have ' + str(len(quote.messages)) + ' quotes in total.')
                exit()
            elif opt in ("-v","--version"):
                logo()
                exit()
            else:
                quotes()
                exit()

    except getopt.GetoptError:
        print("Invalid argument.")
        exit()

def notify(who):
    if who == "all":
        print("Email:\n"+contacts.emailContacts)
        print("MMS:\n"+contacts.mmsContacts)
        print("SMS:\n"+contacts.smsContacts)
    elif who == "email":
        print(contacts.emailContacts)
    elif who == "mms":
        print(contacts.mmsContacts)
    elif who == "sms":
        print(contacts.smsContacts)
# Start the script
if __name__ == "__main__":
    main(sys.argv[1:])
