# 📝 Django REST Framework Todo API 프로젝트

간단한 Todo API를 구현한 Django REST Framework(DRF) 기반의 학습용 프로젝트입니다. 이 프로젝트는 API 설계, 직렬화, 뷰셋, 라우팅 등 DRF의 기본 개념을 실습하는 데 초점을 맞춥니다.

---

## 📚 추천 학습 자료

[![코담 - 코드에 세상을 담다](https://codam.kr/assets/images/og-image.jpg)](https://codam.kr/)

> **코담 - 파이썬, 장고, 프론트엔드 학습에 강력 추천!**

---


## 🔖프로젝트 구조
```bash
todoList_DRF/
├── config/                 # 프로젝트 설정 디렉토리
├── templates/              # HTML 템플릿 디렉토리
├── todo/                   # 앱 디렉토리
│   ├── __pycache__/        # 파이썬 캐시 파일
│   ├── migrations/         # 마이그레이션 파일
│   ├── __init__.py         # 패키지 초기화 파일
│   ├── admin.py            # 관리자(admin) 설정
│   ├── apps.py             # 앱 설정 파일
│   ├── models.py           # 모델 정의
│   ├── serializers.py      # DRF용 Serializer 정의
│   ├── tests.py            # 테스트 코드
│   ├── urls.py             # URL 라우팅 설정
│   ├── views.py            # 뷰(View) 정의
├── .gitignore              # Git 무시 파일 목록
├── db.sqlite3              # SQLite 데이터베이스 파일
├── manage.py               # Django 프로젝트 관리 명령어 실행 파일
└── README.md               # 프로젝트 설명 문서

```




## ⚙️ 개발 환경

* Python 3.12.3
* Django 5.2.1
* Django REST Framework
* 가상환경: `venv` 사용

---

## ⭕ 프로젝트 생성
### 1.시작하기
```bash
mkdir todoList_DRF  #루트 폴더 따로, 설정 폴더 따로
cd todoList_DRF    
django-admin startproject config .   # 현재 디렉토리에 장고 프로젝트 시작하기
python manage.py startapp todo   # todo 앱 생성
```

### 2.앱 등록 (settings.py 수정)
```python
INSTALLED_APPS = [
    ...
    'todo',
    'rest_framework',  # DRF 사용 시
]
```
### 3. 마이그레이션 적용  && superuser 생성 && 개발 서버 실행
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 4.추가적으로 할 것
1. todo/admin.py에서 모델 Todo 등록
2. todo/models.py에 모델 정의
3. urls.py를 todo/urls.py, config/urls.py로 나누고 include 설정


---


## ▶️ 실행 방법

1. 가상환경 활성화

```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

2. 패키지 설치

```bash
pip install -r requirements.txt

# Windows PowerShell 전용:
$env:PYTHONUTF8=1; pip install -r requirements.txt
```

3. 서버 실행

```bash
python manage.py runserver
```

---

## 📆 데이터베이스 마이그레이션

```bash
# 모델 변경 사항 생성
python manage.py makemigrations

# 실제 DB에 반영
python manage.py migrate

# 반영 내역 확인
python manage.py showmigrations
```

> 새 앱 생성 시:

```bash
python manage.py startapp api
```

---




## 🧹 마이그레이션 초기화 (선택적)

```bash
rm -f db.sqlite3
rm -r api/migrations
python manage.py makemigrations api
python manage.py migrate
python manage.py createsuperuser
```

---

## ✅ Django 모델 시각화

### 1. 패키지 설치

```bash
pip install django-extensions pydot
```

### 2. `settings.py` 설정

```python
INSTALLED_APPS = [
    ...
    'todo',
    'rest_framework',  # DRF 사용 시
]
```

### 3. `.dot` 파일 생성

```bash
python manage.py graph_models api > models.dot
```

> `api`는 시각화할 앱 이름입니다.

### 4. Graphviz 설치

* 다운로드: [https://graphviz.org/download/](https://graphviz.org/download/)
* 설치 후 `dot` 명령어가 터미널에서 인식되어야 함

### 5. `.dot` 파일을 이미지로 변환

```bash
dot -Tpng models.dot -o models.png
```

> 생성된 `models.png`로 모델 관계를 시각적으로 확인할 수 있습니다.

### 🔍 온라인 시각화 도구

* [Graphviz Visual Editor](https://edotor.net/)
* [Viz.js Online](https://dreampuf.github.io/GraphvizOnline/?engine=dot)

---

## 📦 Commit 메시지 컨벤션 (Conventional Commits)

명확하고 일관된 Git 기록 작성을 위해 [Conventional Commits](https://www.conventionalcommits.org/) 형식을 따릅니다.

### 📌 타입 예시

| 타입         | 설명                |
| ---------- | ----------------- |
| `feat`     | 새로운 기능 추가         |
| `fix`      | 버그 수정             |
| `docs`     | 문서 수정 (README 등)  |
| `style`    | 코드 포맷팅 (기능 변화 없음) |
| `refactor` | 리팩토링 (기능 변화 없음)   |
| `test`     | 테스트 코드 추가/수정      |
| `chore`    | 기타 설정 변경 등        |

### 💡 예시 커밋

```bash
git commit -m "feat: Todo 목록 조회 API 구현"
git commit -m "fix: 날짜 형식 오류 수정"
git commit -m "docs: README 업데이트"
git commit -m "style: 불필요한 공백 제거"
git commit -m "refactor: view 함수 분리"
git commit -m "test: Todo 생성 테스트 추가"
git commit -m "chore: requirements.txt 정리"
```

---

## 🔑 관리자 계정 생성

```bash
python manage.py createsuperuser
```

---


##### 배포
```bash
curl -L https://fly.io/install.sh | sh

```


##### Fly 배포용 ALLOWED_HOSTS 설정
```bash
APP_NAME = os.environ.get("FLY_APP_NAME")
ALLOWED_HOSTS = [f"{APP_NAME}.fly.dev", "localhost", "127.0.0.1"]
```

✅  flyctl 명령어 사용 팁
```bash
로그인: flyctl auth login
새 프로젝트 시작: flyctl launch
앱 배포: flyctl deploy
상태 확인: flyctl status
```


## 👨‍💻 Author

**코담(Codam)**
👩‍🏫 이유정
👉 [https://codam.kr](https://codam.kr)
