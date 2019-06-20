from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 產生辭典 import 用字會使無


class 用字標準試驗(TestCase):
    def tearDown(self):
        self.assertEqual(用字會使無(拆文分析器.建立詞物件(self.漢, self.羅)), self.結果)

    def test_教典用字(self):
        self.漢 = '媠'
        self.羅 = 'suí'
        self.結果 = True

    def test_標點(self):
        self.漢 = '，'
        self.羅 = ','
        self.結果 = True

    def test_違法攏全型標點(self):
        self.漢 = '，'
        self.羅 = '，'
        self.結果 = False

    def test_羅馬字(self):
        self.漢 = 'uán-na'
        self.羅 = 'uán-na'
        self.結果 = True

    def test_華文(self):
        self.漢 = '一路'
        self.羅 = '一路'
        self.結果 = False

    def test_英文(self):
        self.漢 = 'Taigi'
        self.羅 = 'Taigi'
        self.結果 = False


class 無對照試驗(TestCase):
    def tearDown(self):
        self.assertEqual(用字會使無(拆文分析器.建立詞物件(self.漢)), self.結果)

    def test_教典用字(self):
        self.漢 = '媠'
        self.結果 = False
