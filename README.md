## Simple Web Application developed in Flask with Colorful background 

* name: app-webcolor
* port: 9000

Supported colors/tags:
* v1 - blue
* v2 - red
* v3 - green
* v4 - pink
* v5 - yellow
* v6 - orange
* v7 - darkblue

### Deploy:
```
kubectl apply -f https://raw.githubusercontent.com/wiktorvip/app-webcolor/main/manifests/Deployment.yaml
kubectl apply -f https://raw.githubusercontent.com/wiktorvip/app-webcolor/main/manifests/Service.yaml
```
