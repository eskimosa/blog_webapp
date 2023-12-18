from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import datetime

Base = declarative_base()
engine = create_engine('sqlite:///blogdb.db', echo=True, connect_args={'check_same_thread': False})
Session = scoped_session(sessionmaker(bind=engine))
session = Session()


class User(Base):
    __tablename__ = 'users'

    user_id = Column('user_id', Integer, primary_key=True)
    username = Column('username', String)
    password_hash = Column('password_hash', String)

    @classmethod
    def get_all(cls):
        return session.query(User).all()

    @classmethod
    def get_by_username(cls, username):
        return session.query(User).filter(User.username == username).first()

    @classmethod
    def create_user(cls, session, username, password_hash):
        new_user = cls(username=username, password_hash=password_hash)
        session.add(new_user)
        session.commit()

    def __repr__(self):
        return self.user_id + ' ' + self.username + ' ' + self.password_hash


class BlogPost(Base):
    __tablename__ = 'blogposts'

    id = Column('id', Integer, primary_key=True)
    subject = Column('subject', String)
    content = Column('content', String)
    created = Column('created', DateTime, default=datetime.datetime.now)

    @classmethod
    def get_all(cls):
        return session.query(BlogPost).all()

    @classmethod
    def create_post(cls, session, subject, content):
        new_post = cls(subject=subject, content=content)
        session.add(new_post)
        session.commit()

    def __repr__(self):
        return self.subject + ' ' + self.content + ' ' + self.created


Base.metadata.create_all(bind=engine)


