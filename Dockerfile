# Dockerfile

# Sử dụng base image của NVIDIA với CUDA 12.4 và Ubuntu 22.04
FROM nvidia/cuda:12.4.1-devel-ubuntu22.04

# Ngăn các câu lệnh tương tác trong quá trình build
ENV DEBIAN_FRONTEND=noninteractive

# Cài đặt các gói hệ thống cần thiết
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
    python3.12 \
    python3.12-venv \
    python3.12-dev \
    python3-pip \
    build-essential \
    ninja-build \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Gỡ bỏ pip hệ thống và cài lại pip cho python3.12
RUN apt-get remove -y python3-pip && \
    apt-get autoremove -y && \
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3.12 get-pip.py && \
    rm get-pip.py

# Đảm bảo các lệnh `python` và `pip` đều trỏ đến phiên bản 3.12
RUN ln -sf /usr/bin/python3.12 /usr/bin/python && \
    ln -sf /usr/local/bin/pip /usr/bin/pip

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép file requirements
COPY requirements_docker.txt .

# Cài đặt các thư viện Python, bao gồm llama-cpp-python từ GitHub
ENV CMAKE_ARGS="-DGGML_CUDA=on"
ENV FORCE_CMAKE=1
RUN pip install --no-cache-dir -r requirements_docker.txt

# Sao chép code dự án
COPY . .

# Lệnh mặc định
CMD ["bash"]