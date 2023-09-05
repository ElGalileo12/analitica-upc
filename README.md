# analitica-upc

Código para el proyecto de grado

Abrir la carpeta analitica de datos en Visual
Esto se hace solo una vez

Instalar el entorno virtual
- py -m pip install virtualenv
- py -m virtualenv -p python3 venv

Activar el entorno virtual
- .\venv\Scripts\activate

Instalar paquetes
- py -m pip install -r src/requirements.txt
- python manage.py collectstatic -- esto solo se hace una vez

Base de datos
Para configurar la base de datos llenar los campos con sus datos
IMPORTANTE TENER SOLAMENTE POSGREST 15.4
   - 'ENGINE': 'django.db.backends.postgresql_psycopg2'
   - 'NAME': 'ADI' <-- nombre de la base de datos
   - 'USER':'postgres'
   - 'PASSWORD': 'root' <--- contraseña que pusieron lo mas probable 123a456c o root en mi caso
   - 'HOST': '127.0.0.1'
   - 'DATABASE_PORT': '5432' <----- puerto que usaron


Servidor
-El servidor se lanza desde la carpeta Project
- cd src/Project
  - py .\manage.py migrate
  - py .\manage.py makemigrations
  - py .\manage.py runserver


