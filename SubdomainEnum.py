from typing import List
import bbot.core.event
import bbot.modules
import bbot.scanner
import logging
import bbot

#Disable logging info in terminal
logging.getLogger('bbot').setLevel(0)

def GetSDEModules() -> list[str]:
    '''
    Returns name of all subdomain enumeration related modules available on bbot.
    '''
    try:
        ScanModules = bbot.configurator.module_loader.filter_modules(mod_type='scan')
        SubEnumModules = []
        
        for Module in ScanModules:
            Name, Properties = Module
        
            if 'subdomain-enum' in Properties['flags']:
                SubEnumModules.append(Name)
        
        return SubEnumModules
    
    except Exception:
        print("An error occured while loading some modules, check you connection")
        exit(1)


def getScanner(targets, name) -> bbot.scanner.Scanner :
    '''
    Return the prepared scanner object.
    '''
    SDScanner = bbot.scanner.Scanner(*targets, modules=GetSDEModules(), name=name)
    return SDScanner
    

def runScan(targets, name) -> List[str]:
    SubDomains = []
    PreparedScanner = getScanner(targets, name)
    
    try:
        for event in PreparedScanner.start():
            if type(event) == bbot.core.event.base.DNS_NAME:
                if 'in-scope' in event.tags:
                    print(f'found subdomain in scope: {event.data}')
                    SubDomains.append(event.data)

        print(f"Found {len(SubDomains)} Subdomains!")
        return SubDomains
        
    except Exception as e:
        print(f"An error occured {e}")
