correct_user = "Admin"
correct_pass = "TheMaster"
  
def whos_there():
    userName = input("Who is there? ")
    
    if userName != correct_user:
        print("Fuck off")
    else:
        password_checker()
    
def password_checker():
    userPassword = input("what is your password? ")

    if userPassword == correct_pass:
        print("Welcome")
    else:
        print("incorrect password")

whos_there()