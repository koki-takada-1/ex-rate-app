import streamlit as st

import ex_control
from view import his_page, main_view, sidebar_view


def main():
    # st.session_stateはstreamlitが動いている間、値をそのまま保持できる
    # 初期設定(session_stateの中に'root'というキーがなければ、初期化を開始)
    if 'root' not in st.session_state:
        # rootというキーを作成し、'done'を代入
        st.session_state.root = 'done'
        
        # ページのレイアウトをwideに設定
        st.set_page_config(layout="wide")
        
        # コントローラーをインスタンス化
        st.session_state.control = ex_control.ExControl()
        # usdテーブルをdbから取得
        st.session_state.df = st.session_state.control.ex_usd_get()
        # 起動したときのメインページが見える状態
        st.session_state.home_page = 'visible'
        # sidebarを表示するクラスをインスタンス化 実引数としてコントローラのインスタンスを代入
        # sideberのセレクトボックスで日付を選択したものをコントローラが受け取りdbに問い合わせするため
        st.session_state.sidebar = sidebar_view.Sidebar_view(st.session_state.control)
    
    # サイドバー表示
    st.session_state.sidebar.sidebar_display()
    
    # home_pageがvisibleならばメインページ表示
    if st.session_state.home_page == 'visible':
        main_view.main_page(st.session_state.df)
    # home_pageがinvisibleならば検索結果を表示 検索ボタンを押して無事検索できればhome_pageにinvisibleを代入
    else:
        # sidebar_view.pyで選択した項目をselectionに代入したものをselect_dictに代入
        select_dict = st.session_state.selection
        # his_page.pyのhistroy_page_display関数で検索結果を表示
        his_page.history_page_display(select_dict['csv'],select_dict['table_html'],select_dict['year'],select_dict['month'],select_dict['day'])

if __name__ == "__main__":
    main()