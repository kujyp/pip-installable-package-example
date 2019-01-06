import click


def main():
    cli()


@click.group()
def cli():
    """hello world package"""
    pass


@cli.command(short_help="say \"hello world!\"")
def world():
    """say \"hello world!\""""
    print("hello world!")


@cli.command(short_help="say \"hello ${name}!\"")
@click.argument('yourname')
def name(yourname):
    """say \"hello ${yourname}!\""""
    print("hello {}!".format(yourname))


if __name__ == '__main__':
    main()
