"""
a = {
    "name": "Home",
    "routes": [
        {
            "length": 5,
            "destionation": {
                "name": "School",
                "routes": [
                    {
                        "length": 5,
                        "destination": {
                            "name": "Home",
                            "routes": []
                        }
                    }
                ]
            }
        },
        {
            "length": 3,
            "destionation": {
                "name": "Park",
                "routes": []
            }
        },
        {
            "length": 2,
            "destionation": {
                "name": "Mall",
                "routes": []
            }
        }
    ]
}
"""
class Location:
    def __init__(self, name):
        self.name = name
        self.routes = []

    def link_route(self, destination, length):
        self.routes.append({
            "length": length,
            "destination": destination
        })
        destination.routes.append({
            "length": length,
            "destination": self
        })

    def show_all_routes(self):
        print(f"From '{self.name}' you can go to: ")
        for route in self.routes:
            print(f'-> {route["destination"]} - {route["length"]} km')

    def __str__(self):
        # Special method that knows what to do with this object when you call str method on it
        return self.name

    def __repr__(self):
        return self.name




home = Location("Home")
school = Location("School")
park = Location("Park")
shop = Location("Shop")
mall = Location("Mall")

home.link_route(school, 5)
home.link_route(park, 3)
home.link_route(mall, 2)
school.link_route(park, 1)
school.link_route(shop, 3)

shop.link_route(park, 4)
shop.link_route(mall, 1)

park.link_route(mall, 3)

# shop.link_route(school, 3)
# park.link_route(school, 1)
# park.link_route(shop, 4)
# park.link_route(home, 3)
# school.link_route(home, 5)

# mall.link_route(home, 2)
# mall.link_route(park, 3)
# mall.link_route(shop, 1)


home.show_all_routes()
school.show_all_routes()
park.show_all_routes()
shop.show_all_routes()
mall.show_all_routes()
