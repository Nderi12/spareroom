from spare_bot import SpareBot
from sender import Sender
import time

def main():
    bot = SpareBot()
    bot.login()

    # Perform a search and open the first ad
    bot.get_ads_in_page()
    bot.open_ad_by_index(0)

    # Send an automated message
    custom_message = "Hi Arundathi, this is an automated message!"
    bot.send_custom_message(custom_message)

    # Close the browser after some delay (you can adjust the time as needed)
    time.sleep(5)
    bot.driver.quit()

if __name__ == "__main__":
    main()
