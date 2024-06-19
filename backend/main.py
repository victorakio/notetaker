from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import users, tags, categories, notes, auth
from backend.database import Base, engine, SessionLocal
from backend.models import User, Note, Tag, Category, Note

# Initialize FastAPI application
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")
except Exception as e:
    print("An error occurred while creating tables:", e)

# Dependency for getting a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Run the application (not needed if running with an ASGI server like uvicorn)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

app.include_router(users.router)
app.include_router(tags.router)
app.include_router(categories.router)
app.include_router(notes.router)
app.include_router(auth.router)
