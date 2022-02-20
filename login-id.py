
import random
import time

def login_id():
    login_id = []
    for login in range(0,12):
        login_password = random.randint(0,1000)

        class_login_id = (login,login_password)
        login_id.append(class_login_id)
        print(class_login_id)
    #----------------- This code will implement on server ---------------# 

def password_genrated():
    print('password_genrated')
    print('session is about to start in 5 seconds')
    #----------------- When session Expire ------------------------------# 

def session_end():
    print('session_end')

def create_emp_password():
    #---------------- For CMS TESTING DEV TEACHER NETWORKING ------------#
    emp_count = 5
    while emp_count > 0:
        emp_count -= 1
        login_id()
        if emp_count == 0:
            password_genrated()

def session_start():
    #--------------- session start --------------------------------#
    print('session will end afer 10 seconds')
    time.sleep(5)
    create_emp_password()
    time.sleep(10)
    #--------------- session End --------------------------------#
    session_end()

session_start()