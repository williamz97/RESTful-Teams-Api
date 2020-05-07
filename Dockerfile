FROM python:3.6
MAINTAINER Weili Zhong "wz16874n@pace.edu"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]