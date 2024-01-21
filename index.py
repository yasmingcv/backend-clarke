# Objetivo: EndPoints para integração do desafio técnico Clarke Energia
# Autor: Yasmin Gonçalves
# Data: 20/01/2024
# Versão: 1.0

from flask import Flask, make_response, request
from controller import providersController

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = True


@app.get('/fornecedores')
def getFornecedores():
    return make_response(
        providersController.getAllProviders()
    )

@app.route('/fornecedores/minimo', methods=['GET'])
def getFornecedoresPorKwhMinimum():
    minimum_kwh = request.args.get('minimum_kwh')
    print(minimum_kwh)
    
    return make_response(
        providersController.getProvidersByKwhMinimum(minimum_kwh)
    )

    
    
app.run()