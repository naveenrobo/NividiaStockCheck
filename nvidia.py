import requests
from twilio.rest import Client

account_sid = ""
auth_token = ""
numbers = ["+91xxxxxxxxx"]
debug = "+91xxxxxxxxxxxxx"

# declare constants here
url = "https://in-and-ru-store-api.uk-e1.cloudhub.io/rashi/products/13"


def whatsapp(to, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                                from_='whatsapp:+14155238886',
                                body=message,
                                to='whatsapp:'+to
                            )
    print(message.sid)

print("Running 5 mins script")
# do the stuffs here
try:
    r = requests.get(url)
    if(r.status_code == 200):
        try:
            print("getting content")
            content = r.json()
            status = content["products"]["product"][0]["inventoryStatus"]["productIsInStock"]
            quantity = content["products"]["product"][0]["inventoryStatus"]["availableQuantity"]
            if (status is True) or (quantity > 0):
                print("Jetson is in stock")
                whatsapp(debug,"Jetson is in stock. Available quantity is "+quantity+". Hurry!!!😀😀")
        except Exception as e:
            print("Exception!!!")
            whatsapp(debug,"Exception in your script. Idiot 😐😐"+e)
            print(e)
    else:
        print("error while loading page")
        whatsapp(debug,"Error while loading the page. 😐😐")
except Exception as e:
    whatsapp(debug,"Exception in your script. Idiot 😐😐."+e)

