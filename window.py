import cv2 as cv
import numpy as np
import sys 

def imshow(_input,named=True,window_flag=cv.WINDOW_NORMAL):
	global errlog
	frame = sys._getframe(1)
	var_dict = frame.f_locals

	if type(_input) == str:
		try:
			vars = _input.split('.')
			print(vars)
			ref = var_dict[vars[0]]
			for i in range(1,len(vars)):
				if ref is None:
					print('referece is empty')
					return
				ref = getattr(ref, vars[i])
			if named:
				cv.namedWindow(_input,window_flag)
			cv.imshow(_input,ref)
		except:
			return
	if type(_input) == tuple or type(_input) == list:
		for i in range(len(_input)):
			name = _input[i]
			if name not in var_dict:
				print(f'variable {name} not found')
				continue
			if var_dict[name] is None:
				print('image is empty')
				return
			if named:
				cv.namedWindow(name,window_flag)
			cv.imshow(name,var_dict[name])