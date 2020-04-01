# Facebook Post Data Scraper
**Note** : this is just a small side project. this might not work 100% (also. it's no pretty code. sorry. i'm open for pull request)

## Requirements
- admin access to the page you want to scrape
- an application (just create a random one)
- access to the page you want to scrape
- an access token to do so:
  1. go to https://developers.facebook.com/tools/explorer/v2/
  2. click on `User or Page`
  3. select the page you want to scrape (you might need to request permissions again)
  4. copy the content of `Access Token` into a file called `page_access_token` in this folder

## Setup
 - get your Page ID
  - open your page on facebook
  - navigate to the about section
  - there should be an entry called `Page ID`. copy the value in the `data.py` file into the variable `page_id`

## Settings
- **Fields:**
 - fields are values which you can request from the posts themselves ([reference](https://developers.facebook.com/docs/graph-api/reference/v6.0/page/feed#readfields "reference"))
- **Metrics:**
 - metrics are values that you can request from the insights. at the moment, it only works with metrics that use the period: `lifetime` . this can be changed later ([reference](https://developers.facebook.com/docs/graph-api/reference/v6.0/insights#page-post-engagement "reference"))