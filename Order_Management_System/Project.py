# Create class of Order, Order Detail, Items, State - Chaitanya
# Create class of Customer, Address, Contract Details - Anudeep

#A Customer class which has the attributes of contact details, Address and Orders of a Customer
class Customer:
    def __init__(self, contact_details, address, orders):
        self.contact_details = contact_details
        self.address = address
        self.orders = orders

    def get_contact_details(self):
        return self.contact_details   # Function to return the contact details to customer class

    def get_address(self):   
        return self.address           # Function to return the address details to customer class

    def get_orders(self):
        return self.orders            #  Function to return the order details to customer class

 #A Address  class which has the attributes of country, city, postalcode, street and number details   

class Address:
    def __init__(self, country, city, postalcode, street, number):
        self.country = country
        self.city = city
        self.postalcode = postalcode
        self.street = street
        self.number = number

    def get_country(self):    
        return self.country          # Function to return the Country details to Address class

    def get_city(self):
        return self.city               # Function to return the City details to Address class

    def get_postalcode(self):
        return self.postalcode        # Function to return the postalcode details to Address class

    def get_street(self):
        return self.street            # Function to return the street details to Address class

    def get_number(self):
        return self.number           # Function to return the Country details to Address class

    def get_full_address(self):
        return f"{self.number} {self.street}, {self.postalcode} {self.city}, {self.country}"
    
 #A ContactDetails  class which has the attributes of firstname, lastname, email and phone number of a customer   

class ContactDetails:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def get_first_name(self):
        return self.first_name          # Function to return the first_name details to ContactDetails class

    def get_last_name(self): 
        return self.last_name           # Function to return the last_name details to ContactDetails class

    def get_email(self):
        return self.email               #  Function to return the email details to ContactDetails class

    def get_phone_number(self):
        return self.phone_number        #  Function to return the phone_number details to ContactDetails class

# Create class of Payment, Cash, Bank Transfers, Credit Card - Kamendu
# Test the code - Jay
