
import random
import time

    #----------------- This code will implement on server ---------------# 
def login_id():
    login_id = []
    for login in range(0,12):
        login_password = random.randint(0,1000)

        class_login_id = (login,login_password)
        login_id.append(class_login_id)
        print(class_login_id)

    #----------------- When session Expire ------------------------------# 
def password_genrated():
    print('password_genrated')
    print('session is about to start in 5 seconds')

def session_end():
    print('session_end')

    #----------------Password Genrate For CMS TESTING DEV TEACHER NETWORKING ------------#
def create_emp_password():
    emp_count = 5
    while emp_count > 0:
        emp_count -= 1
        login_id()
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
