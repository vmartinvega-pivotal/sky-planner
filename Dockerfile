FROM arm32v7/python:3.7.10-buster

RUN pip install beautifulsoup4
RUN pip install requests

COPY script.py /script.py
COPY sshelper.py /sshelper.py

CMD ["python", "/script.py"]


