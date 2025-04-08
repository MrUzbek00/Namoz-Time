from flask import Flask, render_template, request
from datetime import datetime
from cities import cities
import pytz
import requests




app = Flask(__name__)

@app.route("/")
def new_index():
    time_zone = pytz.timezone("Asia/Tashkent")
    week_days = { "Monday":"Dushanba", 
                 "Tuesday":"Seshanba", 
                 "Wednesday":"Chorshanba", 
                 "Thursday":"Payshanba", 
                 "Friday": "Juma",
                  "Saturday": "Shanba", 
                  "Sunday": "Yakshanba" }
    td = datetime.now(time_zone)
    today =  td.weekday() 
    current_time = td.strftime("%H:%M")
    day_of_week = td.strftime('%A')
    
    city = request.args.get("city")

    if not city:
        city ="Toshkent"
    
    api_response = requests.get(
    url=f"https://islomapi.uz/api/present/day?region={city}")

    data = api_response.json()
    
    pray_times = data["times"]

    return render_template("new_index.html", time= current_time, 
                                             today =week_days[day_of_week], 
                                             pray_times=pray_times,
                                             cities=cities, selected_city=city)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)

