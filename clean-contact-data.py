
# Cleans contact data such as names and phone numbers

# author: Michelle Vered
# date updated: 4/23/19

# smaller functions
def alpha_only(string):
    """Removes non-alpha characters"""
    letters = [char for char in str(string) if char.isalpha()]
    return ''.join(letters)

def digit_only(string):
    """Removes non-digit characters"""
    digits = [char for char in str(string) if char.isdigit()]
    return ''.join(digits)

def check_invalid(string,*invalids,defaults=True):
    """Checks if input string matches an invalid value"""

    # Checks inputted invalid values
    for v in invalids:
        if string == v:
            return True

    # Checks default invalid values
    if  defaults == True:
        default_invalids = ['INC','inc','incomplete','NaN','nan','N/A','n/a','missing']
        for v in default_invalids:
            if string == v:
                return True

    # If the string is valid
    return False


# main functions
def clean_phone(phone_number, drop_invalid=False, area_code='406'):
    """Standardizes phone number formatting for American numbers"""
    
    # Removes non-digit characters
    clean_number = digit_only(phone_number)

    # Removes US country code if present
    if len(clean_number) == 11 and clean_number[0] == '1': 
        clean_number = clean_number[1:]

    # Adds area code if missing
    elif len(clean_number) == 7:
        clean_number = area_code + clean_number

    # If drop_invalid is true, returns empty string for still too long/short numbers
    elif drop_invalid == True and len(clean_number)!=10:
        clean_number = ''

    return clean_number


def clean_lastname(name, *additional_invalids, check_defaults=False):
    """Removes invalid values and non-alphabetical characters, standardizes case"""

    # Returns empty string if name matches an additional invalid value
    if check_invalid(name,*additional_invalids, defaults=check_defaults) == True:
        return ''

    # Converts all characters to upper case
    clean_name = clean_name.upper()

    # Checks for suffixes and titles
    

    # Removes non-alpha characters
    clean_name = alpha_only(name)


    return clean_name, suffix



