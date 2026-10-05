from devlog_funcs import initialize_database, add_entry, list_entries, clear_screen, remove_entry
from datetime import datetime
import time

def main():
    initialize_database()
    print('Hey.. Whats new? Please be as precise as possible about the topic and description.')
    print()
    time.sleep(1)
    print('Type [ q or quit:quit | ls or list:list ALL entries ]')
    time.sleep(1.5)
    print()
    while True:
        
        #Assuming that no one else will use this program, I don't bother sanitizing the user input.. Bad habit that I need to just get used to performing.
        user_input = input('> ')
        if user_input.lower() == 'q' or user_input.lower() == 'quit':
            break

        elif user_input == 'clear':
            clear_screen()

        elif user_input == 'ls' or user_input == 'list':
            list_entries()

        elif user_input == 'remove' or user_input == 'delete':
            list_entries()
            num = int(input('What ID would you like to remove?\n> '))
            remove_entry(num)
            print(f'Removed content located at {num} this is your current table')
            list_entries()

        uinput = user_input 
        words = user_input.split()
        if words != 'list' and words != 'clear':
            try:
                if words != ' ':
                    add_entry(uinput)
            except:
                print('caught the error')
            add_entry(uinput)
            print('Entry added!')
        print('end loop')

if __name__ == '__main__':
    main()
        

