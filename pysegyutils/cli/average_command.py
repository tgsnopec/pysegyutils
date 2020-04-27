import os 
import click 

from ..ops import add 

@click.command(
    help="""Add/average two or more SEG-Y files.
         """
)
@click.option('-i', '--input-files', required=True, 
              is_flag=False, metavar='<comma-separated-list>', type=click.STRING, 
              help='Path of the input SEGY-Y files')
@click.option('-o', '--output-file', required=True, 
              type=click.Path(writable=True, exists=False), 
              help='Path of the output SEG-Y file')
@click.option('-average', '--average', required=False,
              is_flag=True, default=False, show_default=True,  
              help='Flag to indicate averaging')
@click.option('-iline', '--iline', required=False, 
              is_flag=False, default=9, show_default=True, 
              help='Byte location of the inline number in the header')
@click.option('-xline', '--xline', required=False, 
              is_flag=False, default=21, show_default=True, 
              help='Byte location of the crossline number in the header')
def add(input_files, output_file, average, iline, xline):
    
    # Parse the string to get a list of files
    input_file_list = [c for c in input_files.split(',')]

    # Verify if all the files exist
    for entry in input_file_list:
        if not os.path.isfile(entry):
            error_message = f'File {entry} does not exist.'
            raise FileNotFoundError(error_message)
    
    # Call add function 
    try:
        add(input_file_list, output_file, average=average, iline=iline, xline=xline)
    except Exception as e: 
        raise e 
