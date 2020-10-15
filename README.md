# Instructions

To ensure the program runs, you must first ensure Selenium is installed by running the following command:

`pip install selenium`

Once that is installed you must download chrome driver and put it in your downloads folder. I completed this program on Mac so my copy of chrome driver is located at the following destination:

`/Users/luthraar/Downloads/chromedriver`

Lastly, to run the program, type in the following command into terminal:

`python3 starting_price_lookup.py`

## Assumptions and Limitations

I am assuming the user will enter a valid color as I am not checking the user input against a valid list of colors available for the phones. So certain colors like AppleBlack and AppleJetBlack won't match if the user enters Black as one of their color preferences.

One thing I could have done more efficiently is processing the info for each of the phones only if they meet the criteria specified by the user. Currently I am getting all the relevant info for each phone for the brands the user selected and then checking if it matches their full/monthly price and color preferences. 

Another issue I ran into while working on this is trying to get chrome to run in headless mode. I could get it to work and pull data from other websites such as google.com but if i tried with Bell it would return an "Internal Server Error".
