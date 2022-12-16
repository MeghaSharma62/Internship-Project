# import xml.etree.ElementTree as ETree
# import pandas as pd
  
# # give the path where you saved the xml file
# # inside the quotes
# # <xml version="1.0" encoding="UTF-8">
# # xmldata = encoding="UTF-8"
# xmldata = "POSSales_V6_Web_Sales.xml"
# prstree = ETree.parse(xmldata)
# root = prstree.getroot()
# all_items=[]  
# print(root)
# for element in root.iter('POSLog'):
    
#     store_Nr = element.attrib.get('Transaction')
# #     itemsF = storeno.find('foodItem').text
# #     price = storeno.find('price').text
# #     quan = storeno.find('quantity').text
# #     dis = storeno.find('discount').text
#     st=[store_Nr]
#     all_items.append(st)    
# #     store_items = [store_Nr, itemsF, price, quan, dis]
# #     all_items.append(store_items)
  
# xmlToDf = pd.DataFrame(all_items, columns=[
#     'Transaction','name'])
# #   'SL No', 'ITEM_NUMBER', 'PRICE', 'QUANTITY', 'DISCOUNT'])
  
# print(xmlToDf.to_string(index=False))
a=[100,400,500,200]
a.sort()
print(a)