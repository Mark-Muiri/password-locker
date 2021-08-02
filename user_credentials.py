class User:
	"""
	Classthat generates new instances of users
	"""

	user_list = []#Empty User list

	def __init__(self,first_name,last_name,password):

		self.first_name = first_name
		self.last_name = last_name
		self.password = password


class credentials:
	"""
	Class generates new instances of credentials
	"""

	credential_list = [] #Empty Credential list

	def __init__(self,u_name,s_name,acc_name,pwd):

		self.u_name = u_name
		self.s_name = s_name
		self.acc_name = acc_name
		self.pwd = pwd
