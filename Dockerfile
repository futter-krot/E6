FROM python:3.8
WORKDIR /app
COPY requirements.txt /app
COPY ./app /app
RUN pip install -r requirements.txt
ENTRYPOINT ["flask"]
CMD ["run"]