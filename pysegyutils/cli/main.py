import click 

from .average_command import add 
from .negate_command import negate 
from .clip_like_command import clip_like 

@click.group()
def cli():
    """
    Command Line Interface (CLI) for pysegyutils.
    """
    pass 

def add_commands(cli):
    cli.add_command(add)
    cli.add_command(negate)
    cli.add_command(clip_like)

add_commands(cli)
