from urllib.request import urlopen
def load_url(url, binary=False):

    with urlopen(url) as u:

        if binary:

            return u.read()

        else:

            return u.read().decode('utf-8')