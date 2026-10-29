from fastapi.middleware.cors import CORSMiddleware


# Middleware to handle CORS , rate limiting and other security features can be added here
# Add CORS middleware to allow cross-origin requests

def add_cors_middleware(app):
    """
    Add CORS middleware to the FastAPI application.
    You can customize the allowed origins, methods, and headers as needed.

    Args:
        app (FastAPI): The FastAPI application instance.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allow all origins for simplicity; adjust as needed
        allow_credentials=True,
        allow_methods=["*"],  # Allow all HTTP methods
        allow_headers=["*"],  # Allow all headers
    )
