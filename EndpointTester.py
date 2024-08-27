import requests
import json
import dns.resolver

CNAME = 0
NOANSWER = 1
NXDOMAIN = 2
ERROR = 3

with open('fingerprints.json', 'r') as file:
    fingerprints = json.load(file)

def CheckNXDOMAIN(domain):
    try:
        # Attempt to resolve the domain
        answers = dns.resolver.resolve(domain, 'A')
        return False  # If resolution is successful, NXDOMAIN is not returned
    except dns.resolver.NXDOMAIN:
        return True  # NXDOMAIN was returned, meaning the domain does not exist
    except (dns.resolver.Timeout, dns.resolver.NoNameservers, dns.exception.DNSException) as e:
        # Handle other possible DNS errors
        print(f"An error occurred: {e}")
        return False

def GetCNAME(domain) -> tuple:
    Res = dns.resolver.Resolver()
    Res.nameservers=['1.1.1.1','1.0.0.1','8.8.8.8']
    try:
        # Query the CNAME record
        answers = Res.resolve(domain, 'CNAME')
        for rdata in answers:
            return True, rdata.target.to_text().strip()
        
    except Exception as e:
        return False, ""

def TestEndpoint(target) -> tuple :
    print(f'Testing --> {target}')
    found, data = GetCNAME(target)
    NoTestPassed = True

    if found:
        try:
            response = requests.get(f'https://{data}')
            if response.encoding:
                bodyHTML = response.content.decode(response.encoding)
            else:
                bodyHTML = response.content.decode('utf-8')

        except Exception as e:
            print('####### \n\n')
            print(f"An error occurred: {e}")
            print('####### \n\n')

    
        for fingerprint in fingerprints:
            for CnameFingerpint in fingerprint['cname']:
                if CnameFingerpint in data and CnameFingerpint['nxdomain']:
                    if CheckNXDOMAIN(data):

                        NoTestPassed = False
                        return True, fingerprint, target
                        
            if fingerprint['fingerprint'] in bodyHTML:
                NoTestPassed = False
                return True, fingerprint, target
            
        if NoTestPassed:
            return False, "Not vulenrable", target

    else:
        return False, "No CNAME record found.", target