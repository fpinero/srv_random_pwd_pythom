# srv_random_pwd_python
servicio REST hecho en Python que devuelve una contraseña aleatoria de 16 caracteres

* Dockerfile
```
# Imagen base
FROM python:3.9-slim-buster

# Creación de un usuario no-root
RUN adduser --disabled-password --gecos '' appuser

# Directorio de trabajo
WORKDIR /app

# Copia de los archivos requeridos
COPY secure_password.py requirements.txt ./

# Instalación de las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Configuración de logging
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    LOG_LEVEL=INFO

# Ejecución del servidor
CMD ["python", "secure_password.py"]
```
```
docker build -t fpinero/secure-password-generator:0.0.1 .
```

* Si lo quieres probar en local:
````
docker run -d -p 5000:5000 secure-password-generator
````
y ve a la url http://127.0.0.1:5000/password

* Desplegar la aplicación en el k3s

`````
cd k8s
`````

* crear el namespace
````
kubectl create namespace python-generate-pwd
````
* desplegar la aplicación

````
kubectl apply -f app-deployment.yaml -n python-generate-pwd
````

* desplegar el servicio

````
kubectl apply -f app-service.yaml -n python-generate-pwd
````

* desplegar el ingress

`````
kubectl apply -f app-ingress.yaml -n python-generate-pwd
`````

* test de la aplicación

````
curl "http://orck3s.n0-reply.com/password"
````
