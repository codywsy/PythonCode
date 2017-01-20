#!/usr/bin/env python
# -*- coding: utf-8 -*-

# lines产生一个生成器generator对象，作用在文件file参数的最后追加一个空行'\n'
def lines(file):
	for line in file: yield line
	yield '\n'

#
def blocks(file):
	block = []
	for line in lines(file):
		if line.strip():	# strip()是为了去除文本内容开头和结尾中多余的空格
			block.append(line)	#加入列表对象block中
		elif block:	#如果此时line为空行（文本块结束标志），则将block元素链接起来，作为文本块输出
			yield ''.join(block).strip()
			block = []
