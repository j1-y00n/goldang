
# 🥭 망고플레이트 🥭

> 맛집 정보 및 후기 공유 사이트 클론코딩

<img width="1430" alt="스크린샷 2023-05-07 오후 11 07 31" src="https://github.com/user-attachments/assets/3115610f-40a5-46fe-80aa-bb6530d71677">

## 📖 Description

- 진행기간 : 2023.04.26 ~ 2023.05.08
- 팀 구성 : 프론트엔드 2명, 백엔드 1명, 서버 1명

## 👨‍💻 Role & Contribution

**Frontend (Web)**

- figma를 활용한 구조도 작업
- index page, profile page, login/sign up page 작업
- 식당 평점에 따른 색상 변경
- 메인화면의 카테고리별 필터 적용하여 반영
- 가고싶다(좋아요 누른 식당)기능 구현, 가고싶다에 추가한 식당 모아보기

## 💻 Getting Started

### Installation
가상환경 생성
```python
  python -m venv venv
```
가상환경 활성화
```python
  source venv/bin/activate
```
django 설치
```python
  pip install django==3.2.18
```
gitclone  
의존성 파일 설치
```python
  pip install -r requirements.txt
```
### Develop Mode
서버실행
```python
  python manage.py runserver
```

## 🔧 Stack
- **Language**: Python, JavaScript
- **Library & Framework** : Django, Bootstrap
- **Database** : SQLite3
- **Deploy**: aws

## :open_file_folder: Project Structure

```markdown
project
├── accounts
│   ├── templats
│   │   ├── accounts
│   │   └── socialaccount
│   └── static
│       └── accounts
├── config
├── media
│   ├── posts
│   ├── profile
│   └── reviews
│       └── images
├── plates
│   ├── static
│   │   └── plates
│   ├── templates/plates
│   └── templatetags
├── static
└── templates
```
