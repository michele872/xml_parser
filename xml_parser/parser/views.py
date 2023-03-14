# import xml element tree
import xml.etree.ElementTree as ET
  
  
# import mysql connector
import mysql.connector
def executeParse(request):  
    # give the connection parameters
    # user name is root
    # password is empty
    # server is localhost
    # database name is database
    conn = mysql.connector.connect(user='root', 
                                password='root', 
                                host='localhost', 
                                database='xml',
                              auth_plugin='mysql_native_password')
    ciao = 'ciao'
    # reading xml file , file name is vignan.xml
    tree = ET.parse('example.xml')
    
    # in our xml file student is the root for all 
    # student data.
    data2 = tree.findall('details')
    print(len(data2))
    # retrieving the data and insert into table
    # i value for xml data #j value printing number of 
    # values that are stored
    for i, j in zip(data2, range(1, 6)):
        firstname = i.find('firstname').text
        lastname = i.find('lastname').text
        title = i.find('title').text
        division = i.find('division').text
        building = i.find('building').text
        room = i.find('room').text
        
        # sql query to insert data into database
        data = """INSERT INTO xml(firstname,lastname,title,division,building,room) VALUES(%s,%s,%s,%s,%s,%s)"""
    
        # creating the cursor object
        c = conn.cursor()
        
        # executing cursor object
        c.execute(data, (firstname,lastname,title,division,building,room))
        conn.commit()
        print("employee No-", j, " stored successfully")
        #return ciao
# from django.shortcuts import render


# # importing the required modules
# import csv
# import requests
# import xml.etree.ElementTree as ET
  
# def loadRSS():
  
#     # url of rss feed
#     url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
  
#     # creating HTTP response object from given url
#     resp = requests.get(url)
  
#     # saving the xml file
#     with open('topnewsfeed.xml', 'wb') as f:
#         f.write(resp.content)

     
  
# def parseXML(xmlfile):
  
#     # create element tree object
#     tree = ET.parse(xmlfile)
  
#     # get root element
#     root = tree.getroot()
  
#     # create empty list for news items
#     newsitems = []
  
#     # iterate news items
#     for item in root.findall('./channel/item'):
  
#         # empty news dictionary
#         news = {}
  
#         # iterate child elements of item
#         # for child in item:
  
#         #     # special checking for namespace object content:media
#         #     if child.tag == '{http://search.yahoo.com/mrss/}content':
#         #         news['media'] = child.attrib['url']
#         #     else:
#         #         news[child.tag] = child.text.encode('utf8')
  
#         # # append news dictionary to news items list
#         # newsitems.append(news)
      
#     # return news items list
#     return newsitems
  
  
# def savetoCSV(newsitems, filename):
  
#     # specifying the fields for csv file
#     fields = ['firstname', 'lastname', 'title', 'division', 'building', 'room']
  
#     # writing to csv file
#     with open(filename, 'w') as csvfile:
  
#         # creating a csv dict writer object
#         writer = csv.DictWriter(csvfile, fieldnames = fields)
  
#         # writing headers (field names)
#         writer.writeheader()
  
#         # writing data rows
#         writer.writerows(newsitems)
  
      
# def main():
#     executeParse()
# #     # load rss from web to update existing xml file
# #     # loadRSS()
  
# #     # parse xml file
# #     newsitems = parseXML('example.xml')
  
# #     # store news items in a csv file
# #     savetoCSV(newsitems, 'example.csv')
      
      
# if __name__ == "__main__":
  
#     # calling main function
#     main()
    
    
# def parseMio():
#  # parse xml file
#     newsitems = parseXML('example.xml')
  
#     # store news items in a csv file
#     savetoCSV(newsitems, 'example.csv')
    
#     return 'ciao'