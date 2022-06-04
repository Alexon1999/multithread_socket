FROM python:latest
WORKDIR /app
COPY multithreadserver.py ./
COPY utils.py ./
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./multithreadserver.py"]
EXPOSE 8000