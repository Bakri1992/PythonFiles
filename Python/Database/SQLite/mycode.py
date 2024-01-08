# import sqlite3
import sqlite3

# connect to Database:
db=sqlite3.connect("app.db")
# Setting up the cursor:
cr = db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER, name TEXT)")
cr.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT , progress INTEGER , user_id INTEGER )")

# Inserting Data 
# cr.execute("INSERT INTO users (user_id,name) VALUES(1,'Ahmed')")
# cr.execute("INSERT INTO users (user_id,name) VALUES(2,'Sayed')")
# cr.execute("INSERT INTO users (user_id,name) VALUES(3,'Omar')")
my_list=["Ahmed","Sayed","Mahmoud","Ali","Kamel","Ibrahim","Sameh","Enas"]
for user in my_list:
    index=my_list.index(user)+1
    cr.execute(f"INSERT INTO users (user_id,name) VALUES({index},{user})")



# Notice that the insertion was unsuccessful cause I didnt commit the chnages to Database=> commit
# Save Changes => commit
db.commit()

# Close Database 
db.close()
