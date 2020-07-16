#!/usr/bin/python3

# Import Python Libraries
import random, getopt, smtplib, sys
from os import system, name

# Import script modules
import contacts, mailserver, quote

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
        body = (quote.messages[random.randint(0,len(quote.messages) - 1)])
        return body
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
                print(quotes())
                exit()

    except getopt.GetoptError:
        print("Invalid argument.")
        exit()

def notify(who):
    if who == "all":
        smtp(who)
    elif who == "email":
        smtp(who)
    elif who == "mms":
        smtp(who)
    elif who == "sms":
        smtp(who)

def smtp(who):
    try:
        # Attempt to contact the SMTP server to send a message
        body = quotes()
        fromaddr = mailserver.sender
        fqdn = mailserver.server

        if who == "all":
            toaddr = (contacts.email, contacts.mms, contacts.sms)
        elif who == "email":
            toaddr = contacts.email
        elif who == "sms":
            toaddr = contacts.sms
        elif who == "mms":
            toaddr = contacts.mms

        server = smtplib.SMTP(fqdn)
        server.set_debuglevel(1)
        server.sendmail(fromaddr,toaddr,body)
        server.quit()

    except OSError:
        print("Something went wrong...")
    except smtplib.SMTPServerDisconnected:
        # Server disconnected
        print("The SMTP server unexpectedly disconnected or an attempt to connect was made too soon.")
    except smtplib.SMTPResponseException:
        # Built to show errors from SMTP server
        print("The SMTP server responded with an error.")
    except smtplib.SMTPSenderRefused:
        # Server refused sender info
        print("The SMTP server refused the sender address.")
    except smtplib.SMTPRecipientsRefused:
        # Server refused recipient(s)
        print("The SMTP server refused one or more recipients.")
    except smtplib.SMTPDataError:
        # Server refused the message data
        print("The SMTP server refused the content.\nMotivator Bot REALLY screwed up this time.")
    except smtplib.SMTPConnectError:
        # Server failed to connect to the SMTP server
        print("The server failed to establish a connection with the SMTP server.")
    except smtplib.SMTPHeloError:
        # Server refused HELO message
        print("The SMTP server refused our 'HELO' message.")
        exit()
    except smtplib.SMTPNotSupportedError:
        # SMTP not supported
        print("The attempted operation is not supported by the SMTP server.")
    except smtplib.SMTPAuthenticationError:
        # Server was unable to authenticate
        print("Motivator Bot was unable to authenticate with SMTP.\nPlease check your username/password combination.")
        exit()

# Start the script
if __name__ == "__main__":
    main(sys.argv[1:])
