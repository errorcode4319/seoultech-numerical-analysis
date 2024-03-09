# seoultech-numerical-analysis
Seoultech Numerical Analysis 


## Pre-Install Required 
- docker
- docker-compose


## Setup (using Container)
```
cd container-env

docker build -t py-env:0.1 .

# Startup
docker compose up -d

# Shutdown
docker compose down

# Logging
docker compose logs -f

# running on localhost:8888
```