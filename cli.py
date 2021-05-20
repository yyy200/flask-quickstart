import click
import os

"""
TODO
    generate --> create new template, module, layout, stylesheet, controller
    new --> set up new project
    add --> add new dependency to virtualenv
    run --> run flask app
    serve --> run with GUNICORN
"""

__authors__ = ["Mohamed Ahmed", "Youssef El Mays"]

@click.group()
def cli():
    pass

@click.command()
@click.option('-t', '--template', 'filetype', flag_value="template")
@click.option('-m', '--module', 'filetype', flag_value="module")
@click.option('-s', '--stylesheet', 'filetype', flag_value="stylesheet")
@click.option('-c', '--controller', 'filetype', flag_value="controller")
@click.argument("name", required=True)
def generate(name, filetype):
    print(name, filetype)

@click.command()
@click.argument("modulename", required=True)
def add(modulename):
    print(modulename)

@click.command()
@click.option('-s', '--flask-session', prompt=True, type=bool, default=True)
@click.option('-m', '--flask-mail', prompt=True, type=bool, default=True)
@click.option('-b', '--bootstrap', prompt=True, type=bool, default=True)
@click.option('-f', '--font-awesome', prompt=True, type=bool, default=True)
@click.argument("name", required=True)
def new(name, bootstrap, font_awesome, flask_session, flask_mail):
    print(name, bootstrap, font_awesome)


@click.command()
@click.option('-p', "--port", type=int)
@click.option('-h', "--host")
def run(port, host):
    print(port, host)

@click.command()
def serve():
    click.echo()


cli.add_command(generate)
cli.add_command(add)
cli.add_command(new)
cli.add_command(run)

if __name__ == "__main__":
    cli()