import urllib
import urllib2
import cookielib

login_url = "https://www.tedbaker.com/us/login"
item_url = "http://www.tedbaker.com/us/Mens/Clothing/Shirts/BERBO-Floral-paisley-cotton-shirt-Navy/p/134447-NAVY?plpSlots=1"
discounted_item_url = "http://www.tedbaker.com/us/Mens/Clothing/Shirts/POLSERF-Geo-print-cotton-shirt-Red/p/134054-RED?plpSlots=1"

def main():
    url = "http://www.tedbaker.com/us"
    values = {"email" : "frank.wang6356@gmail.com",
              "password" : "wrnmbydh"}
    response = urllib2.urlopen(discounted_item_url)
    html = response.read()
    print html

if __name__ == "__main__":
    main()