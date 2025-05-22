import sqlite3
from pprint import pprint

DATABASE = 'cpu.db'

def print_all_cpu():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM cpu')
        results = cursor.fetchall()

        # Print column headers (assuming known columns)
        print(f'{"ID":<4}{"Brand":<10}{"Model":<10}{"Cores":<6}{"Threads":<8}{"BaseGHz":<8}{"BoostGHz":<9}{"TDP":<6}{"Socket":<10}{"ReleaseDate":<15}')

        for cpu in results:
            # Defensive check in case of unexpected row length
            if len(cpu) >= 10:
                print(f'{cpu[0]:<4}{cpu[1]:<10}{cpu[2]:<10}{cpu[3]:<6}{cpu[4]:<8}{cpu[5]:<8}{cpu[6]:<9}{cpu[7]:<6}{cpu[8]:<10}{cpu[9]:<15}')
            else:
                print("Error: CPU entry has missing fields:", cpu)

def main():
    while True:
        user_input = input('What would you like to do?\n1. Print all CPU\n2. Exit\n')
        if user_input == '1':
            print_all_cpu()
        elif user_input == '2':
            print('Goodbye!')
            break
        else:
            print('Invalid input. Please choose 1 or 2.')

if __name__ == '__main__':
    main()
