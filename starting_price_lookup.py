from selenium import webdriver
from selenium.webdriver.chrome.options import Options

brands = ['samsung', 'apple', 'lg', 'google', 'huawei', 'tcl', 'motorola']

def get_valid_brand(response):
    if (len(response) == 0):
        return 0

    if (response.lower() not in brands):
        while (response.lower() not in brands):
            if (len(response) == 0):
                return 0
            print(response + " is not one of the available brands.\n")
            response = input("Please enter a brand from the following list: " +
            "Samsung, Apple, LG, Google, Huawei, TCL and Motorola\n")

    return response

def get_preferrred_brands():
    user_brand_preferences = []
    
    response = get_valid_brand(input("If you have a brand preference, please enter them now one at a time and once you are done enter a blank space to move onto the next question. \n\n"))
    if response != 0:
        user_brand_preferences.append(response)

    while (response != 0):
        response = get_valid_brand(input("You can enter another brand here now or press enter without typing anything to move onto the next question.\n"))
        if response != 0:
            user_brand_preferences.append(response)
    
    return user_brand_preferences

def get_price_limit():

    price_limit = input()

    if(len(price_limit) == 0):
        return -1

    if(not price_limit.isdigit()):
        print("You have not entered a valid price limit. \n")
        while (not price_limit.isdigit()):
            price_limit = input("Please enter your preferred price limit now. If you have no preference, please press enter without typing anything to move onto the next question.")

    return price_limit

def get_preferred_colors():
    user_color_preferences = []

    response = input("If you have a color preferences please enter them here one at a time. If you have no preference, please press enter without typing anything to move onto the next question")
    if (len(response) != 0):
        user_color_preferences.append(response.lower())
    
    while(len(response) != 0):
        response = input("You can enter another color here now or press enter without typing anything to move onto the next question.\n")
        if len(response) != 0:
            user_color_preferences.append(response.lower())
    
    return user_color_preferences

def get_price_ranges():
    print("\nPlease enter your preferred minimum full price for a device now. If you have no preference, please press enter without typing anything to move onto the next question.")
    min_full_price = get_price_limit()

    print("Please enter your preferred maximum full price for a device now. If you have no preference, please press enter without typing anything to move onto the next question.")
    max_full_price = get_price_limit()

    full_price = [min_full_price,max_full_price]

    print("Please enter your preferred minimum 24-month monthly price for a device now. If you have no preference, please press enter without typing anything to move onto the next question.")
    min_monthly_price = get_price_limit()

    print("Please enter your preferred maximum 24-month monthly price for a device now. If you have no preference, please press enter without typing anything to move onto the next question.")
    max_monthly_price = get_price_limit()

    monthly_price = [min_monthly_price,max_monthly_price]

    return full_price, monthly_price

def get_phone_info(phone):
    name = phone.find_element_by_class_name("dl-tile-name").text
    full_price = phone.find_element_by_class_name("dl-tile-full-price").find_element_by_class_name("qc").text
    monthly_price = phone.find_element_by_class_name("dl-tile-price-wrap").find_element_by_class_name("dl-tile-price-month").find_element_by_class_name("dl-tile-price").text
    colors_select = phone.find_element_by_class_name("dl-tile-colors").find_element_by_class_name("smartpay-color-selector").find_elements_by_tag_name("li")
    colors = []
    for color in colors_select:
        colors.append(color.get_attribute("title"))
    return [name, full_price, monthly_price, colors]

def check_color_preference(phone_colors, user_color_preferences):
    valid = False

    #If the user has no color preference, the phone is valid to show
    if(len(user_color_preferences) == 0):
        return True

    #If the phone has a color that the user prefers, then the phone is valid to show
    for color in phone_colors:
        print(color)
        if color.lower() in user_color_preferences:
            valid = True

    return valid

def check_full_price_preference(phone_full_price, user_full_price_preference):
    
    #Converting the string full price to a float
    if(',' in phone_full_price):
        comma = phone_full_price.index(',')
        price = float(phone_full_price[1:comma] + phone_full_price[comma+1:])
    else:
        price = float(phone_full_price[1:])
    
    #Converting user input price preference to integers
    min = int(user_full_price_preference[0])
    max = int(user_full_price_preference[1])

    #No lower and no upper bound
    if(min == -1 and max == -1):
        return True

    #Upper bound with no lower bound
    elif(min == -1 and max >= 0):
        return (price < max)
    
    #Lower bound with no upper bound
    elif(min >= 0 and max == -1):
        return (price > min)
    
    #Upper and lower bound
    else:
        return (price > min and price < max)


#Setting Chrome to run Headless
chrome_options = Options()
chrome_options.add_argument("start-maximized")
#chrome_options.headless = True

#Started chromedriver and navigated to Bell's smartphone paage
driver=webdriver.Chrome('/Users/luthraar/Downloads/chromedriver',options = chrome_options)
driver.get('https://www.bell.ca/Mobility/Smartphones_and_mobile_internet_devices')

print("Welcome to Bell's starting price lookup program for mobile phones."
+ "After answering a few questions, the program will tell you all the info you need about the best phone for you.\n")

user_brand_preferences = get_preferrred_brands()

user_full_price_preference, user_monthly_price_preference = get_price_ranges()

user_color_preferences = get_preferred_colors()

user_phones = []

#If the user has no brand preferences, check all the brands
if(len(user_brand_preferences) == 0):
    user_brand_preferences = brands

for brand in user_brand_preferences:
    driver.find_element_by_id("filter_nav_" + brand.lower()).click()
    phones = driver.find_element_by_xpath("""//*[@id="dl-list-""" + brand.lower() + """"]/div[2]/div""").find_elements_by_class_name("dl-tile")
    for phone in phones:

        #Some tabs have a view all button that i'm skipping (Like samsung and apple)
        if('view-all' in phone.get_attribute("class")):
            continue

        #Getting the info for the phones
        phone_info = get_phone_info(phone)

        #Filtering phones based on user inputted preferences
        valid_color = check_color_preference(phone_info[3], user_color_preferences)
        valid_full_price = check_full_price_preference(phone_info[1], user_full_price_preference)

        #If all the criteria are met, add the phone to the list shown to the user
        if(valid_color and valid_full_price):
            user_phones.append(phone_info)