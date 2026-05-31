from flask import Flask ,render_template,request
import requests 
import random


app = Flask(__name__)

@app.route("/" ,methods=['GET','POST'])
def home():
        city_name = None
        icon = None
        condition = None
        temp = None
        FeelingTemp = None
        humidity = None
        windspeed = None
        pressure = None
        clouds= None
        visibalty = None
        bg_class = None
        localtime = None
        uv = None
        time = None
        date = None
        error = None
        form_class = "Fwelcom"
        input_class= "Iwelcom"
        B_class = "Bwelcom"

        
        if request.method =="POST":
            city_name = request.form.get('city')
            API_KEY = "9548c753dfdf4b609b2182935262805"
            url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_name}&aqi=no"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                icon = data["current"]["condition"]["icon"]
                condition = data["current"]["condition"]["text"]
                temp = data["current"]["temp_c"]
                FeelingTemp = data["current"]["feelslike_c"]
                humidity = data["current"]["humidity"]
                windspeed = data["current"]["wind_kph"]
                pressure = data["current"]["pressure_mb"]
                clouds = data["current"]["cloud"]
                visibalty = data["current"]["vis_km"]
                uv = data["current"]["uv"]
                localtime = data["location"]["localtime"].split()
                time = localtime[1]
                date = localtime[0]
                error = None
                if "sunny" in condition.lower() or "clear" in condition.lower():
                     classes = ["sky","sky1","sky2","sky3"]
                     bg_class = random.choice(classes)
                elif condition.lower() in ["cloudy","overcast","mist","partly cloudy"]:
                     classes = ["cloud1","cloud2","cloud3","cloud4"]
                     bg_class = random.choice(classes)
                elif "rain" in condition.lower():
                    classes = ["rain1","rain2","rain3"]
                    bg_class = random.choice(classes)
                elif "storm" in condition.lower() or "thunder" in condition.lower():
                    classes = ["storm1","storm2","storm3"]
                    bg_class = random.choice(classes)
                elif condition.lower() in ["sandstorm","dust","windy"] or "fog" in condition.lower():
                    classes = ["windy1","windy2"]
                    bg_class = random.choice(classes)
                elif condition.lower() in ["ice pellets","blizzard"] or "snow" in condition.lower():
                    classes = ["snow1","snow2"]
                    bg_class = random.choice(classes) 

            elif response.status_code != 200:
                error = "City Not Found"
            
            if city_name and condition :
                form_class = "Ffact"
                input_class= "Ifact"
                B_class = "Bfact"
                



        return render_template('index.html', city_name=city_name, icon=icon, condition=condition, 
                                temp=temp, FeelingTemp=FeelingTemp, humidity=humidity, windspeed=windspeed,
                                    time=time, date=date,error=error, pressure=pressure,clouds= clouds, 
                                    visibalty=visibalty, uv=uv, bg_class=bg_class ,form_class=form_class,
                                    input_class = input_class, B_class = B_class)

if __name__ == "__main__":
    app.run(debug=True)