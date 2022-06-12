import main
import pytest

def test_not_lc():
	with pytest.raises(SystemExit):
		assert main.login_or_create('a')
		assert main.login_or_create('b')
		assert main.login_or_create('d')
		assert main.login_or_create('e')

def test_new_user():
	
