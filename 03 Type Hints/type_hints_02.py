from dataclasses import dataclass


def greet(name:str, times: int = 1) -> str:
    return (f'Hello {name}!')*times

def average(scores: list[float]) -> float | None:
    return sum(scores) / len(scores) if scores else None

@dataclass  # Python decorator that automatically generates common methods for a class that is primarily used to store data.
class User:
    id: int
    email: str
    is_active : bool = True
    
u = User(id=1, email='abc@email.com')
print(greet("Monirul", 2), average([3.5, 2.5, 7.8]), u)



