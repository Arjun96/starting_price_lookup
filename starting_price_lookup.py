from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_valid_brand(response):
    brands = ['samsung', 'apple', 'lg', 'google', 'huawei', 'tcl', 'motorola', 'other']
    if (len(response) == 0):
        return 0

    if (response.lower() not in brands):
        while (response.lower() not in brands):
            print(response + " is not one of the available brands.\n")
            response = input("Please enter a brand from the following list:" +
            "Samsung, Apple, LG, Google, Huawei, TCL, Motorola and Other\n")

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
        user_color_preferences.append(response)
    
    while(len(response) != 0):
        response = input("You can enter another color here now or press enter without typing anything to move onto the next question.\n")
        if len(response) != 0:
            user_color_preferences.append(response)
    
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


#Setting Chrome to run Headless
chrome_options = Options()
#chrome_options.headless = True

#Started chromedriver and navigated to Bell's smartphone paage
driver=webdriver.Chrome('/Users/luthraar/Downloads/chromedriver', options = chrome_options)
driver.get('https://www.bell.ca/Mobility/Smartphones_and_mobile_internet_devices')

print("Welcome to Bell's starting price lookup program for mobile phones."
+ "After answering a few questions, the program will tell you all the info you need about the best phone for you.\n")

user_brand_preferences = get_preferrred_brands()

full_price, monthly_price = get_price_ranges()

user_color_preferences = get_preferred_colors()