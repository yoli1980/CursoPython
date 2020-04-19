import re
expresion_texto = "^[a-zA-ZáéíóúÁÉÍÓÚñÑäëïöüÄËÏÖÜ@().,;:_\- 0-9]{2,8000}$"
expresion_anio = "^[0-9]{4}$"
expresion_duracion = "^[0-9]{2,3}$"
expresion_pais = "^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]{2,50}$"


def validar_texto(texto):
    validador = re.compile(expresion_texto)
    return validador.match(texto)

def validar_anio(anio):
    validador = re.compile(expresion_anio)
    return validador.match(anio)

def validar_duracion(duracion):
    validador = re.compile(expresion_duracion)
    return validador.match(duracion)

def validar_pais(pais):
    validador = re.compile(expresion_pais)
    return validador.match(pais)
