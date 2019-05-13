import boto3

session = boto3.Session(profile_name='personal-practice')
ec2 = session.client('ec2')

custom_filter = [{
    'Name':'tag:Project',
    'Values': ['acloudguru']}]


response = ec2.describe_instances(Filters=custom_filter)


for i in response['Reservations'][0]['Instances']:
    print(i['InstanceId'])
