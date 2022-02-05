import datetime
import random
import read_vcf
import pyinputplus as pyinp
import logging

logging.basicConfig("%(asctime)s %(funcName)s [%(levelname)s]: %(message)s", level = logging.DEBUG)
logger = logging.getLogger()

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
        logger.info("new person %(self.__name)s has been created and allocated time is %(self.date)s")

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
        self.people = dict()

    def add_person(self,name, new_person):
        self.people[name] = new_person
        logger.info("person added to Callday successfully")

    def add_date(self, date):
        self.dates.append(date)
        logger.info("date has been registered successfully")

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
        logger.error("an error encountered but managed accordingly")
        print("Sorry, there's an error in your input, please check it and try again")
        starting_hour, ending_hour = get_time()
    logger.info("suitable date obtained successfully")
    return starting_hour, ending_hour

def assign_date(starting_hour, ending_hour):
    """
    This function takes in the expected starting time and ending time for the calls to be made and generates a random
    time allocation based on that
    PARAMETERS:

    INPUT:
    starting_hour : time frame to start the time allocation from according to user
    ending_hour : time frame to end the time allocation as specified by te user

    OUTPUT
    date_assigned : randomly assigned time generated
    """

    try:
        day = random.randint(1,31)
        month = random.randint(1,12)
        year = datetime.datetime.now().year
        hour = random.randint(starting_hour.hour, ending_hour.hour)
        minute = random.randint(1,60)
        date_assigned = datetime.datetime(year, month, day, hour, minute)
        logger.info("a new random date %(date_assigned)s has been assigned")
    except:
        logger.info("Oops!!! seems the date date does not exist on the calender")
        date_assigned = assign_date(starting_hour, ending_hour)

    return date_assigned

def verify_date(starting_hour, ending_hour, date_assigned, dates):
    """
    This function verifies the random date verified for 3 things:
    within_time: To verify that the time frame is with the timeframe the user specified
    not_in list : To verify the date has not been assigned before
    not_close_to_another : To verify that it is not within 30 minutes range of any other time allocated

    PARAMETERS:
    INPUT:
    starting_hour : Time frame from which user wants to start calling
    ending_hour : Time frame from which user wants calls to end
    date_assigned : Random date and time allocation created
    dates: list of all the dates created

    OUTPUT:
    bool: True/False to ascertain that all parameters have been met

    """
    within_time = False
    not_in_list = False
    close_to_another = False


    if date_assigned > datetime.datetime(date_assigned.year, date_assigned.month, date_assigned.day,
                                        starting_hour.hour, starting_hour.minute) or date_assigned \
                    <= datetime.datetime(date_assigned.year, date_assigned.month, date_assigned.day,
                                        ending_hour.hour, ending_hour.minute) + datetime.timedelta(minutes = 30):
        within_time = True

    for date in dates:
        if date_assigned >= date - datetime.timedelta(minutes =30) or date_assigned <= date + datetime.timedelta(minutes = 30):
            close_to_another = True

    if date_assigned not in dates:
        not_in_list = True

    if within_time and not_in_list and not close_to_another:
        logger.info("date has been verified to be within allocated time frame, not previously allocated and not close to another date")
        return True
    else:
        logger.info("date not verified to pass")
        return False



def main():
    name_and_number = read_vcf.read_contact()
    starting_hour, ending_hour = get_time()
    date_list = list()
    call_day = CallDay()
    for number in range(len(name_and_number)):
        date_assigned = assign_date(starting_hour, ending_hour)
        if verify_date(starting_hour, ending_hour, date_assigned, call_day.dates ):
            name = name_and_number[number][0]
            number = name_and_number[number][1],
            new_person = Person(name,number, date_assigned)
            call_day.add_person(name, new_person)
            call_day.add_date(date_assigned)

if __name__ == "__main__":
    main()
