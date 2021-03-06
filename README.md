MYSQL 시스템 변수 모니터링
===================================

진행사항
---------------------------
1. Todo
~~~
    - [x] system variables 리스트와 검색기능
    - [x] ajax를 이용한 페이지 새로고침 없이 1분마다 데이터 동기화
    - [x] system variables log 저장
~~~
프로그램 설명
---------------------------
1. 구조 : page 에서 system variables를 보여주는 프로그램
~~~
    - Page
        - index페이지 : / : 시스템 변수 모니터링 페이지
    - Api
        - get_show_variable : /get_show_variable : 시스템 변수 모니터링 api
        - get_time : /get_time : 현재 서버 시간 api
~~~
프로그램 세팅
---------------------------
1. Mysql서버 5.7, 파이썬 3.8 설치 후 Github repo clone
~~~
    - git clone https://github.com/bjm1244/db_monitoring.git
~~~
2. 프로젝트에 들어간 후 가상환경 생성
~~~
    - 가상환경 생성
        1) python3.8 -m venv venv
    - 가상환경 접속
        1) ubuntu / mac : source ./venv/bin/activate 실행
        2) window : \venv\Scripts 아래 activate.bat 실행
    - pip update 후에 requirements에 있는 디펜던시 설치
        1) pip install -r requirements.txt
            - 파이썬이 3.8 아래 버젼이면 django 에러가 나옴. 버젼 확인 필요함.
            - mysql 없을 시에 mysql-client 디펜던시 설치가 에러 나오기에 디펜던시 설치 전에 mysql 설치 필요함.
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
	- 주소 접속 : http://localhost:8000
~~~