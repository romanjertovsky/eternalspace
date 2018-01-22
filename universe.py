import hashlib
import math


class Universe:
    _seed = 'huipizdadjigurda'  # unique key of whole Universe
    _divisor = 4294967295  # 4294967295 = 0xffffffff = last 8 symbols of hash
    _density = 100

    _G = 6.67408e-11  # Universal Gravitational Constant

    def md5(self, string):
        return hashlib.md5(string.encode('utf-8')).hexdigest()

    def hash_to_int(self, the_hash, min_int, max_int):
        return round((int(the_hash[-8:], 16) / self._divisor) * max_int + min_int)

    def get_sector(self, any_x, any_y):
        """
         start_x, start_y - ANY coordinates of ANY sector
        """
        sector = []
        corner = self.get_corner(any_x, any_y)
        sector_coord = '{}:{}'.format(corner[0], corner[1])
        cur_hash = self.md5(sector_coord + self._seed)
        planet_count = self.hash_to_int(cur_hash, 10, 100)

        for i in range(planet_count):
            cur_hash = self.md5(cur_hash)
            x = ((self.hash_to_int(cur_hash, 0, 1000)) + abs(corner[0])) * (-1 if any_x < 0 else 1)

            cur_hash = self.md5(cur_hash)
            y = ((self.hash_to_int(cur_hash, 0, 1000)) + abs(corner[1])) * (-1 if any_y < 0 else 1)

            sector.append([x, y])

        return sector

    @staticmethod
    def get_corner(any_x, any_y):
        # print(any_x, any_y)
        """
        x, y - coordinates of planet.
        Will returned coordinates of sector corner neatest to zero
        It so happened that from this corner starts generating of sector.
        """
        # +1  or -1 to the 1001 instead 1000
        # to avoid the same corners, for ex.: 1000:1000 and -1000:-1000 without +1 will be 0:0
        any_x = int(any_x / 1000) * 1000 + (-1 if any_x < 0 else 1)
        any_y = int(any_y / 1000) * 1000 + (-1 if any_y < 0 else 1)
        return [any_x, any_y]

    def get_visible_planets(self, own_x, own_y, radar_range):
        """
        x, y - coordinates of your planet.
        will returned list with coordinates of planets in field of view
        """
        visible_sectors = self.get_visible_sectors(own_x, own_y, radar_range)
        all_planets = []
        for sector in visible_sectors:
            all_planets.extend(self.get_sector(sector[0], sector[1]))

        visible_planets = []
        for planet in all_planets:
            distance = self.get_distance(own_x, own_y, planet[0], planet[1])
            if distance < radar_range:
                visible_planets.append(planet)
        visible_planets.sort()
        return visible_planets

    def get_visible_sectors(self, own_x, own_y, radar_range):
        first_sector = self.get_corner(own_x - radar_range, own_y - radar_range)
        last_sector = self.get_corner(own_x + radar_range, own_y + radar_range)

        visible_sectors = []

        y = first_sector[1]
        while y <= last_sector[1]:
            x = first_sector[0]
            while x <= last_sector[0]:
                visible_sectors.append([x, y])
                x = self.get_corner(x + 1000, y)[0]
            y = self.get_corner(x, y + 1000)[1]

        return visible_sectors

    def get_distance(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def check_planet(self, x, y):
        # If planet exist return True, else False
        if [x, y] in self.get_sector(x, y):
            return True
        else:
            return False

    def get_planet(self, x, y):
        if not self.check_planet(x, y):
            return None

        planet_coord = '{}:{}'.format(x, y)

        cur_hash = self.md5(planet_coord + self._seed)
        print(cur_hash)
        mass = self.hash_to_int(cur_hash, 1e23, 9.972e24)  # Kg

        #cur_hash = self.md5(cur_hash)
        print(cur_hash)
        radius = self.hash_to_int(cur_hash, 2000000, 8500000)  # Meters

        cur_hash = self.md5(cur_hash)
        print(cur_hash)
        g = round((self._G * (mass / (radius ** 2))), 2)  # Acceleration of gravity, m/sec

        cur_hash = self.md5(cur_hash)
        print(cur_hash)
        av_t = self.hash_to_int(cur_hash, -200, 350)  # Average temperature, Celsius

        planet = {
            'M': ['{:.4e}'.format(mass), 'Mass (Kg)'],
            'R': [radius, 'Radius (m)'],
            'g': [g, 'Acceleration g (m/s)'],
            'av_t': [av_t, 'Average temperature (c°)'],
        }

        return planet
