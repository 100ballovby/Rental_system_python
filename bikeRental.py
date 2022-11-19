import datetime

class BikeRental:
    
    def __init__(self,stock=0):
        """
        Our constructor class that instantiates bike rental shop.
        """

    def displaystock(self):
        """
        Displays the bikes currently available for rent in the shop.
        """

    def rentBikeOnHourlyBasis(self, n):
        """
        Rents a bike on hourly basis to a customer.
        """
     
    def rentBikeOnDailyBasis(self, n):
        """
        Rents a bike on daily basis to a customer.
        """
        
    def rentBikeOnWeeklyBasis(self, n):
        """
        Rents a bike on weekly basis to a customer.
        """

    
    def returnBike(self, request):
        """
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        """



class Customer:

    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """

    
    def requestBike(self):
        """
        Takes a request from the customer for the number of bikes.
        """
     
    def returnBike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """
