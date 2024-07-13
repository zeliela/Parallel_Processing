from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
import subprocess
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Dictionary for folders and scenarios
folders = {
    "Pro_1": ["scenario1.py", "scenario2.py", "scenario3.py"],
    "Pro_2": ["scenario1.py", "scenario2.py", "scenario3.py"],
    "Pro_3": ["scenario1.py", "scenario2.py", "scenario3.py"],
    "Pro_4": ["scenario1.py", "scenario2.py", "scenario3.py"],
    "Pro_5": ["scenario1.py", "scenario2.py", "scenario3.py"],
    "Pro_6": ["scenario1.py", "scenario2.py", "scenario3.py"],
    "Pro_7": ["scenario1.py", "scenario2.py", "scenario3.py"],
    "Pro_8": ["scenario1.py", "scenario2.py", "scenario3.py"],
    "Tr_1": ["scenario1.py", "scenario2.py", "scenario3.py"],
    "Tr_2": ["scenario1.py", "scenario2.py", "scenario3.py"],
    "Tr_3": ["scenario1.py", "scenario2.py", "scenario3.py"],
    "Tr_4": ["scenario1.py", "scenario2.py", "scenario3.py"],
    "Tr_5": ["scenario1.py", "scenario2.py", "scenario3.py"],
    "Tr_6": ["scenario1.py", "scenario2.py", "scenario3.py"],
    "Tr_7": ["scenario1.py", "scenario2.py", "scenario3.py"]
}

# Handle CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def validation_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)},
    )

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    try:
        return templates.TemplateResponse("index.html", {"request": request, "scenarios": folders})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})

@app.post("/run_scenario", response_class=HTMLResponse)
async def run_scenario(request: Request, folder: str = Form(...), scenario: str = Form(...)):
    try:
        script_path = os.path.join("E:/Parallel_Processing", folder, scenario)
        if os.path.exists(script_path):
            result = subprocess.run(["python", script_path], capture_output=True, text=True)
            output = result.stdout + result.stderr
            return templates.TemplateResponse("result.html", {"request": request, "folder": folder, "scenario": scenario, "output": output})
        else:
            return JSONResponse(status_code=404, content={"detail": "Script not found"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})

@app.get("/show_code", response_class=HTMLResponse)
async def show_code(request: Request, folder: str, scenario: str):
    try:
        script_path = os.path.join("E:/Parallel_Processing", folder, scenario)
        with open(script_path, 'r') as f:
            code = f.read()
        return templates.TemplateResponse("code.html", {"request": request, "folder": folder, "scenario": scenario, "code": code})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

