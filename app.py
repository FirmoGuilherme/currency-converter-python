from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from src.connectors.db import Base, engine
from src.logging import setup_logging, get_logger
from src.error.error_handlers import register_error_handlers
from src.middlewares.exception_middleware import ExceptionMiddleware
from src.routers import user_router, transaction_router

setup_logging()
logger = get_logger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(ExceptionMiddleware)

register_error_handlers(app)

app.include_router(user_router.router, prefix="/user", tags=["Users"])
app.include_router(transaction_router.router, prefix="/transactions", tags=["Transactions"])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
