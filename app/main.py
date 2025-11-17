from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Glossary")
app.include_router(router)