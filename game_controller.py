from welcome import greeting_screen
from profile import Profile
from universe import Universe
from output import msg_out
from checkinput import get_cmd, get_login
import re


class GameController:

    universe = object
    profile = object

    cmd_dict = {
        'help': 'Get this help',
        'radar': 'Get coordinates of planet where you are, and list of planets in range of vision.',
        'goto': 'Traveling on planet with coordinates. Use digits through colon, ex.: <goto 123:456>.',
        'password': 'Change your password.',
        'exit': 'Save and logout.',
        'explore': 'Explore the planet, on which you are.',

        # Below just an ideas, doesn't work!!!
        # 'message': 'leave a message on the planet. To read the left messages, use the command <explore>',
        # 'update': 'Level up your skills. To learn about existing use <help skills>',
        # 'mine': 'Mining of resources on the current planet.'
    }

    to_exit = False

    def __init__(self):
        greeting_screen()
        self.universe = Universe()
        self.profile = Profile()

    def act(self):

        cmd_string = get_cmd('Command: ')
        cmd = cmd_string.split()

        if cmd[0] in self.cmd_dict:
            try:
                eval('self.{0}(\'{1}\')'.format(cmd[0], cmd[1]))
            except IndexError:
                eval('self.{0}(None)'.format(cmd[0]))
        else:
            msg_out('Sorry, unknown command. Use <help>, please.', 'r')

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    #  Commands:
    #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # goto # # # # # # # # # # # # # # #
    def goto(self, params):

        if params is None:
            msg_out('Empty coordinates. Use <help>, please.', 'r')
            return
        pattern = r'^(\-?[0-9]+):(\-?[0-9]+)$'

        if re.match(pattern, params):
            req_coord = params.split(':')
            req_coord[0] = int(req_coord[0])
            req_coord[1] = int(req_coord[1])
        else:
            msg_out('Coordinates input error. Ex. use: <goto 123:456>, or with minus sign: <goto -123:-456>', 'r')
            return

        user_coord = self.profile.user_data['coord']
        distance = self.universe.get_distance(user_coord[0], user_coord[1], req_coord[0], req_coord[1])

        if distance > self.profile.user_data['radar']:
            msg_out('You can not fly that far!', 'r')
            return
        elif req_coord == user_coord:
            msg_out('You are already here. Use <radar> to discover visible planets, please.', 'r')
            return

        if self.universe.check_planet(req_coord[0], req_coord[1]):
            self.profile.user_data['coord'] = req_coord
            msg_out('You are successfully transferred to {}:{}.'.format(self.profile.user_data['coord'][0], self.profile.user_data['coord'][1]), 'y')
            self.profile.save_user_data()
        else:
            msg_out('{}:{} non-existent planet! Use <radar> please.'.format(req_coord[0], req_coord[1]), 'r')

    def radar(self, params):
        self_coord = self.profile.user_data['coord']
        radar_range = self.profile.user_data['radar']
        visible_planets = self.universe.get_visible_planets(self_coord[0], self_coord[1], radar_range)
        msg_out('You are on: {}:{}'.format(self_coord[0], self_coord[1]), 'y')
        for planet in visible_planets:
            msg_out('{}:{}'.format(planet[0], planet[1]), ('r' if self_coord == planet else 'y'))

    def password(self, params):
        password = get_login("Enter new password: ", 3, 12)
        self.profile.user_data['password'] = password
        self.profile.save_user_data()

    def help(self, params):
        msg_out('You can use this commands:', 'y')
        for key in sorted(self.cmd_dict):
            msg_out("  {} - {}".format(key, self.cmd_dict[key]), 'y')

    def exit(self, params):
        self.profile.save_user_data()
        msg_out('Switching the engines off...ok.', 'y', 3)
        self.to_exit = True

    def explore(self, params):
        self_coord = self.profile.user_data['coord']
        planet = self.universe.get_planet(self_coord[0], self_coord[1])
        if planet is None:
            msg_out('Nothing to explore! You are in open space!', 'r')
            return
        msg_out('Planet {}:{} parameters:'.format(self_coord[0], self_coord[1]), 'y')

        for key in sorted(planet):
            msg_out('{}: {}'.format(planet[key][1], planet[key][0]), 'y')
        msg_out('Messages on the planet:', 'b')


