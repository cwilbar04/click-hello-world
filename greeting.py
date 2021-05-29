import click

@click.command()
@click.option('--name', prompt=True)
@click.option('--excited/--not-excited',default=False)
@click.option('--spanish',is_flag=True)
@click.option('--shout',is_flag=True)
def hello(name,excited,spanish,shout):
    # Defualt settings
    punctuation = '.'
    greeting = 'Hello'
    
    # Change punctuation if excited
    if excited:
        punctuation = '!'

    # Change greeting if Spanish
    if spanish:
        greeting = 'Hola'

    # All upper case if shout
    if shout:
        name = str.upper(name)
        greeting = str.upper(greeting)


    message = f'{greeting} {name}{punctuation}'
    click.echo(message)

if __name__ == '__main__':
    hello()