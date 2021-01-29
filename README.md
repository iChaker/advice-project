Advice
=========
Advice is a simple application that provides powerful pieces of advice using the latest state of the art AI wisdom distillation algorithms.
This service was deployed using a Docker Swarm cluster and monitored with Grafana and Prometheus.


## Endpoints

| Path                                  | Type  | Description                                                      | 
|:--------------------------------------| :---: |:-----------------------------------------------------------------|
| /goodadvice                       |  GET  | Return a piece of good advice.|
| /badadvice                        |  GET  | Return a piece of bad advice.             | 
| /metrics                          |  GET  | Return the metrics provided by Prometheus.                        |      

## Deploy

1. Clone this repository <br>
`$ git clone https://github.com/iChaker/advice-project`
2. Change the current working directory <br>
`$ cd /advice-project`<br>
3. Create the docker image : server-image  <br>
`$ docker build -t server-image .`<br>
4. Initialize the swarm <br>
`$ docker swarm init`<br>
Don't forget to save the token.<br>
5. Deploy the stack to the swarm<br>
`$ docker stack deploy --compose-file docker-compose.yml  $SERVICE_NAME`<br>
6. Check that it’s running <br>
`$ docker stack services $SERVICE_NAME`<br>

```





