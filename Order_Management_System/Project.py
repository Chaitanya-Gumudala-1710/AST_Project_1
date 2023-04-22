# Create class of Order, Order Detail, Items, State - Chaitanya

# Creating a class named "State" to represent different states of an order
class State:
    PENDING = "Order is Pending"
    ACCEPTED = "Order is Accepted"
    REJECTED = "Order is Rejected"
    PROCESSING = "Order is Processing"
    SHIPPING = "Order is Shipping"
    CLOSED = "Order is Closed"

# Creating a class named "Order" to represent an order placed by a customer 
class Order:
    def __init__(self, date, customer, order_details, state) -> None:
        self.date = date
        self.customer = customer
        self.order_details = order_details
        self.state = state
    
    # Method to cancel an order by changing its state to "Order is Closed"
    def cancel(self):
        self.state = State.CLOSED
    
    # Method to set an order to state to "Order is Processing"
    def process(self):
        self.state = State.PROCESSING
    
    # Method to set an order to state to "Order is Shipping"
    def dispatch(self):
        self.state = State.SHIPPING
    
    # Creating a method to calculate the total cost of the order
    def calculate_total(self):
        return None
    
    # Creating a method to calculate the total weight of the order
    def calculate_total_weight(self):
        return None
    
    

# Create class of Customer, Address, Contract Details - Anudeep
# Create class of Payment, Cash, Bank Transfers, Credit Card - Kamendu
# Test the code - Jay
