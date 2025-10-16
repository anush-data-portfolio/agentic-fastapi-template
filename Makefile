
.PHONY: build run test

# Build the Docker image
build:
	docker build -t fastapi-app .

# Run the Docker container
run:
	docker run -p 8000:8000 fastapi-app

