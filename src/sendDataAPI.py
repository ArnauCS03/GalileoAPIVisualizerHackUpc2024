from flask import Flask, jsonify  
import requests
import json

# endpoint global on volem enviar  (url on volem enviar)
data_endpoint = "http://127.0.0.1:5000/provaPost"

def send_data_api(lat, long):
    # llista dades
    body = {
        "latitud": lat,
        "longitud": long
    }
    response = requests.post(data_endpoint, 
                              data = json.dumps(body))

    return response.status_code, response.text



send_data_api(1,2)
send_data_api(5,3)
send_data_api(12,52)
send_data_api(5,123123)

