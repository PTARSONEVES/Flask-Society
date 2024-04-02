###########
# BUILDER #
###########

#pull official base image
FROM python:3.11.3-slim-buster as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc


# lint
RUN pip install --upgrade pip
RUN pip install flake8
COPY . /usr/src/app/
#RUN flake8 --ignore=E501,F401 .

# install python dependencies
#RUN --mount=type=cache,target=/root/.cache/pip \
#    --mount=type=bind,source=requirements.txt,target=requirements.txt \
#    python -m pip install -r requirements.txt

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

#pull official base image
FROM python:3.11.3-slim-buster

# create directory for the app user
RUN mkdir -p /home/app && mkdir -p /home/app/web && mkdir -p /run/secrets

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
WORKDIR $APP_HOME

# install dependencies
#RUN apt-get install -y --no-install-recommends netcat
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
#RUN apt-get update && apt-get install -y wkhtmltopdf xvfb
RUN apt-get update 
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy entrypoint-prod.sh
COPY ./entrypoint.sh $APP_HOME
COPY ./entrypoint.sh /usr/local/bin/


# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME
RUN chmod 755 entrypoint.sh

# change to the app user
 USER root

#RUN entrypoint.sh
#CMD [ "flask", "--app", "flaskr", "--host=0.0.0.0" ]
#ENTRYPOINT ["/home/app/web/entrypoint.sh"]
