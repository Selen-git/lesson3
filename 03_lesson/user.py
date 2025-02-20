class User:     
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
from user import User
