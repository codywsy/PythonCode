#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
        self.level = ''

    def print_score(self):
        print "student {0}'s score: {1}".format(self.name,self.score)
    


if __name__=='__main__':
    t1 = Student("CodyWU", 99)
    t2 = Student("MaryLi", 100)
    t3 = Student("JeremyLin", 30)

    stu_list = [t1, t2, t3]
    for t in stu_list:
        t.print_score()