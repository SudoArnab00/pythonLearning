import bitly_api

Access_Token = "55b4b6f075a5e1dec0a3620435269305d529eeaf"

connection = bitly_api.Connection(access_token = Access_Token)

delink = input("A link please:  ")

shorten_url = connection.shorten(delink)

print(shorten_url.get('url'))
