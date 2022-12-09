import requests


class Hero:
    def __init__(self, name, heroes_db):
        self.name = name
        pers_stats = list(filter(lambda person: person['name'] == name, heroes_db))[0]
        self.intelligence = pers_stats['powerstats']['intelligence']
        self.strength = pers_stats['powerstats']['strength']
        self.speed = pers_stats['powerstats']['speed']
        self.durability = pers_stats['powerstats']['durability']
        self.power = pers_stats['powerstats']['power']
        self.combat = pers_stats['powerstats']['combat']

    def __str__(self):
        res = f"{self.name}:\nIntelligence: {self.intelligence}\nStrength: {self.strength}\n" \
              f"Speed: {self.speed}\nDurability: {self.durability}\nPower: {self.power}\nCombat: {self.combat}\n"
        return res


def get_heroes_info(heroes):
    """requests info about heroes"""
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    com = '/all.json'
    heroes_params = list(filter(lambda person: person['name'] in heroes, requests.get(url=url + com).json()))
    return heroes_params


def main():
    heroes = ["Hulk", "Captain America", "Thanos"]
    heroes_info = get_heroes_info(heroes)
    hulk = Hero("Hulk", heroes_info)
    cap = Hero("Captain America", heroes_info)
    thanos = Hero("Thanos", heroes_info)
    int_dict = {hulk.name: hulk.intelligence, cap.name: cap.intelligence, thanos.name: thanos.intelligence}
    print(f"Самый умный среди героев {', '.join(int_dict)} является {max(int_dict, key=int_dict.get)} "
          f"с показателем интеллекта {int_dict[max(int_dict, key=int_dict.get)]}.")


if __name__ == '__main__':
    main()
