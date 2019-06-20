from 用字 import 教典
from 用字 import 標點
from 用字 import 甘字典
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from sys import stdout, stdin


def 用字會使無(詞物件):
    for 字物件 in 詞物件.篩出字物件():
        if 教典.有這个字無(字物件):
            continue
        if 標點.有這个字無(字物件):
            continue
        if 甘字典.有這个字無(字物件):
            continue
        if (
            字物件.型 == 字物件.音
            and not 字物件.敢是標點符號()
            and 字物件.音標敢著(臺灣閩南語羅馬字拼音)
        ):
            continue
        return False
    return True


def main():
    su = set()
    for tsua in stdin.readlines():
        for 詞物件 in 拆文分析器.分詞句物件(tsua.rstrip()).網出詞物件():
            if 用字會使無(詞物件):
                su.add(詞物件.看分詞())
    print('\n'.join(sorted(su)), file=stdout)


if __name__ == '__main__':
    main()
