import datetime

def datatime_demo():
    time_now = datetime.datetime.now()
    time_now_format = datetime.datetime.strptime(str(time_now),'%y-%m-%d %H:%M:%S')
    print(time_now)
    print(time_now_format)


if __name__ == '__main__':
    datatime_demo()