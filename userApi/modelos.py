from dataclasses import dataclass


@dataclass
class User():
    id: int
    name: str
    last_name: str
    email: str
