import os
import time

directory = "data/input"

def ensure_directory_exists():
    if not os.path.exists(directory):
        os.makedirs(directory)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def count_files():
    ensure_directory_exists()  
    file_count = 0
    for root, dirs, files in os.walk(directory):
        file_count += len(files)
    return file_count

def display_art(file_count):
    num_str = f"{file_count}".zfill(3)  
    space = ' ' * (3 - len(num_str))
    art = rf"""
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  Welcome to     |  |  |     |         |      |
     |  |  Clyde          |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( {num_str}{space} |    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"     
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'
    """
    clear_screen()
    print(art)
    time.sleep(3)

def display_with_art(function):
    def wrapper(*args, **kwargs):
        file_count = count_files()  
        display_art(file_count)  
        return function(*args, **kwargs)
    return wrapper

