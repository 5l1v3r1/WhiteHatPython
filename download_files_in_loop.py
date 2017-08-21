# in the name of GOD
# SeyyedMahdi HassanPour
# Seyyedmahdihp@gmail.com
# smahdi1991@gmail.com
# file downloader with iteration

import urllib.request


def download_web_image(url):
    full_name = str(url.split("/")[-1])
    print(full_name, "downloaded")
    urllib.request.urlretrieve(url, full_name)

n = int(input("enter number of iteration:"))   # number of files to download
for i in range(n):
    try:
        img_url = "http://www.sample.com/pdf/rpdf_{0}.pdf".format(i)
        download_web_image(img_url)
    except Exception as e:
        print(e)
