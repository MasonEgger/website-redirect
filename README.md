# website-redirect [![Deploy to DO](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/masonegger/website-redirect/tree/main)

This simple Flask app allows you to perform a 301 redirect. You set the redirect
the location you want to redirect to in the `REDIRECT_TO` environment variable.

This app is Dockerized for deployment and can also be deployed on DigitalOcean's
[App Platform](https://docs.digitalocean.com/products/app-platform/) using the 
Deploy to DO Button above.


## Sample Use Cases
* I personally use this to power [discord.mason.dev](https://discord.mason.dev).
I wanted a permantely available link for my personal discord server and this allows
me to redirect the URL I want to the Discord invite link.
