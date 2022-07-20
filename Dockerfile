FROM python:3

RUN apt-get update && \
    apt-get -y install mingw-w64 && \
    apt-get -y autoremove && \
    apt-get -y clean

WORKDIR /dllgenerator

ENTRYPOINT ["python3", "generator.py"]
