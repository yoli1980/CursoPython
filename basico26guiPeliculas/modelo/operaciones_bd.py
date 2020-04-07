

import mysql.connector
from modelo import constantes_sql

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
    valores_a_insertar = (pelicula.titulo, pelicula.anio, pelicula.duracion, pelicula.pais, pelicula.reparto, pelicula.genero, pelicula.sinopsis)
    cursor.execute(sql, valores_a_insertar)
    conexion.commit()
    conexion.disconnect()
    
def obtener_peliculas():
    sql = constantes_sql.SQL_SELECT_PELICULAS
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(sql)
    lista_resultado = cursor.fetchall()
    conexion.disconnect()
    return lista_resultado