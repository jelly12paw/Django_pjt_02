# π μν λ¦¬λ·° μΉ κ΅¬ννκΈ°
<br>

    Djangoλ‘ CRUD νμ©ν μν λ¦¬λ·° μΉ μ¬μ΄νΈ κ΅¬ννκΈ°    

<hr>

![w-bingbong](https://user-images.githubusercontent.com/107910587/194854302-e23905b3-21d4-49ec-b0b8-95bed1fb0fb9.gif) ![m-bingbong](https://user-images.githubusercontent.com/107910587/194718583-df06245d-1897-4abb-bcf8-341c59b69b1c.gif)
<br>

## π§° μ¬μ©κΈ°μ 

<br>

<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=ffffff"/> γ<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=ffffff"/> γ<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=ffffff"/> γ<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=ffffff"/> γ<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=ffffff"/> γ<img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=ffffff"/>

<br>

<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=ffffff"/>γ<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=ffffff"/>γ<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=ffffff"/>

<br>

## π νλ‘μ νΈ κΈ°κ°

### 2022.10.07

<br>

## π©π»βπ» μ­ν 

### Front-end & Back-end

<br>

<hr>

<br>

## β¨ 1. λͺ©ν μλΉμ€
<br>

### 1.1 μν λ¦¬λ·° κ²μν

<br>

1. μν λ¦¬λ·° κ²μκΈ μμ±, μ­μ , μμ  κΈ°λ₯
2. νμ  κΈ°λ₯

<br>

## β¨ 2. μ€μ  κ΅¬ν μ λ
<br>

### 2.1 μν λ¦¬λ·° κ²μν

<br>

1. μν λ¦¬λ·° μμ±, μ­μ , μμ  κΈ°λ₯
2. νμ  κΈ°λ₯
3. λ°μν κ΅¬ν

<br>

<hr>
<br>

## β 3. νλ‘μ νΈ μ§νκ³Όμ 

<br>

### 3.1 κ°μνκ²½ μμ± λ° μ₯κ³  μ€μΉ
<br>

```python
python -m venv venv
```

```bash
pip install django==3.2.13
```
<br>

### 3.2 νλ‘μ νΈ μμ±
<br>

```bash
django-admin startproject movie .
```

<br>

### 3.3 μ± μμ±
<br>

```bash
python manage.py startapp reviews
```
<br>

### 3.4 λͺ¨λΈ μμ±
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

### 3.5 λͺ¨λΈ νΌ μμ±
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

### 3.6 μν λ¦¬λ·° κ²μκΈ CRUD
<br>

1. κΈμ°κΈ° λ²νΌμ λλ₯΄λ©΄ μμ±λ λͺ¨λΈ νΌ νλ©΄μ΄ λμ μ¬μ©μκ° μλ ₯ν μ λ³΄λ₯Ό λ°μ λ°μ΄ν°λ² μ΄μ€μ μ μ₯νκΈ°
<br>

2. μμΈλ³΄κΈ° λ²νΌμ λλ₯΄λ©΄ μ¬μ©μκ° μλ ₯ν κ²μκΈμ λ³΄μ¬μ£ΌκΈ°
<br>

3. μμ νκΈ° λ²νΌμ λλ₯΄λ©΄ μ¬μ©μκ° μλ ₯νλ μ λ³΄λ₯Ό λ°μμ λ³΄μ¬μ£Όκ³  μμ λ μ λ³΄λ₯Ό μ μ₯νκΈ°
<br>

4. μ­μ  λ²νΌμ λλ₯΄λ©΄ μ¬μ©μκ° μμ±ν κ²μκΈμ μ­μ νκΈ°

<br>

## π₯ 4. μ€μ  κ΅¬ν νλ©΄

<br>

### 4.1 μν λ¦¬λ·° λ©μΈ νμ΄μ§

<br>

1. GIF μ΄λ―Έμ§ μ½μ, κΈμ¨μ μ λλ©μ΄μ ν¨κ³Όλ₯Ό μ£Όμ΄ λ©μΈνμ΄μ§λ₯Ό κ΅¬μ±

2. λ°μν κ΅¬νμ λ°λΌ λͺ¨λ°μΌ ν¬κΈ°μ μΉ ν¬κΈ°μμ κ° νλ©΄μ λ§λ ν°νΈν¬κΈ°λ‘ κ΅¬ν

3. λ€λΉκ²μ΄μ λ°μ μνλ‘κ³  μ΄λ―Έμ§, λͺ©λ‘μ list, addλ₯Ό μμ±, λ°μν κ΅¬νμΌλ‘ λͺ¨λ°μΌ ν¬κΈ°μΌ λλ ν κΈ λ²νΌμ΄ λ³΄μ¬μ§. μνλ‘κ³  μ΄λ―Έμ§λ₯Ό ν΄λ¦­νλ©΄ λ©μΈ νμ΄μ§λ‘ μ°κ²°, listλ₯Ό ν΄λ¦­νλ©΄ λͺ©λ‘ νμ΄μ§λ‘ μ°κ²°, addλ₯Ό ν΄λ¦­νλ©΄ λ¦¬λ·° μμ± νμ΄μ§λ‘ μ°κ²°λ¨ 

<br>

#### π» μΉ ν¬κΈ°
![w-main](https://user-images.githubusercontent.com/107910587/194854261-83e7371e-0521-4b2e-b0a6-6712c6104997.gif)


<br>

#### π± λͺ¨λ°μΌ ν¬κΈ°

![m-main](https://user-images.githubusercontent.com/107910587/194718595-0d80c333-01ea-4980-b919-ac1b110d06e7.gif)

<br>

### 4.2 μν λ¦¬λ·° λͺ©λ‘ νμ΄μ§

<br>

1. μμ±λ λ¦¬λ·° κ²μκΈμ μΉ΄λννλ‘ κ΅¬ν

2. λ°μν κ΅¬νμ λ°λΌ λͺ¨λ°μΌ ν¬κΈ°μ μΉ ν¬κΈ°μμ λνλλ μΉ΄λ νμ ννλ₯Ό λ€λ₯΄κ² κ΅¬ν 
   <br> (μΉ ν¬κΈ°λ ν μ€μ 4κ°μ μΉ΄λ, λͺ¨λ°μΌ ν¬κΈ°λ ν μ€μ 1κ°μ μΉ΄λ)

3. write λ²νΌμ ν΄λ¦­νλ©΄ λ¦¬λ·° μμ± νμ΄μ§λ‘ μ°κ²°λ¨

<br>

#### π» μΉ ν¬κΈ°

![w-list](https://user-images.githubusercontent.com/107910587/194854276-a88a624c-90c3-4435-8310-0c6b8ce38e74.gif)


<br>

#### π± λͺ¨λ°μΌ ν¬κΈ°

![m-list](https://user-images.githubusercontent.com/107910587/194718603-710edc1d-9372-4d63-8a0a-2386fe49d694.gif)

<br>

### 4.3 μν λ¦¬λ·° μμΈ νμ΄μ§

<br>

1. μλ ₯λ°μ λ°μ΄ν°λ₯Ό μ΄λ―Έμ§, μν μ λͺ©, λ¦¬λ·° μ λͺ©, λ¦¬λ·° λ΄μ©, νμ , μμ±ν μκ°, μμ λ μκ° μμΌλ‘ νμ

2. Go main λ²νΌ, Update λ²νΌ, Delete λ²νΌμ λ§λ€μ΄ κ° λ²νΌμ ν΄λ¦­νλ©΄ ν΄λΉ κΈ°λ₯μ μ€ν

<br>

#### π» μΉ ν¬κΈ°
![w-detail](https://user-images.githubusercontent.com/107910587/194854279-e9c451a3-7551-4d3e-8862-d7fb25ac216d.gif)

<br>

#### π± λͺ¨λ°μΌ ν¬κΈ°

![m-detail](https://user-images.githubusercontent.com/107910587/194718610-e0257005-e719-4136-8b48-68ac8d33d450.gif)

<br>

### 4.4 μν λ¦¬λ·° μμ± (CREATE)

<br>

1. λͺ©λ‘ νμ΄μ§μ write λ²νΌ νΉμ λ€λΉκ²μ΄μ λ°μ addλ₯Ό λλ₯΄λ©΄ μμ± νμ΄μ§λ‘ λμ΄κ°

2. νμ΄λΈ μ»¬λΌ μμλλ‘ λ§λ€μ΄μ§ λͺ¨λΈ νΌμ νμ©ν΄ μ¬μ©μμκ² λ°μ΄ν° κ°μ μλ ₯λ°μ

3. νμ μ 1λΆν° 5μ¬μ΄μ μ«μλ§ μλ ₯ κ°λ₯νκ³  λ²μλ₯Ό λ²μ΄λλ μ«μλ₯Ό μλ ₯νμ μ μ ν¨νμ§ μλ€λ νμμ ν¨κ» μμ±λμ§ μμ

<br>

#### π» μΉ ν¬κΈ°
![w-create](https://user-images.githubusercontent.com/107910587/194854292-6ea3e84d-1868-4264-a9aa-c86011cf20da.gif)


<br>

#### π± λͺ¨λ°μΌ ν¬κΈ°

![m-create](https://user-images.githubusercontent.com/107910587/194718619-0d716d47-bd28-48e2-875a-dc720acdd957.gif)

<br>

### 4.5 μν λ¦¬λ·° μμ  (UPDATE)

<br>

1. μλ ₯λ°μ μ μ₯λμ΄μλ ν΄λΉ κ²μκΈμ λͺ¨λΈ νΌμΌλ‘ λΆλ¬μ λ³΄μ¬μ€

2. λ¦¬λ·° κ²μκΈμ μμ νμ¬ edit λ²νΌμ ν΄λ¦­νλ©΄ μμ μ¬ν­μ΄ λ°μλκ³  λͺ©λ‘ νμ΄μ§λ‘ μ΄λ

<br>

#### π» μΉ ν¬κΈ°
![w-update](https://user-images.githubusercontent.com/107910587/194854247-9ef78673-c605-406b-b005-d9f8c583f124.gif)

<br>

#### π± λͺ¨λ°μΌ ν¬κΈ°

![m-update](https://user-images.githubusercontent.com/107910587/194854318-fa3f6cdf-ccf9-49b6-b1b1-cc987c2769bf.gif)

<br>

### 4.6 μν λ¦¬λ·° μ­μ  (DELETE)
<br>

1. λ¦¬λ·° μμΈ νμ΄μ§μ μλ delete λ²νΌμ ν΄λ¦­νλ©΄ ν΄λΉ κ²μκΈμ λ°μ΄ν°κ° μ­μ λκ³  λͺ©λ‘ νμ΄μ§λ‘ μ΄λ

<br>

#### π» μΉ ν¬κΈ°
![w-delete](https://user-images.githubusercontent.com/107910587/194854283-4d127f7a-7b28-4b12-bd74-09d240b7ec75.gif)

<br>

#### π± λͺ¨λ°μΌ ν¬κΈ°

![m-delete](https://user-images.githubusercontent.com/107910587/194718615-4d2a7534-bd10-4c33-913b-60911dbcd527.gif)

<br>

<hr>
<br>

## 5. νλ‘μ νΈλ₯Ό ν΅ν΄ λ°°μ΄ μ 

<br>

    CRUDλ₯Ό λ°λ³΅ κ΅¬ννλ©΄μ λ³΄κ²λλ μ€λ₯λ©μμ§λ€μ μ΄λμ λ μ΄ν΄νκ³  ν΄κ²°ν  μ μκ² λμλ€.

    μ΄λ―Έ λ§λ€μ΄λ νμ΄λΈ μμ±μ μμ ν  λ models.pyμμ λ³κ²½μ¬ν­μ μΆκ°νκ³  λ€μ makemigrationsμ migrateλ₯Ό νλ©΄ λ³κ²½λ μμ±μ΄ λ°μλμλ€.

<br>


### 5.1 λ°μν κ΅¬ν(π» μΉ, π± λͺ¨λ°μΌ)

<br>

    μΉκ³Ό λͺ¨λ°μΌ ν¬κΈ°μμ λ¦¬λ·° κ²μκΈ μΉ΄λ ν¬κΈ°λ₯Ό λ€λ₯΄κ² μ€μ νλ €κ³  νμ§λ§ νμ§ λͺ»νλ€.

    λ°μν κ΅¬νμ μ κ²½μ°λ©΄μ λ§λ€μλλ μκ°μ΄ λ μ€λ κ±Έλ Έλ€.

<br>

## 6. λλμ 

<br>

    κ³μ λ°λ³΅ν΄μ μ΅μν΄μ§κ² λ§λ€μ΄μΌκ² λ€. μ²μ μ€μ ν  λ μκ°μ΄ λλ¬΄ μ€λ κ±Έλ¦°λ€.
