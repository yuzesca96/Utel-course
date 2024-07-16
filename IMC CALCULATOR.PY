def calcular_imc(peso, altura):
    """
Calcula el Índice de Masa Corporal (IMC) y devuelve el valor junto con su categoría.
    
    Parámetros:
    peso (float): Peso en kilogramos.
    altura (float): Altura en metros.
    
    Retorna:
    tuple: Contiene el valor del IMC y su categoría.
    """
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        categoria = "peso bajo"
    elif 18.5 <= imc <= 24.99:
        categoria = "peso normal"
    elif 25 <= imc <= 29.99:
        categoria = "sobrepeso"
    elif 30 <= imc <= 34.99:
        categoria = "obesidad leve"
    elif 35 <= imc <= 39.99:
        categoria = "obesidad media"
    else:
        categoria = "obesidad mórbida"
    
    return imc, categoria

# Ejemplo de uso
peso = 75  # en kilogramos
altura = 1.68  # en metros

imc, categoria = calcular_imc(peso, altura)
print(f"El IMC es: {imc:.2f}")
print(f"Categoría: {categoria}")