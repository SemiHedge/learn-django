# 디버그 모드를 통해 오류를 확인해보자

## 실행 profile을 만들기
1. 실행 및 디버그 버튼을 클릭
2. `create a launch.json` 을 클릭
3. django를 선택하면 JSON 파일 생성

```
{
    // IntelliSense를 사용하여 가능한 특성에 대해 알아보세요.
    // 기존 특성에 대한 설명을 보려면 가리킵니다.
    // 자세한 내용을 보려면 https://go.microsoft.com/fwlink/?linkid=830387을(를) 방문하세요.
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}\\manage.py",
            "args": [
                "runserver"
            ],
            "django": true,
            "justMyCode": true
        }
    ]
}
```
- 현재 Python 인터프리터는 작업 위치의 manage.py를 실행하고
- runserver라는 인수가 추가되어 있습니다.
- 포트를 지정하려면 다음처럼도 할 수 있습니다.
    - `"runserver", "9000"` 이렇게 하면 다음처럼 실행하는 것과 같습니다.
    - `python manage.py runserver 9000`
    - 9000을 넣어줘서 충돌을 피하도록 합시다.
- 저는 workspaceFolder가 아니라 한번 더 tutorial_django가 들어가 있으므로 추가합니다.
    - `"program": "${workspaceFolder}\\tutorial_django\manage.py"`

## 디버깅 모드 실행해보기
1. views.py를 다음처럼 변경
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    x = 1
    y = 2
    return render(request, 'hello.html', {'name': 'Semi'})
```
2. x = 1 에 break point 넣기
3. 실행 및 디버그 탭에서 재생 버튼 클릭

### 혹시 이 단계에서 에러가 난다면?
```
ImportError
Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
```
- 현재 python 인터프리터가 가상환경 걸로 잡히지 않아서 그렇다.

### python 인터프리터 경로 변경하기
1. 명령 팔레트(Ctrl+Shift+P)를 열어 Python3 인터프리터를 선택합니다.
2. `Python: Select interpreter`를 입력
3. 경로에 `virtualenv\` 가 들어간 python 을 선택. 우측에 PipEnv라고 뜰 것
4. 터미널에서 Python Debug Console을 삭제 후 다시 실행해보면 성공

## url을 들어가보자.
- 현재 대문 페이지는 나오지 않는다.
- 저번에 프로젝트 urls.py에서 사용자 지정 경로 `playgorund/hello`를 등록했기 때문에 기본 프로젝트가 사라져있다.

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
]
```

## /playground/hello를 붙여 접속
1. 입력하면 변화는 없는데 VSCode에서 걸어놓은 break point로 이동된다.
2. 디버그 창에서 변수>Locals에 현재의 지역변수 정보를 볼 수 있다.
    - 우리가 주고받는 request 객체도 보인다.

## breakpoint에서 하나 실행하고 싶으면 step over
- 단축키는 f10
- 현재 라인을 실행하고 넘깁니다.
- 어떤 특정 라인이 실행이 안된다고 의심되면 이와 같은 방식을 사용할 수 있다.
- F10을 눌러 say_hello 함수를 끝내면 정상적인 페이지가 등장

## watch(조사식) 탭
- 변수에는 모든 데이터가 보인다. 너무 많다.
- 조사식에 보고싶은 변수명만 적으면 현재 적용되는 값을 확인할 수 있다.
- 마치 검색 창의 Filter 같은 기능이다.


## 디버깅 모드 Step into
- 이번엔 plaground/views.py에 함수를 응용해보았다.
```python
def calculate():
    x = 2
    y = 3
    return x * y

def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Semi'})
```
- ` x = calculate()`에 break point를 넣고 실행
- 만일 StepOver를 하면 아래의 `return render...` 코드로 넘어가지만
- StepInto(F11)를 누르면 해당 줄의 함수 내부로 들어간다.
- 호출한 함수가 잘못 되었을 수도 있는데, 이를 사용할 수 있다.

## 디버깅 모드 Step Out
- 함수로 들어왔는데 해당 함수의 모든 라인을 실행할 필요없이 탈출하고 싶을 때
- 더이상 확인할 필요가 없을 때는 StepOut(Shift+F11)

## 디버깅 모드를 끝냈다면 중단점을 없애자.
- 미리 삭제를 안해두면 나중에 디버깅시 방해가 될 수 있다.
- 디버깅 연결을 종료하고 싶으면 정지버튼(Shift+F5)

## 디버깅 모드없이 실행하려면 Ctrl + F5
- 디버깅 모드로 실행하려면 F5
- 메뉴 실행(R) 탭에 있다.
