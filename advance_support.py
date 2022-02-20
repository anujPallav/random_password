def do_change_password():
    c = open('login-id.txt','w')
    for i in range(100,8000):
        c.write(chr(i)+chr(i*2))

do_change_password()
