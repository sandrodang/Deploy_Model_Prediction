import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from fastapi import FastAPI
from middleware import LogProcessAndTime, setup_cors
from routes.base import router

app = FastAPI()

app.add_middleware(LogProcessAndTime)
setup_cors(app)
app.include_router(router)