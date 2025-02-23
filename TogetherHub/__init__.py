def sign_in():
    print("SIGN IN for a better experience.")
    username = input("Enter " "Username: ")
    password = input("Enter " "Password: ")

    if authenticate(username, password):
        print("Sign in successful! Welcome to TogetherHub, {}.".format(username))
    else: 
        print("Incorrect username or password. Please try again!.")
sign_in()        