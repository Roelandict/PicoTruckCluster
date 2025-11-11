from random import randint
from typing import Literal
import json

class Item:
    def __init__(item):
        item.type = None
        item.id: int = 0
        item.status: Literal["Ready", "NotSet", "Offline", "Registered"] = "NotSet"
        item.name: str = ""
        item.optionalParameter:dict = {}


    def item_register(item,inputName:str,type:str):
        item.id = randint(0, 9999)
        item.name = inputName + str(item.id)
        item.status = "Registered"
        item.type = type
        return item.create_json()

    def create_json(item):
        return json.dumps({
            "id": item.id,
            "status": item.status,
            "name": item.name,
            "type": item.type,
            **item.optionalParameter
        })
        
    class meters:
        def __init__(meters):
            meters.type: str
            meters.averValueH: int
            meters.lastValue: int

        def registerMeter(meters,name:str):
            type = "IoT-Meter"
            Item.item_register(name, type)

