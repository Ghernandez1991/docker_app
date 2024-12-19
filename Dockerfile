FROM python:3.12.0-slim-bullseye

# docker build -t my_image .
# docker run -d -p 8080:8080 my_image
#install only requirements.txt so we can cache this layer
WORKDIR /temp/requirements_temp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


WORKDIR /app
#copy source code to app
COPY . /app
#can only use this locally- heroku does not support docker EXPOSE command
# EXPOSE 8080


ENTRYPOINT ["python"]

CMD ["app.py"]
