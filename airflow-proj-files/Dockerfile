FROM python:3.7-slim-buster

RUN apt-get update -yqq \
    	&& apt-get upgrade -yqq \
    	&& apt-get install -yqq --no-install-recommends \
	apt-utils \
	build-essential \
	libffi-dev \
	libpq-dev \
	libssl-dev \
	python3-pandas \
	python3-numpy

ENV PYTHONPATH="${PYTHONPATH}:/usr/lib/python3/dist-packages"

RUN pip install -U pip setuptools wheel \
	&& pip install pyOpenSSL \
    	&& pip install apache-airflow \
		 --use-feature=2020-resolver

COPY ./entrypoint.sh /entrypoint.sh

EXPOSE 8080

ENV AIRFLOW_HOME=/app/airflow
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
ENV AIRFLOW__CORE__LOAD_DEFAULT_CONNECTIONS=False
ENV AIRFLOW__CORE__FERNET_KEY=0897eeabe6de2d4ec89c5f331057b9028f35f47bfd33cff0e36ff51e861c2de4
ENV AIRFLOW__WEBSERVER__EXPOSE_CONFIG=True

ENTRYPOINT [ "/entrypoint.sh" ]
