

from django.core.management.base import BaseCommand
from 臺灣言語工具.語言模型.KenLM語言模型訓練 import KenLM語言模型訓練


class Command(BaseCommand):

    def handle(self, *args, **參數):
        KenLM語言模型訓練().訓練(
            ['ku.txt'],
            '語言模型資料夾',
            連紲詞長度=3,
            使用記憶體量='80%',
        )
