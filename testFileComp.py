# -*- coding: utf-8 -*-

import filecmp


print filecmp.cmp("dircomp/src/f1", "dircomp/src/f1")
print "-"*20

a = "dircomp/src"
b = "dircomp/des"
print filecmp.cmpfiles(a,b,['f1','subdir1/f1-1','subdir1/f1-2'])
print "-"*20

dirobj=filecmp.dircmp(a,b)
print dirobj.report()
print "-"*10
print dirobj.report_partial_closure()
print "-"*10
print dirobj.report_full_closure()
print "-"*10
print "left_list:"+ str(dirobj.left_list)
print "right_list:"+ str(dirobj.right_list)
print "common:"+ str(dirobj.common)
print "left_only:"+ str(dirobj.left_only)
print "right_only:"+ str(dirobj.right_only)
print "common_dirs:"+ str(dirobj.common_dirs)
print "common_files:"+ str(dirobj.common_files)
print "common_funny:"+ str(dirobj.common_funny)
print "same_file:"+ str(dirobj.same_files)
print "diff_files:"+ str(dirobj.diff_files)
print "funny_files:"+ str(dirobj.funny_files)
