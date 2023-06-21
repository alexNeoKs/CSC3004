minikube start

minikube addons enable ingress
START kubectl port-forward -n ingress-nginx service/ingress-nginx-controller 8080:80
START kubectl port-forward -n ingress-nginx service/ingress-nginx-controller  443:443

minikube image build -t chatserver ../app/
minikube image ls

kubectl apply -f ../kubernetes/deployment.yaml
kubectl get deployment flask-app --output=wide

kubectl apply -f ../kubernetes/service.yaml
kubectl get service flask-service --output=wide

kubectl create secret tls     self-tls  --key ../servercert/server.key --cert ../servercert/server.crt
kubectl create secret generic ca-secret --from-file=ca.crt=../cacert/ca.crt

kubectl get secret --output=wide
kubectl delete -A ValidatingWebhookConfiguration ingress-nginx-admission
kubectl apply -f ../kubernetes/ingress.yaml
kubectl get ingress flask-ingress --output=wide

START minikube tunnel
START curl -k -v --cacert ../cacert/ca.crt --key ../clientcert/client.key --cert ../clientcert/client.crt https://chatserver.com/