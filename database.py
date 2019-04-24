import sqlite3, os
from sqlite3 import Error

db = 'Accounts.db'
path = "c:\\sqlite"
dbfullpath = path + "\\" + db

def db_check(path, db):
	if os.path.isdir(path) == False:
		os.mkdir(path)
		create_customers_table()
		create_security_questions_table()
		default_info()
	elif os.path.isfile(dbfullpath) == False:
		create_customers_table()
		create_security_questions_table()



def customers_table_path():
	pass



def create_connection(db_file):
	try:
		return sqlite3.connect(db_file)
		
	except Error as e:
		print(e)
	return None



def default_info():
	conn = create_connection(dbfullpath)
	c = conn.cursor()
	c.execute("INSERT INTO customers ('last', 'first', 'middle', 'username', 'phone', 'email', 'password', 'accnum', 'accstatus') VALUES (?,?,?,?,?,?,?,?,?)", ('Holt', 'Gene', 'Emmanuel', 'gene.holt', '2222222222', 'gholt15104@gmail.com', 'U886x565', 12345678, 'active'))
	conn.commit()
	conn.close()
	
	
	
def create_customers_table():
	conn = create_connection(dbfullpath)
	c = conn.cursor()
	c.execute("""CREATE TABLE IF NOT EXISTS customers (
			ID integer PRIMARY KEY AUTOINCREMENT,
			last text NOT NULL,
			first text NOT NULL,
			middle text,
			username text NOT NULL,
			phone text,
			email text,
			password text NOT NULL,
			accnum integer NOT NULL,
			accstatus text NOT NULL,
			UNIQUE (accnum),
			UNIQUE (username),
			UNIQUE (ID)
			)""")

	
	conn.commit()
	conn.close()
	
	

def add_to_customers_table(newlast, newfirst, newmiddle):
	conn = create_connection(dbfullpath)
	c = conn.cursor()	
	c.execute("INSERT INTO customers ('last', 'first', 'middle') VALUES (?, ?, ?)",(newlast, newfirst, newmiddle))
	conn.commit()
	conn.close()
	
	

def get_all_from_customers():
	conn = create_connection(dbfullpath)
	c = conn.cursor()
	c.execute("SELECT * FROM customers")
	rows = c.fetchall()
	for row in rows:
		print("ID: {} | Last: {} | First: {} | Middle: {} | Username: {}".format(row[0], row[1], row[2], row[3], row[4]))
		
		
	
def create_security_questions_table():
	conn = create_connection(dbfullpath)
	c = conn.cursor()
	c.execute("""CREATE TABLE IF NOT EXISTS securityquestions (
			securityID interger,
			questions text NOT NULL,
			UNIQUE (securityID)
			)""")

	conn.commit()
	conn.close()


	
def add_security_questions_table(question, answer):
	conn = create_connection(dbfullpath)
	c = conn.cursor()
	c.execute("INSERT INTO securityquestions ('questions', 'answers') VALUES (?,?)",(question), (answer))
	conn.commit()
	conn.close()
	
	
def check_username(uname):
	conn = create_connection(dbfullpath)
	c = conn.cursor()
	c.execute('''SELECT * FROM customers WHERE username = ?''',(uname,))
	if c.count > 0:
		return True
	else:
		return False
	
	

if __name__ == '__main__':
	pass
else:
	print("This will run once bank_v2.py starts")
	db_check(path, db)
	#conn = create_connection(path, path + "\\" + db)
	#c = conn.cursor()	
	#conn.commit()
	#conn.close()