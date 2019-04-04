# Micro Test

Test micriservices on a kubernetes cluster.


## Build Container

Simple rest container, using python3 hug module to implement 

[ ] API Versions
[ ] Service Versions
[ ] Uptime


```
docker build -t micro-test:3.2 -t micro-test:latest .
```

```
docker image ls
```


Start the container

```
docker run -p 8000:8000 micro-test
```

Connect to : http://localhost:8000/v2/version


Store image in registry.

### Deploy Container from local repository

```
minikube ssh
docker images
```


```
eval $(minikube docker-env)
kubectl run --image=micro-test:latest micro-test-app --port=8000 --image-pull-policy=Never
```

Expose Container
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
```
http://10.106.54.189:8000/v2/uptime
```



Rolling Upgrade
```
docker build -t micro-test:v2 .

```




## Create Pod


### [Pull Local Image](https://stackoverflow.com/questions/40144138/pull-a-local-image-to-run-a-pod-in-kubernetes)

```
eval $(minikube docker-env)
```


```
minikube start --insecure-registry
```


### Persistent Storage

### Authentication

### Scaling
