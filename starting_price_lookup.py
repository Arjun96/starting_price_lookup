from selenium import webdriver
from selenium.webdriver.chrome.options import Options

brands = ['samsung', 'apple', 'lg', 'google', 'huawei', 'tcl', 'motorola']
error_msg = "If you have no preference, please press enter without typing anything to move onto the next question"

def get_valid_brand(response):
    """
    Inputs the user response to what brand they prefer
    Returns a brand once it confirms it is one of the ones that Bell offers
    """

    #No brand preference
    if (len(response) == 0):
        return 0

    #Error checking on user input
    if (response.lower() not in brands):
        while (response.lower() not in brands):
            if (len(response) == 0):
                return 0
            print(response + " is not one of the available brands.\n")
            response = input("Please enter a brand from the following list: " +
            "Samsung, Apple, LG, Google, Huawei, TCL and Motorola\n")

    return response

def get_preferrred_brands():
    """
    Returns a list that contains the user's brand preferences
    """

    user_brand_preferences = []
    
    #Gets the first brand the user prefers
    response = get_valid_brand(input("If you have a brand preference, please enter them one at a time.\n"))
    if response != 0:
        user_brand_preferences.append(response)

    #Allows the user to enter more than 1 brand as a preference
    while (response != 0):
        response = get_valid_brand(input("\nYou can enter another brand here now or press enter without typing anything to move onto the next question.\n"))
        if response != 0:
            user_brand_preferences.append(response)
    
    return user_brand_preferences

def get_price_limit():
    """
    Helper function to get a valid price for both monthly and full price preferences
    Returns the price limit
    """

    price_limit = input()

    #No preference
    if(len(price_limit) == 0):
        return -1

    #Checks to make sure the user has entered a valid number as the input
    if(not price_limit.isdigit()):
        print("You have not entered a valid price limit. \n")
        while (not price_limit.isdigit()):
            price_limit = input("Please enter your preferred price limit now.")

    return price_limit

def get_preferred_colors():
    """
    Returns a list of colors that contains the user's color preferences
    """
    user_color_preferences = []
    response = input("\nIf you have a color preferences please enter them here one at a time.\n")

    #Adds the color to the list to be returned
    if (len(response) != 0):
        user_color_preferences.append(response.lower())
    
    #Allows the user to enter more colors
    while(len(response) != 0):
        response = input("\nYou can enter another color here now or press enter without typing anything to move onto the next question.\n")
        if len(response) != 0:
            user_color_preferences.append(response.lower())
    
    return user_color_preferences

def get_price_ranges():
    """
    Returns 2 lists that contain the min and max values for the monthly and full price the user is willing to pay for a device
    """

    #Gets the min/max full price preference
    print("\nPlease enter your preferred minimum full price for a device now.")
    min_full_price = get_price_limit()
    print("\nPlease enter your preferred maximum full price for a device now.")
    max_full_price = get_price_limit()

    full_price = [min_full_price,max_full_price]

    #Gets the min/max monthly price preference
    print("\nPlease enter your preferred minimum 24-month monthly price for a device now.")
    min_monthly_price = get_price_limit()
    print("\nPlease enter your preferred maximum 24-month monthly price for a device now.")
    max_monthly_price = get_price_limit()

    monthly_price = [min_monthly_price,max_monthly_price]

    return full_price, monthly_price

def get_phone_info(phone):
    """
    Inputs the web element that corresponds to a phone
    Returns an array that contains all the necessary info to be displayed back to the user
    """

    #Gets the phones relevant information from the web element
    name = phone.find_element_by_class_name("dl-tile-name").text
    full_price = phone.find_element_by_class_name("dl-tile-full-price").find_element_by_class_name("qc").text
    monthly_price = phone.find_element_by_class_name("dl-tile-price-wrap").find_element_by_class_name("dl-tile-price-month").find_element_by_class_name("dl-tile-price").text
    colors_select = phone.find_element_by_class_name("dl-tile-colors").find_element_by_class_name("smartpay-color-selector").find_elements_by_tag_name("li")
    colors = []

    for color in colors_select:
        colors.append(color.get_attribute("title"))

    return [name, full_price, monthly_price, colors]

def check_color_preference(phone_colors, user_color_preferences):
    """
    Inputs a list that contains all the colors available for a phone and another list that contains all the colors the user prefers
    Returns a boolean value indicating if the phone is available in a color that the user has a preference for
    """
    valid = False

    #If the user has no color preference, the phone is valid to show
    if(len(user_color_preferences) == 0):
        return True

    #If the phone has a color that the user prefers, then the phone is valid to show
    for color in phone_colors:
        if color.lower() in user_color_preferences:
            valid = True

    return valid

def check_price(price, user_price_preference):
    """
    Inputs the price for the phone and a list containing the min/max price the user is willing to pay for a phone
    Returns a boolean value indicating if the phone is in the users price preference
    """

    #Converting user input price preference to integers
    min = int(user_price_preference[0])
    max = int(user_price_preference[1])

    #No lower and no upper bound
    if(min == -1 and max == -1):
        return True

    #Upper bound with no lower bound
    elif(min == -1 and max >= 0):
        return (price <= max)
    
    #Lower bound with no upper bound
    elif(min >= 0 and max == -1):
        return (price >= min)
    
    #Upper and lower bound
    else:
        return (price >= min and price <= max)


def check_full_price_preference(phone_full_price, user_full_price_preference):
    """
    Inputs the full price of a phone and the users min/max full price preference
    Returns a boolean value indicating if the phone is in the users price preference
    """
    
    #Converts the string to a float value to be processed by the helper
    if(',' in phone_full_price):
        comma = phone_full_price.index(',')
        price = float(phone_full_price[1:comma] + phone_full_price[comma+1:])
    else:
        price = float(phone_full_price[1:])

    return check_price(price, user_full_price_preference)
    

def check_monthly_price_preference(phone_monthly_price, user_monthly_price_preference):
    """
    Inputs the full price of a phone and the users min/max full price preference
    Returns a boolean value indicating if the phone is in the users price preference
    """

    #Converts the string to a float value to be processed by the helper
    price = float(phone_monthly_price[1:-4])
    return check_price(price, user_monthly_price_preference)


#Setting Chrome to run Headless
chrome_options = Options()
chrome_options.add_argument("start-maximized")
#chrome_options.headless = True

#Started chromedriver and navigated to Bell's smartphone paage
driver=webdriver.Chrome('/Users/luthraar/Downloads/chromedriver',options = chrome_options)
driver.get('https://www.bell.ca/Mobility/Smartphones_and_mobile_internet_devices')

print("\n\n\nWelcome to Bell's starting price lookup program for mobile phones.\n"
+ "After answering a few optional questions, the program will tell you all the info you need about the best phone for you.\n" +
"If you do not have a preference for one of the optional questions, please press enter without typing anything to move on \n \n")


user_brand_preferences = get_preferrred_brands()
user_full_price_preference, user_monthly_price_preference = get_price_ranges()
user_color_preferences = get_preferred_colors()

user_phones = []

#If the user has no brand preferences, check all the brands
if(len(user_brand_preferences) == 0):
    user_brand_preferences = brands

for brand in user_brand_preferences:

    #Getting the phones that are available by the current brand
    driver.find_element_by_id("filter_nav_" + brand.lower()).click()
    phones = driver.find_element_by_xpath("""//*[@id="dl-list-""" + brand.lower() + """"]/div[2]/div""").find_elements_by_class_name("dl-tile")
    
    for phone in phones:

        #Some tabs have a view all button that i'm skipping (Like samsung and apple)
        if('view-all' in phone.get_attribute("class")):
            continue

        #Getting the info for the phones
        phone_info = get_phone_info(phone)

        #Filtering phones based on user inputted preferences
        valid_full_price = check_full_price_preference(phone_info[1], user_full_price_preference)
        valid_monthly_price = check_monthly_price_preference(phone_info[2], user_monthly_price_preference)
        valid_color = check_color_preference(phone_info[3], user_color_preferences)

        #If all the criteria are met, add the phone to the list shown to the user
        if(valid_color and valid_full_price and valid_monthly_price):
            user_phones.append(phone_info)

driver.quit()

for phone in user_phones:
    print(phone[0])
    print(phone[1])
    print(phone[2])