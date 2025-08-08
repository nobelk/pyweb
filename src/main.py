import argparse
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


def main() -> None:
    parser = argparse.ArgumentParser(description="webservice")
    parser.add_argument("--port", type=int, default=8000, help="Default port")
    parser.add_argument("--workers", type=int, default=2, help="Number of workers")
    arg = parser.parse_args()
    uvicorn.run("src.main:app", host="0.0.0.0", port=arg.port, workers=arg.workers)


if __name__ == "__main__":
    main()
