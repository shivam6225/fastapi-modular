from fastapi import FastAPI , HTTPException

from routers import user_data_router

# Add a description for the Service
description = """
This is a simple FastAPI service that provides an endpoint to display user data.
You can use this service to retrieve user information based on the provided user ID.
"""

# Create a FastAPI instance with metadata
app = FastAPI(
    title="User Data Service",
    description=description,
    version="1.0.0",
    contact={
        "name": "Shivam Pahariya",
        "email": "shivam.email@example.com"
    }
)

app.include_router(user_data_router.router)  # Include the user data router in the FastAPI application

# First create an endpoint for health check
@app.get("/health", tags=["Health Check"])
async def health_check():
    """
    Health check endpoint to verify if the service is running.
    Returns a simple message indicating the service status.
    """
    return {"status": "Service is running"}

#To run the service using uvicorn, use the command: uvicorn src.main:app --reload
#This command will start the FastAPI service and enable hot-reloading for development purposes.
#This runs the service on 8000 port by default. You can access the service at http://localhost:8000
#Stop the service by pressing Ctrl+C in the terminal where the command is running.

if __name__ == "__main__":

    import uvicorn
    # Run the FastAPI service using uvicorn with the specified host and port
    # Run the service with python src.main.py command in the terminal
    uvicorn.run("main:app", 
                host="0.0.0.0", 
                port=8000, 
                )

