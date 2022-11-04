import click
from plugins.cli import pass_context
from cookiecutter.main import cookiecutter
# from cookicutter.exceptions import OutputDirExistsException
import json


@click.command('cookiecutter', short_help='Shows file changes.')
@click.option('--template_path', '-a', help='The path to directory which holds the template project and cookiecutter json')
@pass_context
def cli(ctx, template_path):
    cookiecutter(
    f"templates/{template_path}",
    no_input=True,
    overwrite_if_exists=True
)

# @click.command('cookiecutter', short_help='Shows file changes.')
# @click.option('--template_path', '-a', help='The path to directory which holds the template project and cookiecutter json')
# @click.option('--template_name', '-n', help='The name of config file which holds the template project and cookiecutter json')
# @pass_context
# def cli(ctx, template_path, template_name):

#     with open(f"templates/{template_path}/{template_name}") as jfile:
#         cust_context = json.load(jfile)
#         print(cust_context)

#     cookiecutter(f"templates/{template_path}",
#     extra_context=cust_context,
#     output_dir="root",
#     no_input=True
# )