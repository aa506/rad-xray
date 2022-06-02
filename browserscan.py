#!/usr/bin/python3
# coding: utf-8
import subprocess
import sys

def main(data1):
	target = data1
	cmd = ["/usr/local/bin/xray","webscan","--browser-crawler",target,"--html-output" ,"report__datetime__.html"]
	rsp=subprocess.Popen(cmd)
	output, error = rsp.communicate()
	print(output)

file1 = sys.argv[1]
if __name__=='__main__':
	file = open(file1)
	for text in file.readlines():
		data1=text.strip('\n')
		main(data1)
