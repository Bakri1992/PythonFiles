'''
This is a programm that show how to connect to a database in postgres 
and creates a table in this database
'''


import psycopg2

def create_table(db_config,table_name,attributen):
    conn=None
    try:
        conn =psycopg2.connect(**db_config)
        cur=conn.cursor()
        create_table_query=f"CREATE TABLE IF NOT EXISTS {table_name} ({attributen})"
        cur.execute(create_table_query)
        conn.commit()
        print(f"Table {table_name} was created succesfully.")

    except Exception as e:
        print(f"An error occurred :{e}")

    finally:
        if conn is not None:
            cur.close()
            conn.close()

def main():
    print("Lets configurate the database")
    db_config = {
        "host": input("Please enter the host of the database ? "),
        "database": input("Please enter the name of the database ? "),
        "user": input("Username ? "),
        "password": input("Password? "),
        "port": input("port number? ")
    }
    table_name=input("Please Enter the table name you want to create?")
    attributen=input("Please Enter the attributen the same way as id int , fname varchar(50), ....?")
    create_table(db_config,table_name,attributen)

if __name__=="__main__":
    main()

