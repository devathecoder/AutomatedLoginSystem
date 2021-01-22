from Generate_password import generatepass
def viewdata(platform):
    count = 0
    f = open("data.txt")
    platname = platform
    for line in f:
        if line.startswith(platname) or line.startswith(platname.upper()) or line.startswith(platname.lower()) or line.startswith(platname.capitalize()):
            x = line.split()
            print(f"Your id is : {x[1]}")
            print(f"Your password is : {x[2]}")
            temp = []
            temp.append(x[1])
            temp.append(x[2])
            return temp


def enterdata():
    f = open("data.txt", "a")
    platform = input("Enter the platform for which you want to enter the data : ")
    Username = input("Enter the user name or email id : ")
    print('''
                1. Generate password
                2. Write your own

        ''')
    choice = int(input("Enter your choice : "))
    if choice == 1:
        password = generatepass()
    else:
        password = input("Enter your password : ")
    try:
        description = input("Enter the sort description if any : ")
    except:
        description = "No description"
    f.write("\n")
    f.write(platform + " ")
    f.write(Username + " ")
    f.write(password + " ")
    f.write(description)
    f.write("\n")
    f.close()



def truth(name):
    print(f'''
                                'Welcome to your DataCenter {name}'
    ''')
    print('''
                                1. View your data
                                2. Enter the data
    ''')
    what = int(input("Enter your choice : "))
    if what == 1:
        viewdata()
    else:
        enterdata()



def dare(name):
    print(f'''
                          'You have entered the wrong PIN Mr. {name}'
                                        'Exiting out'
    ''')


def store():
    print(f'''
                                        'Dear User,
                                         Please enter the PIN to proceed'
                ''')
    for i in range(3):
        x = 1501
        nm = 'Dev'
        try:
            n = int(input("Enter the PIN : "))
        except:
            n = 0
        try:
            name = input("Enter your name : ")
        except:
            name = 'Unknown'
        if n == x and name == nm:
            truth(name)
            exit()
        else:
            if i == 2:
                dare(name)
            else:
                print(f"You have entered the wrong PIN Mr. {name}. {3 - (i + 1)} attempt left")
                continue
