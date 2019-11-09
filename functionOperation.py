import cv2
import imageOperation
import aiOperation

def handleLoop(handleSketchPool):
    while True:
        handleSketch(handleSketchPool)


def handleSketch(handleSketchPool):
    if len(handleSketchPool) > 0:
        path, sketch = handleSketchPool[0]
        del handleSketchPool[0]
        improved_sketch = sketch.copy()
        improved_sketch = imageOperation.min_resize(improved_sketch, 512)
        improved_sketch = imageOperation.cv_denoise(improved_sketch)
        improved_sketch = imageOperation.sensitive(improved_sketch, s=5.0)
        improved_sketch = aiOperation.go_tail(improved_sketch)
        cv2.imwrite(path + '/improvedSketch.jpg', improved_sketch)
    return
