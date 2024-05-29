# Crypto-Price-Alerts
A user-friendly Python GUI application for monitoring Bitcoin, Solana, & Ethereum prices and receiving desktop notifications based on your defined thresholds. You'll also be able to check the current price of all three crypto-currencies from within the application.

![image](https://github.com/C3-Security/Crypto-Price-Alerts/assets/167286637/e89d105e-a228-4982-a90a-2d5384b16ccc)


# Features
- Check Current Prices: Crypto Price Alerts will allow you check the currency prices of Bitcoin, Solana, & Ethereum.

- Real-Time Data: The application pulls data directly from CoinMarketCap's API, ensuring that you're receiving accurate prices & alerts.

- Set Price Targets & Stop Losses: Within Crypto Price Alerts, you'll be able to specify a price target & stop loss for Bitcoin, Solana, and Ethereum . Whenever the price reaches that price target/Stop Loss, it'll trigger a notification sent straight to your desktop.

- Desktop Notifications: Desktop notifications are sent when the price reaches the set target or the stop loss threshold is passed.

- Automatic Price Checking : Crypto Price Alerts automatically compare the price targets/stop losses that you set with the prices on CoinMarketCap using CMC's API every 60 seconds.

- Enable/Disable features: While this script does check the price every 60 seconds, then compares it against your current values. I did include the option to completely turn off/on price checking for both price targets & stop losses.

- API Integration: The script integrates with the CMC API to fetch crypto prices

# Examples

Enable/Disabling features & updating price targets/stop losses

![Code_UosEJnDb4D](https://github.com/C3-Security/Crypto-Price-Alerts/assets/167286637/9d3f3e84-b699-486d-a6fb-b6d75e59385d)

Price target of $165 being passed on SOL being reached, thus triggering a desktop notification.

![Code_UR3hOXkAVb](https://github.com/C3-Security/Crypto-Price-Alerts/assets/167286637/ac987271-92a5-4c30-bd39-0e4f8d3a6388)

Stop Loss of $170 on SOL being reached, thus triggering a desktop notification

![Code_LZjCFHVC4z](https://github.com/C3-Security/Crypto-Price-Alerts/assets/167286637/4117468e-2155-49ba-a835-6e70cae10d72)

# Dependencies
To use this crypto alert bot, you'll need the following dependencies installed in your Python environment:
- [Tkinter](https://docs.python.org/3/library/tkinter.html): A standard GUI (Graphical User Interface) toolkit for Python. It provides various widgets and functions to create graphical applications.
- [Requests](https://pypi.org/project/requests/): A library used to make HTTP requests in Python. It's used here to fetch data from the CoinMarketCap API.
- [Plyer](https://pypi.org/project/plyer/): A Python library for accessing features commonly found on various platforms (like desktop notifications). It provides a unified API for different platforms.

# Getting Started
In order to use this bot, you'll have to obtain an API key from [Coinmarketcap](https://coinmarketcap.com/api/) simply by registering and clicking "Obtain Key". While API keys are free, you do have a monthly limit of 10,000 credits. You'll most likely never exceed that limit though.

1. Clone the repository to your local machine
2. Ensure you have Python & the required dependencies installed
3. Add your API key to the section that states "APIKEYHERE"

![image](https://github.com/C3-Security/Crypto-Price-Alerts/assets/167286637/d177bb40-febd-4377-95b6-1038c8917d9a)

4. Run alerts.py script to launch the application & set your desired price targets/stop losses.
5. The application will have everything turned on by default, you can adjust it according to your needs.

# Functions Explained

- fetch_current_prices: This function sends a request to the CoinMarketCap API to retrieve the latest prices of cryptocurrencies (BTC, ETH, SOL). It then parses the API response to extract the relevant information (current prices) and formats it as a string.

- check_prices: The purpose of this function is to monitor cryptocurrency prices. When called with manual=True, it displays the current prices in a message box. When called with manual=False, it automatically checks prices based on the settings and sends notifications if the prices exceed the set thresholds for target and stop loss.

- send_alert: This function is responsible for sending desktop notifications using the Plyer library. It takes parameters such as the cryptocurrency symbol, current price, and whether the notification is for reaching a price target or stop loss.

- update_target_threshold: This function updates the target price threshold for a specified cryptocurrency. It takes the cryptocurrency symbol and the corresponding entry widget (where the user inputs the new threshold) as parameters.

- update_stop_loss_threshold: Similar to update_target_threshold, this function updates the stop loss threshold for a specified cryptocurrency.

# Author Notes

Thank you for checking out my crypto alerts bot. This bot was designed to be a light-weight application that's ran in the background of the computer to send desktop notifications whenever one of my favorite Crypto-currencies reach a price target or breaks a stop losss.

While creating this project, we've learned the following..
- API Integration: Understanding how to interact with external APIs to fetch real-time data, in this case, cryptocurrency prices from the CoinMarketCap API.

- GUI Development: Creating a graphical user interface (GUI) using tkinter, including widgets such as buttons, checkboxes, labels, and entry fields.

- Event Handling: Understanding how to handle events such as button clicks and checkbox changes to trigger specific actions in the program.

- Error Handling: Implementing error handling mechanisms to handle exceptions, such as connection errors or timeouts when making API requests.

- Desktop Notifications: Exploring how to send desktop notifications using the Plyer library, enabling users to receive alerts even when the application is running in the background.

- Data Parsing and Formatting: Parsing JSON data retrieved from the API response and formatting it appropriately for display in the GUI or for processing within the application.
