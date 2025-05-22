class User(object):
    def __init__(self, *args, username, password):
        super(User, self).__init__(*args)
        username = username
        password = password

d = User("d","d")
print(d.username)
        