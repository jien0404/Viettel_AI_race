# Public_372

# 1. Quy định chung

# 1.1 Khái quát

# 1.1.1 Khả năng của AIS

AIS có khả năng cung cấp cho các tàu và bờ thông tin của một tàu, một cách tự động với độ chính xác và tần suất theo yêu cầu, nhằm mục đích để theo dõi chính xác đường đi của tàu.

# 1.1.2 Kiểm định chất lượng

Các nhà sản xuất được yêu cầu có hệ thống kiểm soát chất lượng được kiểm định để đảm bảo việc thoả mãn điều kiện được ban hành. Cơ quan quản lý sẽ đánh giá sản phẩm sau khi được đơn vị uỷ quyền đánh giá đảm bảo chất lượng trước khi lắp đặt trên tàu.

# 1.2 Chế độ vận hành

Hệ thống phải có khả năng hoạt động theo các chế độ sau:

1.2.1 Chế độ “tự động và liên tục”

Chế độ “tự động và liên tục” có thể hoạt động liên tục ở mọi khu vực biển: ngoài khơi, trong khu vực cảng, trong luồng hẹp.

# 1.2.2 Chế độ “chỉ định”

Chế độ “chỉ định” hoạt động tại một vùng cụ thể, tuỳ thuộc vào bộ phận điều khiển giao thông tại đây, theo đó khoảng thời gian truyền dữ liệu và/hoặc các khe thời gian có thể được thiết lập từ xa bởi bộ phận điểu khiển giao thông.



# 1.2.3 Chế độ “kiểm soát vòng”

Chế độ "kiểm soát vòng” khi tàu cần truyền dữ liệu để trả lời truy vấn của tàu khác hoặc của trạm điều khiển giao thông.

# 2. Quy định kỹ thuật

# 2.1 Khái quát

Các quy định trong phần này liên quan từ lớp 1 đến lớp 4 (Lớp vật lý, Lớp kết nối, Lớp mạng, Lớp vận tải) trong mô hình OSI.

<table><tr><td rowspan=1 colspan=3>Lop ung dung</td></tr><tr><td rowspan=1 colspan=3>Lop trinh dién</td></tr><tr><td rowspan=1 colspan=3>Lóp phien</td></tr><tr><td rowspan=1 colspan=3>Lop van tai</td></tr><tr><td rowspan=1 colspan=3>Lop mangKénh 1                          Kénh 2</td></tr><tr><td rowspan=1 colspan=1>Lop lien kétLME</td><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1>Lop lien kétLME</td></tr><tr><td rowspan=1 colspan=1>Lop lien két DLS</td><td rowspan=1 colspan=1>Lop lien két DLS</td></tr></table>



Hình 2 - Mô tả mô hình các lớp trong một trạm AIS   

<table><tr><td rowspan=1 colspan=1>L6p lien kétMAC</td><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1>Lóp lien kétMAC</td></tr><tr><td rowspan=1 colspan=1>Lop vat ly</td><td rowspan=1 colspan=1>Lop vat ly</td></tr><tr><td rowspan=1 colspan=1>Rx1</td><td rowspan=1 colspan=1>Tx 1/2</td><td rowspan=1 colspan=1>Rx2</td></tr></table>

# 2.2 Lớp vật lý

Lớp Vật lý làm nhiệm vụ truyền các luồng bít từ đầu ra ban đầu trên kênh dữ liệu. Lớp Vật lý tuân theo ITU-R M.1371-1, Phụ lục 2, Chương 2.

Bảng 1 bao gồm các thông số kỹ thuật sẽ áp dụng cho các bộ thu TDMA.

Bảng 1 - Các yêu cầu đặc tính bộ thu   



<table><tr><td>Triet dap ing xuyén diéu ché va triet nghen</td><td>20 % PER</td><td>N/A</td></tr></table>

# 2.3 Lớp liên kết

Lớp liên kết chỉ định phương thức đóng gói gói tin nhằm thực hiện việc phát hiện và sửa lỗi cho quá trình truyền dữ liệu. Lớp liên kết chia thành 3 lớp con.

# 2.3.1 Lớp liên kết con 1: Điều khiển truy nhập môi trường (MAC)

Lớp con MAC chỉ định phương thức truy nhập tới môi trường truyền dữ liệu, tức là kênh dữ liệu VHF. Lớp này dùng phương thức truy nhập TDMA dùng tham chiếu thời gian thông thường.

# 2.3.2 Lớp liên kết con 2: Dịch vụ kênh dữ liệu (DSL)

Lớp con DLS chỉ định phương thức:

a. Khởi tạo và giải phóng kênh dữ liệu.   
b. Truyền dữ liệu.   
c. Giám sát và phát hiện lỗi.

2.3.3 Lớp liên kết con 3: Thành phần quản lý kênh (LME) LME điều khiển hoạt động của DLS, MAC và lớp vật lý.

# 2.4 Lớp mạng

Lớp mạng dùng để:

a. Thiết lập và duy trì các kết nối kênh;



b. Quản lý các phép gán ưu tiên cho bản tin;   
c. Phân phối các gói tin truyền vào các kênh.

Lớp mạng có cấu trúc tuân thủ Khuyến nghị ITU-R M.1371-1-1, Phụ lục 2, Chương 4.

Mọi thiết lập được khai thác vùng được lưu đều được gán thẻ ngày/giờ và các thông tin đầu vào mà thiết lập được khai thác vùng thu được (TDMA Msg 22, tín hiệu mã DSC, đầu vào nhập qua bàn phím, đầu vào chuỗi ACA nhập qua giao diện trình diễn).

AIS sẽ liên tục kiểm tra, nếu biên gần nhất của vùng được khai thác của mọi thiết lập cách tàu đang đo trên $^ { 8 0 4 , 5 \mathrm { k m } }$ , hoặc nếu mọi thiết lập được khai thác vùng đã dùng trên 5 tuần.

# 2.5 Lớp vận tải

Lớp vận tải dùng để:

a. Chuyển đổi dữ liệu thành các gói tin với kích thước phù hợp để phát đi b. Kiểm soát thứ tự các gói tin   
c. Làm giao thức cầu nối với các lớp cao hơn.

Lớp vận tải có cấu trúc tuân thủ Khuyến nghị ITU-RM.1371-1-1, Phụ lục 2, Chương 5.

3. Yêu cầu về nguồn điện và đảm bảo an toàn

3.1 Độ bền với các điều kiện khác nhau của môi trường

Bảng 2 - Độ bền với các điều kiện khác nhau của môi trường   





<table><tr><td rowspan=1 colspan=1>Dieu kien</td><td rowspan=1 colspan=1> Xach tay</td><td rowspan=1 colspan=2>Duocche chan</td><td rowspan=1 colspan=1>Ngoai troi</td><td rowspan=1 colspan=1>Ngap nuro&#x27;c</td></tr><tr><td rowspan=1 colspan=1>Rung lac</td><td rowspan=1 colspan=5>Rung tai tan só 2 Hz - 13,2 Hz d@ dich chuyén ± 1 mm, tai 13,2 Hz -100 Hz do dich chuyén 7 m/s² va trong 2 h voi mδi lan cong huong,noi cach khac 2h quét tai 30 Hz theo cä 3 truc</td></tr><tr><td rowspan=1 colspan=1>Mua va buinuroc</td><td rowspan=1 colspan=2>X</td><td rowspan=1 colspan=2>Voi 12,5 mm , luuluong 100 lit/phutva khoang cach 3m</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Nhung     vaonuoc</td><td rowspan=1 colspan=1>100 kPa (1 bar) trong 5 phut10 kPa (0,1 bar)voiVHF2chieu</td><td rowspan=1 colspan=3>X</td><td rowspan=1 colspan=1>600 kPa (6 bar)trong 12 h</td></tr><tr><td rowspan=1 colspan=1>Birc xa mat troi</td><td rowspan=1 colspan=1>1120 W/m²80 h</td><td rowspan=1 colspan=2>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Chóng dau bam</td><td rowspan=1 colspan=1>ISO Oil No. 124 h,19 ℃</td><td rowspan=1 colspan=2>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td></tr></table>



<table><tr><td rowspan=1 colspan=1>Dieu kien</td><td rowspan=1 colspan=1> Xach tay</td><td rowspan=1 colspan=1>Drocche chan</td><td rowspan=1 colspan=1>Ngoai troi</td><td rowspan=1 colspan=1>Ngap nuo&#x27;c</td></tr><tr><td rowspan=1 colspan=1>An mon</td><td rowspan=1 colspan=4>Bón chu ky, mi chu ky trong vong 7 ngay tai 40 C, do ám tuong dói 90 % - 95 % sau 2h phun nuóc muói</td></tr><tr><td rowspan=1 colspan=5>CHU THICH: “x&quot; - Khong quy dinh</td></tr></table>

# 3.2 Nguồn điện

# 3.2.1 Nguồn điện

Quy trình đo đầu vào và ra của nguồn điện tuân theo các quy định IEC 61162-1 hoặc IEC 61162-2 về điện áp và dòng lớn nhất và nhỏ nhất trên các kết cuối đầu vào.

# 3.2.2 Yêu cầu kết quả

Các giao diện đáp ứng đầy đủ theo 2 tiêu chuẩn trên (IEC 61162-1 hoặc IEC 61162-2).

# 4. Các điều kiện thử nghiệm

# 4.1 Khái quát

Khi một yêu cầu trong tiêu chuẩn này khác với trong IEC 60945, yêu cầu trong tiêu chuẩn này sẽ được áp dụng.

4.2 Điều kiện thử nghiệm thông thường và tới hạn



# 4.2.1 Điều kiện thử nghiệm thông thường

4.2.1.1. Nhiệt độ và độ ẩm

Nhiệt độ và độ ẩm phải nằm trong dải:

• Nhiệt độ từ $+ 1 5 ~ ^ { \circ } \mathrm { C }$ đến $+ 3 5 ~ ^ { \circ } \mathrm { C }$ .

• Độ ẩm từ $20 \%$ đến $75 \%$ .

4.2.1.2. Nguồn cấp

Nguồn cấp trong điều kiện thử nghiệm thông thường sẽ có dung sai tương đối trong khoảng là $\pm 3 \%$ so với điện áp danh nghĩa của nguồn điện trên tàu đã được thiết kế để cung cấp cho thiết bị.

# 4.2.1.3. Điều kiện thử nghiệm tới hạn

Điều kiện thử nghiệm tới hạn được chỉ rõ trong IEC 60945. Khi được yêu cầu, phép thử trong điều kiện tới hạn được thực hiện trong môi trường khô ráo và có điện áp cao hơn giới hạn điện áp cấp cùng lúc đó, có nhiệt độ thấp và thấp hơn giới hạn điện áp cấp cùng lúc.

# 4.2.2 Môi trường đo chuẩn

EUT được đo trong môi trường sử dụng thiết bị đo để mô phỏng và lưu các bản tin VDL. Môi trường chuẩn gồm ít nhất 5 mục tiêu mô phỏng. Mức tín hiệu đầu vào ở cổng RF input của EUT với mỗi mục tiêu ít nhất là -100 dBm. Các đầu vào thu được bằng cảm biến của EUT, được mô phỏng bằng hệ thống đo kiểm hoặc các phương pháp khác. Được khai thác và kiểm tra trên các kênh trong băng tần di động hàng hải.

Các kênh đang dùng sẽ được lựa chọn bằng tay thông qua các đầu vào hoặc các bản tin đã gán kênh trước khi bắt đầu đo.
