from datetime import datetime


class BikeRental:
    
    def __init__(self, stock=0):
        """
        Our constructor class that instantiates bike rental shop.
        """
        self.stock = stock  # задаю количество велосипедов для аренды

    def displaystock(self):
        """
        Displays the bikes currently available for rent in the shop.
        """
        print(f'We have {self.stock} bikes available for rent.')
        return self.stock  # это значение можно будет использовать в других методах

    def rentBikeOnHourlyBasis(self, n):
        """
        Rents a bike on hourly basis to a customer.
        """
        if n <= 0:
            print('Number of bikes should be positive!')
            return None
        elif n > self.stock:
            print(f'Sorry, we have only {self.stock} bikes now.')
            return None
        else:
            now = datetime.now()
            print(f'Youve rented a {n} bikes on hourly basis today at {now.hour} hours')
            print('You will be charged $5 for every bike.')
            self.stock -= n
            return now

     
    def rentBikeOnDailyBasis(self, n):
        """
        Rents a bike on daily basis to a customer.
        """
        if n <= 0:
            print('Number of bikes should be positive!')
            return None
        elif n > self.stock:
            print(f'Sorry, we have only {self.stock} bikes now.')
            return None
        else:
            now = datetime.now()
            print(f'Youve rented a {n} bikes on hourly basis today at {now.hour} hours')
            print('You will be charged $20 for every bike.')
            self.stock -= n
            return now
        
    def rentBikeOnWeeklyBasis(self, n):
        """
        Rents a bike on weekly basis to a customer.
        """
        if n <= 0:
            print('Number of bikes should be positive!')
            return None
        elif n > self.stock:
            print(f'Sorry, we have only {self.stock} bikes now.')
            return None
        else:
            now = datetime.now()
            print(f'Youve rented a {n} bikes on hourly basis today at {now.hour} hours')
            print('You will be charged $60 for every bike.')
            self.stock -= n
            return now

    
    def returnBike(self, request):
        """
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        """
        bill = 0
        rentalBasis, rentalTime, numOfBikes = request
        if rentalBasis and rentalTime and numOfBikes:
            self.stock += numOfBikes  # возвращаю велики на склад
            now = datetime.now()  # фиксирую время сдачи
            rentalPeriod = now - rentalTime  # считаем время аренды

            if rentalBasis == 1:  # часовой тариф
                bill = (rentalPeriod.seconds / 3600) * 5 * numOfBikes
            elif rentalBasis == 2:  # дневной тариф
                bill = rentalPeriod.days * 20 * numOfBikes
            elif rentalBasis == 3:  # недельный тариф
                bill = (rentalPeriod.days / 7) * 60 * numOfBikes

            if 3 <= bill <= 5:
                bill *= 0.7

            print('Thank you for returning bikes.')
            print(f'That would be ${bill}')
            return bill
        else:
            print('Are you sure you rented a bike with us?')
            return None



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
            return self.rentalBasis, self.rentalTime, self.bikes  # вернуть эти значения
        else:
            return 0, 0, 0

