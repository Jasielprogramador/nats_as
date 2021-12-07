
# Trabajo individual de Administración de Sistemas

## Autor: Asier Rosa Pacho

###Dependencias:
1. Se necesita que este [Docker](https://docs.docker.com/get-docker/) instalado
2. Se necesita que este [Kubernetes](https://kubernetes.io/es/docs/tasks/tools/install-kubectl/) instalado

Para poder ejecutar localmente la aplicación de nats sigue los siguientes pasos:

1. `git clone https://github.com/Jasielprogramador/nats_as.git`
2. `cd dockerErabiltzailea`
3. `sudo docker-compose up`
4. En otra terminal ejecuta el siguiente comando: `sudo docker exec -it app-nats /bin/bash`
5. `python3 main.py`

