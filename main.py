import get_image
import json

if __name__ == '__main__':
    try:
        f = open('config.json')
    except OSError:
        f = open('config.json','w')
        json.dump({'path':0},f)
        f.close()
        f = open('config.json')
    js = json.load(f)
    get_image.start(js['path'])
