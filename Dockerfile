FROM python:3.10
WORKDIR /calcifer
COPY requirements.txt /calcifer/
RUN pip install -r requirements.txt
COPY . /calcifer
CMD python main.py