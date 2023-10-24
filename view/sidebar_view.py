import streamlit as st
import streamlit.components.v1 as components



class Sidebar_view:
    def __init__(_self,init_control) -> None:
        # scraperオブジェクト
        _self.init_control = init_control
        # 未選択
        _self.UNSELECT = ['--']
        # dbに記録されている一番過去の日にち
        _self.START_YEAR = _self.init_control.db_old_info()
        # dbに記録されている一番最新の日にち
        _self.NOW_DATE = _self.init_control.db_now_info()
        # 各月の日数
        _self.DAYS_MAX = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


    # 検索ボタンが押されたときの処理(コールバック関数)
    def colled_search(_self,year,month,day) -> None:
        
        if year != _self.UNSELECT[0] and month != _self.UNSELECT[0] and day != _self.UNSELECT[0]:
            # コントローラ(ex_control.py)のex_history_getメソッドが選択した日付を問い合わせ.結果をhis_dictに代入
            his_dict = _self.init_control.ex_history_get(year,month,day)
            if his_dict == 'error':
                components.html('<script> alert("選択された年月日には、データが存在しません");</script>')
            else:
                # home_pageの状態更新
                st.session_state.home_page = 'invisible'
                st.session_state.selection = {'year':year,'month':month,'day':day,'csv':his_dict['csv'],'table_html':his_dict['table_html']}
                
        else:
            components.html('<script> alert("未選択の項目があります。西暦、月、日付すべて選択してください。");</script>')
        

    # うるう年判定メソッド
    @st.cache_data()
    def leep_year(_self,year) -> list:
        return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)
    
    @st.cache_data()
    def setting_days(_self,year,month) -> list:
        # 2月が選択されたならば
        if month == 2:
            if _self.leep_year(year):
                # うるう年ならば29日までオプション作成
                return ['--'] + list(range(1,29+1)) 
            else:
                # うるう年でなければ28日までオプション作成
                return ['--'] + list(range(1,28+1)) 
        else:
            # 2月が選択されていなければ、DAYS_MAXの(month+1)番目までオプション作成
            return ['--'] + list(range(1,_self.DAYS_MAX[month-1]+1)) 
        
    def sidebar_display(_self) -> None:

        # 選択できる西暦リスト作成
        years = list(range(_self.START_YEAR,_self.NOW_DATE.year+1)) + _self.UNSELECT

        # 月リスト作成
        month = _self.UNSELECT + list(range(1,_self.NOW_DATE.month+1))  

        # 年、月、最新のものから選びやすいように逆順にする
        years.reverse()
        
        
        st.sidebar.markdown('## 過去の為替情報')
        # コンボボックス、検索ボタン配置
        year_selector = st.sidebar.selectbox('年',years)
        month_selector = st.sidebar.selectbox('月',month)

        # 西暦と月が選択されたかどうかで日付セレクトボックス表示
        if year_selector != _self.UNSELECT[0] and month_selector != _self.UNSELECT[0]:
            # 選んだ月と年が現在であれば、日付のセレクトボックスを現在までの日にちに設定
            if _self.NOW_DATE.year == year_selector and _self.NOW_DATE.month == month_selector:
                days = _self.UNSELECT + list(range(1,_self.NOW_DATE.day+1)) 
            else:
                days = _self.setting_days(year_selector,month_selector)
            # 日付を最新のものから選びやすいように逆順にする
            
            day_selector = st.sidebar.selectbox('日',days)

            # 検索ボタン配置、押された時の処理をon_cllickに登録
            s_btn = st.sidebar.button('検索')
                    
            if s_btn:
                _self.colled_search(year_selector,month_selector,day_selector)
            else:
                pass
        
          
