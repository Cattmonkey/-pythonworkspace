import pymysql
import numpy as np
import matplotlib
matplotlib.use('Agg')
import cv2
from multiprocessing import Queue, Process
import json
import os
import seaborn as sns
from datetime import datetime
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
# import sys

def ResultIter(cursor, arraysize=1000):
    # 'An iterator that uses fetchmany to keep memory usage down'
    while True:
        results = cursor.fetchmany(arraysize)
        if not results:
            break
        for result in results:
            yield result


def calcData(startTime, endTime, width, height, camID, tarWidth, tarHeight, lines, M, q):
	startTime, endTime = datetime.fromtimestamp(startTime), datetime.fromtimestamp(endTime)	

	conn = pymysql.connect(host='192.168.100.244', user='pcm', password='pcm=pwd@2016', db='pcmwork', charset="utf8")
	cursor = conn.cursor()
	cursor.execute('SELECT startR, endR, startC, endC FROM heatmap_data WHERE CamID = %s AND (MapDate BETWEEN %s AND %s)', (camID, startTime, endTime))


	mat = np.zeros((height, width))
	for result in ResultIter(cursor):
		startRow = int(height * result[0])
		endRow = min(int(height * result[1]), height - 1)
		startColumn = int(width * result[2])
		endColumn = min(int(width * result[3]), width - 1)
		mat[startRow:endRow, startColumn:endColumn] += 1
	conn.close()

	mat = cv2.warpAffine(mat, M, (tarWidth, tarHeight))
	
	for i in range(tarHeight):
		for j in range(tarWidth):
			for line in lines:
				if line[0] == '>':
					if j * line[1] + i * line[2] +line[3] > 0:
						mat[i, j] = 0
						break
				else:
					if j * line[1] + i * line[2] +line[3] <= 0:
						mat[i, j] = 0
						break
	q.put(mat)




def getHeatmap(startTime, endTime, camNum=2, width=1280, height=960):
	img = cv2.imread('model/heatmapAPINew/cfg/designgraph.png')
	tarHeight, tarWidth = img.shape[:2]

	

	q = Queue()
	for camID in range(camNum):
		with open('model/heatmapAPINew/cfg/cam_{}.json'.format(camID)) as f:
			d = json.load(f)
		lines = d['lines']

		pts1 = np.float32(d['first_3_pt'])
		pts2 = np.float32(d['second_3_pt'])
		M = cv2.getAffineTransform(pts1,pts2)

		p = Process(target=calcData, args=(startTime, endTime, width, height, camID, tarWidth, tarHeight, lines, M, q))
		p.daemon = True
		p.start()

	heatmap = np.zeros((tarHeight, tarWidth))
	for _ in range(camNum):
		heatmap += q.get()


	heatmap = cv2.GaussianBlur(heatmap, (51, 51), 0)

	#lower the maxValue to increase the amount of red spots
	maxValue = np.max(heatmap)

	maxValue *= .9

	heatmap[heatmap > maxValue] = maxValue

	myCmap = LinearSegmentedColormap.from_list('myCmap', [(0., 'white'), (.2, 'blue'), (.4, 'green'), (.5, 'yellow'), (1., 'red')])
	sns.heatmap(heatmap, xticklabels=False, yticklabels=False, cmap=myCmap, cbar=False)

	heatmap = plt.savefig('tmp.jpg')

	heatmap = cv2.imread('tmp.jpg')
	os.remove('tmp.jpg')

	heatmap = cv2.resize(heatmap, (tarWidth, tarHeight))
	xShift = 65
	yShift = 52
	M = np.float32([[1, 0, xShift], [0, 1, yShift]])
	heatmap = cv2.warpAffine(heatmap, M, (tarWidth, tarHeight))

	heatmap[:yShift, :] = 255
	heatmap[:, :xShift] = 255

	print (img.shape)
	print (heatmap.shape)
	cv2.addWeighted(img, .5, heatmap, .5, 0., img)
   
	cv2.imwrite("static/images/heatmap/heatmap.jpg", img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	return 0



if __name__ == '__main__':
	# if len(sys.argv) != 3:
	# 	print ('Error: 2 arguments')
	# 	exit()
    dt_1 = datetime.strptime("2017-10-30 15:00:00", "%Y-%m-%d %H:%M:%S")
    dt_2 = datetime.strptime("2017-10-30 17:40:00", "%Y-%m-%d %H:%M:%S")

    dt_1 = datetime.timestamp(dt_1)
    dt_2 = datetime.timestamp(dt_2)
    print(dt_1, dt_2)
    getHeatmap(dt_1, dt_2)

	# cv2.imshow('heatmap', getHeatmap(dt_1, dt_2))

	# cv2.waitKey(0)
	
