import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from apps.calculator.route import router as calculator_router
from fastapi.middleware.cors import CORSMiddleware


from constants import SERVER_URL, PORT, ENV

@asynccontextmanager
async def lifespan(app: FastAPI):
   yield
   
app = FastAPI(lifespan=lifespan)


app.add_middleware(
   CORSMiddleware,
   allow_origins=["http://localhost:5173", "https://draw-math.vercel.app"],
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)

@app.get("/")
async def health():
   return {"message" : "server is running"}

app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])
if __name__ == "__main__":
    uvicorn.run("main:app", host=SERVER_URL, port=int(PORT), reload=(ENV == "dev"))