# Imagen base
FROM ubuntu

#Actualizar
RUN apt -qq update

#Descargar el enviroment
RUN apt install python3-pip -y
RUN apt install virtualenv -y

#crer el venv
RUN virtualenv /venv

#instalar las dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

#Runear la app
COPY main.py .
CMD ["python", "main.py"]
