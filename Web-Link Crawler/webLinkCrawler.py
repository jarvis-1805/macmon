import re
import sys
import urllib.request

def read_page(websiteName):
    # requesting the webpage to get the html page
    fp = urllib.request.urlopen(websiteName)
    _bytes = fp.read()

    # decode the page into readable formate, i.e., utf-8
    html = _bytes.decode("utf8")
    fp.close()

    return html


def extract_links(html):
    # RE to match the links in the page
    links = re.findall(r"\"(http://[^\"]*|https://[^\"]*)\"", html)
    
    print("\nThe links in the web page", sys.argv[1], ":")
    print("--------------------------------------------------------------\n")
    for link in links:
        print('[+]', link)


def main():
    websiteName = sys.argv[1]
    html = read_page(websiteName)
    extract_links(html)


if __name__ == "__main__":
    main()
