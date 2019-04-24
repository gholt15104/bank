def invalid():
	cls()
	print("YOU'VE ENTERED AN INVALID ENTRY")



def cls():
	os.system('cls')



def login_error():
	cls()
	print("USERNAME/PASSWORD IS INCORRECT.")



def login():
	while True:
		print("******LOGIN PAGE******")
		username = input("ENTER YOUR USERNAME OR TYPE Q TO QUIT: ")
		if username.upper() == "Q":
			cls()
			print("SIGN-IN CANCELLED")
			break
		else:
			password = getpass.getpass("ENTER YOUR PASSWORD OR TYPE Q TO QUIT: ")
			if password.upper() == "Q":
				cls()
				print("SIGN-IN CANCELLED")
				break
			else:
				try:
					if username.upper() in admin_account and password == admin_account[username.upper()]['Password']:
						admin_page()
						break
					elif username.upper() in analyst_account and password == analyst_account[username.upper()]['Password']:
						analyst_page()
						break
					else:
						login_error()
						break
				except KeyError:
					login_error()
					break



#####Main page#####	
def main_page_create_account():
	new_account = acc()
	db.add_to_customers_table(new_account.lastname, new_account.firstname, new_account.middlename, new_account.username, new_account.password)
		
	
	
#####Customer page#####
def customer_page():
	print("******CUSTOMER PORTAL******")
	print("1) ACCOUNT SUMMARY")
	print("2) DEPOSIT")
	print("3) WITHDRAWAL")
	print("4) CHANGE PASSWORD")
	print("5) UPDATE SECURITY QUESTIONS")
	print("6) LOGOUT")



#####Admin page#####
def admin_page():
	cls()
	while True:
		print("******ADMIN CONSOLE******")
		print("1)  SEARCH FOR USER")
		print("2)  GET ALL USERS")
		print("3)  UNLOCK/ENABLE ACCOUNT")
		print("4)  LOCK/DISABLE ACCOUNT")
		print("5)  RESET USER PASSWORD")
		print("6)  RESET USER SECURITY QUESTIONS")
		print("7)  DELETE ACCOUNT")
		print("8)  ADD SECURITY QUESTION TO DATABASE")
		print("9)  REMOVE SECURITY QUESTION FROM DATABASE")
		print("10) EXIT ADMIN CONSOLE")
	
	
		user_selection = input("SELECT AN OPTION: ")
		
		if user_selection == '1':
			cls()
			continue
		elif user_selection == '2':
			cls()
			db.get_all_from_customers()
		elif user_selection == '3':
			cls()
			continue
		elif user_selection == '4':
			cls()
			continue
		elif user_selection == '5':
			cls()
			continue
		elif user_selection == '6':
			cls()
			continue
		elif user_selection == '7':
			cls()
			continue
		elif user_selection == '8':
			while True:
				user_selection = input("ARE YOU SURE YOU WANT TO EXIT TO THE MAIN PAGE?(Y/N) ")		
				if user_selection.upper() != 'N' and user_selection.upper() != 'Y':
					invalid()
				else:
					if user_selection.upper() == 'Y':
						cls()
						main_page()
						break
					elif user_selection.upper() == 'N':
						cls()
						admin_page()
		elif user_selection == '9':
			continue
		elif user_selection == '10':
			cls()
			break
		else:
			invalid()


#####Analyst Page#####
def analyst_page():
	cls()
	print("******ANALYST CONSOLE******")
	print("1) SEARCH FOR USER")
	print("2) GET ALL USERS")
	print("3) EXIT ANALYST CONSOLE")
	
	user_selection = input("SELECT AN OPTION: ")

	while True:
		cls()
		
		if user_selection == '1':
			continue
		elif user_selection == '2':
			continue
		elif user_selection == '3':
			while True:
				user_selection = input("ARE YOU SURE YOU WANT TO EXIT TO THE MAIN PAGE?(Y/N) ")		
				if user_selection.upper() != 'N' and user_selection.upper() != 'Y':
					invalid()
				else:
					break
			if user_selection.upper() == 'Y':
				cls()
				break
			elif user_selection.upper() == 'N':
				cls()
				analyst_page()			
		else:
			invalid()



#####Start of the program#####
import os, getpass, string
import database as db #database.py
from Accounts import Accounts as acc #Accounts.py
from random import choice

accounts = {}
admin_account = {"ADMIN":{"Password": "Start123!@#"}}
analyst_account = {"ANALYST":{"Password": "c0NNect"}}

def main():
	cls()
	while True:
		print("******MAIN PAGE******")
		print("1) CREATE AN ACCOUNT")
		print("2) LOGIN")
		print("3) CHANGE PASSWORD")
		print("4) QUIT")		
		
		user_selection = input("SELECT AN OPTION: ")
		cls()
		
		if user_selection == '1':
			main_page_create_account()
		elif user_selection == '2':
			login()
		elif user_selection == '3':
			continue
		elif user_selection == '4':
			while True:
				user_selection = input("ARE YOU SURE YOU WANT TO QUIT THE PROGRAM?(Y/N) ")		
				if user_selection.upper() != 'N' and user_selection.upper() != 'Y':
					invalid()
				else:
					break
			if user_selection.upper() == 'Y':
				cls()
				break
			elif user_selection.upper() == 'N':
				cls()
				continue
			
		else:
			invalid()
			
			
			
if "__name__" == "__main__":
	pass
else:
	main()
	

	
#Things I'd like to add
###########main page##############
#first option - create an account
	#use the class Accounts to create account
	#mandatory information 
	#first name 
	#last name 
	#middle name
		#can be null 
	#phone number
		#can be null 
	#home address 
	#username
		#can't be 'admin'
		#can't be 'analyst'
		#must be unique
			#check database to determine if username is already being used
	#password 
		#longer than 8 characters
		#start with letter
		#atleast 1 upper
		#atleast 1 lower
		#atleast 1 number
		#no special characters
		#re-enter password to make sure it's the password the customer wants to use
		#compare first and second password to make sure they match
	#account number
		#use random/choice/string to generate a random number
		#minimum of 8 digits
	#email address
		#can be null
		#if customer enters an email, use regex to verify that it matches an email format
	####accounts to open
		#checking and/or savings mandatory with minimum of $50 to open for each account 
	####security questions
		#select 3 questions from a list of options
#second option - customer login
	#move admin and analyst creds to database
	#check database for username
	#check database for password match	
#third option - customer password reset
###########customer page############
#create customer portal
#first - deposits
#second - withdrawals
#third - statement
#fourth - password reset
#fifth - security question changes
#sixth - logout to main page
###########admin page###########
#first - get individual account
#second - get all accounts (although may eliminate as program gets larger)
#third - Unlock/Enable customer account
#fourth - lock/disable customer account
#fifth - reset customers password
#sixth - reset security questions
#seventh - delete customer account
##########analyst page###########
#first - get individual account
#second - get all accounts (although may eliminate as program gets larger)
###########Database###########
#create database
#create table for customer information
	#username
	#first name
	#last name
	#home address
	#email address
	#phone number
	#secondary name on account(optional)
	#password(encrypted if possible)
	#accounts(using foreign keys)
	#account status
		#enable
		#disabled
		#locked
		#unlocked
	#account status summary
		#reason account is in the current status
#create table for customer accounts using the foreign keys(Things to link(customer information table, customer accounts)
#create table for transaction history
	#Withdrawals
	#deposits
	#account creations
#create table for customer accounts history for admins
	#logins
	#password changes
	#security question changes

