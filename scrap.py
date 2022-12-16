# from bs4 import BeautifulSoup
# import json
# import requests

# url = "https://www.flipkart.com/search?q=camera&sid=jek%2Cp31%2Ctrv&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=camera%7CDSLR+%26+Mirrorless&requestId=d29efd74-b5d1-4d37-8701-3e92fef811ec&as-searchtext=camer"



# response = requests.get(url)

# htmlcontent = response.content

# soup = BeautifulSoup(htmlcontent,"html.parser")


# top=[]
# titles = []

# prices = []

# images = []

# for d in soup.find_all('div',attrs={'class':'_2kHMtA'}):

   

#     title = d.find('div',attrs={'class':'_4rR01T'})

#     title=title.string

#     titles.append((title))



#     price = d.find('div',attrs={'class':"_30jeq3 _1_WHN1"})

#     price=price.string

#     prices.append((price))



#     image = d.find('img',attrs={'class':'_396cs4 _3exPp9'})

#     image=image.get('src')

#     images.append((image))
# details={'Titles':'','Prices':'','Images':''}
# details['Titles']=titles
# details['Prices']=prices
# details['Images']=images
# top.append(details.copy())
# with open ('a.json','w') as file:
#     json.dump(top,file,indent=4)

# from flask import Flask

# app = Flask(__name__)




# @app.route('/')

# def hello_world():

#     return 'This is my first API call!'
# if __name__ == "__main__":

#     app.run(debug=True)

from flask import Flask  

app = Flask(__name__)  

 

@app.route('/home')  

def home():  

    return "hello, welcome to our website";  

 

if __name__ =="__main__":  

    app.run(debug = True)  


# # print(titles)

# # print(prices)

# # print(images)