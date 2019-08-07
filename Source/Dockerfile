FROM python:3.6

ARG DJANGO_ENV
USER root

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN chmod 755 -R  /code

ADD requirements/base.txt /code/
ADD requirements/$DJANGO_ENV.txt /code/
RUN pip install -r $DJANGO_ENV.txt
ADD . /code/


# ARG DJANGO_ENV
# ARG ENV_WEBAPP_DIR

# USER root

# ENV WEBAPP_DIR=/code
# RUN mkdir $WEBAPP_DIR
# RUN chmod 755 -R $WEBAPP_DIR

# WORKDIR $WEBAPP_DIR

# ADD requirements/base.txt $WEBAPP_DIR/
# ADD requirements/$DJANGO_ENV.txt $WEBAPP_DIR/
# COPY start.sh $WEBAPP_DIR/

# RUN pip install -r $DJANGO_ENV.txt

# #Mapeo del proyecto
# ADD . $WEBAPP_DIR/