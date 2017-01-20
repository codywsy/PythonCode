#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 打开一个文件
foo = open("foo.txt", "w")
print "文件名： ".decode("utf8"), foo.name
print "是否已关闭：".decode("utf8"), foo.closed
print "访问模式：".decode("utf8"), foo.mode
print "末尾是否强制加空格：".decode("utf8"), foo.softspace

# 写入新内容到文件
foo.write("github.com/codywsy/**.git")

# 关闭文件
foo.close()

foo = open("foo.txt", "r")
str = foo.read(2)
print "读取的字符串是：".decode("utf8"), str
foo.close()

