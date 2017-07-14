from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import HTTPError

try:
    html=urlopen("http://www.jiji.com/jc/article?k=2017071401100&g=soc")
except HTTPError as e:
    print(e)
    #return, null, break, or do plan B which is altenertive to plan A
except URLError as e:
    print("URL is wrong!")
else:
    pass

bsObj=BeautifulSoup(html.read(),"lxml")
print(bsObj.h1)
