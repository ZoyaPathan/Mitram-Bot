from fastapi import FastAPI


app = FastAPI(
    title="MITRAM Bot Backend",
    description="Backend API for the MITRAM elderly care robot",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "MITRAM Bot Backend is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }