import json
import get_image

if __name__ == '__main__':
    try:
        f = open('config.json')    
        js = json.load(f)
        path = js['path']
    except OSError:
        path = 0

    get_image.start(path)