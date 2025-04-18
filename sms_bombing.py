import serial
import time
import random

def send_sms(phone_number, message):
    modem_port = 'COM_PORT'  # Replace with the port where your modem is connected
    try:
        # Configure the modem
        modem = serial.Serial(modem_port, 9600, timeout=1)
        time.sleep(2)  # Wait for the modem to initialize
        
        # Send command to set text mode
        modem.write(b'AT+CMGF=1\r')
        time.sleep(1)
        
        # Send the phone number
        modem.write(f'AT+CMGS="{phone_number}"\r'.encode())
        time.sleep(1)
        
        # Send the message
        modem.write(message.encode() + b'\x1A')  # \x1A is the message end character
        time.sleep(1)
        
        # Read the modem's response
        response = modem.read(modem.in_waiting or 1).decode()
        print(f"Message sent: {message}")
        print("Modem response:", response)
        
        modem.close()
    except Exception as e:
        print("Error:", str(e))

# Example usage
if __name__ == "__main__":
    # Prompt the user for the phone number
    phone_number = input("Enter the phone number (with area code): ")  # Example: 11987654321

    # List of realistic messages
    messages = [
        "Hey, did you get my last alert?",
        "I think you forgot to reply to me!",
        "I'm trying to call you, but I can't!",
        "We need to discuss the project!",
        "Are you going to the event tonight?",
        "The delivery has arrived, have you picked it up?",
        "Don't forget to buy some bread!",
        "Did you see the new episode of that show?",
        "I'm at the place we agreed, where are you?",
        "Hey, just checking in to see how you are!"
    ]

    number_of_messages = 10  # Total number of messages to send
    
    for i in range(number_of_messages):
        # Choose a random message from the list
        message = random.choice(messages)
        
        # Alert a random delay between 2 and 5 seconds
        wait_time = random.randint(2, 5)
        print(f"Waiting {wait_time} seconds before sending...")
        time.sleep(wait_time)
        
        send_sms(phone_number, message)
        
        # Wait a fixed time after sending to alert wait time between messages
        time.sleep(2)