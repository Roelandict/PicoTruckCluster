from random import randint
from typing import Literal
import json

class Item:
    def __init__(item):
        item.id: int = 0
        item.status: Literal["Ready", "NotSet", "Offline", "Registered"] = "NotSet"
        item.name: str = ""
        item.optionalParameter:dict = {}
    
    def _item_register(item,inputName:str):
        item.id = randint(0, 9999)
        item.name = inputName + str(item.id)
        item.status = "Registered"
        return item.create_json()

    def __create_json(item):
        return json.dumps({
            "id": item.id,
            "status": item.status,
            "name": item.name,
            **item.optionalParameter
        })

    class meters:
        def __init__(meters):
            meters.type: str
            meters.averValueH: int
            meters.lastValue: int

        def registerMeter(meters,type:str,name:int):
            meters.type = type
            id = meters.id
            meters.name = name

            