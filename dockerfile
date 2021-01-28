FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip3 install -r /app/requirements.txt
EXPOSE 8080
CMD [ "python3" , "advice.py" ]