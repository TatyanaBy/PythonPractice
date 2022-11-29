def get_user():
    user = []
    last_name = input('фамилия: ')
    user.append(last_name)
    first_name = input('имя: ')
    user.append(first_name)
    phone_number = input('номер телефона: ')
    user.append(phone_number)
    comment = input('комментарий: ')
    user.append(comment)
    with open ('Phone.csv', 'a', encoding = 'utf-8') as data:
           data.write(f'{user[0]}; {user[1]}; {user[2]}; {user[3]}\n')
    return user


    


  
 