# Securing an Authentication Service

## Scenario

You are a junior software engineer working on the CodeSafe platform.
A small internal authentication microservice was rushed into production
to support early prototypes and testing.

During a routine security review, your team discovered that **user passwords
are being stored and verified insecurely**. While the service “works,” it
violates fundamental software security principles and puts user data at risk.

Your task is to **secure the authentication logic** without breaking any
existing functionality.

You are NOT expected to design a full authentication system from scratch.
Instead, you will carefully modify the existing code to:

- Secure how passwords are stored
- Secure how passwords are verified
- Ensure incorrect credentials are properly rejected
- Preserve all existing features and behaviors

## Your Task

You must:
1. Replace insecure password handling with a secure approach
2. Ensure authentication still works for valid users
3. Prevent authentication bypasses
4. Pass all automated test cases

You may modify **modify_me.py only**.
All other files are read-only.

## Hints

- Plaintext passwords should never be stored
- Python’s standard library already includes cryptographic tools
- Think about what information should (and should not) be compared directly

Once all tests pass, running the checker will reveal the flag.

Good luck — this mirrors a **real-world security hardening task** commonly
assigned to junior engineers.

