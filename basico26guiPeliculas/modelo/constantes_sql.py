SQL_INSERCION_PELICULA = "INSERT INTO `tabla_peliculas` (`id`, `titulo`, `anio`, `duracion`, `pais`, `reparto`, `genero`, `sinopsis`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s);"
SQL_SELECT_PELICULAS = "SELECT * FROM tabla_peliculas"
SQL_BORRAR_PELICULA = "DELETE FROM tabla_peliculas WHERE id = %s;"
SQL_OBTENER_PELICULA_POR_ID = "SELECT * FROM tabla_peliculas WHERE id = %s;"
SQL_GUARDAR_CAMBIOS_PELICULA = "UPDATE tabla_peliculas SET  titulo = %s, anio = %s, duracion = %s, pais = %s, reparto = %s, genero = %s, sinopsis = %s WHERE id = %s "
