import json
import time
import re
from typing import Dict, Optional

MIN_PASSWORD_LENGTH = 6
USERNAME_REGEX = r"^[a-zA-Z0-9_]+$"

def is_valid_username(username: str) -> bool:
    """
    Check whether a username meets basic formatting rules.
    """
    if not username:
        return False
    return re.match(USERNAME_REGEX, username) is not None


def is_valid_password(password: str) -> bool:
    """
    Basic password validation.
    NOTE: This does NOT enforce strong passwords.
    """
    return password is not None and len(password) >= MIN_PASSWORD_LENGTH


def current_timestamp() -> float:
    """
    Returns the current Unix timestamp.
    """
    return time.time()


class User:
    """
    Represents a user in the authentication system.
    """

    def __init__(self, username: str, password: str):
        self.username = username

        # SECURITY ISSUE:
        # Password is stored in plaintext.
        # This is intentionally insecure and must be fixed by the user.
        self.password = password

        self.created_at = current_timestamp()
        self.last_login: Optional[float] = None

    def verify_password(self, password: str) -> bool:
        """
        Verify whether the provided password is correct.
        """
        # SECURITY ISSUE:
        # Direct string comparison of plaintext passwords
        return self.password == password

    def record_login(self):
        """
        Record the last successful login timestamp.
        """
        self.last_login = current_timestamp()

    def to_dict(self) -> Dict:
        """
        Convert the user object to a dictionary representation.
        Used for internal debugging and analytics.
        """
        return {
            "username": self.username,
            "password": self.password,
            "created_at": self.created_at,
            "last_login": self.last_login
        }


class UserDatabase:
    """
    A simple in-memory user database.
    """

    def __init__(self):
        self.users: Dict[str, User] = {}

    def add_user(self, username: str, password: str) -> bool:
        """
        Add a new user to the database.
        """
        if not is_valid_username(username):
            return False

        if not is_valid_password(password):
            return False

        if username in self.users:
            return False

        self.users[username] = User(username, password)
        return True

    def authenticate(self, username: str, password: str) -> bool:
        """
        Authenticate a user.
        """
        user = self.users.get(username)
        if not user:
            return False

        if user.verify_password(password):
            user.record_login()
            return True

        return False

    def get_user(self, username: str) -> Optional[User]:
        """
        Retrieve a user object by username.
        """
        return self.users.get(username)

    def export_users(self) -> str:
        """
        Export all users as a JSON string.
        WARNING: This currently exposes sensitive information.
        """
        export_data = {}
        for username, user in self.users.items():
            export_data[username] = user.to_dict()

        return json.dumps(export_data, indent=2)


def demo():
    """
    Demonstration of current functionality.
    """
    db = UserDatabase()

    db.add_user("alice", "password123")
    db.add_user("bob", "hunter2")

    print("Authenticating users...")
    print(db.authenticate("alice", "password123"))  # Expected: True
    print(db.authenticate("alice", "wrongpass"))    # Expected: False
    print(db.authenticate("bob", "hunter2"))        # Expected: True

    print("\nExported user data:")
    print(db.export_users())


if __name__ == "__main__":
    demo()

