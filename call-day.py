import datetime
import random

class Person():
    def __init__(self, name, phone_no, date):
        """
        This holds all parameters we'll be using for the app
        name: name of the friend
        phone_number: phone numbe rof the friend
        date: Date expected to call the friend
        """
        self.__name = None
        self.__phone_no = phone_no
        self.date = date

    def change_number(self, number ):
        # function to change the phone_number of the person
        self.__phone_no = number

    def change_date(self, date):
        # function to change the date to call a Person
        self.date = date

class CallDay:
    def __init__(self):
        """
        initialising the class a set of parameters to contain the list of dates
        and names of people to avoid duplication
        dates = list of all dates already assigned
        people = list of people on your contact list
        """
        self.dates = list()
        self.people = list()

    def read 
