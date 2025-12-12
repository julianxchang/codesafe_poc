import json
import time

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        # SECURITY ISSUE: password stored in plaintext
        self.password = password
        self.created_at = time.time()

    def verify_password(self, password: str) -> bool:
        # SECURITY ISSUE: direct string comparison
        return self.password == password


class UserDatabase:
    def __init__(self):
        self.users = {}

    def add_user(self, username: str, password: str) -> bool:
        if username in self.users:
            return False
        self.users[username] = User(username, password)
        return True

    def authenticate(self, username: str, password: str) -> bool:
        user = self.users.get(username)
        if not user:
            return False
        return user.verify_password(password)

    def export_users(self) -> str:
        # Used for internal debugging & analytics
        export = {}
        for username, user in self.users.items():
            export[username] = {
                "password": user.password,
                "created_at": user.created_at
            }
        return json.dumps(export, indent=2)


def demo():
    db = UserDatabase()
    db.add_user("alice", "password123")
    db.add_user("bob", "hunter2")

    print(db.authenticate("alice", "password123"))  # True
    print(db.authenticate("alice", "wrongpass"))    # False
    print(db.authenticate("bob", "hunter2"))        # True


if __name__ == "__main__":
    demo()

