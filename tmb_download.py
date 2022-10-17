import urllib.request

def img_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)


url = 'https://i.ytimg.com/vi/sKSy5ajamd4/sddefault.jpg'

file_name = 'thumbnail'