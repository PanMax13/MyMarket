from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from core.config.database import init_db, close_db
from api.v1.auth import auth_router
from api.v1.catalog import catalog_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting up MyMarket API...")
    await init_db()
    print("Database initialized!")
    
    yield
    
    # Shutdown
    print("Shutting down MyMarket API...")
    await close_db()
    print("Database connections closed!")


app = FastAPI(
    title="MyMarket API",
    description="API for MyMarket e-commerce platform",
    version="1.0.0",
    lifespan=lifespan
)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(catalog_router, prefix="/catalog", tags=["Catalog"])


@app.get("/")
async def root():
    return {"message": "Welcome to MyMarket API!"}


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "MyMarket API"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    ) 