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

    def __init__(self, name):
        """
        Our constructor method which instantiates various customer objects.
        """
        self.name = name
        self.bikes = 0  # количество велосипедов
        self.bill = 0   # сумма заказа
        self.rentalTime = 0  # время аренды
        self.rentalBasis = 0  # тариф


    
    def requestBike(self):
        """
        Takes a request from the customer for the number of bikes.
        """
        bikes = input('How many bikes would you like to rent? ')
        try:  # проверяем пользовательский ввод на целочисленность
            bikes = int(bikes)
        except ValueError:
            print('Thats not a positive integer!')
            return -1  # статус сдачи в аренду
        if bikes < 1:
            print('Number of bikes should be greater than 0!')
            return -1
        else:
            self.bikes = bikes  # присвою параметру "велосипеды" количество, нужное пользователю
        return self.bikes

    def returnBike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """
        if self.rentalBasis and self.rentalTime and self.bikes:  # если долги не закрыты
            return self.rentalTime, self.rentalTime, self.bikes  # вернуть эти значения
        else:
            return 0, 0, 0

