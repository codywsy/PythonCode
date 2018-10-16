# -*- coding: utf-8 -*-

import filecmp
import os
import filecmp
import re
import shutil
holderlist=[]





def compareme(dir1, dir2):  #递归获取更新项函数
    dircomp=filecmp.dircmp(dir1,dir2)
    only_in_one=dircomp.left_only   #源目录新文件或目录
    diff_in_one=dircomp.diff_files  #不匹配文件,源目录文件已发生变化
    dirpath=os.path.abspath(dir1)   #定义源目录绝对路径

    #将更新文件名或目录追加到
    [holderlist.append(os.path.abspath( os.path.join(dir1,x) )) for x in only_in_one]
    [holderlist.append(os.path.abspath( os.path.join(dir1,x) )) for x in diff_in_one]
    if len(dircomp.common_dirs) > 0:    #判断是否存在相同子目录,以便递归
        for item in dircomp.common_dirs:    #递归子目录
            compareme(os.path.abspath(os.path.join(dir1,item)), \
            os.path.abspath(os.path.join(dir2,item)))
        return holderlist
    
def main():
    dir1="dircomp/src"
    dir2="dircomp/des"
    source_files=compareme(dir1,dir2)   #比对源目录与备份目录
    dir1=os.path.abspath(dir1)
    
    print source_files

    #备份目录路径加 ”/” 符
    if not dir2.endswith('/'): dir2=dir2+'/'
    dir2=os.path.abspath(dir2)
    destination_files=[]
    createdir_bool=False
    
    
    for item in source_files:   # 遍历返回的差异文件或目录清单
        destination_dir=re.sub(dir1, dir2, item)    # 将源目录差异路径清单,对应替换成备份目录
        destination_files.append(destination_dir)
        if os.path.isdir(item): # 如差异路径为目录且不存在刚在备份目录中创建
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
                createdir_bool=True # 再次调用compareme函数标记
    
    if createdir_bool:  # 重新调用 compareme 函数,重新遍历新创建目录内容
        destination_files=[]
        source_files=[]
        source_files=compareme(dir1,dir2)   # 调用 compareme 函数
        for item in source_files:   # 获取源目录差异路径清单,对应替换成备份目录
            destination_dir=re.sub(dir1,dir2,item)
            destination_files.append(destination_dir)
    
    print "update item:"
    print source_files
    copy_pair=zip(source_files, destination_files)
    for item in copy_pair:
        print item
        if os.path.isfile(item[0]):
            shutil.copyfile(item[0],item[1])
    
if __name__ == "__main__":
    main()