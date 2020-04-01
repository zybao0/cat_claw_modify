#!coding:utf8
import cgi,cgitb
import urllib.request as urllib2
import urllib
import os
import random
import string
form=cgi.FieldStorage()
path=form.getvalue('path')
url=form.getvalue('down_url')
comm="start ffmpeg -i "+url+" -vcodec copy -acodec copy "+path+"\\"+''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))+".mp4"
# f = open("out.txt", "w")
# f.write(comm)
# f.close()
os.system(comm)