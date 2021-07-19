from flask import Flask, request,render_template
import pickle
import json
import numpy as np

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('from_ex.html')


@app.route('/predict', methods=['POST'])
def home():
    ward= request.form['w']
    vehicle = 'Vehicle_No_' + request.form['a']
    route = 'Route_' + request.form['b']
    day = request.form['c']
    month = request.form['d']
    year = request.form['e']
    hour = request.form['f']
    minute = request.form['g']

    __vehicle = None
    __route = None
    __data_columns = []
    __model = None

    if ward == 'A':
        def get_model(x):
            with open('./artifacts/waste_a.pkl', 'rb') as f:
                __model1 = pickle.load(f)
            return round(__model1.predict([x])[0], 2)
    elif ward == 'B':
        def get_model(x):
            with open('./artifacts/waste_b.pkl', 'rb') as f:
                __model2 = pickle.load(f)
            return round(__model2.predict([x])[0], 2)
    elif ward == 'C':
        def get_model(x):
            with open('./artifacts/waste_c.pkl', 'rb') as f:
                __model3 = pickle.load(f)
            return round(__model3.predict([x])[0], 2)
    else:
        def get_model(x):
            with open('./artifacts/waste_d.pkl', 'rb') as f:
                __model4 = pickle.load(f)
            return round(__model4.predict([x])[0], 2)

    def get_estimated_price(vehicle, route, day, month, year, hour, minute):
        try:
            if ward == 'A':
                with open("./artifacts/columns_a.json", "r") as f:
                    __data_c = json.load(f)['data_columns']
                    print("HEllo ", __data_c)
                    vehicle_index1 = __data_c.index(vehicle.lower())
                    route_index1 = __data_c.index(route.lower())
            elif ward == 'B':
                with open("./artifacts/columns_b.json", "r") as f:
                    __data_c = json.load(f)['data_columns']
                    print("HEllo ", __data_c)
                    vehicle_index1 = __data_c.index(vehicle.lower())
                    route_index1 = __data_c.index(route.lower())
            elif ward == "C":
                with open("./artifacts/columns_c.json", "r") as f:
                    __data_c = json.load(f)['data_columns']
                    print("HEllo ", __data_c)
                    vehicle_index1 = __data_c.index(vehicle.lower())
                    route_index1 = __data_c.index(route.lower())
            else:
                with open("./artifacts/columns_d.json", "r") as f:
                    __data_c = json.load(f)['data_columns']
                    print("HEllo ", __data_c)
                    vehicle_index1 = __data_c.index(vehicle.lower())
                    route_index1 = __data_c.index(route.lower())
        except:
            vehicle_index1 = -1
            route_index1 = -1

        x = np.zeros(len(__data_c))
        x[0] = day
        x[1] = month
        x[2] = year
        x[3] = hour
        x[4] = minute

        if vehicle_index1 >= 0:
            x[vehicle_index1] = 1
        else:
            if route_index1 >= 0:
                x[route_index1] = 1

        return get_model(x)

    pred= get_estimated_price(vehicle,route,day,month,year,hour,minute)

    return render_template('video.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)




