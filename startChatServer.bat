minikube start

minikube addons enable ingress
START kubectl port-forward -n ingress-nginx service/ingress-nginx-controller 8080:80
START kubectl port-forward -n ingress-nginx service/ingress-nginx-controller  443:443

minikube image build -t chatserver .
minikube image ls

kubectl apply -f deployment.yaml
kubectl get deployment flask-app --output=wide

kubectl apply -f service.yaml
kubectl get service flask-service --output=wide


kubectl create secret tls self-tls --key server.key --cert server.crt
kubectl create secret generic ca-secret --from-file=ca.crt=ca.crt

kubectl get secret --output=wide

kubectl delete -A ValidatingWebhookConfiguration ingress-nginx-admission
kubectl apply -f ingress.yaml
kubectl get ingress flask-ingress --output=wide

START minikube tunnel
START curl -v --cacert ca.crt --key client.key --cert client.crt https://chatserver.com/