FROM python:3.12.0-slim-bullseye

# docker build -t my_image .
# docker run -d -p 8080:8080 my_image
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080


ENTRYPOINT ["python"]

CMD ["app.py"]