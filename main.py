from fastapi import FastAPI, Request
from pydantic import BaseModel
import httpx

app = FastAPI()

class IntentRequest(BaseModel):
    intentText: str
    width: int = 800
    height: int = 600

@app.post("/generate-chart")
async def generate_chart(request: IntentRequest):
    # Simulate parsing intentText
    chart_type = "bar" if "attendance" in request.intentText.lower() else "pie"
    filters = {"region": "North", "date_range": "2023-Q1"}
    legend = ["Category A", "Category B", "Category C"]

    # Simulate chart config
    chart_config = {
        "type": chart_type,
        "filters": filters,
        "legend": legend,
        "width": request.width,
        "height": request.height
    }

    # Send chart config to charting service
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8000/render-chart", json=chart_config)

    return {"chart": response.json()}
