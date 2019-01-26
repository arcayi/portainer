FROM portainer/portainer:latest
MAINTAINER Haixin Lee <docker@lihaixin.name>
# ADD favicon.ico /ico
ENTRYPOINT ["/portainer","--templates","https://raw.githubusercontent.com/arcayi/portainer/master/templates.json"]
