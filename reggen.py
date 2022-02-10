#!/usr/bin/env python3

from atexit import register
from nis import match
import yaml
import re
from sys import argv
import os

def print_help():
    print(f'''Usage: {argv[0]} input_file [output_file]
    if no output file is provided, output filename will be th same as the input, with .md extension''')

def my_construct_mapping(self, node, deep=False):
    data = self.construct_mapping_org(node, deep)
    return {(str(key) if isinstance(key, int) else key): data[key] for key in data}

def main():
    if len(argv) not in [2, 3]:
        print_help()
        exit(-1)
    if argv[1] == '-h' or argv[1] == '--help':
        print_help()
        exit(0)

    infile = argv[1]

    if len(argv) == 3:
        outfile = argv[2]
    else:
        outfile = os.path.splitext(infile)[0] + '.md'
    # print(infile)

    with open(infile, 'r') as fp:
        yaml.SafeLoader.construct_mapping_org = yaml.SafeLoader.construct_mapping
        yaml.SafeLoader.construct_mapping = my_construct_mapping
        # data = yaml.safe_load(fp)
        data = yaml.load(fp, Loader=yaml.loader.BaseLoader)

    # print(data)

    if 'register-width' not in data.keys():
        print('register-width missing in input file!')
        exit(-2)
    
    if 'registers' not in data.keys():
        print('registers missing in input file!')
        exit(-2)
    
    width = int(data['register-width'])
    registers = data['registers']

    outStr = '''<h1>Register Summary</h1>\n
<table>
<tr>
<th>Register<br>name</th>
<th>Address<br>(hex)</th>
'''
    for b in range(width):
        outStr += f'<th>bit<br>{width - 1 - b}</th>\n'
    outStr += '<th>Reset<br>value</th>\n<th>Access</th>\n</tr>\n'


    for regName in registers:
        reg = registers[regName]

        if 'address' not in reg.keys():
            print(f'address missing from register {regName}')
            exit(-2)
        if 'reset' not in reg.keys():
            print(f'reset value missing from register {regName}')
            exit(-2)
        if 'access' not in reg.keys():
            print(f'access missing from register {regName}')
            exit(-2)
        
        outStr += f'''<tr>
<td class="reggen_name">{regName}</td>
<td class="reggen_addr">{str(reg['address']).zfill(2).upper()}h</td>
'''
        bits = list(reg.keys())
        # for k in reg.keys():
        #     bits.append(str(k))
        bits.sort(reverse=True)

        cnt = 0

        for bit in bits:
            if bit == 'address' or bit == 'reset' or bit == 'desc' or bit == 'access':
                continue

            if not bool(re.match('^\d+(\-\d+)?$', bit)):
                print(f'invalid bit in register {regName}: {bit}')
                exit(-2)

            if '-' in bit:
                high = int(str(bit).split('-')[0])
                low = int(str(bit).split('-')[1])
                if low > high:
                    high, low = low, high
            else:
                high = low = int(bit)
            
            w = high - low + 1
            cnt += w

            if 'name' not in reg[bit].keys():
                print(f'bit {bit} has no name in register {regName}')
                exit(-2)

            outStr += f'<td class="reggen_bit" colspan="{w}">{reg[bit]["name"]}</td>\n'

        if cnt != width:
            print(f'incorrect register width {regName} ({cnt} instead of {width})')
            exit(-2)
        
        outStr += f'''<td class="reggen_reset">{str(reg['reset']).zfill(2).upper()}h</td>\n<td class="reggen_access">{reg['access']}</td>\n</tr>\n'''

    outStr += '</table>\n\n'
    # print(outStr)

    outStr += '\n<h1>Register description</h1>\n\n'

    for regName in registers:
        reg = registers[regName]

        if 'address' not in reg.keys():
            print(f'address missing from register {regName}')
            exit(-2)
        if 'reset' not in reg.keys():
            print(f'reset value missing from register {regName}')
            exit(-2)
        if 'access' not in reg.keys():
            print(f'access missing from register {regName}')
            exit(-2)
        if 'desc' not in reg.keys():
            print(f'description missing from register {regName}')
            exit(-2)

        outStr += f'''
<h2>{regName} - {str(reg['address']).zfill(2).upper()}h</h2>

<p>{reg['desc']}</p>

<p>Access: {reg['access']}</p>

<p>Reset Value: {str(reg['reset']).zfill(2).upper()}h</p>

<table>
<tr>
'''
        for b in range(width):
            outStr += f'<th>bit<br>{width - 1 - b}</th>\n'
        outStr += '</tr>\n<tr>'
        bits = list(reg.keys())
        bits.sort(reverse=True)

        cnt = 0

        for bit in bits:
            if bit == 'address' or bit == 'reset' or bit == 'desc' or bit == 'access':
                continue

            if not bool(re.match('^\d+(\-\d+)?$', bit)):
                print(f'invalid bit in register {regName}: {bit}')
                exit(-2)

            if '-' in bit:
                high = int(str(bit).split('-')[0])
                low = int(str(bit).split('-')[1])
                if low > high:
                    high, low = low, high
            else:
                high = low = int(bit)
            
            w = high - low + 1
            cnt += w

            outStr += f'<td class="reggen_bit" colspan="{w}">{reg[bit]["name"]}</td>\n'

        if cnt != width:
            print(f'incorrect register width {regName} ({cnt} instead of {width})')
            exit(-2)
        
        outStr += f'''</tr>\n</table>\n'''


        for bit in bits:
            if bit == 'address' or bit == 'reset' or bit == 'desc' or bit == 'access':
                continue

            if not bool(re.match('^\d+(\-\d+)?$', bit)):
                print(f'invalid bit in register {regName}: {bit}')
                exit(-2)

            bitInfo = reg[bit]

            if 'name' not in bitInfo.keys():
                print(f'bit {bit} has no name in register {regName}')
                exit(-2)
            if 'desc' not in bitInfo.keys():
                print(f'bit {bit} has no description in register {regName}')
                exit(-2)
            

            outStr += f'''
<h3>bit {bit} - {bitInfo['name']}</h3>

<p>{bitInfo['desc']}</p>
'''
            if 'values'  in bitInfo.keys():
                outStr += f'''<table>
<tr>
<th>Value</th>
<th>Function</th>
</tr>
'''
                for v in bitInfo['values']:
                    outStr += f'''<tr>
<td class="reggen_bitval">{v}</td>
<td class="reggen_bitfn">{bitInfo['values'][v]}</td>
</tr>'''
                outStr += '</table>\n'

    with open(outfile, 'w') as fp:
        fp.write(outStr)

    return


if __name__ == '__main__':
    main()