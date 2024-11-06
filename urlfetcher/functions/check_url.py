from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

def check_url(url):
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        req = Request(url)
        response = urlopen(req)
        content = response.read()
        try:
            content.decode('utf-8')
        except UnicodeDecodeError:
            content_type = response.headers.get_content_type()
            if content_type == 'image/jpeg':
                print("The URL points to a JPEG image.")
                return True, content_type
            else:
                print("Error: Response content is not UTF-8 encoded")
                return False, None
        return response.status == 200, 'text/html'
    except (URLError, HTTPError) as e:
        print(f"Error: {e}")
        return False, None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False, None
