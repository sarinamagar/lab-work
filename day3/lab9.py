#Take username and password from user and check it again for the three times whether the user has entered the rightusername and password. If yes then print a message "Logged in Successfully", if not then print invalid credentialsfor consecutive 3 times and if the limit exceeds than print "Attempt finished".
username=input("enter your username")
password=input("enter you password")
for i in range(0,3):
    print("enter your credentials")
    username1=input("username: ")
    password1=input("password: ")
    if (username==username1)and (password==password1):
        print("you logged in successfully")
        break
    else:
        if(username!=username1 or password!=password1):
            print("invalid input")
else:
    print("3 attempts fail")

