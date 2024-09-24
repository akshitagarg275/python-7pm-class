import sqlite3
con = sqlite3.connect("todo.db")

cur = con.cursor()
table_name = 'todos' 

# TODO: create a table
# create table if not exists table_name (id integer primary key autoincrement, taskname text)
def create_table():
    sql = f'CREATE TABLE IF NOT EXISTS {table_name} (id integer primary key autoincrement, taskname text)'
    cur.execute(sql)


# TODO: Create a task
# insert into table_name (column_name) values (column_values)
def add_todos(todo_name):
    cur.execute("INSERT INTO " + table_name + " (taskname) Values (?)", [todo_name])
    print("Todo added successfully")
    con.commit()

# TODO: Read all tasks
# select column_name1, column_name2 from table_name
# select * from table_name

def read_todos():
    cur.execute("SELECT * FROM " + table_name)

    for row in cur.fetchall():
        print(f"{row[0]} ---> {row[1]}")

# TODO: Update a task
# update table_name set column_name=new_value where ID=index
def update_todo(index, updated_todo):
    cur.execute("UPDATE " + table_name + " SET taskname = (?) WHERE id = (?)", [updated_todo, index])
    print("Todo updated successfully!")
    con.commit()


# TODO: Delete a task
# delete from table_name where id = index
def delete_todo(idx):
    cur.execute("DELETE FROM " + table_name + " WHERE id = (?)", [idx])
    print("TODO deleted successfully !")
    con.commit()

# TODO: Close connection
def close_connection():
    cur.close()
    con.close()