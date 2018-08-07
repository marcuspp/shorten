# Url shortener

This is a technical exercise to create a Url shortner in python

- git, docker and docker-compose and all required to run the application

The project uses docker, django and the django rest framework to create a API where a url can be posted and a shortened one returned.
A redirect view can then decodes the shortened url and the request is redirected to the longer version.

## Installation instructions

The application will run on port 8000 by default. This can be changed in the docker-compose file if required. 

```
git clone git@github.com:marcuspp/shorten.git .
docker-compose up
```

## Usage

The django rest framework API browser is still enabled to ease with testing. So visting http://127.0.0.1:8000/shorten_url/ provides a nice page and form to post the url.

```
Home - http://127.0.0.1:8000/ - Very basic home page
About- http://127.0.0.1:8000/ - Very basic about page
Shorten Url - http://127.0.0.1:8000/shorten_url/ - Accepts a post of url to shorten
```

## Improvements
- Use nginx and uwsgi and not the development server
- Change storage engine from postgres to something like redis
- Add caching to the redirect view

## Scaling
To scale I would at very least implement the above improvements. However this microservice would be a good candiate to use AWS lambda and elasticache. Using lambda would take care of any scaling issues as long as the application was reworked correctly. Django and the rest framework would not be required as lots of what they bring would be handled by lambda and the API gateway.
