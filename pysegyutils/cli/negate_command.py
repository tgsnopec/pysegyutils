import os
import click 

from ..ops import negate_file  

@click.command(
    help="""Negate a given SEG-Y file.
         """
)
@click.option('-i', '--input-file', required=True, metavar='FILE', 
              type=click.Path(exists=True, dir_okay=False), 
              help='Path of the input SEG-Y file')
@click.option('-o', '--output-file', required=True, metavar='FILE', 
              type=click.Path(writable=True, file_okay=True, dir_okay=False), 
              help='Path of the output SEG-Y file')
@click.option('-iline', '--iline', required=False, 
              is_flag=False, default=9, show_default=True, 
              help='Byte location of the inline number in the header')
@click.option('-xline', '--xline', required=False, 
              is_flag=False, default=21, show_default=True, 
              help='Byte location of the crossline number in the header')
def negate(input_file, output_file, iline, xline):

    try:
        negate_file(input_file, output_file, iline=iline, xline=xline)
    except Exception as e:
        raise e
