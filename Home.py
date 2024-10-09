import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("Giới thiệu")
st.sidebar.info(
    """
    - Web App URL: <https://streamlit.gishub.org>
    - GitHub lưu trữ: <https://github.com/funnyhop/NDVI_plant_health>
    """
)

st.sidebar.title("Liên hệ")
st.sidebar.markdown(
    """
    <div>
        <address>
            <strong><span>Trường đại học Cần Thơ</span></strong><br/>
            🏫Khu 2, Đ. 3/2, P. Xuân Khánh, <br/>
            Q. Ninh Kiều, TP. CT<br/>
            📞(+84) 372 232 899 <br>
            📧dhct@ctu.edu.vn <br><br>
        </address>
    </div>
    """,
    unsafe_allow_html=True
)
st.title("Ứng dụng NDVI trong đánh giá sức khỏe cây trồng")

st.markdown(
    """
    Ứng dụng chỉ số chuẩn hóa khác biệt thực vật (NDVI) để đánh giá tình trạng sức khỏe 
    cây lúa nước vùng Đồng Bằng Sông Cửu Long (tỉnh Kiên Giang) cách hiệu quả và chính xác.
    Thông qua dữ liệu vệ tinh Sentinel 2 sử dụng chỉ số NDVI để phát hiện sớm các vấn đề liên 
    quan đến sức khỏe cây trồng, cải thiện hiệu quả sản xuất thông qua giám sát và quản lý 
    tình trạng sức khỏe cây trồng, đánh giá mức độ xanh của cây trồng để tối ưu hóa được việc 
    sử dụng nước, phân bón. Từ đó giúp người nông dân và người quản lý đưa ra các quyết định 
    chính xác và kịp thời góp phần tăng năng suất và chất lượng cây trồng.
    """
)

st.info("Nhấp vào menu thanh bên trái để điều hướng đến các mục khác nhau.")

st.subheader("Timelapse của hình ảnh vệ tinh")
st.markdown(
    """
    Hoạt ảnh NDVI tua nhanh thời gian của một khu vực tỉnh Kiên Giang. 
"""
)

row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.image("https://raw.githubusercontent.com/funnyhop/NDVI_plant_health/refs/heads/master/imgs/normal_ndvi_timelapse.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/las_vegas.gif")

with row1_col2:
    st.image("https://github.com/giswqs/data/raw/main/timelapse/goes.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/fire.gif")
