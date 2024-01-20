# Objetivo: Funções para consultas no banco de dados na tabela de fornecedores
# Autor: Yasmin Gonçalves
# Data: 20/01/2024
# Versão: 1.0

from database import connection
cursor = connection.db_clarke.cursor()

def getAllProviders():
    
    cursor.execute(
        '''select tbl_provider.*, tbl_state.state
            from tbl_provider
                inner join tbl_state
                    on tbl_state.id = tbl_provider.id_state;''')
    result = cursor.fetchall()
    
    return result

def getProvidersByKwhMinimum(minimumKwhLimit):
    
    cursor.execute(
        '''select tbl_provider.*, tbl_state.state
            from tbl_provider
                inner join tbl_state
                    on tbl_state.id = tbl_provider.id_state
                    
                    where minimun_kwh_limit <= %s''', (minimumKwhLimit,))
    result = cursor.fetchall()
    
    return result