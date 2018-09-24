#
#   This is the Robotics Language compiler
#
#   Parameters.py: Definition of the parameters for this package
#
#   Created on: 05 September, 2018
#       Author: Gabriel Lopes
#      Licence: license
#    Copyright: copyright
#
from RoboticsLanguage.Base.Types import optional, arguments, returns


language = {
    'node': {
        'definition': {
            'optional': {
                'events': optional('anything', None)
            },
        },
    },

    'when': {
        'definition': {
            'arguments': arguments('boolean anything'),
            'returns': returns('nothing')
        }
    }
}
