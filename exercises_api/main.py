import requests
import datetime as dt
API_ID = "c0f23f0c"
API_KEY = "8dc985f54e5c6f64c5f5fb034986b346"
AGE = 19
weight = 74
height = 171
GENDER = "Male"

position_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/791568cec81f3800223a40758d85f37f/munchedboxExercise/workouts"
text = input("Напиши о проделанных упражнениях: ")
headers = {
    "x-app-id":API_ID,
    "x-app-key":API_KEY
}

stock_params = {
    "query":text,
    "weight_kg":weight,
    "height_cm":height,
    "age":AGE,
    "gender":GENDER
}

response = requests.post(url = position_endpoint,json = stock_params,headers=headers)
result = response.json()


today_date = dt.datetime.now().strftime("%d/%m/%Y")
today_time = dt.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input = {
        "workout":{
            "date":today_date,
            "time":today_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url = sheet_endpoint,json = sheet_input,auth = ("munchedbox23","Rfgtkm456879!"))
print(sheet_response.text)


