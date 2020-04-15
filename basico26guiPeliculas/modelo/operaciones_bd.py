

import mysql.connector
from modelo import constantes_sql, clases

def conectar():
    conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            database = "bd_peliculas"        
        )
    return conexion

def registro_pelicula(pelicula):
    sql = constantes_sql.SQL_INSERCION_PELICULA
    conexion = conectar()
    cursor = conexion.cursor()
    valores_a_insertar = (pelicula.titulo, pelicula.anio, pelicula.duracion, pelicula.pais, pelicula.reparto, pelicula.genero, pelicula.sinopsis, pelicula.formato, pelicula.valoracion, pelicula.vista)
    cursor.execute(sql, valores_a_insertar)
    conexion.commit()
    id_generado = cursor.lastrowid
    conexion.disconnect()
    return id_generado
    
def obtener_peliculas():
    sql = constantes_sql.SQL_SELECT_PELICULAS
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(sql)
    lista_resultado = cursor.fetchall()
    conexion.disconnect()
    return lista_resultado

def borrar_pelicula(id_pelicula):
    sql = constantes_sql.SQL_BORRAR_PELICULA
    conexion = conectar()
    cursor = conexion.cursor()
    valores_a_borrar = (id_pelicula,)
    cursor.execute(sql,valores_a_borrar)
    conexion.commit()
    conexion.disconnect()
    
def obtener_pelicula_por_id(id_pelicula):
    sql = constantes_sql.SQL_OBTENER_PELICULA_POR_ID
    conexion = conectar()
    cursor = conexion.cursor()
    valores_a_editar = (id_pelicula,)
    cursor.execute(sql,valores_a_editar)
    pelicula_obtenida = cursor.fetchone()
    print(pelicula_obtenida)
    conexion.disconnect()
    objeto_pelicula = clases.Pelicula(id = pelicula_obtenida[0], titulo = pelicula_obtenida[1], anio = pelicula_obtenida[2], duracion = pelicula_obtenida[3], pais = pelicula_obtenida[4], reparto = pelicula_obtenida[5], genero = pelicula_obtenida[6], sinopsis = pelicula_obtenida[7], formato = pelicula_obtenida[8], valoracion = pelicula_obtenida[9], vista = pelicula_obtenida[10])
    return objeto_pelicula
    
def guardar_cambios_pelicula(pelicula):
    sql = constantes_sql.SQL_GUARDAR_CAMBIOS_PELICULA
    conexion = conectar()
    cursor = conexion.cursor()
    valores_a_guardar = (pelicula.titulo, pelicula.anio, pelicula.duracion, pelicula.pais, pelicula.reparto, pelicula.genero, pelicula.sinopsis, pelicula.formato, pelicula.valoracion, pelicula.vista, pelicula.id)
    cursor.execute(sql,valores_a_guardar)
    conexion.commit()
    conexion.disconnect()
        
    
    

