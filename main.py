from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


continuosIntegrationTools = {

    1:{

        "title": "Continuos Integration - V2",
        "relevanceLevel":1,
        "description": "Automate test and builds to increase efficiency."

    },



    2: {
        "title": "Continuous Delivery - V2",
        "relevanceLevel":2,
        "description":"Implement automated deliveries with security and speed."

    },

    3: {
        "title": "Monitoring - V2",
        "relevanceLevel":3,
        "description":"Ensure high availability and performance of your applications."

    }

}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}


@app.get("/continuosintegration")
async def getIntegration():
    return continuosIntegrationTools


@app.get("/continuosintegration/{tool_id}")
async def get_integration_by_id(tool_id: int):
    tool = continuosIntegrationTools.get(tool_id)
    if not tool:
        return {"error": "Tool not found"}
    return tool

