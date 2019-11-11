# comparis-inmobilien-scraping

## Introduction

This project contains a simple scrapper for properties in the [comparis site](https://en.comparis.ch/immobilien/default).

The idea's initially to pull information for rentals in the postcode 1110 but this can be configured in the script.

The URL requested is not excluded in the [robots configuration file](https://en.comparis.ch/robots.txt) and we're abiding by the rules. 

We're paginating up to 20 pages and we're using a back-off of 5 seconds for each request.  

## Build

The project has the following external dependencies:
```
pip install urllib3
pip install beautifulsoup4
```

## Execution

The scrapper can be executed by running: 

```
python3 propery_main.py
```

## Outcome

The script will create a new file by the name of property-list.csv.

It will be formatted in csv and will contain the following fiedls:

- id
- title
- published_date
- address 
- category
- meters,
- floor
- rooms
- price

A sample file can be [looked up here](sample_property-list.csv).