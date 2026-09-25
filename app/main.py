from fastapi import FastAPI

app = FastAPI(
    title="Task API",
    description="API REST para gerenciamento de tarefas.",
    version="1.0.0",
)

@app.get("/health")
def health():
    return {"status": "ok"}