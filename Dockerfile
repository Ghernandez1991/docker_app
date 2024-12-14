FROM python:3.12.0-slim-bullseye

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080


ENTRYPOINT ["python"]

CMD ["app.py"]