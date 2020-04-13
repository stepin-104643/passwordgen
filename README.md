# passwordgen

The purpose of this code is to generate a password of a user-specified length (6 characters minimum), along with mixed-case letters, numbers, and special symbols.

The user is also given the liberty to specify exact number of letters and numbers in the password.

As the Secrets module was not compatible with my version of Python, I used random.SystemRandom() instead to generate a cryptographically secure password.
