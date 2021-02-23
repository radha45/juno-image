import click
from ebs_snapshot_unmonitored_account import *
from scptest import input1
# import orgtest
CONTEXT_SETTINGS = dict(
    max_content_width=400,
)

@click.group(context_settings=CONTEXT_SETTINGS,help="type juno <cloud-provider-name> for example : juno aws")
def juno():
    pass

# @main.group()
# def juno():
#     pass

@juno.group(help="To deal with AWS policies",context_settings=CONTEXT_SETTINGS)
def aws():
    # aws_org()
    # print("hai")
    pass
@click.command(help="""
....explanation: Get the list of ebs snapshots that aren't authenticated with aws accounts \b""")
@click.argument('region_src')
@click.argument('accountid')
def ebs_snapshot_account(region_src,accountid):
    '''
To get the list of ebs snapshots that aren't authenticated with aws accounts
'''
    # region_src = region_src
    # print(region_src)
    
    ebs_snapshot(region_src,accountid)
    # print("hello")
# @aws.command(help="....explanation: Get the list of rds snapshots that aren't authenticated with aws accounts ")
# def rds_snapshot_account():
#     import rds_snapshot_unmonitored_account
@click.command()
@click.argument('name')
@click.argument('region')
@click.argument('identifiers')
@click.argument('option')
@click.argument('accountid')
@click.argument('description')
def scp_test(name,region,identifiers,option,accountid,description):
  input1(name,region,identifiers,option,accountid,description)
@juno.group(help="To deal with Azure policies")
def azure():
    pass    
@azure.command()
def azure_org():
    print("welcome to azure")

juno.add_command(azure)
juno.add_command(aws)
aws.add_command(ebs_snapshot_account)
# aws.add_command(rds_snapshot_account)
aws.add_command(scp_test)

azure.add_command(azure_org)

if __name__ == "__main__":
    juno()




