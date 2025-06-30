import pywhatkit as kit

# Replace with the recipient's phone number and your message
phone_number = "+916379211686"  # Use the format with country code, e.g., +1 for the US
message = "Hello, this is a test message sent using pywhatkit!"
hour = 19  # 24-hour format
minute = 10  # Minute to send the message

# Send the message
kit.sendwhatmsg(phone_number, message, hour, minute)