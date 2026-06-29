# BUG-001: Movie Search is Case-Sensitive

**Status**: Closed  
**Severity**: Medium  
**Priority**: P2  

## Description
When a user searches for a movie using lowercase letters (e.g., "avengers"), the API returns a `404 Not Found` if the movie title is stored with capital letters in the database ("Avengers"). The Business Requirements explicitly state that search must be case-insensitive.

## Expected Behavior
`GET /api/v1/movies?title=avengers` should return the movie "Avengers".

## Actual Behavior
`GET /api/v1/movies?title=avengers` returns `404 Not Found`.

## Root Cause
The SQLAlchemy query in `app/crud.py` used exact matching (`Movie.title == search_term`) instead of case-insensitive matching (`Movie.title.ilike(f"%{search_term}%")`).

## Retest Result
- **Test Executed**: `pytest tests/test_movies.py -m regression`
- **Result**: PASS
- **Resolution**: Bug was fixed in branch `demo/bug-case-sensitive-search` and merged to `main`.
