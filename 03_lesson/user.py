class User:
    first_name: str
    last_name: str

    def __init__(self, first_name, last_name):
        self.first_name: str = first_name
        self.last_name: str = last_name

    def print_first_name(self):
        print(f"First name: {self.first_name}")

    def print_last_name(self):
        print(f"Last name: {self.last_name}")

    def print_full_name(self):
        print(f"Full name: {self.first_name}")