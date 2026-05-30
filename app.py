from flask import Flask ,render_template,request
import requests 


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
        localtime = None
        time = None
        date = None
        error = None
 
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
                localtime = data["location"]["localtime"].split()
                time = localtime[1]
                date = localtime[0]
                error = None
            elif response.status_code != 200:
                error = "City Not Found"



        return render_template('index.html', city_name=city_name, icon=icon, condition=condition, 
                                temp=temp, FeelingTemp=FeelingTemp, humidity=humidity, windspeed=windspeed,
                                    time=time, date=date,error=error, pressure=pressure,clouds= clouds, visibalty=visibalty)

if __name__ == "__main__":
    app.run(debug=True)