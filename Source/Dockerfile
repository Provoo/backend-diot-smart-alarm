#Imagen pthon de docker hub
FROM python:3.6 

#Se agregan las variables de entorno
ARG DJANGO_ENV
USER root

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

# Se deifine un directorio de instalación
WORKDIR /code
# Se da los permisos necesarios 
RUN chmod 755 -R  /code

#Se agrega las dependencias
ADD requirements/base.txt /code/
ADD requirements/$DJANGO_ENV.txt /code/

#Instalación de dependencias python
RUN pip install -r $DJANGO_ENV.txt

#Se agrega el código fuente al directorio code 
ADD . /code/
