import boto3
import json
import logging
import os
from dbconnection import get_crendentails,cred_env
def ebs_snapshot(region_src,accountid):
   ACCESS_KEY, SECRET_KEY, SESSION_TOKEN = cred_env(accountid)
   logger = logging.getLogger(__name__)
   # sqs = boto3.client('sqs')
   # region_src = region_src
   # print(region_src)
   # print(ACCESS_KEY, SECRET_KEY, SESSION_TOKEN )
   ec2 = boto3.resource('ec2')
   if SESSION_TOKEN:
      print("haiii")
      client_src = boto3.client('ec2',region_name=region_src,aws_access_key_id= ACCESS_KEY ,aws_secret_access_key=SECRET_KEY,aws_session_token=SESSION_TOKEN)
   else:   
      client_src = boto3.client('ec2',region_name=region_src,aws_access_key_id= ACCESS_KEY ,aws_secret_access_key=SECRET_KEY)
   response1 = client_src.describe_snapshots(OwnerIds=[
         'self'])        
   b = response1['Snapshots']
   if not b:
      print("No ebs snapshots available")
   else:   
   # print(b)
      c= len(b)
      d = []
      f = []
      g = []
      count=0
      client2 = boto3.client('organizations')   
      response2 = client2.list_accounts()
      if not response2["Accounts"]:
         print("No Accounts under organisation,cannot proceed further")
      else:   
         for i in range(len(response2["Accounts"])):   
            f.append(response2["Accounts"][i]["Id"])
         print(f)   

         for i in range(c):
            d.append(b[i]['SnapshotId'])
         print(d)
         for i in d:    
            snapshot = ec2.Snapshot(i)
            response = snapshot.describe_attribute(
               Attribute='createVolumePermission',
               DryRun=False)
            if (response['CreateVolumePermissions'])!= []:
               for j in f:
                  for i in range(len(response['CreateVolumePermissions'])):
                     if(response['CreateVolumePermissions'][i]["UserId"]) != j:
                        #  print(response['SnapshotId'])
                        count = count + 1 
                        if (count == len(f)):
                           g.append(response['SnapshotId'])
               count = 0
      print(g)         
         # queue_url = 'https://sqs.us-east-1.amazonaws.com/126806377151/rks-test'
         # queue_url = input("please enter the queue url: ")
         # str = ' , '.join(map(str,g))
         # # for i in g:
         # response = sqs.send_message(
         #       QueueUrl=queue_url,
         #       # DelaySeconds=10,
         #       MessageAttributes={
         #          'Title': {
         #                'DataType': 'String',
         #                'StringValue': 'The following snapshots that are not authenticated with aws accounts'
         #          }
         #       },
         #       MessageBody = str
         #    )
         # print("The following snapshots that are not authenticated with aws accounts\n ", str)                       
#    print(response['MessageId'])
   # print(response)

# messages = sqs.receive_message(QueueUrl=queue_url,MaxNumberOfMessages=1, WaitTimeSeconds=1)
# response = sqs.receive_message(
#     QueueUrl=queue_url,
#     AttributeNames=[
#         'SentTimestamp'
#     ],
#     MaxNumberOfMessages=1,
#     MessageAttributeNames=[
#         'All'
#     ],
#     VisibilityTimeout=0,
#     WaitTimeSeconds=0
# )
# msg=response['Messages'][0]
# print(msg)
# print(messages)
# for mgs in messages:
#        print(mgs.id)
# print ("Queue info : {}".format(messages))
# print(messages['Messages'][0])

# while len(messages) > 0:
   #  for message in messages:
   #      mail_body = json.loads(message.body)
   #      print("E-mail sent to: %s" % mail_body['to'])
   #      email = EmailMessage(mail_body['subject'], mail_body['message'], to=[mail_body['to']])
   #      email.send()
   #      message.delete()   
# for msg in messages:
#    logger.info("Received message: %s: %s", msg.message_id, msg.body)
