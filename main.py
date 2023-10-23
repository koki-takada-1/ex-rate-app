import streamlit as st

import ex_control
from view import his_page, main_view, sidebar_view


def main():
    # 初期設定(session_stateの中に'root'というキーがなければ、初期化を開始)
    if 'root' not in st.session_state:
        # rootというキーを作成し、'done'を代入
        st.session_state.root = 'done'
        
        # ページのレイアウトをwideに設定
        st.set_page_config(layout="wide")
        
        # コントローラー
        st.session_state.control = ex_control.ExControl()
        st.session_state.df = st.session_state.control.ex_usd_get()
    
        st.session_state.home_page = 'visible'
    
        st.session_state.sidebar = sidebar_view.Sidebar_view(st.session_state.control)
    
    st.session_state.sidebar.sidebar_display()
    
    if st.session_state.home_page == 'visible':
        main_view.main_page(st.session_state.df)
    else:
        select_dict = st.session_state.selection
        his_page.history_page_display(select_dict['csv'],select_dict['table_html'],select_dict['year'],select_dict['month'],select_dict['day'])

if __name__ == "__main__":
    main()