# Objetivo: Arquivo responsável pela regra de negócios da tabela de fornecedores
# Autor: Yasmin Gonçalves
# Data: 20/01/2024
# Versão: 1.0

from model import providersDAO
from modulo import config
from flask import jsonify


def getAllProviders():
    providers = providersDAO.getAllProviders()
    
    if not providers:
        return jsonify(config.ERROR_NOT_FOUND), config.ERROR_NOT_FOUND["status"]
        
    else:
        providersFormatted = list()
        for provider in providers:
            providersFormatted.append(
                {
                  'id': provider[0],
                  'name': provider[1],
                  'logo': provider[2],
                  'cost_per_kwh': provider[3],
                  'minimun_kwh_limit': provider[4],
                  'average_rating': provider[5],
                  'state': provider[9]
                }
            )
        
        return jsonify({
            "status": config.SUCCESS_REQUEST["status"],
            "message": config.SUCCESS_REQUEST["message"],
            "data": providersFormatted
        }), config.SUCCESS_REQUEST["status"]