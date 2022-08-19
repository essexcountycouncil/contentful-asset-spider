# Essex County Council Asset Spider

This is a one-off project to spider essex.gov.uk and find all files hosted on the contentful asset CDN that are in use, to aid in migration.

## Running

There are two options for running this programme. They will both output CSV and JSON documents to the output directory.

N.B.: These files are appended to, so if you'd like to re-run the spider then delete these files if present.

### Docker

There is a Docker environment available. Ensure you have docker installed (note, the Docker Desktop application requires a paid licence in many situations). Then, start the spider using:

    docker compose up

This will configure the spider then run it, outputting status to the screen.

N.B.: The docker container will contain the spider code, so this isn't well suited for development of spider changes. You'll need to run `docker compose build` to refresh the build each time.

### Python

Ensure you have Python 3.9 installed, as well as pipenv. Then run the following:

    pipenv install
    pipenv run scrapy runspider scraper.py -o ./output/output.json -o ./output/output.csv
