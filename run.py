'''
This python program invokes terraform script to create instances. 
Usage: python3 invoke.py -t <variables file name> -p <pattern name> -i -d(optional, for destroy action)
'''

#import argparse
import os
import sys
import json

# parser = argparse.ArgumentParser(description='Creates terraform workspaces and resources')
# parser.add_argument('-t', '--tfvars', required=True, help = "variables tfvars file name")
# parser.add_argument('-p', '--pattern', required=True, help = "pattern name")
# parser.add_argument('-i', '--instance', required=True, action='store_true')

# parser.add_argument('-d', '--destroy', required=False, action='store_true',help = "set the argument to destroy resource")

# args = parser.parse_args()


def get_resourcename(filename):
    with open(filename) as f:
        params = json.load(f)
    return(params)
params = get_resourcename("pipeline_parameters.json")
pattern = params["patternName"]
resourceName = params["resourceName"]
resourceAction = params["resourceAction"]

#varFileName = "tfvars\"+args.tfvars

rname = resourceName

print("rname: "+rname)
if resourceAction=="Create":
    msg = "Creating {} ".format(rname)
        
if resourceAction=="Destroy":
    msg = "Destroying {} ".format(rname)
try:
    print(msg)
except:
    sys.exit(1)
os.chdir("pattern/"+pattern)
initCommand = "terraform init -backend-config=\"key\"=\""+rname+"\""
applyCommand = "terraform apply -var-file=..\\..\\tfvars\\"+resourceName+".tfvars --auto-approve"
if resourceAction == "Destroy":
    print("Runnign command: " +initCommand)
    os.system(initCommand)
    os.system("terraform destroy  --auto-approve")
else:
    try:
        os.system("terraform  workspace new " + rname)
    except:
        print("Instance already exists. Please choose a different instance name")
    print("Runnign command: " +initCommand)
    os.system(initCommand)
    os.system(applyCommand)