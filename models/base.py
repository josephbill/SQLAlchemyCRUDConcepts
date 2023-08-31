# this file will contain a dec. of declaritive_base function :(creation of the base class called Base)
# parent class for the object relational mapping 
# purpose is to provide a common set of functionalities and attributes to be shared amongst the ORM model classes.
# They Inherit 
#  mapping of db columns to class attributes , creation of db tables and handling sessions. 
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()