FROM python:3.11.4-slim

ENV PYTHONNDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

#RUN apt-get update && apt-get install -y netcat
RUN apt-get update

RUN pip install --upgrade pip

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

COPY . .

#CMD [ "flask", "--app", "project", "run", "--host=0.0.0.0" ]