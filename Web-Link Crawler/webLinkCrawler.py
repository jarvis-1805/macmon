import re
import sys
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from http.client import InvalidURL

def read_page(websiteName):
    # requesting the webpage to get the html page
    fp = urlopen(websiteName)
    _bytes = fp.read()

    # decode the page into readable formate, i.e., utf-8
    html = _bytes.decode("utf8")
    fp.close()

    return html


def extract_links(html):
    # RE to match the links in the page
    links = re.findall(r"\"(http://[^\"]*|https://[^\"]*)\"", html)

    return links


def check_status(links):
    print("\nThe links in the web page", sys.argv[1], " with their status:")
    print("-"*99, "\n")
    for link in links:
        print('[+]', link)
        try:
            status = urlopen(link).getcode()
            print(' -', status, 'OK')
        except HTTPError as err:
            print(' -', err)
        except URLError as err:
            print(' -', err)
        except InvalidURL as err:
            print(' -', err)


def main():
    websiteName = sys.argv[1]
    html = read_page(websiteName)
    links = extract_links(html)
    check_status(links)


if __name__ == "__main__":
    main()
