from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request
# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

# 회원 가입 /users/insert
@router.get("/insert")  
async def insert(request:Request):
    return templates.TemplateResponse(name="users/inserts.html"
                                      , context={'request':request})
