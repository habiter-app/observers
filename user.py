"""
Minimal reproducible example for the observer pattern with Habiter models.
For usage example see `tests` function
"""
from sqlalchemy import Table, Column, String, Integer, Boolean, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from typing import List

base = declarative_base()

class Observer():
    def __init__(self):
        self._observers = {}

    def add_observer(self, name: str, function, args: List):
        """
        Args:
            args: list of argument, will be passed to function
            likke function(*args)

        Example:
        ```
        self.add_observer(
                'score',  update_level, [self])
        ```
        """
        self._observers[name] = (function, args)

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        if not hasattr(self, "_observers"):
            return
        if self._observers.get(name) is not None:
            observer, args= self._observers.get(name) 
            observer(*args)

class User(base, Observer):
    __tablename__ = "users"
    id = Column(String, primary_key=True)

    name = Column(String)
    app = Column(String)

    # going to be deprecated, renamed
    screenshot_submitted = Column(Integer)

    score = Column(Integer)

    def __init__(self, id):
        base.__init__(self)
        Observer.__init__(self)

        self.__setattr__('id', id)

        self.add_observer(
                'screenshot_submitted', self._compute_score, [])
        self.add_observer(
                'id', self._compute_score, [])
        self.add_observer(
                'score',  update_level, [self])

    def _compute_score(self):
        self.score = self.screenshot_submitted + self.id


level = 0
def update_level(user: User):
    """
    We can do this differently based on how the roles
    infra is set up
    """
    global level
    if user.score > 2:
        level = 1
    if user.score > 5:
        level = 2

def tests():
    """
    This need to be added to User tests (test__User)
    """
    user = User(1)
    user.name = 'alex'
    assert user.id == 1
    assert user.name == 'alex'
    assert level == 0

    user.screenshot_submitted = 2
    assert user.screenshot_submitted == 2
    assert user.score == 3
    assert level == 1

    user.id = 5
    assert user.score == 7
    assert level == 2
    return True

if __name__ == "__main__":
    assert tests
