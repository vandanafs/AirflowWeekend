## Using Docker to handle Airflow

for running
```
docker run --name airflow -p 8080:8080 -d airflow:0.1.0
```

for building
```
time docker build --tag airflow:0.1.0 .
```

This is SOOO much better than trying to onstall it on your machine. Use Docker to handle all the isolation aspects of running airflow.

