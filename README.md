MYSQL 시스템 변수 모니터링
===================================

진행사항
---------------------------
1. 진행사항
~~~
[x] system variables 리스트와 검색기능
[x] ajax를 이용한 페이지 새로고침 없이 1분마다 데이터 동기화
[x] system variables log 저장
~~~
프로그램 설명
---------------------------
1. 서비스 구조
~~~
    - Page
        - index페이지 : / : 시스템 변수 모니터링 페이지
    - Api
        - get_show_variable : /get_show_variable : 시스템 변수 모니터링 api
        - get_time : /get_time : 현재 서버 시간 api
~~~
프로그램 설치를 위한 세팅
---------------------------
1. 파이썬 3.8 설치
2. 가상환경 생성
~~~
    - 아래 셋 중에 하나 실행 시켜 가상환경 생성
        1) python -m venv venv
        2) python3.8 -m venv venv
        3) python3 -m venv venv
    - 가상환경 접속
        1) ubuntu / mac : source ./venv/bin/activate 실행
        2) window : \venv\Scripts 아래 activate.bat 실행
    - pip install -r requirements.txt
~~~
3. 장고 세팅 & 실행
~~~
    - 프로젝트 conf.json 아래와 같이 수정하고 저장하기
        {
                "ENGINE": "django.db.backends.mysql",
                "NAME": "사용할 데이터베이스",
                "USER": "사용할 유저",
                "PASSWORD": "유저 비밀번호",
                "HOST": "localhost",
                "PORT": "3306"
        }
    - conf.json 저장 후 장고 마이그레이트 실행 :  python manage.py migrate 
~~~
4. localhost:8000 주소로 접속
~~~
    - 실행 : python manage.py runserver 8000 
	- ex) http://localhost:8000
~~~