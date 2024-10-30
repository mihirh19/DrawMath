import uvicorn
from constants import SERVER_URL, PORT, ENV
if __name__ == "__main__":
    uvicorn.run("main:app", host=SERVER_URL, port=int(PORT), reload=(ENV == "dev"))