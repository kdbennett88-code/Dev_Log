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
    print('Or..')
    time.sleep(0.5)
    print('If you would like to clear the screen type, "clear"')
    time.sleep(1)
    print('You Bot!!')
    print()
    while True:
        
        user_input = input('> ')
        if user_input.lower() == 'q' or user_input.lower() == 'quit':
            break
        if user_input == 'clear':
            
            clear_screen()
        if user_input == 'ls' or user_input == 'list':
            
            list_entries()
        title = 'devlog'
        print()
        add_entry(title, user_input)
        print()
        print('Entry added successfully!')
        print()
        
        print()
if __name__ == '__main__':
    main()
        

