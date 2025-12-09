FROM python:latest
RUN mkdir /app
WORKDIR /app
RUN pip install fastapi uvicorn
COPY main.py /app/main.py
CMD ["uvicorn", "main:app", "--reload"]