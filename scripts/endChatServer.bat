docker rmi chatserver:latest
kubectl delete ingress    flask-ingress
kubectl delete secret     self-tls
kubectl delete secret     ca-secret
kubectl delete service    flask-service
kubectl delete deployment flask-app
minikube stop