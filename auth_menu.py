import hashlib
from db_manager import execute_query
from logging_file import log_decorator


admin_name = '00'
admin_password = '00'


@log_decorator
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


@log_decorator
def register():
    try:
        name = input('Enter your name: ')
        password = input('Enter your password: ')
        confirm_pass = input('Re-enter your password: ')
        phone = input('Phone: ')
        if password != confirm_pass:
            print('Password do not match!')
            return None
        is_active = False

        params = name, hash_password(password), phone, is_active
        command = """insert into users (name, password, phone, is_active)
        values (%s, %s, %s, %s) 
        """

        execute_query(query=command, params=params)
        print('Seccess!')
    except ValueError:
        print('Card number must be a whole number!')


@log_decorator
def login():
    name = input('Enter your name: ')
    password = input('Enter your password: ')

    if name == admin_name and password == admin_password:
        return 'admin'

    password = hash_password(password)
    name_from_db = execute_query(f"select name from users where password = '{password}'", fetch='one')
    if name_from_db:
        if name_from_db[0] == name:
            command = f"update users set is_active = true where password = '{password}'"
            execute_query(command)
            return 'user'
        else:
            return 'No such a user, try again!'
    else:
        return 'No such a user, try again!'


@log_decorator
def logout():
    sql = "update users set is_active = false where is_active = true"
    execute_query(sql)
