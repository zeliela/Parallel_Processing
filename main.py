from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
import subprocess
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Set the base path for the scenario scripts to match your system's directory structure
base_path = "/absolute/path/to/Parallel_Processing"


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
        folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]
        scenarios = {folder: [f for f in os.listdir(os.path.join(base_path, folder)) if f.startswith('scenario')] for folder in folders}
        return templates.TemplateResponse("index.html", {"request": request, "scenarios": scenarios})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})

@app.post("/run_scenario", response_class=HTMLResponse)
async def run_scenario(request: Request, folder: str = Form(...), scenario: str = Form(...)):
    try:
        script_path = os.path.join(base_path, folder, scenario)
        result = subprocess.run(["python", script_path], capture_output=True, text=True)
        output = result.stdout + result.stderr
        return templates.TemplateResponse("result.html", {"request": request, "folder": folder, "scenario": scenario, "output": output})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})

@app.get("/show_code", response_class=HTMLResponse)
async def show_code(request: Request, folder: str, scenario: str):
    try:
        script_path = os.path.join(base_path, folder, scenario)
        with open(script_path, 'r') as f:
            code = f.read()
        return templates.TemplateResponse("code.html", {"request": request, "folder": folder, "scenario": scenario, "code": code})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
