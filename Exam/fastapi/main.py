# main.py

import os
from typing import Optional
from routes.test import router as test_router
from fastapi import FastAPI # FastAPI 모듈 가져오기

app = FastAPI() # 객체 생성

@app.get("/") # Route Path
def test_index():
	
    # Json 타입으로 값 반환
    return {
	    "Python": "Framework",
	}
    
@app.get("/something")
def something():
    return {
        "Something": "Page",
    }
    
#uvicorn main:app --reload --port 8000
#uvicorn을 통해 실행시킨다

#만약 cake.py, FastAPI() 모듈이 할당된 객체명이 serum 일 경우
#unicorn cake:serum --reload

#관리 페이지 http://localhost:8000/docs, redoc