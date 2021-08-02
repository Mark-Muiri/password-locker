import unittest
from user_credentials import User, Credential

class TestUser(unittest.TestCase):
	'''
	Test class that defines test cases for the user class behaviours.

	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def setUp(self):
		'''
		Creates new acc before each test
		'''
		self.new_user = User('Mark','Muiri','example1')

	def test__init__(self):
		'''
		Checking initialization of instances "using the variables"
		'''
		self.assertEqual(self.new_user.fname,'Mark')
		self.assertEqual(self.new_user.lname,'Muiri')
		self.assertEqual(self.new_user.pwd,'example1')

	def test_save_user(self):
		'''
		Test to check if the new users info is saved into the users list
		'''
		self.new_user.save_user()
		self.assertEqual(len(User.users_list),1)

class TestCredentials(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.

	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User('Mark','Muiri','example')
		self.new_user.save_user()
		user2 = User('Mk','Mr','exampl')
		user2.save_user()

		for user in User.users_list:
			if user.fname == user2.fname and user.pwd == user2.pwd:
				current_user = user.fname
		return current_user

		self.assertEqual(current_user,Credential.check_user(user2.pwd,user2.f_name))

	def setUp(self):
		'''
		Creates user credentials
		'''
		self.new_credential = Credential('Mark','Facebook','Macingtosh','example2')

	def test__init__(self):
		'''
		Initialization of credential instances "using credential instances"
		'''
		self.assertEqual(self.new_credential.u_name,'Mark')
		self.assertEqual(self.new_credential.s_name,'Facebook')
		self.assertEqual(self.new_credential.acc_name,'Macingtosh')
		self.assertEqual(self.new_credential.pwd,'example2')

	def test_save_credentials(self):
		'''
		Checking if credentials are saved
		'''
		self.new_credential.save_credentials()
		twitter = Credential('Mark','Twitter','Macingtosh','example3')
		twitter.save_credentials()
		self.assertEqual(len(Credential.credentials_list),2)

	def tearDown(self):
		'''
		Checking if credentials are cleared 
		'''
		Credential.credentials_list = []
		User.users_list = []

	def test_display_credentials(self):
		'''
		Test to check if the display_credentials method, displays the correct credentials.
		'''
		self.new_credential.save_credentials()
		twitter = Credential('Mark','Twitter','Macingtosh','example3')
		twitter.save_credentials()
		gmail = Credential('Mark','Gmail','Macintosh','example4')
		gmail.save_credentials()

		def test_find_by_site_name(self):
			'''
			Test to check if the find_by_site_name method returns the correct credential
			'''
			self.new_credential.save_credentials()
			twitter = Credential('Mark','Twitter','Macingtosh','example3')
			twitter.save_credentials()
			credential_exists = Credential.find_by_site_name('Twitter')
			self.assertEqual(credential_exists,twitter)

		def test_copy_credential(self):
			'''
			Test to check if the copy a credential method copies the correct credential
			'''
			self.new_credential.save_credentials()
			twitter = Credential('Mark','Twitter','Macintosh','example3')
			twitter.save_credentials()
			find_credential = None
			for credential in Credential.user_credentials_list:
					find_credential =Credential.find_by_site_name(credential.site_name)
					return pyperclip.copy(find_credential.password)
			Credential.copy_credential(self.new_credential.site_name)
			self.assertEqual('pwd2001',pyperclip.paste())
			print(pyperclip.paste())

if __name__ == '__main__':
	unittest.main(verbosity=2)