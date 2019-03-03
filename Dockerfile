FROM python:3


ADD . /root/dalcoder

RUN pip install flask

EXPOSE 5000

CMD [ "python", "/root/dalcoder/dalapi.py" ]
