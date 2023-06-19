minikube start
minikube addons enable ingress
minikube image build -t chatserver .
minikube image ls

kubectl apply -f deployment.yaml
kubectl get deployment flask-app --output=wide

kubectl apply -f service.yaml
kubectl get service flask-service --output=wide




kubectl apply -f secret.yaml

kubectl get secret chatserver-tls --output=wide
kubectl delete -A ValidatingWebhookConfiguration ingress-nginx-admission
kubectl apply -f ingress.yaml
kubectl get ingress flask-ingress --output=wide

minikube tunnel