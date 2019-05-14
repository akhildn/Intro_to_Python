import boto3
import botocore
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
def cli():
    """Main group"""


@cli.group('volumes')
def volumes():
    """Command for volumes"""


@volumes.command('list')
@click.option('--project', default=None,
              help='lists all volumes of the ec2 instances in the project')
def ls_volumes(project):
    """List EC2 Volumes"""
    instances = filter_instances(project)

    for i in instances:
        for v in i.volumes.all():
            print(",".join((
                v.id,
                i.id,
                v.state,
                str(v.size) + "gb",
                v.encrypted and "Encrypted" or "Not Encrypted"
            )))


@cli.group('instances')
def ls_instances():
    """Command for instances"""


@ls_instances.command('snapshot',
                      help='Create snapshots of all volumes')
@click.option('--project', default=None)
def create_snapshots(project):
    """Create snapshots for instances"""

    instances = filter_instances(project)

    for i in instances:
        print('Stopping instance {0}'.format(i.id))
        i.stop()
        i.wait_until_stopped()
        for v in i.volumes.all():
            print('Creating snapshot of {0}'.format(v.id))
            v.create_snapshot(Description="Created by python script")
        print('Starting instance {0}'.format(i.id))
        i.start()
        i.wait_until_running()
        print('instance {0} is running'.format(i.id))


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


@ls_instances.command('start')
@click.option('--project', default=None,
              help='Start instances by project tag')
def start_instances(project):
    """Stop EC2 instances"""

    instances = filter_instances(project)

    for i in instances:
        print("Starting {0}...".format(i.id))
        try:
            i.start()
        except botocore.exceptions.ClientError as e:
            print('Cloud not start instances {0}'.format(i.id) + str(e))
            continue


@ls_instances.command('stop')
@click.option('--project', default=None,
              help='Stop instances by project tag')
def stop_instances(project):
    """Stop EC2 instances"""

    instances = filter_instances(project)

    for i in instances:
        print("Stopping {0}...".format(i.id))
        try:
            i.stop()
        except botocore.exceptions.ClientError as e:
            print('Cloud not stop instances {0}'.format(i.id) + str(e))
            continue


if __name__ == '__main__':
    cli()
