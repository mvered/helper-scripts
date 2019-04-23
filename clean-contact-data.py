
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

    # Checks string against inputted invalid values
    for v in invalids:
        if string == v:
            return True

    # Checks string against default invalid values, if defaults=True
    if  defaults == True:
        default_invalids = ['INC','inc','incomplete','NaN','nan','N/A','n/a','missing']
        for v in default_invalids:
            if string == v:
                return True

    # For valid strings 
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


def clean_lastname(name, *additional_invalids, check_defaults=False, check_titlesuffix=False):
    """Removes invalid values and non-alphabetical characters, standardizes case"""

    # Returns empty string if name matches an invalid value
    if check_invalid(name,*additional_invalids, defaults=check_defaults) == True:
        return ''

    # Converts all characters to upper case
    clean_name = name.upper()

    # Checks for suffixes and titles if option is set to True
    if check_titlesuffix == True:
        
        # checks for suffixes in suffix_list, strips from clean_name and saves as suffix
        suffix_list = ['JR','J.R.','SR','S.R.','III','IV']
        suffix = ''
        for s in suffix_list:
            if clean_name[(-len(s)-1):] == ' ' + s:
                suffix = clean_name[-len(s):]
                clean_name = clean_name[:(-len(s)-1)]

        # Checks for titles in title_list and strips from clean_name
        title_list = ['MD','M.D.','DO','D.O.','DVM','D.V.M.','JD','J.D.','PHD','PH.D.']
        for t in title_list:
            if clean_name[(-len(t)-1):] == ' ' + t:
                clean_name = clean_name[:(-len(t)-1)]

    # Removes non-alpha characters
    clean_name = alpha_only(clean_name)

    # Returns name and suffix if check_titlesuffix=True
    if check_titlesuffix == True:
        return clean_name, suffix

    # Otherwise just returns name
    else:
        return clean_name

def clean_firstname(name, *additional_invalids, check_defaults=False, check_title=False):
    """Separates out middle names, titles, extra names. Removes invalid values."""

    # Returns empty strings if name matches an invalid value
    if check_invalid(name,*additional_invalids, defaults=check_defaults) == True:
        return '','',''

    # Converts all characters to upper case
    name = name.upper()

    # Removes additional household members who may have been included in the same field
    name = name.replace(' and ', ' , ')  #replace 'and' delimiter with comma 
    name = name.replace(' & ',' , ')     #replace '&' delimiter with comma
    split_name = name.split(',',1)       #splits text field in two at comma
    main_name = split_name[0]            #saves the first name in list as main_name
    
    # Saves additional names to extra_names if any exist, otherwise it will be an empty string
    if len(split_name) > 1:
        extra_names = split_name[1]
    else:
        extra_names = ''

    # Checks for titles if option is set to True and removes them from main_name field
    if check_title == True:
        title_list = ['DR.','DR','REV.','REVEREND','HON.','HON','THE HONORABLE','THE REVEREND DR.']
        for t in title_list:
            if main_name[:(len(t)+1)] == t + ' ':
                main_name = main_name[(len(t)+1):]

    # Removes middle names from main_name
    split_main_name = main_name.split(' ',1)
    main_name = split_main_name[0]

    # Saves middle names to middle_name if any exist, otherwise it will be an empty string
    if len(split_main_name) > 1:
        middle_name = split_main_name[1]
    else:
        middle_name = ''

    # Removes non-alpha characters from main and middle names
    main_name = alpha_only(main_name)
    middle_name = alpha_only(middle_name)

    return main_name, middle_name, extra_names