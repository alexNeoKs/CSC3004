

kubectl  delete service    -A --all
kubectl  delete deployment -A --all
kubectl  delete replicaset -A --all
kubectl  delete pods       -A --all
kubectl  delete ingress    -A --all
kubectl  delete secret     -A --all
minikube image rm chatserver:latest
minikube delete               --all
minikube stop
