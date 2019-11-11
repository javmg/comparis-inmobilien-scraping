# comparis-inmobilien-scraping

## Author

javmg - Javier Moreno Garcia

## Introduction

This project contains a <strong>simple scrapper for properties</strong> in the [comparis site](https://en.comparis.ch/immobilien/default).

The idea's initially to pull information for rentals in the postcode 1110 but this can be configured in the script.

The URL requested is not excluded in the [robots configuration file](https://en.comparis.ch/robots.txt) and we're abiding by the rules. 

We're pulling up to 20 pages and we're using a back-off of 5 seconds for each request.  


## Implementation

The scrapper is comprised of the following parts:

- propery_main.py: it's where the <strong>main</strong> of the application resides and it contains default parameters like the maximum number of pages to navigate or the backoff in seconds after each request.
- propery_reader.py: this file contains an implementation to <strong>pull a certain number of properties</strong> from Comparis.
- propery_writer.py: this file contains the functionality to <strong>write the properties</strong> into a csv file.


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

It will be formatted in csv and will contain the following fields:

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