
#persistencia es manejar la bd desde el front
# ORM es el lenguaje para conectar con l bd

#datos para la conexion a BD

from sqlalchemy import create_engine,event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine


dataBaseName="gestordb"
userName="root"
userPassword=""
connectionPort=3306
server="localhost"

#creando la conexion
dataBaseConnection=f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{connectionPort}/{dataBaseName}"

# creanddo el motor de coneccion
engine = create_engine(dataBaseConnection)

#abrir la sesion con la bd

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

