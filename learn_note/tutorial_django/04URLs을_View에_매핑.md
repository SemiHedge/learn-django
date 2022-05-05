# URLs을 View에 매핑
- 다음처럼 작동하도록 해보자.
    - `127.0.0.1:8000/playground/hello`로 접근하면 
    - View함수 `say_hello()`가 호출되서 `Hello World!`가 반환되도록

## 생성 : playground/urls.py
- 이름은 중요하지않으나 관례적으로 urls.py라고 짓고 있다.
- 이 모듈에서는 URL을 View함수에 매핑한다.

### 매핑 과정 1
- `django.urls`에 `path` 함수 참조
- `views` 모듈을 참조하여 View함수를 참조할 수 있도록

```python
from django.urls import path
from . import views
```

### 매핑 과정 2
- `urlpatterns = []` 라는 특수 변수를 정의
    - 모두 소문자
    - django가 이 특수 변수를 찾아 사용합니다.
- `path`함수를 사용합니다.
    - 첫번째 매개변수 route : 문자열로 된 경로.
    - 두번째 매개변수 view : HttpResponse 객체를 반환하는 View함수
    - 함수의 반환 유형 : URLPattern을 반환

```python
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('playground/hello', views.say_hello)
]
```

### playgorund/urls.py의 urlpatterns를 프로젝트/urls.py에 적용
- `playgorund/urls.py`에 정의된 URL 구성을 프로젝트 기본 url로 가져와야한다.
- `Django프로젝트폴더/urls.py` 를 열면 어떻게 추가할 수 있는 지 나와있다.
    - 여기서는 `tutorial_django/urls.py`

```
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
```
- `from django.urls import include, path`를 참조하고
- `urlpatterns`에 `path('blog/', include('blog.urls'))`과 같은 방식으로 추가

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
]
```

- 첫번째 인자는 `playground/`로 시작되는 모든 URL
- 두번째 인자는 `playground`앱으로 라우팅되어야 하므로 `include`함수를 사용
    - `playground.urls`를 참조할 것이므로 문자열로 기입

### 이제 작동될 일 + playground/urls.py 수정
- 이제 `playground/hello`로 요청을 보내는 경우
    - 맨 처음에는 `django_tutorial/urls.py`를 확인한다.
    - django는 `playground/`로 시작하는 모든 요청이
    - `playground 앱`에서 처리되어야 한다는 알고 있으므로
    - `playground/hello`에서 앞 부분을 잘라내고
    - 나머지 `hello`는 `playground 앱`의 URL구성모듈(`urls.py`)에 전달한다.
- 그런데 `playground/urls.py`에 전달 되었을 때
    - 기본 urls.py에서 `playground/` 경로가 한 번 추가되었기 때문에
    - 여기서는 더 이상 `playground/`를 추가할 필요가 없다.
    - `hello`만 남기고 뒤에 `/`를 추가해준다.

```python
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello)
]
```

### [주의] 경로를 항상 슬래시(/)로 끝내야한다.


## 동작 확인
- http://127.0.0.1:8000/playground/hello/
    - Hello World! 가 출력된다.
- 현재 단계에서 http://127.0.0.1:8000는 404가 뜬다.

```
Using the URLconf defined in tutorial_django.urls, Django tried these URL patterns, in this order:

admin/
playground/
The empty path didn't match any of these.
```