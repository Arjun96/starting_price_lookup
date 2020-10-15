# Starting Price Lookup

At Bell, our sales department receives thousands of calls per day from customers inquiring about the prices of our smartphones. One of the sales directors is very hip and loves vintage things, especially vintage graphic cards! Everyone in the department must use new computers with weak graphic cards that cannot load most of today's graphic intensive websites.

To help our sales people get information quickly to serve our customers more efficiently, we need to create a program that spits out a list of phones that matches given criteria on a CLI (Command-line interface).

## Technology

Below is a list of technology to use:

- You can use any programming language, we recommend: Ruby, Python, or Java
- You can use any environment, we recommend a linux environment
- Selenium WebDriver
- A driver like chromedriver (chrome) or geckodriver (firefox)

## Expectations

- When a user (sales staff) starts the program, the user should get a welcome message
- The CLI should then take the user through a series of questions asking the caller about their preferences for purchasing a new phone
- The CLI should ask the following **OPTIONAL** questions: list of preferred vendors, preferred full price range, preferred 24-month monthly price (with $0 down) range, and list of preferred colours
- The program should then go to the [Bell Smartphone page](https://www.bell.ca/Mobility/Smartphones_and_mobile_internet_devices) and using the answers of the above optional questions capture a list of devices that match the criteria
- The program should then present a formatted list of matching devices with the Vendor Name, Model Name, Full Price, 24-month w/ $0 down price, and list out all colours per device

## Things to keep in mind

- You should build the CLI so that it allows the sales staff to find the price efficiently
- How you make the CLI user-friendly is entirely up to you
- Make sure you have a detailed README with instructions on how to run your program

## How to manage your work

- Create a fork of this repo
- Make sure the repo is set to **private** and add the following GitHub users: `jbhandari` & `fztr`
- Make sure to commit your code in logical portions, we like a good git workflow and a clean git history !
  - ex: `Added ability to fetch price`

## Additional Information

- Should you need any further clarifications please do not hesitate to contact me via email at `jatin.bhandari@bell.ca`
- Once the deadline has been reached (set by the hiring manager), the repo will be cloned and then analyzed privately
