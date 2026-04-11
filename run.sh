#!/usr/bin/env bash

# 1. 마스터 디렉터리에 venv 폴더가 없으면 최초 1회 생성
if [ ! -f "venv/bin/activate" ]; then
    echo "[System] venv 폴더가 없습니다. 가상환경을 최초 1회 생성합니다..."
    if command -v python3 &>/dev/null; then
        python3 -m venv venv
    else
        python -m venv venv
    fi
fi

# 2. 무조건 venv 활성화
echo "[System] 가상환경(venv)을 활성화합니다..."
source venv/bin/activate

# 3. 패키지 설치 및 서버 실행
echo "[System] 패키지 상태를 확인하고 서버를 켭니다..."
pip install -r requirements.txt
uvicorn main:app --reload