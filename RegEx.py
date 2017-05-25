
import urllib.request
import sys
import re

mainURL = "http://www.rarbt.com"
req = urllib.request.Request( mainURL )
temp = urllib.request.urlopen(req)
#print ( temp )
encode = temp.headers.get_content_charset()
data = temp.read().decode(encode)
#print ( encode )
reg = re.compile("</span><a href=\"(.*\.html)\"\stitle=\"(.*)\"\starget")
imdbReg = re.compile("href=\"/index\.php/search/index\.html\?imdb=(.*)\">" )


result = reg.findall(data)
#catch = re.match( str ,data)
#print (result[0] )
for i,obj in enumerate(result):
    print ( str(i+1)+"."+obj[1],end="")
    req = urllib.request.Request( mainURL+obj[0] )
    temp = urllib.request.urlopen(req)
    #encode = temp.headers.get_content_charset()
    #print ( encode )
    data = temp.read().decode("utf-8")
    print ( "\t\timdb:"+imdbReg.search(data).group(1) )
    

print ( "共"+ str(len(result) )+"筆資料" )
#print (sys.stdin.encoding)

"""fileout = open("output.txt","w",encoding='utf-8')
fileout.write(data)
fileout.close()

print ( type( data ) )"""
#print ( type( str87 ) )

#input()
#print (response.read().decode("UTF-8",'replace') )

