import os
import time

file_name = None
directory = "data/input"

def ensure_directory_exists():
    if not os.path.exists(directory):
        os.makedirs(directory)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def count_files():
    ensure_directory_exists()
    return sum(len(files) for _, _, files in os.walk(directory))

def display_art():
    num_files = count_files()  
    num_str = f"{num_files}".zfill(3)
    space = ' ' * (3 - len(num_str))

    if file_name:
        file_display = f"C:\\>{file_name[:13]}"
        
        art = rf"""
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |{file_display:<17}|  |  |     | -==----'|      |
     |  |                 |  |  |     |         |      |
     |  |                 |  |  |/----|`---=    |      |
     |  |                 |  |  |   ,/|==== ooo |      ;
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
    else:
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
        global file_name  
        if 'file_name' in kwargs:
            file_name = kwargs['file_name']
        display_art()
        result = function(*args, **kwargs)
        return result
    return wrapper

@display_with_art
def process_file(file_name):
    print(f"Processing file: {file_name}")

if __name__ == "__main__":
    display_art()
    process_file(file_name="example.csv")