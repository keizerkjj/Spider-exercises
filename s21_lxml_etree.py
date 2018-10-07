from lxml import etree

html = etree.parse('./s20.html')

rsp = html.xpath("/bookstore/book")

print(rsp)

rst = html.xpath("//book[@category='sport']/year ")
#因为上面解析的rst是一个list，下面这一步将数据从list里面拿出来，重新放到rst里面
rst = rst[0]
print(rst.tag)
print(rst.text)