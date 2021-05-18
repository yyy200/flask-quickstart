import click
import os

__author__ = "Youssef El Mays"

@click.command()
@click.argument("name", required=True)
@click.option()
def main(name):
    click.echo("{}".format(name))
    print("hello")

if __name__ == "__main__":
    main()