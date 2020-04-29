
import sys
import json
import tweepy
import yweather
import pprint


# Authenticate to Twitter
auth = tweepy.OAuthHandler("G9Rtluy2antY7VS4AJrZKKIw4", "6TvT2Pv4xH7wlinY3grouP2FBBG5Q99LvkL2vWrR1zWzelB5Q5")
auth.set_access_token("1254018042511622144-LJjE1f57lVoIK5Dtt7B5pfH76qFecY", "mDcYFQrOl7K6vOdQh7xapuXpNTY9pwRr2FG3YBp1ogmHE")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

# calling the data from the json file to get woeid id
country=input("enter a country")
Country_WOE_ID=None
input_file = open('trends-locations.json')
data = json.load(input_file)  # get the data list
for element in data:
    if (element['country'].lower() == country):
        id = element['parentid']
        print (id)
        Country_WOE_ID = id
        break  # print it

# check if country is exsists  and printy trednds

if Country_WOE_ID is not None:
    country_trends = api.trends_place(Country_WOE_ID)
    trends = json.loads(json.dumps(country_trends, indent=1))
    list=[]
    for trend in trends[0]["trends"]:
        print (trend["name"])
    #    list.append(trend["name"])
    #print(list)
# else print list of countries
else :
    print("wrong name  choose one of these countries only ")
    country_list=[]
    for element in data:
        if(element['country'] in country_list):
            continue
        else:
            country_list.append(element['country'])
    for c in country_list:
        print(c)



#trends_result = api.trends_place(1)
#for trend in trends_result[0]["trends"]:
    #print(trend["name"])
