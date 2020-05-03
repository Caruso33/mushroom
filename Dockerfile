FROM python:3.7-slim-stretch

RUN apt update
RUN apt install -y python3-dev gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install fastai

RUN pip3 install starlette uvicorn python-multipart aiohttp

ADD data/export.pkl export.pkl

COPY production production/

# Run it once to trigger resnet download
RUN python production/server.py

EXPOSE 8008

# Start the server
CMD ["python", "production.py", "serve"]