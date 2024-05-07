FROM python:3.9-slim-bullseye

RUN pip install mysql-connector-python
RUN pip install requests
RUN pip install pandas

COPY ./app /app

WORKDIR /app

CMD [ "python", "crawltomysql.py",  "--host", "0.0.0.0", "--port", "3000" ]
