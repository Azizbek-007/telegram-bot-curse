import requests

def QQ_TO_UZ(text, til1, til2):
    url = "https://from-to.uz/api/v1/translate"
    header = {
    'Host': 'from-to.uz',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json;charset=utf-8',
    'Content-Length': '79',
    'Origin': 'https://www.from-to.uz',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Referer': 'https://www.from-to.uz/',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'trailers'}

    data = {
        "body":{
            "resultCase":"latin",
            "lang_from":f"{til1}",
            "lang_to":f"{til2}",
            "text":f"{text}"
            }
        }
    post = requests.post(url=url, json=data, headers=header)
    print(post.json())
    return post.json()['result']

print(QQ_TO_UZ("Salem", "kaa", "uz"))