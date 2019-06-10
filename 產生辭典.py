from 用字.教典規範 import 教典
from 用字.標點規範 import 標點
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


def 用字會使無(詞物件):
    for 字物件 in 詞物件.篩出字物件():
        if 教典.有這个字無(字物件):
            continue
        if 標點.有這个字無(字物件):
            continue
        if 字物件.型 == 字物件.音 and 字物件.音標敢著(臺灣閩南語羅馬字拼音):
            continue
        return False
    return True
