FROM portainer/portainer:latest
MAINTAINER arcayi
# ADD favicon.ico /ico
ENTRYPOINT ["/portainer","--templates","https://raw.githubusercontent.com/arcayi/portainer/master/templates.1.20.0.json"]


