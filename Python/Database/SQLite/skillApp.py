import sqlite3          # Import SQLite Module
db=sqlite3.connect("app.db")  # Connect to the database 
cr= db.cursor() # Global Variable so we can use inside the method
# My User ID
uid=1

def commit_and_close():
    # Save (Commit) Changes 
    db.commit()
    # close database 
    db.close()
    print("Connection to database is closed!")


input_message='''What Do you want to Do?
"s" => Show All Skills
"a" => Add new Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit the App
Choose Option:
'''
# Input Option choose
user_input=input(input_message).strip()

# Command List
commands_list=["s","a","d","u","q"]

# Setup the methods
def show_skills():
    show_skills=cr.execute("select * from skills")
    print(show_skills)
    commit_and_close()


def add_skill():
    sk=input("Write Skill Name:").strip().capitalize()
    prog=input("Write Skill Progress:").strip()
    cr.execute(f"insert into skills(name, progress, user_id) values ('{sk}',{prog},{uid})")
    commit_and_close()


def delete_skill():
    print("Delete Skill")
    commit_and_close()


def update_skill():
    print("update Skill")
    commit_and_close()

# Check if command is exists
if user_input in commands_list:
    # print(f"Command found: '{user_input}'")
    if user_input=="s":
        show_skills()
    elif user_input=="a":
        add_skill()
    elif user_input=="d":
        delete_skill()
    elif user_input=="u":
        update_skill()
    else:
        print("App is closed!")
else:
    print(f"Sorry This Command '{user_input}' Is Not Found !")
    