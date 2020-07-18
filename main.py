import json
import get_image

if __name__ == '__main__':
    try:
        f = open('config.json')
    except OSError:
        f = open('config.json','w')
        json.dump({'path':0},f)
        f.close()
        f = open('config.json')
    js = json.load(f)
    path = js['path']
    get_image.start(path)