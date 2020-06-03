from sqlalchemy import Table, Column, String, Integer, Boolean, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class User(base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)


    name = Column(String)
    app = Column(String)

    # going to be deprecated, renamed
    screenshot_submitted = Column(Integer)

    score = Column(Integer)

    def __init__(self, id):
        self.__setattr__('id', id)

        self.observers = []

    def _compute_score(self):
        self.score = self.screenshot_submitted 



if __name__ == "__main__":
    user = User(1)
    user.name = 'a'
    assert user.id == 1
    assert user.name == 'a'
    user.screenshot_submitted = 2
