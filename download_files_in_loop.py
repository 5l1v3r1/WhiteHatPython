# in the name of GOD
# SeyyedMahdi HassanPour
# Seyyedmahdihp@gmail.com
# smahdi1991@gmail.com
# file downloader with iteration

import urllib.request


def download_web_image(url):
    full_name = str(url.split("/")[-1]) + ".png"
    print(full_name, "downloaded")
    urllib.request.urlretrieve(url, full_name)

n = int(input("enter number of iteration:"))   # number of files to download
for i in range(n):
    img_url = "http://some-files-download.com/resource/391800/c/45984/get/dsPID=ma{0}&scale=1.82".format(i)
    download_web_image(img_url)
