# log in
logged_in = False

while logged_in == False:
    login_username = input('username: ')
    if login_username != "root":
        print('Username invaild')
    else:
        login_password = input('password: ')
        if login_password == "pass":
            print('success!')
            logged_in = True
        else:
            print('Incorrect password')