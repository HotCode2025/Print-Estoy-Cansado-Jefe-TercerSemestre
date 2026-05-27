class Persona:
    def __init__(self, id_persona: int = None, nombre: str = "",
                 apellido: str = "", email: str = ""):
        self.__id_persona = id_persona
        self.__nombre     = nombre
        self.__apellido   = apellido
        self.__email      = email
 
    # Getters 
    def get_id_persona(self) -> int:
        return self.__id_persona
 
    def get_nombre(self) -> str:
        return self.__nombre
 
    def get_apellido(self) -> str:
        return self.__apellido
 
    def get_email(self) -> str:
        return self.__email
 
    # Setters 
    def set_id_persona(self, id_persona: int) -> None:
        self.__id_persona = id_persona
 
    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre
 
    def set_apellido(self, apellido: str) -> None:
        self.__apellido = apellido
 
    def set_email(self, email: str) -> None:
        self.__email = email
 
    # Representación 
    def __str__(self) -> str:
        return (f"Persona(id={self.__id_persona}, "
                f"nombre='{self.__nombre}', "
                f"apellido='{self.__apellido}', "
                f"email='{self.__email}')")
    