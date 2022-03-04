import requests, argparse
from bs4 import BeautifulSoup

def getUrl(url):
    urls = []
    with open(url, "r") as ufile:
        allurl = ufile.readlines()
        for i in range(len(allurl)):
            urls.append(allurl[i].strip('\n'))
        return urls

parse = argparse.ArgumentParser()
parse.add_argument('-u', '--url', help='Input site(with http/https)')
parse.add_argument('-f', '--file', help='scanning hash in the file')
args = parse.parse_args()

def scan(url):
    data = {
	"url": url,
	"go": "Gaskan"
}
    #Makasih exploits.my.id untuk webnya
    base = 'http://v1.exploits.my.id:1337/?tools=wpplugins'
    r = requests.post(base, data=data)
    soup = BeautifulSoup(r.content, 'html.parser')
    result = soup.find('pre').text.replace('[+] Loading ... ( 1 sites )', '').replace('[+] Done ...', '')
    return result

if args.url:
    print(scan(args.url))
elif args.file:
    url = getUrl(args.file)
    for i in url:
        print('======================')
        print(scan(i))
else:
    print('Input argument')