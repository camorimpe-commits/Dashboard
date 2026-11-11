import os
from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from core.config import BASE_DIR, UPLOADS_DIR
from core.data_processor import data_processor
from core.watcher import file_watcher
from api.routes_auth import router as auth_router
from api.routes_metrics import router as metrics_router
from api.routes_decisions import router as decisions_router
from api.routes_data import router as data_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: ensure upload dir exists & initial load
    UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
    print("[SYSTEM] Initializing Operational Efficiency Engine...")
    data_processor.load_and_process()
    file_watcher.start()
    yield
    # Shutdown
    print("[SYSTEM] Shutting down watcher...")
    file_watcher.stop()

app = FastAPI(
    title="OptimaOps - Monitor de Eficiência Operacional",
    description="Solução Integrada de Monitoramento e Inteligência Operacional com Python, FastAPI e Dashboard Interativo",
    version="2.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
static_dir = BASE_DIR / "static"
static_dir.mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# Include API Routers
app.include_router(auth_router)
app.include_router(metrics_router)
app.include_router(decisions_router)
app.include_router(data_router)

# HTML Template Renderers
templates_dir = BASE_DIR / "templates"

@app.get("/", response_class=HTMLResponse)
def index_redirect():
    return RedirectResponse(url="/login")

@app.get("/login", response_class=HTMLResponse)
def get_login_page():
    login_path = templates_dir / "login.html"
    if login_path.exists():
        with open(login_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse("<h1>Login page not found</h1>", status_code=404)

@app.get("/dashboard", response_class=HTMLResponse)
def get_dashboard_page():
    dash_path = templates_dir / "dashboard.html"
    if dash_path.exists():
        with open(dash_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse("<h1>Dashboard page not found</h1>", status_code=404)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
