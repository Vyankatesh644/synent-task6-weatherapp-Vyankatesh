import requests

# Enter your API key here
API_KEY = "Enter Your Key"

# User input
city = input("Enter city name: ")

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={"Enter Your Key"}&units=metric"

try:
    # Send request
    response = requests.get(url)

    # Convert response to JSON
    data = response.json()

    # Check if city exists
    if data["cod"] != 200:
        print("City not found!")

    else:
        # Extract weather details
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        # Display output
        print("\n=== Weather Report ===")
        print("City:", city)
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", weather)

except Exception as e:
    print("Error:", e)
