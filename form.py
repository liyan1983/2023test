import requests


class TestReq():

    def setup_class(self):
        self.proxy = {"http":"http://127.0.0.1:8080","https":"htpp://127.0.0.1:8080"}

    def test_data(self):
        datas = {
            "a":1,
            "b":2
        }
        r = requests.post("https://httpbin.testing-studio.com/post",data = datas,
                          proxies=self.proxy,verify = False)
        print(r.json())

if __name__ == '__main__':
    TestReq.test_data()