import configparser


def get_url(name):
    config = configparser.ConfigParser()
    config.read('config.ini')
    url = config.get("Url_Config", name)
    return url


res = get_url("baseurl")
print(res)
