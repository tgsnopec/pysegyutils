import os
import click 

from ..ops import clip_file 

@click.command(
    help="""Clip a given SEG-Y file.
         """
)
@click.option('-i', '--input-file', required=True, metavar='FILE', 
              type=click.Path(exists=True, dir_okay=False), 
              help='Path of the input SEG-Y file')
@click.option('-o', '--output-file', required=True, metavar='FILE', 
              type=click.Path(writable=True, file_okay=True, dir_okay=False), 
              help='Path of the output SEG-Y file')
@click.option('-depth', '--depth-range', required=False, metavar='TUPLE',
              is_flag=False, default=None, show_default=True, 
              type=(int, int), help='Depth range for clipping')
@click.option('-iline', '--iline', required=False, 
              is_flag=False, default=9, show_default=True, 
              help='Byte location of the inline number in the header')
@click.option('-xline', '--xline', required=False, 
              is_flag=False, default=21, show_default=True, 
              help='Byte location of the crossline number in the header')
def clip(input_file, output_file, depth_range, iline, xline):
    pass
