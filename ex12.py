#-*-coding:utf-8-*-
#从sys库中提取argv功能
from sys import argv

#从控制台得到文件名
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#获得用户输入以确定是结束还是继续 PS：然而RETURN到底是什么
raw_input("?")

#以‘w’方式打开文件
print "Opening the file..."
target = open(filename, 'w')

#不太懂。为何要删除？也没分步啊。
print "Truncating the file. Goodbye!"
target.truncate()

#从控制台获得三行文字信息来录入文件
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

#啊哈，write文件
print "I'm going to write these to the file."

#改改看能不能只用一次
target.write(line1+"\n"+line2+"\n"+line3)

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#close就是保存。
print "And finally, we close it."
target.close()