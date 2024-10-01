import hashlib
import time

class PasswordCracker:
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.password_length = 4

    def create_test_case(self, password, salt):
        """Create a test case by hashing the password concatenated with the salt."""
        hash_value = hashlib.sha256((password + salt).encode()).hexdigest()
        return hash_value

    def recover_password(self, hash_value, salt):
        """Recover the password given the hash value and salt."""
        start_time = time.time()
        for i in range(len(self.alphabet) ** self.password_length):
            guess = ""
            index = i
            for _ in range(self.password_length):
                guess += self.alphabet[index % len(self.alphabet)]
                index //= len(self.alphabet)
            if self.create_test_case(guess, salt) == hash_value:
                end_time = time.time()
                time_cost = end_time - start_time
                return guess, time_cost

    def evaluate_time_create_test_case(self):
        """Evaluate the time cost to create a test case."""
        password = "test"
        salt = "1234567890123456"
        start_time = time.time()
        self.create_test_case(password, salt)
        end_time = time.time()
        time_cost = end_time - start_time
        return time_cost

    def evaluate_time_recover_password(self, hash_value, salt):
        """Evaluate the time cost to recover the password."""
        start_time = time.time()
        self.recover_password(hash_value, salt)
        end_time = time.time()
        time_cost = end_time - start_time
        return time_cost

# usage:
pc = PasswordCracker()
salt = "1234567890123456"
password = "test"
hash_value = pc.create_test_case(password, salt)
print("Test case hash value:", hash_value)

recovered_password, time_cost = pc.recover_password(hash_value, salt)
print("Recovered password:", recovered_password)
print("Time cost to recover password:", time_cost)

time_cost_create_test_case = pc.evaluate_time_create_test_case()
print("Time cost to create test case:", time_cost_create_test_case)

time_cost_recover_password = pc.evaluate_time_recover_password(hash_value, salt)
print("Time cost to recover password:", time_cost_recover_password)
