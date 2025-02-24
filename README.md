
# The sign-in function to request data from user
def sign_in():
    print("SIGN IN for a better experience.")
    username = input("Enter " "Username: ")
    password = input("Enter " "Password: ")

# To verify user input data
    if authenticate(username, password):
        print("Sign in successful! Welcome to TogetherHub, {}.".format(username))
    else: 
        print("Incorrect username or password. Please try again!.")
sign_in()        