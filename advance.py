import random
import time
import change_password as cp

login_ids = []
    #----------------- This code will implement on server ---------------# 
def login_id():
    global login_ids
    for class_name in range(0,12):
        login_password = random.randint(0,1000)
        class_login_id = (class_name,login_password)
        login_ids.append(class_login_id)
        print(class_login_id)

    #----------------- When session Expire ------------------------------# 
def password_genrated():
    print('password_genrated')
    print('session is about to start in 5 seconds')

def session_end():
    print('data getting change...')
    time.sleep(1)
    cp.do_change_password()
    print('session_end')

    #----------------Password Genrate For CMS TESTING DEV TEACHER NETWORKING ------------#
def create_emp_password():
    emp_count = 5
    while emp_count > 0:
        emp_count -= 1
        login_id()
        f = open('login-id.txt','w')
        for data in login_ids:
            f.write(str(data))
        if emp_count == 0:
            password_genrated()

    #--------------- session start --------------------------------#
def session_start():
    print('session will end afer 10 seconds')
    time.sleep(5)
    create_emp_password()
    #--------------- session End --------------------------------#
    time.sleep(10)
    session_end()


session_start()
