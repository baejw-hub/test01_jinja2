# test01_jinja2/main.py


# fastapi 객체 생성
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()


# 템플릿 파일들이 위치하는 디렉토리 정보를 전달하면서 Jinja2Templates 객체를 생성한다.
templates = Jinja2Templates(directory="templates")


# response_class=HTMLResponse 옵션은 html 형식의 문자열을 응답하겠다는 의미
@app.get("/", response_class=HTMLResponse)
def index(req: Request): # Request type 객체가 매개변수에 전달된다.
    # DB 에서 불러온 공지 사항이라고 가정하자
    noticeList = ["교제가 오늘 도착했습니다", "교제 도착 확인을 해주세요", "어쩌구..", "저쩌구..."]


    result = templates.TemplateResponse(
        request=req, # request 에는 index() 함수에 전달되는 req 객체 전달
        name="index.html", # templates/index.html 을 템플릿 문서로 사용하겠다는 의미
        context={
            "fortuneToday":"happy 하게 대박이나서 소원이 성취됨으로 웃게됩니다",
            "noticeList":noticeList
        } # 템플릿 문서를 해석하는데 필요한 data 를 담고 있는 dict 를 context 에 전달
    )
    return result
# GET 방식 "/members" 요청에 대한 응답
@app.get("/members", response_class=HTMLResponse)
def members(req: Request):
    # DB 에서 읽어온 데이터라고 가정하자
    list = [
        {"num":1, "name":"김구라", "addr":"노량진"},
        {"num":2, "name":"해골", "addr":"행신동"},
        {"num":3, "name":"원숭이", "addr":"동물원"}
    ]


    return templates.TemplateResponse(
        request=req,
        name="members.html",
        context={
            "list":list
        }
    )
