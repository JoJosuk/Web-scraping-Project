# Price Comparison using Web Scraping 



## Introduction

This is repo is for our mini project, Price Comparison using Web Scraping. Its a
software which allows users to gain data on a specific product from over
multiple e-commerce websites.



## Implementation

This project scrapes data from e-commerce website and extracts prices,product 
names,... from it and compiles it into datasets for further processing and 
analysis.

The project makes use of the following tools or technology

+ ### Python Requests Library 

    Requests is an elegant and simple HTTP library for Python. It takes in the 
website page of the specified product and returns the html file.

+ ### Beautiful Soup

    Beautiful Soup is a Python library for pulling data out of HTML and XML 
    files. The html file returned by request library is passes through the BS 
    object and the required data is extracted from the HTML using BS. The class
    names and known and certain tags without class names are accessed by 
    indexing tag.

## Docker Image + Running Container

Create the docker image by running the following command at the the root directory of the project.

```
docker build -t fashion_scraper .
```

Run the following command to start the container 

```
docker run --name web -p 8000:8000 fashion_scraper
```

The container will now be runnign on port 8000
Visit http://localhost:8080/ to view the application

Stop the container by running

```
docker stop web

docker container prune -f
```