# Stages


1. Inspired by Majestic API crawling. Wondered could I build my own rudimentary
web crawler bot. 
Majestic API - 4 billion URLs/day
	       approx. 46,296 per Second


## EXTRA CHALLENGE : Using no APIs or Cloud Services

###Build your own Crawler. How hard can it be??!


2. Created basic Python web crawler bot for Malicious Compliance subReddit
to run on Raspberry Pi. Automated with cron to run twice every hour


	PROBLEM: As signal is constantly originating from the same location,
		Reddit blocked the bot from receiving input fairly quickly.


3. CLOUD: Selenium, Docker  

"Improved performance, NOT Efficiency

PROBLEM: most specialist Selenium code found online is written in Java

SOLUTION: DuckDuckGo API content fed into Scrapy and Algoria (Compatibility issues between urllib2 and urllib3) Then the fact urllib no longer exists due to security issues
Did Not work. Had to rewrite a lot of DuckDuckGo's API. Lot of work. No yield

4. CLOUD: CommonCrawl and Beautiful Soup to scrape Google Search Results for the Word 'Spartan'. FAILED DUE TO MODULE Compatibility Issues AND LACK OF KNOWLEDGE.
