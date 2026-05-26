# 🌦️ Weather App (API Integration)

A simple Weather Application built using Python and OpenWeatherMap API.  
This command-line application fetches real-time weather information for any city, including temperature, humidity, and weather conditions.

---

## 📌 Features

✔ Real-Time Weather Data  
✔ Search Weather by City Name  
✔ Displays Temperature  
✔ Displays Humidity  
✔ Displays Weather Condition  
✔ API Integration using Requests Library  
✔ Error Handling for Invalid Cities  

---

## 🚀 Technologies Used

- Python 3
- Requests Library
- OpenWeatherMap API

---

## 📂 Project Structure

```bash
weather-app/
│
├── weather_app.py
└── README.md
```

---

## ▶ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/weather-app.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd weather-app
```

### 3️⃣ Install Required Library

```bash
pip install requests
```

### 4️⃣ Get API Key

Create a free account at:

https://openweathermap.org/api

Generate your API key and replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your actual API key.

---

### 5️⃣ Run the Program

```bash
python weather_app.py
```

---

## 💻 Program Code

```python
import requests

# Enter your API key here
API_KEY = "YOUR_API_KEY"

# User input
city = input("Enter city name: ")

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

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
```

---

## 📸 Example Output

```bash
Enter city name: Mumbai

=== Weather Report ===
City: Mumbai
Temperature: 31 °C
Humidity: 74 %
Condition: scattered clouds
```

---

## ⚠ Error Handling

The application handles:

- Invalid city names
- API request errors
- Network-related issues
- Unexpected exceptions

Example:

```bash
City not found!
```

---

## 📚 Concepts Used

- API Integration
- HTTP Requests
- JSON Data Handling
- Exception Handling
- User Input
- String Formatting
- Python Requests Library

---

## 🔮 Future Improvements

- Add wind speed
- Add weather icons
- 5-day weather forecast
- GUI version using Tkinter
- Voice-based weather assistant
- Save weather history

---

## 🤝 Contributing

Contributions are welcome.  
Feel free to fork this repository and improve the project.

---

## 📜 License

This project is open-source and available under the MIT License.

---
