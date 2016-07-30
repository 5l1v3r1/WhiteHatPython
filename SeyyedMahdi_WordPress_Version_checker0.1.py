# in the name of God
# this is A Wordpress Version Checker
# SeyyedMahdi HassanPour matikolaee
# smahdi1991@gmail.com
import re
import requests

temp = input("please enter the Wordpress domain(default:127.0.0.1/wp451): ")
if temp == "":
    domain = "127.0.0.1/wp451"
else:
    domain = temp


# Aspect oriented programming : AOP
def time_decorator(func):
    def wrapper(*args, **kwargs):
        import time
        t1 = time.time()  # time.clock()
        ret_value = func(*args)
        t2 = time.time()  # time.clock()
        print("{name} : {time:10.10f}".format(name=func.__name__, time=t2 - t1))
        return ret_value

    return wrapper


@time_decorator
def request_webpage(address):
    r = requests.get(address)
    search_list = list()
    search_list.append(re.search(r'Version ([0-9]+\.[0-9]+\.?[0-9]*)', str(r.text)))
    search_list.append("js_" + str(re.search(r'ver=([0-9]+\.[0-9]+\.?[0-9]*)', str(r.text))))
    return search_list


match = list()
match.append(request_webpage("http://{}".format(domain)))
match.append(request_webpage("http://{}/readme.html".format(domain)))
print(match)
