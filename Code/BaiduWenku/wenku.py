#coding=utf-8  
import re;  
import urllib;  
import urllib.request;  
  
header = {  
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 UBrowser/1.0.370.1388 Safari/537.36",   
}  
  
URL_GETBDWKDOC = "http://wenku.baidu.com/play/{0}?pn={1}";  
URL_BDWK = "http://wenku.baidu.com/view/{0}.html";  
  
class BdWkDownloader:  
    def __init__(self):  
        pass;  
          
    def getTotalPages(self, id):  
        return int(re.compile(r"totalPageNum'\s*:\s*'(\d+)'").findall(urllib.request.urlopen(URL_BDWK.format(id)).read().decode("gb2312"))[0]);  
          
    def download(self, id, dir = "./"):  
        num = self.getTotalPages(id);  
        for i in range(0, num):  
            request = urllib.request.Request(URL_GETBDWKDOC.format(id, i + 1), headers = header);  
            data = urllib.request.urlopen(request).read();  
            file = open("{0}{1}.{2}".format(dir, i, "swf"), "wb");  
            file.write(data[106:]);  
            file.close();  
          
def main():  
    downloader = BdWkDownloader();  
    downloader.download("ef13d84ea6c30c2259019e5b");  
      
if(__name__ == "__main__"):  
    main();  
