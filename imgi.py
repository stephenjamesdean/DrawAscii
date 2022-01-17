import numpy as np
from PIL import Image
import cv2

gscale = "██▓▓▒▒$@B%#*wZ0\/+={}[]--;;::,,^^``.. "
pscale = (10, 10, 10), (20, 20, 40), (70, 70, 80), (100, 100, 100), (100, 120, 130), (105, 150, 1600), (
210, 220, 230), (250, 250, 250)
cols = 150
scale = .4


def getAve(image):
    im = np.array(image)
    w, h = im.shape
    return np.average(im.reshape(w * h))


def makeAsciiim(img):
    image = img.convert("L")
    W, H = image.size[0], image.size[1]
    w = W / cols
    h = w / scale
    rows = int(H / h)
    aimg = []
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)
        if j == rows - 1:
            y2 = H
        aimg.append("")
        print("")
        for i in range(cols):
            x1 = int(i * w)
            x2 = int((i + 1) * w)
            if i == cols - 1:
                x2 = W
            img = image.crop((x1, y1, x2, y2))
            avg = int(getAve(img))
            gsval = gscale[int((avg * 37) / 255)]
            print(gsval, end='')
            aimg[j] += gsval


def makePixel(fn):
    piximg = 255 * np.ones((512, 800, 3), np.uint8)
    cv2.namedWindow("image")
    image = Image.open(fn).convert("L")
    W, H = image.size[0], image.size[1]
    w = W / cols
    h = w / scale
    rows = int(H / h)
    aimg = []
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)
        if j == rows - 1:
            y2 = H
        for i in range(cols):
            x1 = int(i * w)
            x2 = int((i + 1) * w)
            if i == cols - 1:
                x2 = W
            img = image.crop((x1, y1, x2, y2))
            avg = int(getAve(img))
            gsval = pscale[int((avg * 7) / 255)]
            cv2.rectangle(piximg, (x1, y1), (x2, y2), gsval, -1)
    while (1):
        cv2.imshow("image", piximg)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyWindow("image")


def makeAscii(fn):
    image = Image.open(fn).convert("L")
    W, H = image.size[0], image.size[1]
    w = W / cols
    h = w / scale
    rows = int(H / h)
    aimg = []
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)
        if j == rows - 1:
            y2 = H
        aimg.append("")
        print("")
        for i in range(cols):
            x1 = int(i * w)
            x2 = int((i + 1) * w)
            if i == cols - 1:
                x2 = W
            img = image.crop((x1, y1, x2, y2))
            avg = int(getAve(img))
            gsval = gscale[int((avg * 37) / 255)]
            print(gsval, end='')
            aimg[j] += gsval


def main():
    makeAscii("kimi.jpg")
    makePixel("kimi.jpg")


if __name__ == '__main__':
    main()
