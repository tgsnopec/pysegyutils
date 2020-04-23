import click 

@click.group()
def cli():
    """
    Command Line Interface (CLI) for pysegyutils.
    """
    pass 

def add_commands(cli):
    pass 

add_commands(cli)
