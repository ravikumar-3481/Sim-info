import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# Example Number (India)
number = input("Enter your number: ")
parsed_number = phonenumbers.parse(number)

# Get region (State or City)
region = geocoder.description_for_number(parsed_number, "en")

# Get carrier (Airtel, Jio, etc.)
service_provider = carrier.name_for_number(parsed_number, "en")

# Get timezone (circle can be approx judged from this in India)
time_zones = timezone.time_zones_for_number(parsed_number)

# TRAI Circle guess (manually mapping timezone to circle for India)
circle_mapping = {
    'Asia/Kolkata': 'All India / Local Circle (TRAI)',
    # Ye mapping aur refine kar sakte ho agar chaho
}

circle = circle_mapping.get(time_zones[0], "Unknown Circle")

# Output
print(f"Phone Number: {number}")
print(f"Region (State/City): {region}")
print(f"Carrier: {service_provider}")
print(f"Approx Circle (Based on timezone): {circle}")
