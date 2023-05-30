# CSC3004

# KUBERNETES
# install minikube
# put minikube.exe into environment path
# in cmd (admin) type "minikube start"
# type "minikube dashboard" in cmd, this will open the dashboard
# in vs code terminal, type "minikube docker-env | Invoke-Expression"
# type "docker build -t chatserver ." to build the image
# type "minikube image ls" to check if image is inside
# type "kubectl apply -f deployment.yaml"(do it for the rest of the yaml files too)
# wait a few seconds and you should see it working in the dashboard
# to enable loadbalancing service, open another cmd in admin mode and type "minikube tunnel --cleanup" (must leave this running)
# more info here -> https://minikube.sigs.k8s.io/docs/start/
# loadbalancer -> https://minikube.sigs.k8s.io/docs/handbook/accessing/#using-minikube-tunnel