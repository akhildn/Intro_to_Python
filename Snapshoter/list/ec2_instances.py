import boto3
import click

session = boto3.Session(profile_name='personal-practice')
ec2 = session.resource('ec2')


def filter_instances(project):
    instances = []
    if project:
        ec2_filter = [{
            'Name': 'tag:Project',
            'Values': [project]
        }]

        instances = ec2.instances.filter(Filters=ec2_filter)
    else:
        instances = ec2.instances.all()
    return instances


@click.group()
def ls_instances():
    """Command for instances"""


@ls_instances.command('stop')
@click.option('--project', default=None,
              help='Stop instances by project tag')
def stop_instances(project):
    """Stop EC2 instances"""
    start_or_stop_instances(project, 'stop')


@ls_instances.command('start')
@click.option('--project', default=None,
              help='Start instances by project tag')
def start_instances(project):
    """Stop EC2 instances"""
    start_or_stop_instances(project, 'start')


def start_or_stop_instances(project, action):
    instances = filter_instances(project)

    for i in instances:
        if action == 'start':
            print("Starting {0}...".format(i.id))
            i.start()
        elif action == 'stop':
            print("Stopping {0}...".format(i.id))
            i.stop()


@ls_instances.command('list')
@click.option('--project', default=None,
              help="List instances of a project, i.e. instances with (tag Project:<name>")
def list_instances(project):
    """lists ec2 instances in a region"""

    instances = filter_instances(project)

    for i in instances:
        tags = {t['Key']: t['Value'] for t in i.tags or []}
        print(','.join((
            i.id,
            i.instance_type,
            i.state['Name'],
            tags.get('Project', '<no project>')
        )))


if __name__ == '__main__':
    ls_instances()
