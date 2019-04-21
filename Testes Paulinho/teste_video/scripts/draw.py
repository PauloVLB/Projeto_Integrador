#!/usr/bin/env python

import cv2

class DrawCircles():
    def __init__(self, color=(0,255,0), thick=3, isCenter=False):
        self.isCenter = isCenter
        self.color = color
        self.thick = thick

	def draw(self, img, objeto):
		for (x,y,w,h) in objeto:
			cv2.circle(img, (x+(w/2), y+(h/2)), (w/2), self.color, self.thick)

		return img

	def draw(self, img, arrayCoordenadas):
		x = int(arrayCoordenadas[0])
		y = int(arrayCoordenadas[1])
		w = int(arrayCoordenadas[2])
		h = int(arrayCoordenadas[3])

		cv2.circle(img, (x+(w/2), y+(h/2)), (w/2), self.color, self.thick)

		return img

    def draw(self, img, circle):
        center = (circle.x, circle.y)
        radius = 1 if self.isCenter else circle.raio

        cv2.circle(img, center, radius, self.color, self.thick)

        return img

class DrawLines():
    def __init__(self, color=(0,255,0), thick=1):
        self.color = color
        self.thick = thick

    def line(self, img, pt1, pt2):
        cv2.line(img, pt1, pt2, self.color, self.thick)

    def horizontal(self, img):
        w = img.shape[1]
    	h = img.shape[0]

        pt1 = (w, h/2)
    	pt2 = (0, h/2)
        self.line(img, pt1, pt2)

    def vertical(self, img):
        w = img.shape[1]
    	h = img.shape[0]

        pt1 = (w/2, h)
    	pt2 = (w/2, 0)
    	self.line(img, pt1, pt2)

class Write():
    def __init__(self, translate=False, font=cv2.FONT_HERSHEY_SIMPLEX, length=0.6, color=(0,255,0), thick=2):
        self.font = font
        self.length = length
        self.color = color
        self.thick = thick
        self.translate = translate

    def onCircles(self, img, circle):
        index, x, y, radius = circle.index, circle.x, circle.y, circle.raio
        w = img.shape[1]
        h = img.shape[0]

        org = (x-radius, y-radius)

        if self.translate:
            x = ((w/2)-x)*-1
            y = ((h/2)-y)

        text = '%s: (%s,%s)'%(str(index), x, y)
        cv2.putText(img, text, org, self.font, self.length, self.color, self.thick)
