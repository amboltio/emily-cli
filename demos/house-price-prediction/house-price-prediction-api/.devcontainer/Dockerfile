
FROM ambolt/emily:1.0.0-slim

COPY requirements.txt /workspace/requirements.txt
WORKDIR /workspace
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /workspace
