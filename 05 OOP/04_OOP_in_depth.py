from abc import ABC, abstractmethod

class PaymentMethod(ABC):                           # abstraction
    def __init__(self, amount:float)->None:
        self._amount = amount                       # encapsulation (by convention, _ = internal)
        
    @property                                       
    def amount(self) -> float:                      # read-only access to internal data
        return self._amount
    
    @abstractmethod
    def pay(self) -> str:
        ...
        
class BKash(PaymentMethod):                         # inheritance
    def pay(self) -> str:
        return f"Paid {self.amount} BDT via bKash"
    
class Card(PaymentMethod):                          # inheritance
    def pay(self) -> str:                           # polymorphism: same method, different behaviour
        return f"Charged {self.amount} BDT to Card"

for method in [BKash(500), Card(1200)]:
    print(method.pay())
    
"""
Output:

Paid 500 BDT via bKash
Charged 1200 BDT to Card

"""

"""
Note:

@property allows the function amount() to be used like object.amount instead of object.amount()
 

"""