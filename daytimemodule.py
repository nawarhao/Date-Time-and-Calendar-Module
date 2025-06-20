from datetime import date, time, datetime

#calling the today
#function of date class
today = date.today()
now = datetime.now()
print("Today's date is", today)
print("\nCurrent Date and Time is", now)

#printing date's components
print("\nDate components", today.year, today.month, today.day)

import random
import time

def getRandomDate(startDate, endDate): #defining function
    print(f"Printing random date between {startDate} and {endDate}")
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'
    
    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))
    
    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

#display result
print("Random date - ", getRandomDate("12/12/1999", '1/1/2025'))

# define a fucntion called hotel_cost with one argument night as input.
def hotel_cost(nights):
    return 140*nights

#define a function called plane_ride_cost that takes a string, city as input.
def plane_ride_cost(city):
    if "charlotte" == city:
        return 183
    elif "tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475
    
#define a function called rental_car_ with an arguement called days
def rental_car_cost(days):
    if days>=7:
        return 40*days - 50
    if days>=3:
        return 40*days - 20
    else:
        return 40*days
    
#define a function called trip cost with argument day, money and city
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("Cost of car rental:", rental_car_cost(5))

print("Cost of plane ride:", plane_ride_cost("Lose Angeles"))

print("Cost of hotel room:", hotel_cost(7))

print("Total cost of trip:", trip_cost("Los Angeles", 7,500))

print(trip_cost("tampa", 6,500))
