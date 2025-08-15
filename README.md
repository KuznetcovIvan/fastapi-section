docker run -d -p 6379:6379 --name redis -v /path/on/host:/data redis:latest
docker exec -it redis redis-cli
docker run -d -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=your_password postgres:latest