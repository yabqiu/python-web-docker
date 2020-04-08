FROM python:3.7-alpine
ADD app.py requirements.txt ./
RUN pip install -r requirements.txt
ENV HTTP_PORT 80
CMD ["python", "app.py"]
