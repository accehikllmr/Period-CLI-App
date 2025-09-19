from modules.mod_input_data import input_data
from modules.mod_check_enter import check_enter
from modules.mod_check_escape import check_escape
from modules.mod_delete_line import delete_line
from modules.mod_reset import reset

def add_contact():
    '''
    '''

    with open('contact_info.txt', 'w') as contact:

        number = ""

        while len(number) != 10:
            print("***1: Add*** \nWhat is your phone number? [No spaces]")
            number = input_data("numbers")

            if check_enter(number, 3):
                return add_contact()
            elif check_escape(number):
                output = check_escape(number)[1]
                return output
            elif len(number) != 10:
                print("Your phone number must have exactly 10 digits.")
                reset(3)
            else:
                contact.write(number)
                print(number)   #need to print otherwise next input prompt erases it

        num = 0

        while not 0 < int(num) < 10:                 
            print("Who is your mobile phone service provider? \n1: Bell \n2: Rogers \n3: Virgin \n4: Fido \n5: Telus \n6: Freedom \n7: Koodo \n8: Public \n9: Other")
            num = input_data("numbers")

            providerList = [[1, "bell"],[2, "rogers"],[3, "virgin"],[4, "fido"],[5, "telus"],[6, "freedom"], [7, "koodo"], [8, "public"]]

            if check_enter(num, 11):
                num = 0
                continue
            elif check_escape(num):
                output = check_escape(num)[1]
                return output

            num = int(num)

            if not 0 < num < 10:
                print("Please choose a valid option.")
                reset(11)
            else:
                for i in providerList:
                    if num == i[0]:
                        provider = i[1]
                contact.write("\n" + provider)
                delete_line(9)
                provider = provider[0].upper() + provider[1:]
                print(provider)

        email = ""

        noAt = chr(64) not in email #need to check in ASCII codes differ according to keyboard language, since tried to decode é... also not recognizing @ symbol...
        noPeriod = chr(46) not in email
        tooShort = len(email) < 6

        while tooShort and noAt and noPeriod: #minimum criteria for now, but will need robust module for treating emails as valid or invalid
            print("What is your email address?")
            email = input_data("")

            if check_enter(email, 2):
                email = ""
                continue
            elif check_escape(email):
                output = check_escape(email)[1]
                return output
            elif len(email) < 6:
                print("Your email must be at least 6 characters in length.")
                reset(2)
            elif noAt:
                print("Your email must contain this symbol: @")
                reset(2)
            elif noPeriod:
                print("Your email must contain this symbol: .")
                reset(2)

    return None
