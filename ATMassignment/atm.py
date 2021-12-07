
import customers
class atm:
    def __init__(self, customers=[]) -> None:
        self.customers = customers

    def addCustomer(self, customer):
        self.customers.append(customer)

    def removeCustomer(self, customer):
        self.customers.pop()

    def showDetails(self, customer):
        self.customers = customer
        if customers['accName']== 'Kwame':
            print('Name :: ', customers['customer a'])
        
    # def __init__(self, accNumber: str, pin: int) -> None:
    #     self.accNumber = accNumber 
    #     self.pin = pin
