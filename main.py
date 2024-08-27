import EndpointTester
import SubdomainEnum
import argparse
import Database
from random_word import RandomWords



parser = argparse.ArgumentParser(
                    prog='Subto',
                    description='Discover Possible Subdomain Takeovers!')

parser.add_argument('-t', '--target', type=str, help='Insert Target separated by comma') 
parser.add_argument('-f', '--file', type=str, help='Insert Target from a file (One target each line)')
parser.add_argument('-r', '--register', action='store_true', help='Register a user')
parser.add_argument('-n', '--name', type=str, help='Set Scan name')
parser.add_argument('-ls', '--list-scan', action='store_true', help='Set Scan name') 
parser.add_argument('-sr', '--scan-result', type=int, help='Set Scan name') 
args = parser.parse_args()

targets = []

if args.target:
    targets += args.target.split(',')
if args.file:
    with open(args.file, 'r') as file:
        targets += [line.strip() for line in file]
if not args.name:
    r = RandomWords()
    ScanName = r.get_random_word() + r.get_random_word() + r.get_random_word()
else:
    ScanName = args.name

def main() -> None:
    AuthenticationResult, username = Database.Auth(args.register)

    if AuthenticationResult:
        if targets:
            SubDomainsWithDups = SubdomainEnum.runScan(targets, ScanName)
            SubDomains = list(set(SubDomainsWithDups))
            TestedSubs = []

            for SubDomain in SubDomains:
                TestedSubs.append(EndpointTester.TestEndpoint(SubDomain))
            
            ScanId = Database.RegisterScan(username, ScanName)
            
            for Tested in TestedSubs:
                if Tested[0] == False:
                    fing = "None"
                    vuln = False
                else:
                    fing = Tested[1]
                    vuln = Tested[1]['vulnerable']

                Database.RegisterScanResult(ScanId, Tested[2], fing, vuln)
            
            print(f'Scan Successull, results saved in database with ID: {ScanId}')
        
        if args.list_scan:
            Database.GetUserScans(username)
        
        if args.scan_result:
            Database.GetScanResults(args.scan_result)

if __name__ == '__main__':
    main()