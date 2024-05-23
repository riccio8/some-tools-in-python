# phone numbers locator

import phonenumbers
from phonenumbers import geocoder

phone = input("Enter a phone number (with country code, e.g., +1234567890): \n")
try:
    phone_number = phonenumbers.parse(phone)
    print(f"Phone number entered: {phone}")
    location = geocoder.description_for_number(phone_number, "en")
    print(f"Phone number location: {location}")
except phonenumbers.phonenumberutil.NumberParseException:
    print("The phone number entered is not valid.")
