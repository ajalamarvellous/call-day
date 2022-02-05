import re
import logging

logging.basicConfig(format = "%(asctime)s [%(levelname)s]: %(message)s", level = logging.DEBUG )
logger = logging.getLogger()

def matches(word):
    """
    regular expression to match the name and number of the users
    FN: Prefix before the name in the vcf file_content
    TEL;CELL: Prefix before the phone numbers in the vcf file

    INPUT:
    word = list of words from the vcf containing everying information saved about a person in the vcf file

    OUTPUT:
    regular expression match list of names and number in format [(name, ""), ("", number)]
    """
    match_regex = re.compile(r"FN:(.+)|TEL;CELL:(.+)")
    return match_regex.findall(word)

def get_matches(file_content):
    """
    apply the regular expression function already written to the content of the vcf file to obtain the matches
    INPUT:
    file_content : list containing entries about different people as different entities
                   ["information about person A jammed together", "information about person B jammed together"]

    OUTPUT
    regex_list : list containing the raw result of regular expression matching the name and phone number
                 [[("name1",""), ("","phone_no1")],[("name2",""), ("","phone_no2")]]
    """
    regex_list = list()
    for x in file_content:
        name_number_match = matches(x)
        #print(name_number_match)
        regex_list.append(name_number_match)
    logger.info(f"Regular expression matching done for total {len(regex_list)} entries")
    return regex_list

def get_name_number(list_given):
    """
    get the names and phone numbers only out the returned regular expression list
    INPUT:
    list_given = [[("name1",""), ("","phone_no1")],[("name2",""), ("","phone_no2")]]

    OUTPUT
    name_number_pair = [(name1, number1), (name2,number2)]
    """
    name_number_pair = list()
    for pair in list_given:
        if len(pair) >= 2:
            name, number = pair[0][0], pair[1][1]
            name_number_pair.append((name,number))
    logger.info(f"Name and numbers extracted, {len(name_number_pair)} entries left")
    return name_number_pair


def main():
    #main application to run the application
    f = open("contacts.vcf", "r")
    file_content = f.read()
    logger.info("vcf file read")
    file_content = file_content.split("END:VCARD")
    regex_list = get_matches(file_content)
    name_number_list = get_name_number(regex_list)
    return name_number_list


if __name__ == "__main__":
    main()
