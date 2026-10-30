from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from models.user_data_models import GetUserDataRequest , UserData
from dependencies.logger import user_data_logger

# We have __init__ method in each folder to make it a package. 
# This allows us to import modules from the folder as a package.
# Otherwise, we would have to use relative imports which can be less clear and harder to manage.


# Create a router for user data endpoints

# Create an APIRouter instance for user data endpoints.
# prefix: The prefix for all routes in this router will be "/user-data".
# responses: A dictionary defining custom responses for specific HTTP status codes (e.g., 404 Not Found).
router = APIRouter(
    prefix="/user-data",
    tags=["User Data"]
)

user_data_logger.info("User Data Router initialized")

def get_user_data(payload: GetUserDataRequest):
    """
    Endpoint to retrieve user data based on the provided user ID.

    Args:
        GetUserDataRequest (GetUserDataRequest): The request body containing the user ID.

    Returns:
        JSONResponse: A JSON response containing the user data or an error message.
    """

    user_data_logger.info(f"Received request to fetch user data for user_id: {payload.user_id}")

    # In a real application, you would replace this with actual database queries or API calls.
    user_data = {
        "user_id": payload.user_id,
        "name": "Shivam Pahariya",
        "email": "shivam.pahariya@example.com",
        "age": 25,
        "address": "Karnataka, India"
    }

    # Check if the user ID is valid (for demonstration purposes, we assume user_id > 0 is valid)
    if payload.user_id > 0:
        user_data_logger.info(f"Successfully fetched user data for user_id: {payload.user_id}")
        return JSONResponse(content=user_data, status_code=200)
    else:
        user_data_logger.error(f"Invalid user_id: {payload.user_id}. User not found.")
        raise HTTPException(status_code=404, detail="User Not Found or Invalid User ID")


# You can add  @app.post("/user-data") decorators to define the HTTP method for this endpoint.
# Or use router.add_api_route("/user-data", get_user_data, methods=["POST"]) to add the route to the router.


router.add_api_route("/get-user-data", get_user_data, methods=["POST"])