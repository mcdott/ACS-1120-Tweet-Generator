# Alice in Jabberland Tweet Generator

## Steps to run app in Docker container:

### 1. Build the Image

```bash
docker build -t flask-image .
```

### 2. Run the Container

```bash
docker run -p 5003:5000 --rm --name flask-container flask-image
```

### 3. Access via Browser

http://localhost:5003

## Steps to run app with Docker compose:

### 1. Start Docker container

```bash
docker-compose up
```

### 2. Access via Browser

http://localhost:5005

### 3. Stop the Container

```bash
docker-compose down
```
