
FROM ambolt/emily:1.0.0-pytorch

COPY requirements.txt /workspace/requirements.txt
WORKDIR /workspace
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10
COPY . /workspace
