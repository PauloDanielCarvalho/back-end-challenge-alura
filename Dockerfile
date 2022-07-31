FROM python:3.10.5
WORKDIR /desafio_alura

COPY . /desafio_alura

RUN pip install -r /desafio_alura/requirements.txt

