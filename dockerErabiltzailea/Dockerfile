# Imagen base
FROM ubuntu

#actualizar
RUN apt -qq update

#Descargar el enviroment
RUN apt install python3-pip -y
RUN apt install virtualenv -y

#crer el venv
RUN virtualenv /venv

#instalar las dependencias
RUN python3 -m pip install --default-timeout=100 nats-py


COPY main.py main.py
CMD ["/usr/bin/python3", "main.py"]


