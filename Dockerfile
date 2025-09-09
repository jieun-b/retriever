# 베이스 이미지 (Python 3.10 slim)
FROM python:3.10-slim

# 컨테이너 내 작업 디렉토리
WORKDIR /app

# 시스템 패키지 설치 (예: opencv, numpy 등에 필요한 라이브러리)
RUN apt-get update && apt-get install -y \
    libgl1 libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# requirements.txt 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# 기본 포트 (Streamlit: 8501, FastAPI: 8000)
EXPOSE 8501
EXPOSE 8000

# 멀티 서비스 실행 (Streamlit + FastAPI)
CMD ["bash", "-c", "uvicorn api.main:app --host 0.0.0.0 --port 8000 & streamlit run streamlit_app.py --server.port=8501 --server.address=0.0.0.0"]