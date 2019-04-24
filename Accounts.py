class Accounts:
	def __init__(self):
		self.firstname = Accounts.new_firstname()
		self.lastname = Accounts.new_lastname()
		self.middlename = Accounts.new_middlename()
		self.username = Accounts.new_username()
		self.password = Accounts.new_pass()
		self.account_number = Accounts.newacc_number()
		self.account_email = Accounts.new_email()
	
	
	def new_firstname():
		cls()
		while True:
			new_fname = input("Enter your first name: ")
			if new_fname == '':
				cls()
				print("First name field cannot be blank. Please try again")
			else:
				return new_fname
	
	
	def new_lastname():
		cls()
		while True:
			new_lname = input("Enter your last name: ")
			if new_lname == '':
				cls()
				print("Last name field cannot be blank. Please try again")
			else:
				return new_lname
		
		
	def new_middlename():
		cls()
		new_mname = input("Enter your middle name or press enter to leave it blank: ")
		return new_mname
		cls()
    
	def new_username():
		new_uname = input("Create a username: ")
		while True:
			#Need to fix this to look at the database instead of the dictionary
			if new_uname in db.username:
				print("Username already exists. Please try again")
			else:
				return new_uname


	def new_pass():
		while True:
			new_pass = input("Create a password: (*minimum of 8 characters and must begin with a letter):")
			if len(new_pass) < 8 or new_pass[0].isalpha() != True :
				print("Password does not meet the criteria.  Please try again")
			else:
				return new_pass
				
	
	
	def new_accnumber():
		gen_accnum = string.digits
		accnum = ''.join(choice(gen_accnum) for i in range(8))
		return accnum
		
		
	def new_email():
		while True:
			email = input("Enter your email address: ")
		
import os
import database as db
def cls():
	os.system('cls')