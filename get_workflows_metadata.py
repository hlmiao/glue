import boto3
from botocore.exceptions import ClientError
import pprint

def get_resource_metadata_of_workflows():
   session = boto3.session.Session()
   glue_client = session.client('glue')
   try:
      list_of_workflows = glue_client.list_workflows()
      response = glue_client.batch_get_workflows( Names=list_of_workflows['Workflows'])

      return list_of_workflows, response
   except ClientError as e:
      raise Exception( "boto3 client error in get_resource_metadata_of_workflows: " + e.__str__())
   except Exception as e:
      raise Exception( "Unexpected error in get_resource_metadata_of_workflows: " + e.__str__())

a, b = get_resource_metadata_of_workflows()
#List of Workflows
pprint.pprint(a)
print('\n')

#Resource metadata of each Workflow
pprint.pprint(b)
