# -*- coding: utf-8 -*-

import os
import pandas as pd


def parse_seq(dname):
	task_seq = {}
	path = dname + 'list.txt'
	with open(path, 'r') as fhand:
		for line in fhand:
			k, v = line.strip().split('\t')
			task_seq[k] = v
	return task_seq

def parse_cmd(dname):
	task_seq = parse_seq(dname)
	errcnt = 0
	frames = []
	for fname in os.listdir(dname):
		try:
			if 'CMD' in fname:
				path = dname + fname
				doc = open(path).read().split('\r\n')
				desc = doc[:17]
				subject = desc[5]
				headers = doc[18]
				data = pd.DataFrame([r.split('\t') for r in doc[20:]])
				data.columns = headers.split('\t')
				frames.append(data)
				print 'Complete processing %s' % subject
		except Exception as err:
			errcnt += 1
			print err, fname
			pass
	df = pd.concat(frames)
	print '%d error(s) occured' % errcnt
	return desc, df


if __name__ == '__main__':
	dname = 'data/'
	desc, df = parse_cmd(dname)
	print df
