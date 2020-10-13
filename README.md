# locfilm-api

[![Build Status](https://travis-ci.org/Locfilm/locfilm-api.svg?branch=master)](https://travis-ci.org/Locfilm/locfilm-api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Locfilm is a platform where audiovisual producers find locations to film.

locfilm tries to facilitate the search for spaces to film within Mexico and Colombia.

# Prerequisites

- [Docker](https://docs.docker.com/get-docker/)  
- [Docker Compose](https://docs.docker.com/compose/install/)  

# Local Development

Start the dev server for local development:
```bash
git clone https://github.com/locfilm/locfilm-api.git
cd locfilm-api
docker-compose build
docker-compose run --rm web python manage.py makemigrations
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

# Production
To run this project in production mode you have to modify variables in `production_variables.env`. In case that the variable
`DJANGO_CONFIGURATION` has the value `Local` you have to change it to `Production`.

It is necessary to add your credentials and the name of your bucket from [S3](https://aws.amazon.com/s3/?nc1=h_ls), to do that you should read their documentation.

# API Documentation

https://documenter.getpostman.com/view/12985173/TVRj6UXu


# About us
We are a group of developers that got togheter thanks to Platzi Master Program. This project is the result of weeks of hard work and learning. 

### 🧟‍♂️ 🧟‍♀️ 🤖 Authors 

* **Yeferson Guarin** - Back-end, DS. Col. [jeffaristi92](https://github.com/jeffaristi92)
* **Anfel Flores** - Back-end, DS. Mx. [AngelFA04](https://github.com/AngelFA04)
* **Gabril Ospina** - Back-end. Col. [Gabospa](https://github.com/Gabospa)
* **Camilo Romero** - Back-end. Col. [jromeroc](https://github.com/jromeroc)

* **Rodrigo Reyes** - Front-end, Designer. Mx. [RoiFuries](https://github.com/RoiFuries)
* **Cesar Pentes** - Front-end. Col. [cesarp04](https://github.com/cesarp04)



### ✒️ Coaches
* **Israel Yance** - Coach, Designer. Pe. [RoiFuries](https://github.com/israelyance)
* **Crisly Gonzalez** - Coach, CR. [cesarp04](https://github.com/CrislyGonzalez)



If you want to know about the insights [click here!](https://github.com/locfilm/locfilm-api/pulse)

### 🎁 Contribute

Feel free to contribute to the project!
