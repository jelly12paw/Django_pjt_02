# 🎞 영화 리뷰 웹 구현하기
<br>

    Django로 CRUD 활용한 영화 리뷰 웹 사이트 구현하기    

<hr>

![w-bingbong](https://user-images.githubusercontent.com/107910587/194854302-e23905b3-21d4-49ec-b0b8-95bed1fb0fb9.gif) 　　![m-bingbong](https://user-images.githubusercontent.com/107910587/194718583-df06245d-1897-4abb-bcf8-341c59b69b1c.gif)
<br>

## 🧰 사용기술

<br>

<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=ffffff"/> 　<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=ffffff"/> 　<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=ffffff"/> 　<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=ffffff"/> 　<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=ffffff"/> 　<img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=ffffff"/>

<br>

<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=ffffff"/>　<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=ffffff"/>　<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=ffffff"/>

<br>

## 📅 프로젝트 기간

### 2022.10.07

<br>

## 👩🏻‍💻 역할

### Front-end & Back-end

<br>

<hr>

<br>

## ✨ 1. 목표 서비스
<br>

### 1.1 영화 리뷰 게시판

<br>

1. 영화 리뷰 게시글 생성, 삭제, 수정 기능
2. 평점 기능

<br>

## ✨ 2. 실제 구현 정도
<br>

### 2.1 영화 리뷰 게시판

<br>

1. 영화 리뷰 생성, 삭제, 수정 기능
2. 평점 기능
3. 반응형 구현

<br>

<hr>
<br>

## ✏ 3. 프로젝트 진행과정

<br>

### 3.1 가상환경 생성 및 장고 설치
<br>

```python
python -m venv venv
```

```bash
pip install django==3.2.13
```
<br>

### 3.2 프로젝트 생성
<br>

```bash
django-admin startproject movie .
```

<br>

### 3.3 앱 생성
<br>

```bash
python manage.py startapp reviews
```
<br>

### 3.4 모델 생성
<br>

```python
class Review(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    movie_name = models.CharField(max_length=30)
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img_url = models.TextField()
```

```bash
python manage.py makemigrations
python manage.py migrate
```
<br>

### 3.5 모델 폼 생성
<br>

```python
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'movie_name', 'grade', 'img_url']
```
<br>

### 3.6 영화 리뷰 게시글 CRUD
<br>

1. 글쓰기 버튼을 누르면 생성된 모델 폼 화면이 나와 사용자가 입력한 정보를 받아 데이터베이스에 저장하기
<br>

2. 상세보기 버튼을 누르면 사용자가 입력한 게시글을 보여주기
<br>

3. 수정하기 버튼을 누르면 사용자가 입력했던 정보를 받아와 보여주고 수정된 정보를 저장하기
<br>

4. 삭제 버튼을 누르면 사용자가 작성한 게시글을 삭제하기

<br>

## 🖥 4. 실제 구현 화면

<br>

### 4.1 영화 리뷰 메인 페이지

<br>

1. GIF 이미지 삽입, 글씨에 애니메이션 효과를 주어 메인페이지를 구성

2. 반응형 구현에 따라 모바일 크기와 웹 크기에서 각 화면에 맞는 폰트크기로 구현

3. 네비게이션 바에 영화로고 이미지, 목록에 list, add를 생성, 반응형 구현으로 모바일 크기일 때는 토글 버튼이 보여짐. 영화로고 이미지를 클릭하면 메인 페이지로 연결, list를 클릭하면 목록 페이지로 연결, add를 클릭하면 리뷰 작성 페이지로 연결됨 

<br>

#### 💻 웹 크기
![w-main](https://user-images.githubusercontent.com/107910587/194854261-83e7371e-0521-4b2e-b0a6-6712c6104997.gif)


<br>

#### 📱 모바일 크기

![m-main](https://user-images.githubusercontent.com/107910587/194718595-0d80c333-01ea-4980-b919-ac1b110d06e7.gif)

<br>

### 4.2 영화 리뷰 목록 페이지

<br>

1. 작성된 리뷰 게시글을 카드형태로 구현

2. 반응형 구현에 따라 모바일 크기와 웹 크기에서 나타나는 카드 표시 형태를 다르게 구현 
   <br> (웹 크기는 한 줄에 4개의 카드, 모바일 크기는 한 줄에 1개의 카드)

3. write 버튼을 클릭하면 리뷰 작성 페이지로 연결됨

<br>

#### 💻 웹 크기

![w-list](https://user-images.githubusercontent.com/107910587/194854276-a88a624c-90c3-4435-8310-0c6b8ce38e74.gif)


<br>

#### 📱 모바일 크기

![m-list](https://user-images.githubusercontent.com/107910587/194718603-710edc1d-9372-4d63-8a0a-2386fe49d694.gif)

<br>

### 4.3 영화 리뷰 상세 페이지

<br>

1. 입력받은 데이터를 이미지, 영화 제목, 리뷰 제목, 리뷰 내용, 평점, 생성한 시간, 수정된 시간 순으로 표시

2. Go main 버튼, Update 버튼, Delete 버튼을 만들어 각 버튼을 클릭하면 해당 기능을 실행

<br>

#### 💻 웹 크기
![w-detail](https://user-images.githubusercontent.com/107910587/194854279-e9c451a3-7551-4d3e-8862-d7fb25ac216d.gif)

<br>

#### 📱 모바일 크기

![m-detail](https://user-images.githubusercontent.com/107910587/194718610-e0257005-e719-4136-8b48-68ac8d33d450.gif)

<br>

### 4.4 영화 리뷰 생성 (CREATE)

<br>

1. 목록 페이지의 write 버튼 혹은 네비게이션 바의 add를 누르면 작성 페이지로 넘어감

2. 테이블 컬럼 순서대로 만들어진 모델 폼을 활용해 사용자에게 데이터 값을 입력받음

3. 평점은 1부터 5사이의 숫자만 입력 가능하고 범위를 벗어나는 숫자를 입력했을 시 유효하지 않다는 표시와 함께 생성되지 않음

<br>

#### 💻 웹 크기
![w-create](https://user-images.githubusercontent.com/107910587/194854292-6ea3e84d-1868-4264-a9aa-c86011cf20da.gif)


<br>

#### 📱 모바일 크기

![m-create](https://user-images.githubusercontent.com/107910587/194718619-0d716d47-bd28-48e2-875a-dc720acdd957.gif)

<br>

### 4.5 영화 리뷰 수정 (UPDATE)

<br>

1. 입력받아 저장되어있는 해당 게시글을 모델 폼으로 불러와 보여줌

2. 리뷰 게시글을 수정하여 edit 버튼을 클릭하면 수정사항이 반영되고 목록 페이지로 이동

<br>

#### 💻 웹 크기
![w-update](https://user-images.githubusercontent.com/107910587/194854247-9ef78673-c605-406b-b005-d9f8c583f124.gif)

<br>

#### 📱 모바일 크기

![m-update](https://user-images.githubusercontent.com/107910587/194854318-fa3f6cdf-ccf9-49b6-b1b1-cc987c2769bf.gif)

<br>

### 4.6 영화 리뷰 삭제 (DELETE)
<br>

1. 리뷰 상세 페이지에 있는 delete 버튼을 클릭하면 해당 게시글의 데이터가 삭제되고 목록 페이지로 이동

<br>

#### 💻 웹 크기
![w-delete](https://user-images.githubusercontent.com/107910587/194854283-4d127f7a-7b28-4b12-bd74-09d240b7ec75.gif)

<br>

#### 📱 모바일 크기

![m-delete](https://user-images.githubusercontent.com/107910587/194718615-4d2a7534-bd10-4c33-913b-60911dbcd527.gif)

<br>

<hr>
<br>

## 5. 프로젝트를 통해 배운 점

<br>

    CRUD를 반복 구현하면서 보게되는 오류메시지들을 어느정도 이해하고 해결할 수 있게 되었다.

    이미 만들어둔 테이블 속성을 수정할 때 models.py에서 변경사항을 추가하고 다시 makemigrations와 migrate를 하면 변경된 속성이 반영되었다.

<br>


### 5.1 반응형 구현(💻 웹, 📱 모바일)

<br>

    웹과 모바일 크기에서 리뷰 게시글 카드 크기를 다르게 설정하려고 했지만 하지 못했다.

    반응형 구현을 신경쓰면서 만들었더니 시간이 더 오래 걸렸다.

<br>

## 6. 느낀점

<br>

    계속 반복해서 익숙해지게 만들어야겠다. 처음 설정할 때 시간이 너무 오래 걸린다.
