FROM python:alpine 
RUN pip install flask
COPY src /src/
EXPOSE 5000
ENTRYPOINT ["python", "/src/main.py"]
