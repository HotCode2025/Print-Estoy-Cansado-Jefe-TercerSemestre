@startuml

package catalogo_peliculas {

    package dominio {
        class Pelicula {
            - nombre : str
            + __str__() : str

            --
            Representa un objeto película
        }
    }

    package servicio {
        class CatalogoPeliculas {
            + ruta_archivo : str <<static>>

            + agregar_pelicula(pelicula : Pelicula) <<static>>
            + listar_peliculas() <<static>>
            + eliminar() <<static>>

            --
            Realiza las operaciones sobre el archivo de peliculas.txt
        }
    }

    Pelicula "1" --> "0..*" CatalogoPeliculas : agrega
}

class test_catalogo_peliculas.py {
    --
    Responsabilidades:
    - Contiene un menú con 4 opciones:
    1) Agregar película
    2) Listar películas
    3) Eliminar archivo de películas
    4) Salir
}

@enduml

#Para poder verlo entrar en: https://planttext.com/ y pegar el codigo de arriba