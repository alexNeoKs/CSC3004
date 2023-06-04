kubectl delete ingress    flask-ingress
kubectl delete secret     chatserver-tls
kubectl delete service    flask-service
kubectl delete deployment flask-app
minikube stop