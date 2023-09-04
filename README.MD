### To fix module import error : configure your python interpreter 

cmd + shift + p on VS CODE 
type : python:interpreter
select the global selection 

or alternatively 
reload VS Code.

### Project 
CRUD operations and object relationships using SQLAlchemy. 


### Migrations Workflow 
= Create the migration 
= Apply Migration 
= Test and validate 
= Commit to version control 
= Update and Deployment 


### Steps to adding and using alembic 
1. SQLAlchemy : pip install sqlalchemy/ pip show / pip list 
2. Alembic : pip install alembic 
3. Create your database.py  config : in this reference process in main.py 
4. Initializing your alembic -> python -m alembic init alembic
5. In alembic.ini specify the db.url 
6. Commit the intial migration and apply the migration
python -m alembic upgrade head  : head refers to the latest revision
python -m alembic upgrade 04fd645e3db3

7. To make the update , create a new migration then use the add column command : 
python -m alemebic revision -m "add column  to authors" 


