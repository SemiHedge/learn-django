# views.py에서 View함수 정의
- http 요청(Request)와 응답(Resoponse)에 관여
- 모든 데이터의 요청과 응답 과정이 여기에 포함

## playground 앱의 views.py 에서 View 함수를 정의
### View 함수란?
- 요청을 받고 응답을 반환하는 함수
- 요청 처리기(request handler)라고 이해
- 장고에서는 'View'라고 하는 작업(action)으로 설명하나, 솔직히 명쾌한 정의는 아닌 듯
    - 아키텍쳐 관점에서 View란 단어는 템플릿을 지칭하거나 연관된 것을 설명할 때 쓰기 때문에..

### View함수 정의 1
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
```
- 해당 함수는 요청(request) 객체를 가져와서 응답(response)를 반환합니다.
- 때문에 django.http 패키지에서 HttpResponse 클래스를 참조합니다.

### View함수 정의 2
- 이제 정의된 함수에 시나리오를 적습니다.
    - DB를 액세스하여 CRUD를 한다거나
    - 데이터를 변환(Transform)한다거나
    - email, noti 등을 한다거나
- 일단은 실습을 위해 다음처럼 합니다.
    - HttpResponse를 return하고
    - 해당 객체에 간단한 문자열을 추가

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello World!")
```

## View함수를 정의한 뒤
- 이제 이 View를 url에 매핑해야한다.
- url 매핑을 하면
    - 해당 url에서 요청을 받으면
    - 이 View함수가 호출됩니다.