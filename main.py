import os
import sys
from user_pass import user_pass

curly = '}'

f = open('user_pass.py', 'ab+')
f1 = open('user_pass.py', 'a+')

def login():
	user = input('Enter your username: ')
	password = input('Enter password: ')
	try:
		if password == user_pass[user]:
			print('Logged in')
			loggedin = True

		else:
			print('The password is incorrect' )
			loggedin = False

	except:
		print('The user doesn\'t exist')
		loggedin = False

	return user, loggedin

def start(user):
	print(f'Welcome {user}')

def set_user():
	# user_pass[input('New user: ')] = input('Password: ')
	new_user = input('New username: ')
	if new_user in user_pass:
		sys.exit('User already exists')

	new_user_pass = input('Password: ')
	f.seek(-1, os.SEEK_END)
	f.truncate()
	f1.write(f'    \'{new_user}\' : \'{new_user_pass}\', \n{curly}')
	f.flush()
	f1.flush()
	f.close()
	f1.close()

def login_or_create(l):

	if l.lower().strip() == 'l':
		user, loggedin = login()

	elif l.lower().strip() == 'c':
		set_user()
		print('User created')
		sys.exit(0)

	else:
		sys.exit('An error occurred, try again')

	if loggedin == True:
		start(user)

def main():
	return login_or_create(input('Press and enter "l" to login or "c" to create an account: '))

if __name__ == '__main__':
	main()