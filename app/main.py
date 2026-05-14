from app import models
from fastapi import FastAPI
from app.database import Base,engine
from app.routers import audits,attendance,auth,blogs,campaigns,meetings,payments,pledges,users

app = FastAPI(
        title="Family Website API",
        description="Family contribution and management system",
        version="1.0.0"
)

Base.metadata.create_all(bind = engine)

#Routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(pledges.router)
app.include_router(payments.router)
app.include_router(meetings.router)
app.include_router(campaigns.router)
app.include_router(blogs.router)
app.include_router(audits.router)
app.include_router(attendance.router)

@app.get("/")
def home():
    return {"Message" : "Family api running successfully"}