FROM tiangolo/uwsgi-nginx-flask:python3.6
WORKDIR /usr/src/app
RUN apt-get update
RUN apt-get install --reinstall ca-certificates -y
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN export LDFLAGS="-L/usr/local/opt/openssl/lib"
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app/
