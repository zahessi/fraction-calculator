# Fraction calculator

Fraction calculator app with support of parenthesis.

- `GET /healthcheck` To make sure the app is works properly
- `POST /calc` returns the result of calculation in the format `{"equation": "$equation", "result": "$result"}
`. Might return 400 status code and response with error if the provided expresstion wasn't legal

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

You might need  `docker` in order to run project.

### Installing

Given you are in the root directory of project, firstly we build our image

```
docker build -t calc:latest .
```

And run it, binding to `8080` port

```
docker run -d -p 8080:5000 calc:latest
```
