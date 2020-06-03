class Observer(object):
    def __init__(self):
        print("first")
        self.x = 2

class base(object):
    def __init__(self):
        print("second")
        self.y = 3

class User(base, Observer):
    def __init__(self):
        base.__init__(self)
        Observer.__init__(self)
        print("that's it")

if __name__ == "__main__":
    user = User()
    assert user.x == 2
    assert user.y == 3