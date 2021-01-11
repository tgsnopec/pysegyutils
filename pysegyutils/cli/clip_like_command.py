import os 
import click 

from ..ops import clip_as

@click.command(
    help="""Clip a given SEG-Y file like another
         """
)
@click.option('-i', '--input-file', required=True, 
               type=click.Path(exists=True), 
               help='Path of the input SEG-Y file')
@click.option('-as', '-grid-source-file', required=True, 
               type=click.Path(exists=True),
               help='Path of the SEG-Y file which specifies the surface grid')
@click.option('-o', '--output-file', required=True, 
               type=click.Path(exists=False), 
               help='Path of the SEG-Y output file')
@click.option('-iline', '--iline', required=False, 
              is_flag=False, default=9, show_default=True, 
              help='Byte location of the inline number in the header')
@click.option('-xline', '--xline', required=False, 
              is_flag=False, default=21, show_default=True, 
              help='Byte location of the crossline number in the header')
def clip_like(input_file, grid_source_file, output_file, iline, xline):
    
    try:
        clip_as(input_file, 
                grid_source_file, 
                output_file, 
                iline=iline,
                xline=xline)
    except Exception as e:
        raise e
