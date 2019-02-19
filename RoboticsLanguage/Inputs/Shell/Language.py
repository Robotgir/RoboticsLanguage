#
#   This is the Robotics Language compiler
#
#   Language.py: Definition of the language for this package
#
#   Created on: 15 February, 2019
#       Author: Gabriel Lopes
#      Licence: license
#    Copyright: copyright
#

from RoboticsLanguage.Base.Types import arguments, optional, returns


language = {
  '{shell}script': {
    'definition': {
      arguments: arguments('anything'),
      returns: returns('nothing')
    },
    'output': {
      'Cpp': 'execute_shell("{{text}}")'
    }
  }
}
