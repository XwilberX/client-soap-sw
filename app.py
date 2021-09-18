from flask import Flask, render_template, redirect, url_for, request
from zeep import Client
#Consumir el servicio SOAP

app = Flask(__name__,
            static_url_path='/static')

wsdl = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
client = Client(wsdl=wsdl)

@app.route("/")
def home():
    data = client.service.ListOfContinentsByName()
    
    return render_template('index.html', data = data)

@app.route('/continente/<string:code>')
def continent(code):
    data = client.service.ListOfCountryNamesGroupedByContinent()
    
    for continent in data:
        if continent['Continent']['sCode'] == code:
            data = continent
   
    return render_template('continente.html', data = data)

    
app.run(debug = True)
