# Public_299

# 1. Tổng quan

# 1.1 Mục đích tài liệu

- Tài liệu này được xây dựng nhằm mục đích mô tả thiết $\mathrm { k } \acute { \mathrm { e } }$ các chức năng đáp ứng yêu cầu nghiệp vụ đăng ký tuyển dụng cho bưu tá, nhân viên lái xe trên website: viettelpost.com.vn

# 1.2 Phạm vi

- Luồng nghiệp vụ được áp dụng cho chức năng đăng ký tuyển dụng trên web: https://viettelpost.com.vn/

# 1.3 Thuật ngữ và chữ viết tắt



# 1.4 Danh mục chức năng



# 2. THIẾT KẾ CHỨC NĂNG

# 2.1 Mô tả chung





<table><tr><td></td><td>2. Chon ing tuyén nhanh 3. Nhap thong tin ung tuyén 4. Click Dang ky 5. Hién thi popup dang ky thanh cong</td></tr><tr><td>Post- Condition(s)</td><td>1. Nguoi dung dang ky thong tin ung tuyén thanh cong 2. Du lieu nguoi dung dang ky day ve hé thong tuyén dung</td></tr></table>

# 2.2 Mô tả nghiệp vụ









<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1> Khong tiép nhan ho so co cungthong tin tuong tu)</td></tr><tr><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>Hién thidanh sachtrng vien</td><td rowspan=1 colspan=1>He thongquan ly nhansu</td><td rowspan=1 colspan=1>Hethong</td><td rowspan=1 colspan=1>Hién thi danh sach hö so urng viendugc day vé tur VTP kem cactrang thai:·Tao moi·Dang xur ly· Dat· Khong dat</td></tr><tr><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>Cap nhattrang thai ho so ung vien</td><td rowspan=1 colspan=1>He thongquan ly nhansu</td><td rowspan=1 colspan=1>Nguroidung</td><td rowspan=1 colspan=1>Nguoi dung c@p nhat trang thai hó so ung vien, chuyén trang thai hó so trén danh sach ing vién</td></tr><tr><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>Tra két quaung tuyénqua SMS/Mocha</td><td rowspan=1 colspan=1>He thongquan ly nhansu</td><td rowspan=1 colspan=1>Héthong</td><td rowspan=1 colspan=1>He thong giri thong bao vé tiéntrinh xur ly ho so:Dang xur ly: Ho so da duoctiép nhanDat: Ho so ung tuyén dat.yéu câu, b@ phan tuyéndung thuc hien quy trinhtuyén dung thu cong Khong dat: Ho so bi turchói, nguoi dung c6 théung tuyén lai</td></tr></table>

# 2.3 Mô tả màn hình

<table><tr><td rowspan=1 colspan=1>STT</td><td rowspan=1 colspan=1>Thong tin</td><td rowspan=1 colspan=1>Kiéucontrol</td><td rowspan=1 colspan=1>Batbu@c</td><td rowspan=1 colspan=1> Mac dinh</td><td rowspan=1 colspan=1> Mo ta</td></tr><tr><td rowspan=1 colspan=6> Vao web vietelpost.com.vn &gt; Chon irng tuyén giao hang &gt; Diéu huong vé man ungtuyén nhanh</td></tr><tr><td rowspan=1 colspan=6>Thong tin cä nhan</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Ho vaten</td><td rowspan=1 colspan=1>Textbox</td><td rowspan=1 colspan=1>C6</td><td rowspan=1 colspan=1>Hinttext:</td><td rowspan=1 colspan=1>Cho phép nhap ho va tenMessage:</td></tr></table>



<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Nhap hova ten</td><td rowspan=1 colspan=1>Dé tróng truong thong tin &gt; Hién thimessage:① Ho va tén khóng dugc bó träng!</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>Namsinh</td><td rowspan=1 colspan=1>Textbox</td><td rowspan=1 colspan=1>C6</td><td rowspan=1 colspan=1>Hinttext:Nhapnam sinh</td><td rowspan=1 colspan=1>Chi cho phép nhap só, tói da 4 sóMessage:Dé tróng truong thong tin &gt; Hién thimessage:① Nám sinh khóng dugc bó tröng!</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>s6dienthoai</td><td rowspan=1 colspan=1>Textbox</td><td rowspan=1 colspan=1>C6</td><td rowspan=1 colspan=1>Hinttext:Nhaps6dienthoai</td><td rowspan=1 colspan=1>Chi cho phép nhap só, toi da 10 só, khóngchura ky tu dac bietMessage: - Nhap sai dinh dang &gt; Hién thi message:“Só dien thoai khong hop lé.&quot;- Dé tróng truong thong tin &gt; Hién thimessage:① S6 dien thogi khong dugc bó träng!</td></tr><tr><td rowspan=1 colspan=6>Vi tri ung tuyén</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Vitriingtuyen</td><td rowspan=1 colspan=1>Check box</td><td rowspan=1 colspan=1>C6</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Chon 1 trong 3 vi tri urng tuyén:- Nhan vien buu ta- Nhan vien khai thac- Tai xé xe taiMessage:Dé tróng truong thong tin &gt; Hién thimessage:① Vi tri ung tuyén khóng dugc bó trong!</td></tr><tr><td rowspan=1 colspan=3> Khu virc irng tuyén</td><td rowspan=1 colspan=3></td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Tinh</td><td rowspan=1 colspan=1>Dropdownlist</td><td rowspan=1 colspan=1>C6</td><td rowspan=1 colspan=1>Hinttext:Chontinh</td><td rowspan=1 colspan=1>Chon tinh tur danh sach He thóng quan ly nhan su tra véMessage:D tróng truong thong tin &gt; Hién thimessage:</td></tr></table>
