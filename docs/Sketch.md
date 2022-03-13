Web Scraping SKETCH

## Search engine
For search engine scrapers, there are:
    [Bing, Google, Yahoo, DuckDuckGo]

    Few problems I can think of:
        1. Most of the top images, scraped, are the same images
        2. Sometimes, one of the search engine will scrape farther,
            more images. But it's inconsistent
        3. So that's why I still scrape with multiple search engines

    Bing points:
        1. Can scrape high resolution images, but can't
            scrape a lot of those high resolution images
        2. Is the generally the best choice, when you one want to
            use one search engine
    Google:
        1. Inconsistently scrape high resolution images,
            but I think will return a larger number of
            unique images
        2. Will repeat a lot of images
    Yahoo:
        1. I think if you just want consistent images,
            use this search engine
    DuckDuckGo:
        1. Don't remember


## Medsos -> Instagram
For medsos, instagram, it's finnicky to try to,
    directly scrape from the page.
    Instagram knows that the browser is headless &
    uses selenium.

    So for this problem, we used 3rd party instagram sites
        But that also isn't reliable. Sometimes it's possible
        to get some image, sometimes can't get any at all
    
    It's mostly better than just going straight to instagram,
        But, still, doesn't solve the problem.
        