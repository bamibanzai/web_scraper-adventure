from bs4 import BeautifulSoup
import requests
import json
import io
import gzip
import csv
import codecs
# import argparse

#COMMON CRAWL


# # parse the command line arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-d", "--domain", required=True, help="The domain to target ")
# args = vars(ap.parse_args())

# domain = args['domain'] #if making to search through different domains on each run
domain = "https://bit.ly/2T47UJi" #Google Search for the word Spartan compacted using Bitly API
# list of available indices
index_list = ["2015-35", "2016-07", "2015-48", "2015-22", "2015-18", "2015-32", "2015-27"]

# Searches the Common Crawl Index for a domain.


def search_domain(domain):
    record_list = []
    print("[*] Trying target domain: %s" % domain)

    for index in index_list:
        print("[*] Trying index %s" % index)

        cc_url = "http://index.commoncrawl.org/CC-MAIN-%s-index?" % index #iterating through all available indices for the URL
        cc_url += "url=%s&matchType=domain&output=json" % domain

        response = requests.get(cc_url)
        if response.status_code == 200:
            records = response.content.splitlines()
            for record in records:
                record_list.append(json.loads(record))
            print("[*] Added %d results." % len(records))

    print("[*] Found a total of %d hits." % len(record_list))

    return record_list


def download_page(record):
    offset, length = int(record['offset']), int(record['length'])
    offset_end = offset + length - 1

    prefix = 'https://aws-publicdatasets.s3.amazonaws.com/' #Fetch file from AWS server

    # We can then use the Range header to ask for just this set of bytes
    resp = requests.get(prefix + record['filename'], headers={'Range': 'bytes={}-{}'.format(offset, offset_end)})

    # The page is stored compressed (gzip) to save space
    # We can extract it using the GZIP library
    raw_data = io.StringIO(resp.content)
    f = gzip.GzipFile(fileobj=raw_data)

    # What we have now is just the WARC , formatted:
    data = f.read()
    response = ""

    if len(data):
        try:
            warc, header, response = data.strip().split('\r\n\r\n', 2)
        except:
            pass

    return response


record_list = search_domain(domain)
link_list = []


def extract_external_links(html_content, link_list):
    parser = BeautifulSoup(html_content)

    links = parser.find_all("a")

    if links:
        for link in links:
            href = link.attrs.get("href")

            if href is not None:

                if domain not in href:
                    if href not in link_list and href.startswith("http"):
                        print("[*] Discovered external link: %s" % href)
                        link_list.append(href)

    return link_list


for record in record_list:
    html_content = download_page(record)

    print("[*] Retrieved %d bytes for %s" % (len(html_content), record['url']))

    link_list = extract_external_links(html_content, link_list)

print("[*] Total external links discovered: %d" % len(link_list))

with codecs.open("%s-links.csv" % domain, "wb", encoding="utf-8") as output:
    fields = ["URL"]

    logger = csv.DictWriter(output, fieldnames=fields)
    logger.writeheader()

    for link in link_list:
        logger.writerow({"URL": link})
