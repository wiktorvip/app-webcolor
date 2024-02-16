## Simple Web Application developed in Flask with Colorful background 

* name: app-webcolor
* port: 9000

Supported colors/tags:
* v1 - blue
* v2 - green
* v3 - red
* v4 - pink
* v5 - yellow
* v6 - orange
* v7 - darkblue
* v8 - dark

### Deploy:
```
kubectl apply -f https://raw.githubusercontent.com/wiktorvip/app-webcolor/main/manifests/Deployment.yaml
kubectl apply -f https://raw.githubusercontent.com/wiktorvip/app-webcolor/main/manifests/Service.yaml
```

### Helm 
```
helm repo add app-webcolor https://wiktorvip.github.io/app-webcolor
helm repo update
helm search repo helm-charts
helm install app-webcolor app-webcolor/app-webcolor
```