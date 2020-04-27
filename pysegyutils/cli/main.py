import click 

from .average_command import add 
from .negate_command import negate 

@click.group()
def cli():
    """
    Command Line Interface (CLI) for pysegyutils.
    """
    pass 

def add_commands(cli):
    cli.add_command(add)
    cli.add_command(negate)

add_commands(cli)
