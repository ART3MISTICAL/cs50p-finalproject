import project.project as project
import pytest
import project.user_pass as user_pass

def test_not_lc():
	with pytest.raises(SystemExit):
		assert project.login_or_create('a')
		assert project.login_or_create('b')
		assert project.login_or_create('d')
		assert project.login_or_create('e')

def test_new_user():
	assert project.set_user('user', '123') == 'for pytest'

def test_login():
	user, loggedin =  project.login('abc', '123')
	assert user == 'abc'
	assert loggedin == True

def test_start():
	assert project.start('to CS50p') == 'Welcome to CS50p'
