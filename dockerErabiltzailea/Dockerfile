# Imagen base
FROM ubuntu

#Actualizar ubuntu
RUN apt -qq update

#Crear enviroment
RUN apt install python3-pip -y

#ejecutar main
COPY main.py /programa/main.py
COPY requirements.txt /programa/requirements.py
WORKDIR /programa

#Actualizar pip
RUN pip install --upgrade pip

#Instalar las dependencias
RUN python3 -m pip install --default-timeout=100 -r requirements.txt

CMD ["python3", "main.py"]

