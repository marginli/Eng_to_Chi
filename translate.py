import streamlit as st
from deep_translator import GoogleTranslator

# 1. 設定網頁標題
st.title("🇺🇸 英文 -> 🇹🇼 繁體中文 翻譯機")

# 2. 建立側邊欄 (可選，讓介面更專業)
st.sidebar.header("使用說明")
st.sidebar.text("輸入英文句子，按下翻譯按鈕即可。")

# 3. 建立文字輸入框 (height設定高一點，方便輸入長文章)
# key="input_text" 是為了讓 Streamlit 辨識這個元件的狀態
text = st.text_area("請在下方輸入英文：", height=150, placeholder="Type something here...")

# 4. 建立翻譯按鈕
if st.button("開始翻譯"):
    if text:
        try:
            # 呼叫 Google 翻譯 (source='auto' 表示自動偵測，target='zh-TW' 表示繁體中文)
            translator = GoogleTranslator(source='auto', target='zh-TW')
            translation = translator.translate(text)
            
            # 5. 顯示結果
            st.success("翻譯結果：")
            st.markdown(f"### {translation}")
            
        except Exception as e:
            st.error(f"翻譯出錯了：{e}")
    else:
        st.warning("請先輸入文字再按按鈕喔！")

# 6. 加上分隔線
st.divider()
st.caption("由 Streamlit 與 deep-translator 強力驅動")
