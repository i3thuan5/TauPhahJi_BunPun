

from django.core.management.base import BaseCommand
from 臺灣言語服務.models import 訓練過渡格式
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class Command(BaseCommand):

    def handle(self, *args, **參數):
        ku = set()
        for tsuliau in 訓練過渡格式.objects.all():
            ku.add(
                拆文分析器.分詞句物件(tsuliau.文本)
                .轉音(臺灣閩南語羅馬字拼音)
                .看分詞()
            )
        with open("ku.txt", 'w') as tong:
            print('\n'.join(sorted(ku)), file=tong)
