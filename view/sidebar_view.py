import streamlit as st
import streamlit.components.v1 as components



class Sidebar_view:
    def __init__(self,init_control) -> None:
        # scraperオブジェクト
        self.init_control = init_control
        # 未選択
        self.UNSELECT = ['--']
        # dbに記録されている一番過去の日にち
        self.START_YEAR = self.init_control.db_old_info()
        # dbに記録されている一番最新の日にち
        self.NOW_DATE = self.init_control.db_now_info()
        # 各月の日数
        self.DAYS_MAX = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


    # 検索ボタンが押されたときの処理(コールバック関数)
    def colled_search(self,year,month,day) -> None:
        
        if year != self.UNSELECT[0] and month != self.UNSELECT[0] and day != self.UNSELECT[0]:
            
            his_dict = self.init_control.ex_history_get(year,month,day)
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
    def leep_year(self,year) -> list:
        return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)
    
    @st.cache_data()
    def setting_days(self,year,month) -> list:
        # 2月が選択されたならば
        if month == 2:
            if self.leep_year(year):
                # うるう年ならば29日までオプション作成
                return ['--'] + list(range(1,29+1)) 
            else:
                # うるう年でなければ28日までオプション作成
                return ['--'] + list(range(1,28+1)) 
        else:
            # 2月が選択されていなければ、DAYS_MAXの(month+1)番目までオプション作成
            return ['--'] + list(range(1,self.DAYS_MAX[month-1]+1)) 
        
    def sidebar_display(self) -> None:

        # 選択できる西暦リスト作成
        years = list(range(self.START_YEAR,self.NOW_DATE.year+1)) + self.UNSELECT

        # 月リスト作成
        month = self.UNSELECT + list(range(1,self.NOW_DATE.month+1))  

        # 年、月、最新のものから選びやすいように逆順にする
        years.reverse()
        
        
        st.sidebar.markdown('## 過去の為替情報')
        # コンボボックス、検索ボタン配置
        year_selector = st.sidebar.selectbox('年',years)
        month_selector = st.sidebar.selectbox('月',month)

        # 西暦と月が選択されたかどうかで日付セレクトボックス表示
        if year_selector != self.UNSELECT[0] and month_selector != self.UNSELECT[0]:
            # 選んだ月と年が現在であれば、日付のセレクトボックスを現在までの日にちに設定
            if self.NOW_DATE.year == year_selector and self.NOW_DATE.month == month_selector:
                days = self.UNSELECT + list(range(1,self.NOW_DATE.day+1)) 
            else:
                days = self.setting_days(year_selector,month_selector)
            # 日付を最新のものから選びやすいように逆順にする
            
            day_selector = st.sidebar.selectbox('日',days)

            # 検索ボタン配置、押された時の処理をon_cllickに登録
            s_btn = st.sidebar.button('検索')
                    
            if s_btn:
                self.colled_search(year_selector,month_selector,day_selector)
            else:
                pass
        
          
