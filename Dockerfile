FROM python:3.12.7-slim-bookworm AS backend-build

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    build-essential \
    gcc \
    g++ \
    openjdk-17-jdk \
    && rm -rf /var/lib/apt/lists/*

ENV CFLAGS="-std=c++11"
ENV CXXFLAGS="-std=c++11"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-6.2.1.4610-linux-x64.zip \
    && unzip sonar-scanner-cli-6.2.1.4610-linux-x64.zip \
    && mv sonar-scanner-6.2.1.4610-linux-x64 /opt/sonar-scanner \
    && rm sonar-scanner-cli-6.2.1.4610-linux-x64.zip
ENV PATH=$PATH:/opt/sonar-scanner/bin

COPY . .


EXPOSE 60000

# Start the FastAPI app
CMD uvicorn app:app --host 0.0.0.0 --port 60000
