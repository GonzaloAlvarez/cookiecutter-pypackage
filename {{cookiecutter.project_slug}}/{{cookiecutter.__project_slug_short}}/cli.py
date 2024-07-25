"""Console script for {{cookiecutter.project_slug}}."""

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import sys
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}
{%- if cookiecutter.use_loguru == 'y' %}
from loguru import logger
from click_loguru import ClickLoguru

__program__ = '{{cookiecutter.__project_slug_short}}'
__version__ = '0.0.1'

log_format = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>\n"
click_loguru = ClickLoguru(__program__, __version__, stderr_format_func=lambda x: log_format)
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.group(invoke_without_command=True)
{%- if cookiecutter.use_loguru == 'y' %}
@click_loguru.logging_options
@click_loguru.stash_subcommand()
@click_loguru.init_logger(logfile=False)
{%- endif %}
@click.version_option(prog_name=__program__, version=__version__)
@click.pass_context
def cli(ctx, **kwargs):
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.__project_slug_short}}.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0

{%- endif %}

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def cli(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "{{cookiecutter.__project_slug_short}}.cli.main")
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit(cli(obj={})) # pragma: no cover
