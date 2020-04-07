
# el procedimiento con bases de datos es:
# 1. Conectar
# 2. Operar
# 3. Desconectar

import mysql.connector
from modelo import constantes_sql

def conectar():
    conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            database = "bd_libros"        
        )
    return conexion

def registro_libro(libro):
    sql = constantes_sql.SQL_INSERCION_LIBRO
    conexion = conectar()
    cursor = conexion.cursor()
    valores_a_insertar = (libro.titulo, libro.paginas, libro.precio)
    cursor.execute(sql, valores_a_insertar)
    conexion.commit()
    conexion.disconnect()
    
def obtener_libros():    
    sql = constantes_sql.SQL_SELECT_LIBROS
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(sql)
    lista_resultado = cursor.fetchall()
    conexion.disconnect()
    return lista_resultado
    
    
    
    
    
    
    
    
    
    
    
    