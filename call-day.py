import datetime
import random
import read_vcf
import pyinputplus as pyinp

class Person():
    def __init__(self, name, phone_no, date):
        """
        This holds all parameters we'll be using for the app
        PARAMETERS:
        name: name of the friend
        phone_number: phone numbe rof the friend
        date: Date expected to call the friend
        """
        self.__name = name
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
        self.avail_time = None
        self.dates = list()
        self.people = list()

def get_time():
    """
    THis function enables you to receive the time range which the user wants the calls to be assigned

    OUTPUT
    starting_hour: Time to start the call matching
    Ending_hour: Time to end the call matching
    """
    print("PLease enter the hour range you'll love to make the calls in the day using the format 13:00 - 16:00")
    try:
        starting_hour = datetime.datetime.strptime(input("starting time: "), "%H:%M")
        ending_hour = datetime.datetime.strptime(input("Ending time: "), "%H:%M")
    except:
        print("Sorry, there's an error in your input, please check it and try again")
        starting_hour, ending_hour = get_time()
    return starting_hour, ending_hour

def assign_date(starting_hour, ending_hour):
    day = random.randint(1,31)
    month = random.randint(1,12)
    year = datetime.datetime.now().year
    hour = random.randint(starting_hour.hour, ending_hour.hour)
    minute = random.randint(1,60)
    date_assigned = datetime.datetime(year, month, day, hour, minute)
    print(date_assigned)


def main():
    starting_hour, ending_hour = get_time()
    print(starting_hour, ending_hour)
    date_assigned = assign_date(starting_hour, ending_hour)

if __name__ == "__main__":
    main()
