import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Mobile no. with country code:")
mobileNo= phonenumbers.parse(mobileNo)
print(timezone.time_zones_for_number(mobileNo))
print("Valid mobile number.", phonenumbers.is_valid_number(mobileNo))
print("Checking possibility of Number:", phonenumbers.is_possible_number(mobileNo))
