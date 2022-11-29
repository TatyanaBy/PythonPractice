# для создания файла, но файл Phone.csv не появляляся, добавила запись в interface.py - появился. 
# Вероятно, эти действия теперь лишние?

from interface import get_user 
user=()
def writing_csv ():
    file = 'Phone.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{user[0]}; {user[1]}; {user[2]}; {user[3]}\n')



