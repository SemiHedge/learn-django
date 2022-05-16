# Django Debug Toolbar
- https://django-debug-toolbar.readthedocs.io/en/latest/
- 장고 전용으로 페이지내부에서 디버깅을 도와주는 툴입니다.

### 주의
- 업데이트가 되어 변경될 수 있으니, 공식홈페이지를 참고하자

### 설치
`pip install django-debug-toolbar`

### 기존 환경 체크
- `settings.py`에서
    - 확인 : `INSTALLED_APPS`에 `"django.contrib.staticfiles"`
    - 확인 : `TEMPLATES`에 `"APP_DIRS": True,`가 있는 지 확인

### django-debug-toolbar APP 추가
- `'debug_toolbar'`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'playground',
]
```

### urls.py의 `urlpatterns`에 URLS 추가
- `path('__debug__/', include('debug_toolbar.urls')),`
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
```

### settings.py의 MIDDLEWARE에 추가
- `"debug_toolbar.middleware.DebugToolbarMiddleware",`

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
```

### 추가 IP 세팅
- 생성 : `settings.py`에서 변수 INTERNAL_IPS를 생성해야한다.
- 맨 하단에 생성하자.
```python
# django-debug-toolbar setting
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
```

## 실행해보기
- `django-debug-toolbar`는 html에서만 작동한다.
- `hello.html`을 다음처럼 변경
```html
<html>
    <body>
        {% if name %}
        <h1>Hello {{name}}</h1>
        {% else %}
        <h1>Hello World</h1>
        {% endif %}
    </body>
</html>
```
- 하고 브라우저를 들어가면 우측에 디버그 탭이 등장한다.
    - History
    - Versions
    - Time
    - Settings
    - Headers
    - Request
    - SQL
    - Static files
    - Templates
    - Cache
    - Signals
    - Logging
