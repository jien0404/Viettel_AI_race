# Public_319

# NỘI DUNG QUY TRÌNH

# 1. Quan điểm. mục đích

# + Quan điểm:

Quy trình chỉ ra các bước và các tiêu chí đánh giá, nguồn tri thức và thông tin đáng tin cậy để đơn vị làm căn cứ đánh giá, lựa chọn hệ quản trị cơ sở dữ liệu (DBMS).

Đơn vị cần tuân thủ việc đánh giá đầy đủ qua các bước với các tiêu chí được nêu và căn cứ vào kết quả đánh giá để ra quyết định lựa chọn công nghệ phù hợp với dự án.

Quy trình này nằm trong bước phân tích nghiệp vụ trong Quy trình phát triển phần mềm của Tập đoàn, đầu ra của quy trình này sẽ giúp cho đơn vị đưa ra quyết định lựa chọn DBMS một cách đúng đắn, là cơ sở để xây dựng chỉ tiêu về hệ quản trị CSDL trong CTKT và tài liệu giải pháp.

Các đơn vị có trách nhiệm cung cấp use cases thường xuyên để quy trình này được cập nhật các tri thức mới. Đánh giá liên tục để xem có phù hợp với thực tế hay không.

$+$ Mục đích: Quy trình này nhằm quy định thống nhất phương pháp lựa chọn hệ quản trị CSDL cho các dự án xây mới và nâng cấp phát triển phần mềm.

# 2. Phạm vi, đối tượng áp dụng

Phạm vi: Áp dụng cho hoạt động đánh giá, lựa chọn hệ quản trị CSDL cho các dự án phần mềm.

- Đối tượng áp dụng: Các cơ quan, đơn vị trong Tập đoàn

# 3. Tài liệu liên quan

<table><tr><td rowspan=1 colspan=1>TT</td><td rowspan=1 colspan=1>Tai lieu</td><td rowspan=1 colspan=1>Thoi gian banhanh</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Bo tiéu chuan Luu tru va Van hanh du liéuTC.CNVTQD.CNTT.40</td><td rowspan=1 colspan=1>09/2022</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>Quy dinh thiet lap, quan ly,luu trur, khai thac log hé thongCNTT s6 4137/QD-CNVTQD-CNTT.</td><td rowspan=1 colspan=1>9/2021</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>Quy dinh xay dung, nang cap, bao tri cac san pham phanmém trong Tap doan Cong nghiep - Vién thong Quan doi(3388/QD-CNVQTD-CNTT)</td><td rowspan=1 colspan=1>7/2021</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>B@ tiéu chuan luu trur va van hanh du liéu(TC.CNVTQD.CNTT.40)</td><td rowspan=1 colspan=1>9/2022</td></tr></table>

# 4. Giải thích thuật ngữ và từ viết tắt

# Thuật ngữ

o Dữ liệu (Data): là thông tin được máy tính lưu trữ, xử lý hoặc truy xuất theo yêu cầu của người dùng hoặc theo tiến trình hoạt động của máy tính. o Cơ sở dữ liệu: Chỉ mọi tập hợp dữ liệu được lưu trữ, bất $\mathrm { k } \mathring { \mathrm { e } }$ cấu trúc hoặc nội dung. Trong một số cơ sở dữ liệu lớn CSDL được nhắc đến như là instances và schema.



o Instance: Là một triển khai phần mềm cơ sở dữ liệu (DBMS) có nhiệm vụ kiểm soát quyền truy cập vào một khu vực lưu trữ nhất định. Thường tổ chức có nhiều instance chạy đồng thời, độc lập nhau và mỗi instance kiểm soát truy cập vào các khu vực lưu trữ khác nhau.   
o Hệ quản trị CSDL hay DBMS (Database Management System): Là phần mềm tương tác với người dùng cuối, ứng dụng và chính cơ sở dữ liệu để thu thập và phân tích dữ liệu. Phần mềm DBMS bao gồm các tiện ích cốt lõi được cung cấp để quản trị cơ sở dữ liệu.   
o Node: Một máy tính/ máy chủ vật lý lưu trữ và xử lý dữ liệu như một phần của cơ sở dữ liệu phân tán.

Từ viết tắt:

<table><tr><td rowspan=1 colspan=1>STT</td><td rowspan=1 colspan=1>Thuat ngir va tir viet tat</td><td rowspan=1 colspan=1>Giai thich</td></tr><tr><td rowspan=1 colspan=1>1.</td><td rowspan=1 colspan=1>CSDL</td><td rowspan=1 colspan=1>Co so dur lieu</td></tr><tr><td rowspan=1 colspan=1>2.</td><td rowspan=1 colspan=1>RDBMS</td><td rowspan=1 colspan=1>Relational Database Management System (Hé quantri CSDL quan hé)</td></tr><tr><td rowspan=1 colspan=1>3.</td><td rowspan=1 colspan=1>NoSQL</td><td rowspan=1 colspan=1>NonRelational hoäc Not Only SQL: La loai DBMSdanh cho dur liéu có cäu truc linh hoat, khong códinh.</td></tr><tr><td rowspan=1 colspan=1>4.</td><td rowspan=1 colspan=1>DV PTPM</td><td rowspan=1 colspan=1>Don vi Phat trién phan mém</td></tr><tr><td rowspan=1 colspan=1>5.</td><td rowspan=1 colspan=1>DV Nghiep vu</td><td rowspan=1 colspan=1> Don vi dat hang xay dung phan mém, am hiéu venghiep vu.</td></tr><tr><td rowspan=1 colspan=1>6.</td><td rowspan=1 colspan=1>DV VHKT</td><td rowspan=1 colspan=1>Don vi vän hanh khai thäc co so du liéu</td></tr></table>

5. Nội dung quy trình lựa chọn Hệ quản trị cơ sở dữ liệu cho các dự án xây mới, nâng cấp phần mềm

# • Sự kiện bắt đầu và kết thúc

Sự kiện bắt đầu: Khi có nhu cầu lựa chọn DBMS cho các dự án xây mới, nâng cấp phần mềm.   
Sự kiện kết thúc: Lựa chọn được DBMS phù hợp với yêu cầu của bài toán nghiệp vụ, đưa vào CTKT và tài liệu giải pháp của phần mềm được xây mới hoặc nâng cấp.   
Đầu vào: Khi có yêu cầu xây mới/ nâng cấp phần mềm.   
Đầu ra: DBMS được lựa chọn trong CTKT phần mềm và tài liệu giải pháp.

• Lưu đồ tổng thể quy trình • Diễn giải chi tiết



![](images/1.jpg)

> **Hình chú thích:** a flow diagram for a process



<table><tr><td rowspan=1 colspan=1>Buroc</td><td rowspan=1 colspan=1>Hoatdongchinh</td><td rowspan=1 colspan=1>Cong viec thurc hien</td><td rowspan=1 colspan=1>Phu trachthurc hien</td><td rowspan=1 colspan=1>Dau vao</td><td rowspan=1 colspan=1>Dau ra</td></tr></table>



<table><tr><td rowspan=11 colspan=1></td><td rowspan=15 colspan=1>Dua ra yéucau ve dulieu</td><td rowspan=15 colspan=1>Khi don vi nghiep vu duara yéu cäu vé xay dung, nang cap phan mém (theobiéu mau duoc quy dinhtrong Phu luc O1), don vi PTPM phoi hop voi don vinghiép vu phan tich, lamrö cac yéu cau vé quan ly,luu tru va xir ly dur lieu cuaung dung theo cac tiéu chisau:Cau truc du liéuKiéu t churc dulieuKiéu xur ly du lieuYéu cau däm baotinh ACID/BASE,cac uu tien trongdinh luat CAPNhu cau doc ghi durlieu Quy mo du lieuChi tiét vé cac tiéu chicóng nghé can phan tich,danh gia theo Phu luc 02.</td><td rowspan=1 colspan=1>DV</td><td rowspan=2 colspan=4>Phantichyéu cau xaydung, nangcap  phan</td><td rowspan=3 colspan=1>Cacnhandinh   veloaiDBMSphu  hop</td></tr><tr><td rowspan=1 colspan=1>nghiep vu;DV PTPM</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=4>mém</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=4></td><td rowspan=2 colspan=1>voi  tungtieu    chi</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=4></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=4></td><td rowspan=1 colspan=1>sau    khi</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=4></td><td rowspan=1 colspan=1>danh gia</td></tr><tr><td rowspan=3 colspan=1></td><td rowspan=3 colspan=2></td><td></td><td></td><td></td></tr><tr><td rowspan=2 colspan=2></td><td></td><td></td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=6 colspan=1>yéu cau</td></tr><tr><td rowspan=5 colspan=1></td><td rowspan=1 colspan=4></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=4 colspan=4></td></tr><tr><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>2.</td><td rowspan=1 colspan=1>So   sanhcac nhandinh  saudanh gia oBu6c    1voi    cacloai</td><td rowspan=1 colspan=1>Sau khi dua ra nhan dinh vé loai DBMS phu hop voicac tiéu chi danh gia óBuóc 1, don vi PTPM duara cac dé xuat vé́ các san phäm DBMS có khä nängdap ürng yéu cau bai toan</td><td rowspan=1 colspan=1>DV PTPM</td><td rowspan=1 colspan=4>Cac   loaiDBMS phuhop voi cactieu    chicong nghérieng lé</td><td rowspan=1 colspan=1>Tong hopcacDBMSphuhopvoi tat cacac   tieu</td></tr></table>



<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>DBMSphbientren    thitruong</td><td rowspan=1 colspan=1>vé mat cong nghé, cac uu tien can dap ung cho baitoan.Thóng tin vé dac trung, so sanh cac loai DBMS phóbien xem trong Phu luc03.</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>chi cua baitoan.</td></tr><tr><td rowspan=1 colspan=1>3.</td><td rowspan=1 colspan=1>Danhgiavan de chiphi va banquyen</td><td rowspan=1 colspan=1> Chon DBMS thuong maikhi: Khach hang có yéucauchon1 hoacloaiDBMS va dam bao cóngan sach cua dur an du chiträ, hiéu quä kinh doanh vuot troi so voi chi phi bóra.Cac truong hop con lai:Phai uu tién chon DBMSmä nguon mo va tuan theoHD vé sur dung ma nguon mo cua Tap doan.Cac luu y vé chi phi valicense cho DBMS xemtrong Phu luc 04.</td><td rowspan=1 colspan=1>DV PTPM</td><td rowspan=1 colspan=1> Cac can curlua  chonsan pham thuong mai</td><td rowspan=1 colspan=1>Danh sachsan phamdap  ungduoc tieuchi vé chiphi/banquyen.</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>Danh gianang  lurclam chusän phamcua doi duan</td><td rowspan=1 colspan=1>Doi dur án cúa DV PTPMva Don vi VHKT du lieu(du kién) danh gia nangluc lam chu cua minh doivoi san pham duoc chonqua 3 buóc tren. Uu tienchon san pham ma doi du an am hiéu va thanh thao nhat va van hanh don gian,it 1oi.Truong hop la DBMS moidoi voi don vi thi can phai</td><td rowspan=1 colspan=1>DV PTPMDVVHKT</td><td rowspan=1 colspan=1>Cac    usecases  doidu an datrienkhaihoac tham khao tr cacdon      vikhac.Bien  bandanh  giakét qua thurnghiep theo</td><td rowspan=1 colspan=1>Ket  qualua chonsanphamDBMS toiuu cho duran  duocTruong duan va Lanhdao don vivan hanhCSDL.</td></tr></table>





# • Vai trò của các bên liên quan

<table><tr><td rowspan=1 colspan=1>STT</td><td rowspan=1 colspan=1>Hoat dong chinh</td><td rowspan=1 colspan=1>DV Nghiepvu</td><td rowspan=1 colspan=1>DV PTPM</td><td rowspan=1 colspan=1>DV VHKT</td></tr><tr><td rowspan=1 colspan=1>1.</td><td rowspan=1 colspan=1>Dua ra yéu cau ve du lieu</td><td rowspan=1 colspan=1>A/R</td><td rowspan=1 colspan=1>S</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>2.</td><td rowspan=1 colspan=1>Lua chon san pham có kha nang dapurng yéu cau theo cac tieu chi congnghe</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>A/R</td><td rowspan=1 colspan=1>I</td></tr><tr><td rowspan=1 colspan=1>3.</td><td rowspan=1 colspan=1>Danh gia van dé chi phi va banquyén</td><td rowspan=1 colspan=1>I</td><td rowspan=1 colspan=1>A/R</td><td rowspan=1 colspan=1>R</td></tr><tr><td rowspan=1 colspan=1>4.</td><td rowspan=1 colspan=1>Danh gia kha nang lam chu congnghe</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>R</td></tr><tr><td rowspan=1 colspan=1>5.</td><td rowspan=1 colspan=1>Bao cao, phé duyét, tham dinh vadua vao CTKT</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>A/R</td><td rowspan=1 colspan=1>1</td></tr></table>

Giải thích:   

<table><tr><td rowspan=1 colspan=1>Chir viet tat</td><td rowspan=1 colspan=1>Y nghia</td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>Don vi/vai tro chiu trach nhiém giai trinh két qua cua hoat dong</td></tr><tr><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>Don vi/vai tro chiu trach nhiém thuc hien hoat dong</td></tr><tr><td rowspan=1 colspan=1>S</td><td rowspan=1 colspan=1>Don vi/vai tro cung cap nguon lurc va hö tro thuc hien hoat dong</td></tr></table>



<table><tr><td>C</td><td>Don vi/vai tro cung cap thong tin va tur van hö tro truoc va trong qua trinh thuc hien hoat dong</td></tr><tr><td>I</td><td>Don vi/vai tro duoc thong bao/cung cap thong tin sau khi hoat dong duoc thuc hién</td></tr></table>

# 6. Tiêu chí, chỉ số đánh giá việc thực hiện quy trình

<table><tr><td rowspan=1 colspan=1>Mieu ta KPI</td><td rowspan=1 colspan=1>Cong thirc tinh: Ti lé tuan thu quy trinh = Tong só dur án co bao cao luachon DBMS dung quy trinh truoc khi xay dung CTKT/ Tong so du án.Cach tinh: Hang quy don vi chiu trach nhiém ra soat va lay só luong trénhé thong dé tinh ti le.</td></tr><tr><td rowspan=1 colspan=1>Muc dich KPI</td><td rowspan=1 colspan=1>Quan ly viéc tuan thu quy trinh.</td></tr><tr><td rowspan=1 colspan=1>Nguong KPImuc tieu</td><td rowspan=1 colspan=1> &gt;=90% (Kiem tra thir nghiem sau 3 thang sau dó se dieu chinh nguongKPI theo thuc té)</td></tr><tr><td rowspan=1 colspan=1>Don vi chiutrachnhiémthuc hien KPI</td><td rowspan=1 colspan=1>DV PTPM</td></tr><tr><td rowspan=1 colspan=1>Don vi ra soatviéc thuc hienKPI</td><td rowspan=1 colspan=1> Bo phan Quan tri dur liéu</td></tr></table>

# 7. Phụ lục đính kèm
