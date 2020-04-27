import click 

from .average_command import add 

@click.group()
def cli():
    """
    Command Line Interface (CLI) for pysegyutils.
    """
    pass 

def add_commands(cli):
    cli.add_command(add)

add_commands(cli)
