## The project on this branch explaines the use of docker networks 

## how to use 

```
git clone <repo>
```
```
docker build -t server-image ./server
```
```
docker build -t client-image ./client
```
## now create a custom network to create a bridge btween 2 containers 
```
docker network ls
```
```
docker network create custom-network -d bridge
```
## Now run the container
```
docker run -d -p 4000:4000 --network custom-network --name server server-image
```
```
docker run -d -p 5000:5000 --network custom-network client-image
```
## Check port 5000
```
http://localhost:5000/
```

## Done 
