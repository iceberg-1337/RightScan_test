import ui_global
from pony.orm.core import db_session
from pony import orm
from pony.orm import Database,Required,Set,select,commit
import json


def init_on_start(hashMap,_files=None,_data=None):
    ui_global.init()
    return hashMap


def sample1_on_input(hashMap,_files=None,_data=None):
    if hashMap.get("listener")=="btn_res":
        with db_session:
            p = ui_global.Bird(name=hashMap.get('name'), color=hashMap.get('color'))
            commit()

        hashMap.put("toast", "Добавлено")
        hashMap.put("ShowScreen", "Главное меню")

    return hashMap




def sample1_on_create(hashMap,_files=None,_data=None):
    if not hashMap.containsKey("name"):
        hashMap.put("name","")
    if not hashMap.containsKey("color"):
        hashMap.put("color","")

    return hashMap


def main_menu(hashMap, _files=None, _data=None):
    if hashMap.get("listener") == "list":
        hashMap.put("ShowScreen", "Список птиц")

        return hashMap

    elif hashMap.get("listener") == "create":
        hashMap.put("ShowScreen", "Создание новой птицы")

        return hashMap

    elif hashMap.get("listener") == "card":
        hashMap.put("ShowScreen", "Карточка птицы")

        return hashMap


def table(hashMap, _files=None, _data=None):
    table = {
        "type": "table",
        "textsize": "20",

        "columns": [
            {
                "name": "name",
                "header": "Name",
                "weight": "2"
            },
            {
                "name": "color",
                "header": "Color",
                "weight": "2"
            }
        ]
    }
    # work with SQL via Pony ORM
    query = select(c for c in ui_global.Bird)
    rows = []
    for bird in query:
        rows.append({"name": bird.name, "color": bird.color})

    table['rows'] = rows
    hashMap.put("table", json.dumps(table))

    return hashMap



def search(hashMap, _files=None, _data=None):
    if hashMap.get("listener") == "search":
        table = {
            "type": "table",
            "textsize": "20",

            "columns": [
                {
                    "name": "name",
                    "header": "Name",
                    "weight": "2"
                },
                {
                    "name": "color",
                    "header": "Color",
                    "weight": "2"
                }
            ]
        }

        query = select(c for c in ui_global.Bird)
        rows = []
        for bird in query:
            if bird.name == hashMap.get("name"):
                rows.append({"name": bird.name, "color": bird.color})

        table['rows'] = rows
        hashMap.put("cards", json.dumps(table))

    return hashMap


def search_on_create(hashMap,_files=None,_data=None):
    if not hashMap.containsKey("name"):
        hashMap.put("name","")

    return hashMap