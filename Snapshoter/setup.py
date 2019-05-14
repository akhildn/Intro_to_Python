from setuptools import setup


setup(
    name='snapshoter',
    version='0.1',
    author_email='akhilnayabu@gmail.com',
    url='https://github.com/akhildn/Intro_to_Python/tree/master/Snapshoter',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
    [console_scripts]
    snappy=list.ec2_instances:cli
    '''
)
