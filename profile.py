import pickle
from checkinput import get_login
from output import msg_out


class Profile:

    user_data = {}

    default_user_data = {
        # also used as default if no key exist when
        # checking nonexistent keys in file for update
        # Be careful!
        'name': 'default_name',
        'password': 'default_pass',
        'radar': 300,  # field of view
        'coord': [0, 0]
    }

    def __init__(self):

        user_name = get_login("Enter your profile name (if no exist, will be created): ", 3, 10)

        try:  # Load user data
            msg_out('Searching your profile.')
            with open('profiles/{}.dat'.format(user_name), 'rb') as f:
                self.user_data = pickle.load(f)
            msg_out('Loading...ok. Checking name.')
            if self.user_data.get('name') == user_name:
                msg_out('Name...ok')
            else:
                msg_out('Profile name does not match file name. It can not be! O_o wtf', 'r')

            while True:
                password = get_login("Enter your password: ", 3, 12)
                if self.user_data.get('password') == password:
                    break
                else:
                    msg_out('Sorry. Wrong password. Access denied.', 'r')

        except FileNotFoundError:  # Creating new user data
            print('Profile "{}" not found. Creating new.'.format(user_name))
            self.user_data['name'] = user_name
            self.user_data['password'] = get_login("Enter your password: ", 3, 12)

            # Generating new coordinates:
            from random import randint, choice
            from universe import Universe
            temp_universe = Universe()
            area = temp_universe.get_sector(randint(-10000, 10000), randint(-10000, 10000))
            self.user_data['coord'] = choice(area)
            # GENERATE RANDOM SKILLS???

            from welcome import beginning_of_the_story
            beginning_of_the_story()

            self.save_user_data()

        #  Comparison default user_data with saved in file
        #  to delete outdated elements and add new.
        need_to_save = False
        for key in list(self.default_user_data):  # adding new default keys and default values
            if key not in self.user_data:
                self.user_data[key] = self.default_user_data[key]
                msg_out('Updating profile. Adding new keys with defaults.', 'y')
                need_to_save = True
        for key in list(self.user_data):  # removing old keys with values
            if key not in self.default_user_data:
                del self.user_data[key]
                msg_out('Updating profile. Removing outdated keys.', 'y')
                need_to_save = True
        if need_to_save is True:
            self.save_user_data()

        msg_out("Logged in. Welcome aboard, {}.".format(self.user_data['name']), 'y')
        msg_out('For use help type <help>', 'r')

    def save_user_data(self):
        msg_out('Saving profile...', 'y', 0.5)
        with open('profiles/{}.dat'.format(self.user_data['name']), 'wb') as f:
            pickle.dump(self.user_data, f)
        msg_out('Saving...ok', 'y')
