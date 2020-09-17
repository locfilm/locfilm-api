# locfilm-api

[![Build Status](https://travis-ci.org/locfilm/locfilm-api.svg?branch=master)](https://travis-ci.org/locfilm/locfilm-api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Project to locate film locations. Check out the project's [documentation](https://www.notion.so/angelfa/Locations-2052b3766b714b6fb4cfccf24f7430cc).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

Create the following enviorment variable just afteear creating the database with the correct data
export DATABASE_URL=postgres://example_user:password@localhost:5432/example_database

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```
