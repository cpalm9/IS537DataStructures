import inspect
import re


################################################
###   Serialization to JSON

TAB = '\t'

print("Level 1", TAB, 'Level 2', TAB,TAB, 'Level 3')
def to_json(obj, level=0):
    '''Serializes the given object to JSON, printing to the console as it goes.'''
    obj_type = obj.__dict__

    json = []

    for key, val in sorted(obj_type.items()):
        if isinstance(val, (int, float)):
            if val == True:
                json.append('\n{}\"{}\": {}'.format(TAB * level, key, 'true'))
            elif val == False:
                json.append('\n{}\"{}\": {}'.format(TAB * level, key, 'false'))
            else:
                json.append('\n{}\"{}\": {}'.format(TAB * level, key, val))
        elif isinstance(val, str):
            if "\\" in val:
                val = val.replace('\\', '\\\\')
                json.append('\n{}\"{}\": \"{}\"'.format(TAB * level, key, val))
            else:    
                val = val.replace('"', '\\"')
                json.append('\n{}\"{}\": \"{}\"'.format(TAB * level, key, val))

        elif val is None:
            json.append('\n{}\"{}\": {}'.format(TAB * level, key, 'null'))

        else:
            json.append('\n{}\"{}\": {}'.format(TAB * level, key, to_json(val, level + 1)))

    return '{}{}\n{}{}'.format('{', ','.join(json), (TAB * (level - 1)), '}')
