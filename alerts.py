import tkinter as tk
from tkinter import messagebox
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from plyer import notification
import json

# Function to fetch current prices of BTC, SOL, and ETH
def fetch_current_prices():
    try:
        response = session.get(url, params=parameters)
        data = response.json()
        coins = data.get('data', [])
        prices = []
        for coin in coins:
            symbol = coin.get('symbol')
            if symbol in symbols_to_monitor:
                price = coin['quote']['USD']['price']
                prices.append(f"Current price of {symbol}: ${price}")
        return "\n".join(prices)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return f"Error fetching prices: {str(e)}"

# Function to check prices and display it in a message box
def check_prices(manual=False):
    if manual:
        messagebox.showinfo("Current Prices", fetch_current_prices())
    else:
        try:
            response = session.get(url, params=parameters)
            data = response.json()
            coins = data.get('data', [])

            for coin in coins:
                symbol = coin.get('symbol')
                if symbol in symbols_to_monitor:
                    price = coin['quote']['USD']['price']
                    target_threshold = target_thresholds.get(symbol, 0)
                    stop_loss_threshold = stop_loss_thresholds.get(symbol, 0)
                    # Check for if the notification for price target is enabled
                    if target_threshold_var.get() and price >= target_threshold:
                        send_alert(symbol, price, is_target=True)
                    # Check for if the notification for stop loss is enabled
                    if stop_loss_threshold_var.get() and price <= stop_loss_threshold:
                        send_alert(symbol, price, is_target=False)

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            messagebox.showerror("Error", str(e))

        # How often the price is checked if the "Check Prices Automatically" is selected. 60000 ms = 60 seconds. In this code, I've set the default to 60 seconds below
        if auto_check_var.get() and not manual:
            window.after(60000, check_prices)

# Function to send desktop notifications
def send_alert(symbol, price, is_target=True):
    if is_target:
        title = f"Price target reached: {symbol}"
        message = f"{symbol} has reached the target price at ${price}"
    else:
        title = f"Stop loss reached: {symbol}"
        message = f"{symbol} has reached the stop loss price at ${price}"
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Notification will disappear after 10 seconds
    )

# Function to update price targets
def update_target_threshold(symbol, entry):
    new_threshold = entry.get()
    try:
        target_thresholds[symbol] = float(new_threshold)
        messagebox.showinfo("Update Price Target", f"Price Target for {symbol} updated successfully!")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the price target.")

# Function to update stop losses
def update_stop_loss_threshold(symbol, entry):
    new_threshold = entry.get()
    try:
        stop_loss_thresholds[symbol] = float(new_threshold)
        messagebox.showinfo("Update Stop loss", f"Stop loss for {symbol} updated successfully!")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the Stop loss.")

# Create a Tkinter window
window = tk.Tk()
window.title("Crypto Price Alerts ◦ Coded by C3™")
window.configure(bg="#2d2d2d")  # Set background color to dark grey

# Coinmarketcap Integration
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'10',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'APIKEYHERE',  # Replace with your API key
}

session = Session()
session.headers.update(headers)

# List of crypto-currencies that we're monitoring
symbols_to_monitor = ['BTC', 'ETH', 'SOL']

# Set default price targets here
target_thresholds = {
    'BTC': 80000,
    'ETH': 5000,
    'SOL': 250
}

# Set default stop losses here
stop_loss_thresholds = {
    'BTC': 48000,
    'ETH': 1500,
    'SOL': 120
}

# Create a frame for the automatic checking options
auto_check_frame = tk.Frame(window, bg="#2d2d2d")
auto_check_frame.pack(pady=10)

auto_check_var = tk.BooleanVar()
auto_check_var.set(True)  # Default to automatic price checking
auto_check_button = tk.Checkbutton(auto_check_frame, text="Check Prices Automatically", variable=auto_check_var)
auto_check_button.config(fg="red", bg="#2d2d2d")  # Set text color to red and background color to dark grey
auto_check_button.pack(side=tk.LEFT)

# Create a frame for the threshold options
threshold_frame = tk.Frame(window, bg="#2d2d2d")
threshold_frame.pack(pady=10)

# Create a frame for the target thresholds
target_threshold_frame = tk.Frame(threshold_frame, bg="#2d2d2d")
target_threshold_frame.pack(side=tk.LEFT, padx=20)

target_threshold_var = tk.BooleanVar()
target_threshold_var.set(True)  # Default to sending notifications for price target
target_threshold_checkbutton = tk.Checkbutton(target_threshold_frame, text="Notify when price reaches target", variable=target_threshold_var)
target_threshold_checkbutton.config(fg="red", bg="#2d2d2d")  # Set text color to red and background color to dark grey
target_threshold_checkbutton.pack()

for symbol in symbols_to_monitor:
    target_label = tk.Label(target_threshold_frame, text=f"{symbol} Price Target:", fg="red", bg="#2d2d2d")
    target_label.pack()

    target_entry = tk.Entry(target_threshold_frame, width=10)
    target_entry.insert(0, target_thresholds[symbol])
    target_entry.pack()

    update_target_button = tk.Button(target_threshold_frame, text="Update Target", command=lambda sym=symbol, entry=target_entry: update_target_threshold(sym, entry))
    update_target_button.pack(pady=(5, 0))  # Add some padding between the entry and the button

# Create a frame for the stop loss thresholds
stop_loss_threshold_frame = tk.Frame(threshold_frame, bg="#2d2d2d")
stop_loss_threshold_frame.pack(side=tk.RIGHT, padx=20)

stop_loss_threshold_var = tk.BooleanVar()
stop_loss_threshold_var.set(True)  # Default to sending notifications for stop loss
stop_loss_threshold_checkbutton = tk.Checkbutton(stop_loss_threshold_frame, text="Notify when price reaches stop loss", variable=stop_loss_threshold_var)
stop_loss_threshold_checkbutton.config(fg="red", bg="#2d2d2d")  # Set text color to red and background color to dark grey
stop_loss_threshold_checkbutton.pack()

for symbol in symbols_to_monitor:
    stop_loss_label = tk.Label(stop_loss_threshold_frame, text=f"{symbol} Stop Loss:", fg="red", bg="#2d2d2d")
    stop_loss_label.pack()

    stop_loss_entry = tk.Entry(stop_loss_threshold_frame, width=10)
    stop_loss_entry.insert(0, stop_loss_thresholds[symbol])
    stop_loss_entry.pack()

    update_stop_loss_button = tk.Button(stop_loss_threshold_frame, text="Update Stop Loss", command=lambda sym=symbol, entry=stop_loss_entry: update_stop_loss_threshold(sym, entry))
    update_stop_loss_button.pack(pady=(5, 0))  # Add some padding between the entry and the button

# Create a button to manually check current prices
manual_check_button = tk.Button(window, text="Check Current Prices", command=lambda: check_prices(manual=True))
manual_check_button.config(fg="red", bg="#2d2d2d")  # Set button text color to red and background color to dark grey
manual_check_button.pack(pady=(5, 10))

# Start automatic price checking
check_prices()

# Start the Tkinter event loop
window.mainloop()
