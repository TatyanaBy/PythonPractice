import interface
import logger
import result

def result(last_name, first_name, phone_number, comment):
    res = (interface.get_user(last_name, first_name, phone_number, comment))
    print(f"фамилия, имя, номер телефона, комментарий ")
    return res

    # работает и без этого кода, вероятно тоже лишние действия?