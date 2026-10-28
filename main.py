from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Landing Sites")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ---------- Coffee ----------
@app.get("/", response_class=HTMLResponse)
@app.get("/coffee", response_class=HTMLResponse)
async def coffee_index(request: Request):
    return templates.TemplateResponse(request=request, name="coffee/index.html")

@app.get("/coffee/menu", response_class=HTMLResponse)
async def coffee_menu(request: Request):
    return templates.TemplateResponse(request=request, name="coffee/menu.html")

@app.get("/coffee/booking", response_class=HTMLResponse)
async def coffee_booking_form(request: Request):
    return templates.TemplateResponse(request=request, name="coffee/booking.html", context={"submitted": False})

@app.post("/coffee/booking", response_class=HTMLResponse)
async def coffee_booking_submit(
    request: Request,
    name: str = Form(...),
    phone: str = Form(...),
    table: str = Form("Не выбран")
):
    return templates.TemplateResponse(
        request=request,
        name="coffee/booking.html",
        context={"submitted": True, "name": name, "table": table}
    )

# ---------- Psy ----------
@app.get("/psy", response_class=HTMLResponse)
async def psy_index(request: Request):
    return templates.TemplateResponse(request=request, name="psy/index.html")

@app.get("/psy/booking", response_class=HTMLResponse)
async def psy_booking_form(request: Request):
    return templates.TemplateResponse(request=request, name="psy/booking.html", context={"submitted": False})

@app.post("/psy/booking", response_class=HTMLResponse)
async def psy_booking_submit(
    request: Request,
    name: str = Form(...),
    phone: str = Form(...),
    specialist: str = Form("Не выбран"),
    time: str = Form("Не выбрано")
):
    return templates.TemplateResponse(
        request=request,
        name="psy/booking.html",
        context={"submitted": True, "name": name, "specialist": specialist, "time": time}
    )