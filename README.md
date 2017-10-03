Template docker app.

Requires docker to be installed.

Change the docker-compose.yml file to add or remove additional containers
Set secret env vars in the .env file which is not checked into source control.
Public env vars can be set directly in the environment section of the .yml file.
Env vars are read into the app in the config.py file.

Change exposed ports in the .yml file.
The shared folder is set in the Dockerfile and the volumes mounted in the .yml which enables automatic code reloading.

Start your app using ```docker-compose up``` or ```docker-compose up -d``` to run in the background.