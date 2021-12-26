import requests


def open_file():
    try:
        my_file = open("excpet_fail")
    except BaseException as e:
        print("something went wrong " + str(e.args))


def divide_number():
    try:
        requests.get("http://saasdsd")
    except BaseException:
        print("It seems the url didn't respond ")

open_file()
divide_number()
print("program done")
