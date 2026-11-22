from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError, ExpiredSignatureError
from dependencies.logger import user_data_logger

# HTTPBearer instance — used as a dependency to enforce Bearer token auth on routes.
# This means that any route that includes this dependency will require a valid Bearer token in the 
# Authorization header of the request.
# This doesn't implement the actual token validation logic; 
# it simply checks for the presence of a Bearer token.
oauth2_scheme = HTTPBearer(bearerFormat="Token for User Data Services")

# List of authorized users for demonstration purposes. 
# In a real application, you would typically check against a database or an 
# external authentication service. 
authorized_users = ["Shivam Pahariya", "Sample1", "Sample2"]


# The oauth2_scheme can be used as a dependency in FastAPI routes to enforce authentication.
# Now we create the authentication dependency function that will be used in the routes to 
# validate the token. 

def authenticate_user(token: str = Depends(oauth2_scheme)):
    """
    Dependency function to authenticate a user based on the provided Bearer token.

    Args:
        token (str): The Bearer token extracted from the Authorization header.

    Returns:
        str: The token if authentication is successful.

    Raises:
        HTTPException: If the token is invalid or missing.
    """
    # Here you would implement your actual token validation logic.
    # First, we check if the token is present and valid. 
    # We will decode the jwt token and verify its signature, expiration, and claims.
    if not token:
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    # If the token is present, we can decode it and verify its validity.
    # get encoded token from the token object and decode it to a string
    encode_token = token.credentials.encode("utf-8")
    # Decode the token and also verify the signature and expiration.
    # Algorithm used for encoding the token is HS256, and the secret key is "samplesecretkey_fordemo_usingthiskeyforAuth".
    try:
        decode_token = jwt.decode(encode_token, "samplesecretkey_fordemo_usingthiskeyforAuth", algorithms=["HS256"])
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    username = decode_token.get("name")
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token: missing username claim")
    user_data_logger.info(f"Request from user: {username}")

    # Now we need to see if the user is authorized to access the requested resource.
    # In real applications, this would typically involve checking 
    # the user's roles or permissions against the requested resource.
    # Azure AD, Okta, or other identity providers can be used for this purpose.
    # Azure Graph API are popular choices for managing user roles 
    # and permissions in enterprise applications.
    if username not in authorized_users:
        raise HTTPException(status_code=403, detail="User not authorized to access this resource")
    
    return token.credentials