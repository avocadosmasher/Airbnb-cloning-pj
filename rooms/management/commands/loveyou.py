from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "Test command"

    def add_arguments(self, parser):
        parser.add_argument("--times", help="Test Command2")

    print("Hello")

    def handle(self, *args, **options):
        print(args, options)
        print("hello")
