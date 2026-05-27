import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class Conexion:
    __DATABASE = os.getenv("DATABASE", "mi_db")
    __USERNAME = os.getenv("USERNAME", "postgres")
    __PASSWORD = os.getenv("PASSWORD", "")
    __DB_PORT  = os.getenv("DB_PORT", "5432")
    __HOST     = os.getenv("HOST", "localhost")

    __conexion = None
    __cursor   = None

    @classmethod
    def obtenerConexion(cls):
        if cls.__conexion is None:
            cls.__conexion = psycopg2.connect(
                database = cls.__DATABASE,
                user     = cls.__USERNAME,
                password = cls.__PASSWORD,
                host     = cls.__HOST,
                port     = cls.__DB_PORT,
            )
        return cls.__conexion

    @classmethod
    def obtenerCursor(cls):
        if cls.__cursor is None:
            cls.__cursor = cls.obtenerConexion().cursor()
        return cls.__cursor

    @classmethod
    def cerrar(cls):
        if cls.__cursor is not None:
            cls.__cursor.close()
            cls.__cursor = None
        if cls.__conexion is not None:
            cls.__conexion.close()
            cls.__conexion = None