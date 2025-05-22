import sqlite3
from pprint import pprint
DATABASE = 'cpu.db'


def print_all_cpu():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM cpu'
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f'name                           ')
    for cpu in results:
        pprint(f'{cpu[1]:<6}{cpu[2]:<6}{cpu[3]:<6}{cpu[4]:<6}{cpu[5]:<6}{cpu[6]:<6}{cpu[7]:<6}{cpu[8]:<6}{cpu[9]:<15}')
    db.close()

while True:
    user_input = input('What would you like to do?\n1 Print all cpu.\n3 Exit.')
    if user_input == '1':
        print_all_cpu()
    if user_input == '2':
        break
    else:
        print('Please input 1 or 2')