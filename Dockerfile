FROM python:3.9

RUN python -m pip install pipenv
COPY . /app
RUN mkdir /out
WORKDIR /app
RUN pipenv install
CMD pipenv run scrapy runspider scraper.py -o /out/output.json -o /out/output.csv