import requests

import mongoengine
import time
from models.airlinemodel import Airlines


if __name__ == '__main__':

    mongoengine.connect(host="mongodb+srv://amal:Vv14t8Ig7MukqL5R@cluster0.x4j0e.mongodb.net/flight-routes")

    airline = requests.get("https://cdn.jsdelivr.net/gh/besrourms/airlines@latest/airlines.json", verify=False)

    airline_data = airline.json()

    for airline in airline_data:
        try:
            a = Airlines.objects.get(code=airline.get("code"))
        except Airlines.DoesNotExist:
            Airlines(
             name=airline.get("name"),
             code=airline.get("code"),
             isLowCost=airline.get("is_lowcost"),
             logo=airline.get("logo"),
             createdAt=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
             updatedAt=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
             ).save()
