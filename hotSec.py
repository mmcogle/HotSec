import requests
import subprocess


def get_tweets():
    url = "https://api.twitter.com/1.1/search/tweets.json?q=%23infosec&result_type=popular"
    headers = {
            'Authorization':'Bearer AAAAAAAAAAAAAAAAAAAAALy8CAEAAAAAIQXreUYSiLupPYKU5mljoIneJM0%3Dx491a9pXymvlNzbjjSuXB2kaH8VUmEYywLURsDiCQzyiksmnSt',
            'user-agent':'advanced-rest-client',
            'accept':'*/*'
            }
    response = requests.get(url, headers=headers)
    response = response.json()
    print(response['statuses'][0]['text'])
    print("ugh")

if __name__=='__main__':
    get_tweets()

