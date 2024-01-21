# Objetivo: Arquivo responsável pela regra de negócios da tabela de fornecedores
# Autor: Yasmin Gonçalves
# Data: 20/01/2024
# Versão: 1.0

from model import providersDAO
from modulo import config
from flask import jsonify


def getAllProviders():
    print('caiuadiuasdu')
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
                  'total_clients': provider[9],
                  'state': provider[10]
                }
            )
        
        return jsonify({
            "status": config.SUCCESS_REQUEST["status"],
            "message": config.SUCCESS_REQUEST["message"],
            "data": providersFormatted
        }), config.SUCCESS_REQUEST["status"]
        
def getProvidersByKwhMinimum(minimumKwhLimit):
    print(minimumKwhLimit)
    
    if(minimumKwhLimit == ''):
        return jsonify(config.ERROR_REQUIRED_FIELD), config.ERROR_REQUIRED_FIELD["status"]
    else:
        providers = providersDAO.getProvidersByKwhMinimum(minimumKwhLimit)
        
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
                    'state': provider[9],
                    'total_clients': provider[10]
                    }
                )
            
            return jsonify({
                "status": config.SUCCESS_REQUEST["status"],
                "message": config.SUCCESS_REQUEST["message"],
                "data": providersFormatted
            }), config.SUCCESS_REQUEST["status"]