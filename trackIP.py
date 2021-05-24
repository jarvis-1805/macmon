import requests
#import argparse
import json

def IPtrack(ip):
    #parser = argparse.ArgumentParser()
    #parser.add_argument('-i', '--ipaddress', help='IP address to track')
    #args = parser.parse_args()
    #ip = args.ipaddress
    url = "http://ip-api.com/json/" + ip      # http://ip-api/json/192.168.0.1
    response = requests.get(url)
    data = json.loads(response.content)

    print("[+] IP\t\t\t", data["query"])
    print("[+] CITY\t\t", data["city"])
    print("[+] ISP\t\t\t", data["isp"])
    print("[+] AS\t\t\t", data["as"])
    print("[+] LOC\t\t\t", data["country"])
    print("[+] REG\t\t\t", data["regionName"])
    print("[+] TIME\t\t", data["timezone"])
    print("[+] ZIP\t\t\t", data["zip"])
    print("[+] LAT\t\t\t", data["lat"])
    print("[+] LON\t\t\t", data["lon"])