from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if len(username) < 3:
            raise AuthenticationError("Username minimum 3 signs")

        if not re.match("^[a-z]+$", username):
            raise AuthenticationError("Username contains invalid characters")

#        if len(password) < 3:
#            raise AuthenticationError("Password minimum 8 signs")

        if not re.match('^(?=.*?\d)(?=.*?[a-z])[A-Za-z\d]{8,}$', password):
            raise AuthenticationError("Password don't contain all required characters")

#        else:
#            print("Ok!")
