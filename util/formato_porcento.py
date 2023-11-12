from decimal import Decimal

def contar_casas_decimais(numero):
    decimal_numero = Decimal(str(numero))
    casas_decimais = abs(decimal_numero.as_tuple().exponent)
    return casas_decimais

def formato_porcentagem(numero):
    quantidade_casa_decimal = contar_casas_decimais(numero)
    if(quantidade_casa_decimal == 2 or quantidade_casa_decimal == 1):
        numero_percentual = "{:.0%}".format(numero)
    elif(quantidade_casa_decimal == 3):   
        numero_percentual = "{:.1%}".format(numero)
    else:
        numero_percentual = "{:.2%}".format(numero)
    
    return numero_percentual