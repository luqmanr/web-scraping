'''
main.py
   |_ search_engines:
        |_ bing.py      -> BingScraperObj(chromedriver, keywords, options:{save_path})
        |_ google.py    -> GoogleScraperObj(chromedriver, keywords, options:{save_path})
        |_ yahoo.py     -> YahooScraperObj(chromedriver, keywords, options:{save_path})
                ScraperObj() will have:
                    |_ .scrape(keyword)          returns-> []image
                    |_ .save(image, save_path)   returns-> status,err
                    |_ .display(screen, xserver) returns-> status,err

 
'''