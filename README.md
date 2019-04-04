# Micro Test

Test micriservices on a kubernetes cluster.


## Build Container

Simple rest container, using python3 hug module to implement some limited functionallity. 

    [x] API Versions
    [x] Service Versions
    [x] Uptime


Python file [docker/service.py](docker/service.py)  
[Dockerfile](docker/Dockerfile) for building the container image, builds on a Python3 image.

## Build locally for testing


```
docker build -t micro-test:3.2 -t micro-test:latest .
docker image ls
```

### Run Container in Docker
Start the container
```
docker run -p 8000:8000 micro-test
```

Connect to : [http://localhost:8000/v2/version](http://localhost:8000/v2/version)


## Deploy Container to minikube from local repository

It is possible to store the container image in the local minikube registry.
```
minikube ssh
docker images
```

Build docker image and store it in minicubes registry
```
eval $(minikube docker-env)
docker build -t micro-test:3.2 -t micro-test:latest .
```


It is possible to run it like this, but it's better to do a Deployment as described below.
```
kubectl run --image=micro-test:latest micro-test-app --port=8000 --image-pull-policy=Never
```


### Deploy Container

The file [deployment-update.yaml](docker/deployment-update.yaml) specifies the deployment.
```
kubectl apply -f deployment-update.yaml
kubectl describe deployment micro-test-app
```

Expose Container so we can connect to it.
```
kubectl expose deployment micro-test-app --type=LoadBalancer --port=8000 --target-port=8000
```

Add routing to the service
```
kubectl describe service micro-test-app
Name:                     micro-test-app
Namespace:                jenkins
Labels:                   run=micro-test-app
Annotations:              <none>
Selector:                 run=micro-test-app
Type:                     LoadBalancer
IP:                       10.106.54.189
Port:                     <unset>  8000/TCP
TargetPort:               8000/TCP
NodePort:                 <unset>  30770/TCP
Endpoints:                172.17.0.10:8000,172.17.0.11:8000,172.17.0.12:8000 + 7 more...
Session Affinity:         None
External Traffic Policy:  Cluster
Events:                   <none>
```

via the minikube ip :
```
sudo ip route add 10.106.54.0/24 via $(minikube ip)
```

Then connect to the micro service :

[http://10.96.252.238:8000/v2/version](http://10.96.252.238:8000/v2/version)



### Rolling Upgrade

Update service.py route /version to version 3.4
```
docker build -t micro-test:3.4 -t micro-test:latest .
```

Verify that the new image is visable in the minikube container repository
```
minicube ssh
docker images
```

Update the [deployment-update.yaml](docker/deployment-update.yaml) with the new version number.
```
kubectl apply -f deployment-update.yaml
```

Then connect to the micro service :

   [http://10.96.252.238:8000/v2/version](http://10.96.252.238:8000/v2/version)  
   [http://10.96.252.238:8000/v2/uptime](http://10.96.252.238:8000/v2/uptime)



### Referenses

[Running Local Docker Images in Kubernetes](https://blogmilind.wordpress.com/2018/01/30/running-local-docker-images-in-kubernetes/)


