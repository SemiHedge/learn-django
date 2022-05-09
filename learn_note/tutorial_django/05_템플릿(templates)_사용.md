# 템플릿을 사용하여 HTML 콘텐츠를 클라이언트에 반환하기

### (짚고가기) 장고의 View는 일반적으로 부르는 View가 아니라 Request Handler(처리기) 또는 Request Action(작업)에 가깝다.
- 타 프레임워크의 View == Django의 템플릿

## html 콘텐츠 준비
- 생성 : `playground` 앱에 `templates` 폴더
- 생성 : `templates`폴더에 `hello.html` 파일
    - 가볍게 `<h1>Hello World</h1>`

## playground 앱의 views.py
- `from django.shortcuts import render` 함수를 이용해 html을 반환
- 변경 : 단순 텍스트를 돌려주든 `say_hello`함수를 변경한다.
- `render` 함수 매개변수 살펴보자.
    - 첫번째 : `request : HttpRequest`
        - 해당 요청의 http request에 대한 HttpRequest 객체
        - 따라서 여기선 인자로 들어온 request를 넣어주고 넘어가자.
    - 두번째 : `template_name : str`
        - html 파일명을 문자열로
    - 기존 : `return HttpResponse("Hello World!")`
    - 변경 : `return render(request, 'hello.html')`

```python
def say_hello(request):
    return render(request, 'hello.html')
```

### 작동확인
- http://127.0.0.1:8000/playground/hello/


## 값을 html로 렌더링

### views.py에서 render함수 변경
- views.py에서 render함수 설명을 한 번 더 확인해보자.
- `render` 함수 세번째
    - `context : Mapping[str, Any]`
    - 이 뜻은 map구조를 가지고 key는 문자열, value는 어떤 값이여도 괜찮다는 뜻
    - 딱 `dict`와 맞는 구조
```python
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Semi'})
```

### html 변경
- `{{key}}` 을 입력하면 관련된 value가 나온다.
- 변경 : `<h1>Hello {{name}}</h1>`

### html에 if문 적용하기 - 장고 템플릿 태그
- 장고 템플릿 문법을 이용하여 렌더링 결과를 바꿔보자
- [장고 템플릿 태그 4.0](https://docs.djangoproject.com/ko/4.0/ref/templates/builtins/)

```
{% if name %}
<h1>Hello {{name}}</h1>
{% else %}
<h1>Hello World</h1>
{% endif %}
```

### (두둥!) 그런데 장고 템플릿 태그는 잘 사용하지 않는다.
- 장고 템플릿 태그는 편하고 쉽습니다만..
- 요즘의 실제 프로젝트에선 장고 템플릿 태그는 잘 사용하지 않습니다.
- 장고는 HTML콘텐츠를 렌더링에서 넘겨주는 역할을 하지않고 데이터를 반환하는 API 역할을 수행|빌드합니다.
    - 이건 장고 뿐만이 아니라 웹 백엔드 - 프론트엔드를 그렇게 역할을 나눠둠
    - 때문에 다른 웹 서버 프레임워크도 동일한 상황
- 정말 예외상황 또는 필요한 상황이 발생하지 않는 한 장고 템플릿 태그는 사용하지 않습니다.