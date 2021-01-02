import typer
from ssg import Site

def main(source="content", dest="dist"):
  config = {'source':'souce', 'dest':'dest'}
  Site(**config).build()

  typer.run()