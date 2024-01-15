import requests
from bs4 import BeautifulSoup
from bot import SpareBot

class Sender:
    def send_custom_message(message, recipient_name):
        url = "https://example.com/flatmate/flatmate_detail.pl"  # Replace with the actual URL
        payload = {
            'flatshare_id': '16856055',
            'action': 'sendemail',
            'mode': 'contact',
            'submode': 'byemail',
            'flatshare_type': 'wanted',
            'message': message.format(recipient_name),
            # Include other hidden fields as needed
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        response = requests.post(url, data=payload, headers=headers)

        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
            print(response.text)

    if __name__ == "__main__":
        recipient_name = input("Enter the recipient's name: ")
        custom_message = "Hi {}, this is a custom message from the Python script!"
        send_custom_message(custom_message, recipient_name)

