version 0.0.1
# Django web service skeleton - Nginx ready container

This is a web servie skeleton based on Django. 
Nginx server is included and ready to deploy in a container. Suggest to use this skeletion while developing front-end internet facing web services.

## Development

### Add python package

To add python package, add the package name into /app/requirements.txt

### Before running local server

Need to perform a data migration first as following.
 
* `python3 manage.py makemigrations`
* `python3 manage.py migrate --run-syncd`


## Production

### Build image

This step requires sudo. Suggest sign in as super user using 'su'.

Build image:
* `docker build -t <image_name> .`

### Run image

* `docker run --rm -d -p 4000:80 <image_name>`

Note:
	 - d: detach (run contianer in the background)
	 - p: map outside port: insider port
	--rm: remove the container upon exit

### Push to docker for deployment

#### Tag the image

* `docker tag SOURCE_IMAGE[:TAG] account/repository:tag`
Current default format for this project: 
* `docker tag SOURCE_IMAGE[:TAG] mcgong/service_name:version`

#### Login using docker credentials
* `docker login`

#### Push to docker
* `docker push account/repository:tag`
Current default format for this project: 
* `docker push mcgong/service_name:version`

#### Notify the maintainer through slack
Notify the maintainer at the SmileyApp backend team on Slack.
Need to mention: 
	1. service_name
	2. version
	3. commit message

## Debug

Bash into container to check files
* `docker run -ti -p 4000:80 <image_name> bash`

