import numpy as np
import cv2
from bottle import *

import fileOperation
import functionOperation
import threading
from configuration import *

# sketch处理池
handleSketchPool = []


# 接收草图
@route('/uploadSketch', method='POST')
def getUploadSketch():
    sketch = request.files.get('sketch')
    path = fileOperation.getIdOfRoom()
    sketch.save(path + '/originSketch.jpg', overwrite=True)
    sketch = cv2.imread(path + '/originSketch.jpg')
    handleSketchPool.append((path, sketch))
    while True:
        time.sleep(0.1)
        if os.path.exists(path + "/improvedSketch.jpg"):
            break;
    return 'hello'


threading.Thread(target=functionOperation.handleLoop, args=(handleSketchPool, )).start()

# if multiple_process:
#     run(host="0.0.0.0", port=80, server='paste')
# else:
#     run(host="0.0.0.0", port=8000, server='paste')
run(host="0.0.0.0", port=8000, server='paste')
