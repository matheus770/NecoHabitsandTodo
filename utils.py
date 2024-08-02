import calendar
from datetime import datetime



def obtem_dias_mes_atual():
    ano_atual = datetime.now().year
    mes_atual = datetime.now().month
    dia_atual = datetime.now()
    data_formatada = dia_atual.strftime("%d/%m/%Y")
    nome_mes_atual = dia_atual.strftime("%B")
    dias_no_mes = calendar.monthrange(ano_atual, mes_atual)[1]
    
    data_info_dict = {
        "dia_atual_formatado" : data_formatada,
        "dias_mes": dias_no_mes,
        "nome_mes": nome_mes_atual
    }
    
    return data_info_dict
    

# teste = obtem_dias_mes_atual()
# print(teste)