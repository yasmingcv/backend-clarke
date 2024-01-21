# Objetivo: EndPoints para integração do desafio técnico Clarke Energia
# Autor: Yasmin Gonçalves
# Data: 20/01/2024
# Versão: 1.0

import sys

sys.dont_write_bytecode = True

from flask import Flask, make_response, request
from controller import providersController
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = True
CORS(app, origins='*')

@app.route('/providers', methods=['GET'])
def getFornecedores():
    minimum_kwh = request.args.get('minimum_kwh')
    
    if(minimum_kwh):
        return make_response(
        providersController.getProvidersByKwhMinimum(minimum_kwh)
        )
    else:
        return make_response(
        providersController.getAllProviders()
        )
        
    
app.run()
