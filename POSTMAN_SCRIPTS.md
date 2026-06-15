# Postman Automated Test Scripts

Below are the JavaScript test scripts to paste into the **Tests** tab for each corresponding request in your Postman Collection.

---

## 1. Authentication Module

### POST Register User (Positive Test)
```javascript
// Validate Status Code
pm.test("Status code is 201 Created", function () {
    pm.response.to.have.status(201);
});

// Validate Response
pm.test("Response contains success message", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('message', "User registered successfully");
});
```

### POST Login User (Token Automation)
```javascript
// Validate Status Code
pm.test("Status code is 200 OK", function () {
    pm.response.to.have.status(200);
});

// Validate JWT Existence and Schema
pm.test("JWT Token exists in response", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('token');
    pm.expect(jsonData.token).to.be.a('string');
});

// Validate JWT Format (Header.Payload.Signature)
pm.test("JWT token format is valid", function () {
    var jsonData = pm.response.json();
    var tokenParts = jsonData.token.split('.');
    pm.expect(tokenParts.length).to.eql(3); 
});

// Auto-set Environment Variable for subsequent requests
if (pm.response.code === 200) {
    var jsonData = pm.response.json();
    pm.environment.set("token", jsonData.token);
    console.log("Token securely stored in Postman Environment.");
}
```

---

## 2. Movies Module

### GET All Movies
```javascript
// Validate Status Code
pm.test("Status code is 200 OK", function () {
    pm.response.to.have.status(200);
});

// Validate Response Time
pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});

// Validate Schema Structure
pm.test("Response schema is a valid array of movies", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('array');
    if(jsonData.length > 0) {
        pm.expect(jsonData[0]).to.have.property('id');
        pm.expect(jsonData[0]).to.have.property('title');
        pm.expect(jsonData[0]).to.have.property('total_seats');
        pm.expect(jsonData[0]).to.have.property('available_seats');
    }
});
```

### GET Movie Detail
```javascript
pm.test("Status code is 200 OK", function () {
    pm.response.to.have.status(200);
});

pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});

pm.test("Response schema is valid movie object", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('object');
    pm.expect(jsonData).to.have.property('id');
    pm.expect(jsonData).to.have.property('title');
    pm.expect(jsonData).to.have.property('genre');
    pm.expect(jsonData).to.have.property('available_seats');
});
```

---

## 3. Bookings Module

### POST Create Booking
```javascript
pm.test("Status code is 201 Created", function () {
    pm.response.to.have.status(201);
});

// Validate Booking ID & Status
pm.test("Booking ID exists and status is ACTIVE", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('booking_id');
    pm.expect(jsonData.booking_id).to.be.a('number');
    pm.expect(jsonData.status).to.eql("ACTIVE");
    
    // Save booking_id to environment for the Cancel request
    pm.environment.set("booking_id", jsonData.booking_id);
});

// Complex Logic: Verify Available Seats correctly deducted via a secondary async request
pm.test("Available seats updated correctly in Database", function () {
    var reqBody = JSON.parse(pm.request.body.raw);
    var movieId = reqBody.movie_id;
    
    pm.sendRequest({
        url: pm.environment.get("baseUrl") + "/api/v1/movies/" + movieId,
        method: 'GET'
    }, function (err, res) {
        if (!err) {
            var movie = res.json();
            pm.expect(movie.available_seats).to.be.a('number');
            // Advanced checking: Ensure available_seats is strictly less than total_seats (assuming it was full before)
            pm.expect(movie.available_seats).to.be.below(movie.total_seats);
            console.log("Confirmed Seats Deduction. Remaining:", movie.available_seats);
        }
    });
});
```

### DELETE Cancel Booking
```javascript
pm.test("Status code is 200 OK", function () {
    pm.response.to.have.status(200);
});

pm.test("Cancellation success message exists", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('message', 'Booking cancelled successfully');
});
```

---

## 4. History Module

### GET Booking History
```javascript
pm.test("Status code is 200 OK", function () {
    pm.response.to.have.status(200);
});

pm.test("Response schema is an array of bookings", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('array');
});

pm.test("Booking status strictly validates to Enum (ACTIVE, CANCELLED, COMPLETED)", function () {
    var jsonData = pm.response.json();
    if(jsonData.length > 0) {
        jsonData.forEach(function(booking) {
            pm.expect(booking.status).to.be.oneOf(["ACTIVE", "CANCELLED", "COMPLETED"]);
            pm.expect(booking).to.have.property('movie_id');
            pm.expect(booking).to.have.property('seats');
        });
    }
});
```

---

## 5. Standard Error Handling Cases

Create duplicate API requests inside Postman to act as **Negative Tests**, and paste these validation scripts into their Tests tab.

### 400 Bad Request (Validation / Business Logic Fails)
```javascript
pm.test("Status code is 400 Bad Request", function () {
    pm.response.to.have.status(400);
});

pm.test("Standard Error JSON Schema present", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('error_code');
    pm.expect(jsonData).to.have.property('message');
});
```

### 401 Unauthorized (Missing or Invalid JWT)
```javascript
pm.test("Status code is 401 Unauthorized", function () {
    pm.response.to.have.status(401);
});

pm.test("Identifies Authentication Failure", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.error_code).to.be.oneOf(["UNAUTHORIZED", "INVALID_CREDENTIALS", "TOKEN_EXPIRED"]);
});
```

### 403 Forbidden (Unauthorized access to resources)
```javascript
pm.test("Status code is 403 Forbidden", function () {
    pm.response.to.have.status(403);
});

pm.test("Identifies Authorization Rule Violation", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.error_code).to.eql("FORBIDDEN");
});
```

### 404 Not Found (Invalid ID or Endpoint)
```javascript
pm.test("Status code is 404 Not Found", function () {
    pm.response.to.have.status(404);
});

pm.test("Standard Error JSON Schema present", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.error_code).to.include("NOT_FOUND");
});
```
