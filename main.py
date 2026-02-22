from fastapi import FastAPI

from user_router import router as user_router
app = FastAPI(title="LLM Powered Databased Agent")
app.include_router(user_router)