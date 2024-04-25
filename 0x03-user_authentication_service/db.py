#!/usr/bin/env python3
"""
Database Module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> sessionmaker:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """adding new user"""
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            self._session.add(new_user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            new_user = None
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """get user by request"""
        user_fields = [
                'id', 'email', 'hashed_password',
                'session_id', 'reset_token'
                ]
        for key in kwargs.keys():
            if key not in user_fields:
                raise InvalidRequestError
            result = self._session.query(User).filter_by(**kwargs).first()

            if result is None:
                raise NoResultFound
            return result

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updating user"""
        user_to_update = self.find_user_by(id=user_id)
        user_fields = [
                'id', 'email', 'hashed_password',
                'session_id', 'reset_token'
                ]

        for key, value in kwargs.items():
            if keys in user_fields:
                setattr(user_to_update, key, value)
            else:
                raise InvalidRequestError
        self.session.commit()
