class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @staticmethod
    def logout():
        print('logout')

    def login(self, password):
        if self.password == password:
            return True
        else:
            return False


User.logout()

a = User('admin', 'pass')

if a.login('pass'):
    print('成功')
else:
    print('失敗')

if a.login('pass_no'):
    print('成功')
else:
    print('失敗')


class GuestUser(User):
    def __init__(self):
        super().__init__('guest', 'guest')


b = GuestUser()

if b.login('guest'):
    print('成功')
else:
    print('失敗')
