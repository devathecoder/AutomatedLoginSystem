def generatepass():
    import string
    import random

    print('''
                                                                I am your password generator    
    ''')
    NameOFUser = input("Enter your name : ")
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    plen = int(input(f"Hello, {NameOFUser} enter the length of password you want me generate : "))
    while 1:
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        passw = "".join(random.sample(s, plen))
        print("\n")
        print(f"Here is your password {NameOFUser} : {passw}")
        print(f"Are you ok with the password generated by me {NameOFUser}?")
        ch = input("If yes enter y otherwise enter any character and I will regenerate it for you : ")
        if ch == 'y':
            return passw

