def read(address):
    r = requests.get(address)
    search_list = list()
    search_list.append(re.search(r'Version ([0-9]+\.[0-9]+\.?[0-9]*)', str(r.text)))
    search_list.append("js_" + str(re.search(r'ver=([0-9]+\.[0-9]+\.?[0-9]*)', str(r.text))))
    return search_list
