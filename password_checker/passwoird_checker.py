correct_user = "Admin"
correct_password = "TheMaster"

who_is_it = input("Who's there? ")

if who_is_it == correct_user:
    password = input('Password: ')
    if password == correct_password:
        print("Welcome!")
    elif password == '':
        print("Canceled")
        
    else:
        print("Incorrect Password")
elif who_is_it == '':
    print("Cancelled")
else:
    print("I don't know you")