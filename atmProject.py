import getpass
import string
import os

# Initially creating the list of users and their pin with bank statement.
users = ['venky', 'pradeep', 'kiran']
pins = ['1111', '2222', '3333']
amounts = [20000, 15000, 10000]
count = 0
# while loop checks existance of the enterd username
while True:
	user = input('\nENTER USER NAME: ')
	user = user.lower()
	if user in users: # user user2 user 3
		if user == users[0]:
			n = 0
		elif user == users[1]:
			n = 1
		else:
			n = 2
		break
	else:
		
		print('****************')
		print('INVALID USERNAME')
		print('****************')
		

# comparing pin
while count < 3:
	
	print('******************')
	pin = str(getpass.getpass('PLEASE ENTER PIN: '))
	print('******************')
	
	if pin.isdigit():
		if user == 'venky':
			if pin == pins[0]:
				break
			else:
				count += 1
				
				print('***********')
				print('INVALID PIN')
				print('***********')
				
				print()

		if user == 'pradeep':
			if pin == pins[1]:
				break
			else:
				count += 1
				
				print('***********')
				print('INVALID PIN')
				print('***********')
				
				print()
				
		if user == 'kiran':
			if pin == pins[2]:
				break
			else:
				count += 1
			
				print('***********')
				print('INVALID PIN')
				print('***********')
		
				print()
	else:
		
		print('************************')
		print('PIN CONSISTS OF 4 DIGITS')
		print('************************')
		
		count += 1
	
# if pin is invalid then it will be executed
if count == 3:
	
	print('***********************************')
	print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
	print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
	print('***********************************')

	exit()

print('*************************')
print('LOGIN SUCCESFUL, CONTINUE')
print('*************************')

print()

print('**************************')	
print(str.capitalize(users[n]), 'welcome to ATM')
print('**************************')
print('----------ATM SYSTEM-----------')
# Main menu
while True:
	
	
	print('*******************************')
	response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement_(S) \nWithdraw_(W) \nLodgement(L)  \nChange PIN(P)  \nQuit_______(Q) \n: ').lower()
	print('*******************************')
	
	valid_responses = ['s', 'w', 'l', 'p', 'q']
	response = response.lower()
	if response == 's':
		
		print('*********************************************')
		print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n],'EURO ON YOUR ACCOUNT.')
		print('*********************************************')
		 
		
	elif response == 'w':
		
		print('*********************************************')
		cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
		print('*********************************************')
	
		if cash_out%10 != 0:
	
			print('******************************************************')
			print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 EURO NOTES')
			print('******************************************************')

		elif cash_out > amounts[n]:
			
			print('*****************************')
			print('YOU HAVE INSUFFICIENT BALANCE')
			print('*****************************')
		
		else:
			amounts[n] = amounts[n] - cash_out
			
			print('***********************************')
			print('YOUR NEW BALANCE IS: ', amounts[n], 'EURO')
			print('***********************************')
			
			
	elif response == 'l':
		print()
		
		print('*********************************************')
		cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
		print('*********************************************')
		
		print()
		if cash_in%10 != 0:
			
			print('****************************************************')
			print('AMOUNT YOU WANT TO LODGE MUST TO MATCH 10 EURO NOTES')
			print('****************************************************')
			
		else:
			amounts[n] = amounts[n] + cash_in
			
			print('****************************************')
			print('YOUR NEW BALANCE IS: ', amounts[n], 'EURO')
			print('****************************************')
			
	elif response == 'p':
		
		print('*****************************')
		new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
		print('*****************************')
		
		if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
			
			print('******************')
			new_ppin = str(getpass.getpass('CONFIRM NEW PIN: '))
			print('*******************')
			
			if new_ppin != new_pin:
				
				print('************')
				print('PIN MISMATCH')
				print('************')
				
			else:
				pins[n] = new_pin
				print('NEW PIN SAVED')
		else:
			
			print('*************************************')
			print('NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
			print('*************************************')
			
	elif response == 'q':
		exit()
	else:
		
		print('******************')
		print('RESPONSE NOT VALID')
		print('******************')
		
