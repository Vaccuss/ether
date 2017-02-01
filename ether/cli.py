import click
from build_pkg import build
from upload_pkg import upload
from deploy_pkg import deploy

@click.group()
def main():
    pass


# Build command (builds the zip file into .build folder)
main.add_command(build)
# Upload command (uploads to S3)
main.add_command(upload)
# Version command (Lambda versions)
main.add_command(deploy)






"""
@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('cmd', default='world', required=False)
def main(cmd, as_cowboy):
    ""Ether is a opinionated AWS cli to help organise lambda code management, deployment and testing""
    if cmd == 'bob':
        bob()
    else:
        greet = 'Howdy' if as_cowboy else 'Hello'
        click.echo('{0}, {1}.'.format(greet, cmd))

def bob():
    print("fuck bobo")
    print("fuck bob")
"""