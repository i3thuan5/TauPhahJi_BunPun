

from django.core.management.base import BaseCommand
from 臺灣言語服務.models import 訓練過渡格式


class Command(BaseCommand):

    def handle(self, *args, **參數):
        ku = set()
        for tsuliau in 訓練過渡格式.objects.all():
            ku.add(tsuliau.文本)
        with open("ku.txt", 'w') as tong:
            print('\n'.join(sorted(ku)), file=tong)
