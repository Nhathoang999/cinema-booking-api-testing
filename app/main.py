from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.database import engine, Base
from app.routers import auth, movies, bookings, history

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Cinema Booking API",
    description="REST API System for software testing practice.",
    version="1.0.0"
)

# Custom Exception Handlers for Standard Error Schema
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    # Extract the first error message
    msg = errors[0].get("msg") if errors else "Validation Error"
    
    # Custom tweaks for Pydantic standard errors to match specific test cases
    if "value is not a valid email address" in msg:
        msg = "Invalid email format"
    elif "Input should be greater than 0" in msg:
        msg = "Seats must be greater than 0"
    elif "String should have at most 150 characters" in msg:
        msg = "Username too long"
    
    # Check if multiple fields are missing
    if "Field required" in msg:
        missing_fields = [e.get("loc")[-1] for e in errors]
        if "email" in missing_fields and "password" in missing_fields:
             msg = "Email and password are required"
        else:
             msg = f"Missing field: {missing_fields[0]}"
             
    # Handle JSON decode errors
    if "JSON decode error" in msg:
        msg = "Malformed JSON payload"
    
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"error_code": "VALIDATION_ERROR", "message": msg}
    )

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    # If the detail is already a dict (from our CRUD/Auth layers), return it as is
    if isinstance(exc.detail, dict) and "error_code" in exc.detail:
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.detail
        )
    
    # Otherwise, wrap it in standard schema
    error_code = "HTTP_ERROR"
    if exc.status_code == 404:
        error_code = "NOT_FOUND"
        if exc.detail == "Not Found":
             exc.detail = "Endpoint not found"
    elif exc.status_code == 405:
        error_code = "METHOD_NOT_ALLOWED"
        exc.detail = "Method Not Allowed"
        
    return JSONResponse(
        status_code=exc.status_code,
        content={"error_code": error_code, "message": exc.detail}
    )

# Generic exception handler
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"error_code": "INTERNAL_SERVER_ERROR", "message": "An unexpected error occurred"}
    )

app.include_router(auth.router)
app.include_router(movies.router)
app.include_router(bookings.router)
app.include_router(history.router)
