import tweepy
ckey="d31x2DQB4m066Nry9vL95d5Lx"
csecret="jmOf7QQgBetu5lPlGSpdkSzCaTnuy0KD30KASfhesfMGGxLtRR"
atoken="1011804071198580736-0pSDKsHvR7CyAoibtFykDGuwV7pBw5"
asecret="qDAV74Cfo78jTdk0eMDJiqmy5o3dLWPXMrMujF4zyNAL5"

auth=tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api=tweepy.API(auth)
print(api.search("#sanju"))