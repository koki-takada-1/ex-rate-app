# うるう年判定メソッド

def leep_year(year) -> list:
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


def setting_days(year,month) -> list:
    DAYS_MAX = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 2月が選択されたならば
    if month == 2:
        if leep_year(year):
            # うるう年ならば29日までオプション作成
            return ['--'] + list(range(1,29+1)) 
        else:
            # うるう年でなければ28日までオプション作成
            return ['--'] + list(range(1,28+1)) 
    else:
        # 2月が選択されていなければ、DAYS_MAXの(month+1)番目までオプション作成
        return ['--'] + list(range(1,DAYS_MAX[month-1]+1)) 