import math

# https://code.google.com/p/chromium/codesearch#chromium/src/cc/output/render_surface_filters.cc&ct=rc&cd=6&q=huerotate%20lang:%5Ec%2B%2B$&sq=package:chromium&l=70&dr=CSs

'''
	188: 
		-0.53669703 1.5225505 0.014146432 0.0 0.0 \
		0.40303504 0.4132893 0.18268535 0.0 0.0 \
		0.5334565 1.3235327 -0.85698926 0.0 0.0 \
		0.0 0.0 0.0 1.0 0.0
'''

file = 'armenplzdiejustplz.png'
output = 'new/armenplzdiejustplz.png'

hue = 188

hue = (hue * 3.1415926535897932384626433832795) / 180.0

cos_hue = math.cos(hue)
sin_hue = math.sin(hue)

_ = 0.0

matrix = {1: ([_, _, _, _, _]), 2: ([_, _, _, _, _]), 3: ([_, _, _, _, _]), 4: ([_, _, _, 1.0, _])}

matrix[1][0] = 0.213 + cos_hue * 0.787 - sin_hue * 0.213
matrix[1][1] = 0.715 - cos_hue * 0.715 - sin_hue * 0.715 # RED
matrix[1][2] = 0.072 - cos_hue * 0.072 + sin_hue * 0.928

matrix[2][0] = 0.213 - cos_hue * 0.213 + sin_hue * 0.143
matrix[2][1] = 0.715 + cos_hue * 0.285 + sin_hue * 0.140 # GREEN
matrix[2][2] = 0.072 - cos_hue * 0.072 - sin_hue * 0.283

matrix[3][0] = 0.213 - cos_hue * 0.213 - sin_hue * 0.787
matrix[3][1] = 0.715 - cos_hue * 0.715 + sin_hue * 0.715 # BLUE
matrix[3][2] = 0.072 + cos_hue * 0.928 + sin_hue * 0.072

matrix = ' \\\n'.join([' '.join([str(x) for x in m]) for m in matrix.values()])

print 'convert %s -color-matrix "5x4: %s" %s' % (file, matrix, output)
