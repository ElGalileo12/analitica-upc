# analitica-upc

Código para el proyecto de grado

Instalar paquetes

- python -m pip install -r src/requirements.txt

Entorno virtual

- pip install virtualenv
- virtualenv -p python3 venv
- pip install Django==4.2.4
- pip install psycopg2-binary
- .\venv\Scripts\activate

Servidor

- python manage.py collectstatic

- cd src/Project

  - py .\manage.py runserver

- py .\manage.py migrate
- py .\manage.py makemigrations
