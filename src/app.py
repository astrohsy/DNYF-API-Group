from fastapi import FastAPI

from .routes import item, user

# models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(user.router)
app.include_router(item.router)
