import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Hệ Thống Giao Dịch")

current_dir = os.path.dirname(os.path.abspath(__file__))

# Mount thư mục static
static_dir = os.path.join(current_dir, 'static')
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Chỉ định thư mục templates
templates = Jinja2Templates(directory=os.path.join(current_dir, 'templates'))

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # Trả về giao diện trong file templates/index.html
    return templates.TemplateResponse("index.html", {"request": request})