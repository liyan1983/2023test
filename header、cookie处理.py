import requests

def test_demo_header_cookie():
    url = "https://httpbin.testing-studio.com/cookies"
    header = {
        "cookies": "hogwarts = school",
       'User-Agent': 'python-requests/2.23.0'
    }
    r = requests.get(url = url,headers = header)
    print(r.request.headers)

def test_demo_cookie():
    url = "https://httpbin.testing-studio.com/cookies"
    header = {
       'User-Agent': 'python-requests/2.23.0'
    }
    cookie_data ={
        "hogwarts": "school",
        "teacher": "ad"
    }
    r = requests.get(url = url,headers = header,cookies = cookie_data)
    print(r.request.headers)

if __name__ == '__main__':
    test_demo_header_cookie()
    test_demo_cookie()