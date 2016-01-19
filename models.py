from db import database 

class User(database.Model):
	__tablename__ = 'user'

	id = database.Column(database.Integer, primary_key = True)
	full_name = database.Column(database.String(120))
	email = database.Column(database.String(64), unique = True)
	password = database.Column(database.String(255))
	bio = database.Column(database.String(140))
	avatar = database.Column(database.String(11))
	registered = database.Column(database.DateTime)
	last_login = database.Column(database.DateTime)

	def __repr__(self):
		return 'User {}>'.format(self.full_name)