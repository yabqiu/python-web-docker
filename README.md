## python-web test docker image

### start a web server on default port 80
```
docker run -d -p8080:80 yanbin/python-web
```

### start a web server on custom port
```
docker run -d -e HTTP_PORT=8080 -p8080:8080 yanbin/python-web
```
