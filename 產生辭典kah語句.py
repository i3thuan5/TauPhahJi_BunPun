

from django.core.management.base import BaseCommand
from 用字 import 教典
from 用字 import 標點
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語服務.models import 訓練過渡格式
from 臺灣言語工具.語言模型.KenLM語言模型訓練 import KenLM語言模型訓練


class Command(BaseCommand):

    def handle(self, *args, **參數):
        su = set()
        ku = set()
        for tsuliau in 訓練過渡格式.objects.all():
            ku.add(tsuliau.文本)
            for 詞物件 in 拆文分析器.分詞句物件(tsuliau.文本).網出詞物件():
                for 字物件 in 詞物件.篩出字物件():
                    if not 教典.有這个字無(字物件) and not 標點.有這个字無(字物件):
                        break
                else:
                    su.add(詞物件.看分詞())
        with open("su.txt", 'w') as tong:
            print('\n'.join(sorted(su)), file=tong)
        with open("ku.txt", 'w') as tong:
            print('\n'.join(sorted(ku)), file=tong)
