from flask import Flask, request, jsonify  
import requests  # llibreria per fer http requests
import json

app = Flask(__name__)    # inicialitzar poden correr amb python3  

# crear endpoint        posar la part despres del localhost i port
@app.route("/prova", methods=["GET"])    # podem posar metodes que accepta
def prova():
    return jsonify({"key" : "valor" }), 200   # Rest API retorna jason sempre   
                # return codes HTTP al final


# ara post   # guardar en fitxer
@app.route("/provaPost", methods=["POST"])
def provaPost():
    try:
        record = json.loads(request.data)
        new_str = str(record["latitud"]) + ',' + str(record["longitud"]) + "\n"

        with open("data.csv", 'a') as f:
            f.write(new_str)
        print(f"api saved -> {new_str}")

        return jsonify({"message": "completed successfully"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "internal error"}), 500




# si el fitxer s'importa com a llibreria no executa, peò si és com codi si executa aquesta part (posar tests, en el segon modo)
if __name__ == "__main__":
    app.run(debug=True)

