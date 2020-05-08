# RESTful API in a Docker container
This application is a RESTful API in a docker container that returns the names of NBA teams

# How to run the application

1. Install [Docker](https://docker.com/).

2. Pull the image from docker hub by entering the following command: <br/>
`docker pull docker pull wz16874n/firstimage:latest`

3. To run the docker container enter the following command: <br/>
`docker run -d -p 5000:5000 wz16874n/firstimage:latest`

4. Open a browser and enter `http://localhost:5000/` or `http://localhost:5000/allteams` to view all teams. 

5. To view a team by id enter `http://localhost:5000/allteams + id` <br/>
Id numbers range from 0-29

6. To view a team by their division enter `http://localhost:5000/allteams/ + division` <br/>
Divisions include **Atlantic**, **Central**, **Southeast**, **Pacific**, **Southwest**, and **Nothwest** <br/>
Note: First letter must be uppercase

7. To view a team by their division and id enter `http://localhost:5000/allteams/ + division /+ id`
