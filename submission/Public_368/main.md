# Public_368

# 1. Kích cỡ khối để thử luồng PDH

Kích cỡ khối để thử luồng PDH trong hệ thống đang khai thác được cho trong Bảng 6.

# Bảng 6 - Kích cỡ khối PDH

<table><tr><td>Tóc do bit cua luong PDH kbit/s</td><td>Kich co khi PDH bit</td><td>EDC/khong c6 EDC</td></tr><tr><td>2048</td><td>2048</td><td>CRC-4</td></tr><tr><td>8448</td><td>4224</td><td>Khong c6 EDC</td></tr><tr><td>34368</td><td>4296</td><td>Khong c6 EDC</td></tr><tr><td>139264</td><td>17408</td><td>Kh6ng c6 EDC</td></tr></table>

# 2. Các bất bình thường (Anomatics)

Hai trạng thái bất bình thường trong hệ thống đang khai thác được sử dụng để xác định chỉ tiêu lỗi bit của luồng PDH.

a1: Một tín hiệu đồng bộ khung bị lỗi (an errored frame alignment signal).   
a2: Một khối bị lỗi (EB) được chỉ thị bằng mã phát hiện lỗi (EDC).

# 3. Các sai hỏng

Ba trạng thái sai hỏng của tín hiệu lối vào trong hệ thống đang khai thác được sử dụng để xác định chỉ tiêu lỗi bit của luồng PDH.

d1: Mất khung (Loss of frame).   
d2: Tín hiệu chỉ thị cảnh báo (Alarm Indication Signal).   
d3: Mất đồng bộ khung (Loss of frame alignment).

4. Các kiểu luồng PDH



Tùy theo thiết bị thử ISM liên quan đối với luồng PDH sẽ có 4 loại cấu trúc luồng như sau:

• Kiểu 1: Luồng được cấu trúc bởi khung và khối   
Một tập hợp đầy đủ chỉ thị sai hỏng d1, d2, d3 và các chỉ thị bất bình thường a1, a2 do thiết bị kiểm tra cung cấp khi hệ thống đang khai thác (ISM).   
• Kiểu 2: Luồng được cấu trúc bởi khung   
Một tập hợp đầy đủ chỉ thị sai hỏng d1, d2, d3 và bất bình thường a1 do thiết bị kiểm tra cung cấp khi hệ thống đang khai thác.   
• Kiểu 3: Các luồng được cấu trúc khung khác   
Một loạt các giới hạn của chỉ thị sai hỏng d1, d2 và bất bình thường a1 do thiết bị kiểm tra cung cấp khi hệ thống đang khai thác. Ngoài ra ISM còn chỉ thị cả số lượng chuỗi tín hiệu đồng bộ khung bị lỗi trong mỗi giây.   
• Kiểu 4: Các luồng không định dạng khung   
Một loạt các giới hạn của chỉ thị sai hỏng d1, d2 do thiết bị kiểm tra cung cấp khi hệ thống đang khai thác.

# 5. Các thông số và tiêu chuẩn đo luồng PDH

Bảng 7 - Các thông số và tiêu chuẩn đo   



<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>BBER</td><td rowspan=1 colspan=1>Mot loi khói co ban quan sat duoc khi: mot batbinh thuong a1 hoac a2 xay ra trong mot khóinhung khong thuoc phan giay bi loi nghiemtrong.</td></tr><tr><td rowspan=2 colspan=1>2</td><td rowspan=1 colspan=1>ESR</td><td rowspan=1 colspan=1>Mot giay bi loi quan sat duoc khi trong motgiay it nhat có mot bat binh thuong a1 hoac mótsai hong d1 dén d3 xay ra</td></tr><tr><td rowspan=1 colspan=1>SESR</td><td rowspan=1 colspan=1>Mot giay bi loi nghiem trong quan sat duoc khitrong m@t giay it nhat có ‘x&#x27; bat binh thuong a1hoäc mot sai hong di hoac d2 xay ra.</td></tr><tr><td rowspan=2 colspan=1>3</td><td rowspan=1 colspan=1>ESR</td><td rowspan=1 colspan=1>Mot giay bi loi quan sat duoc khi trong motgiay it nhat có mót bat binh thuong a1 hoac motsai hong di hoac d xay ra.</td></tr><tr><td rowspan=2 colspan=1>SESR</td><td rowspan=1 colspan=1>Mot giay bi loi nghiem trong quan sat duoc khitrong mot giay có it nhat ‘x&#x27; bat binh thuong a1hoäc mot sai hong di hoac d2 xay ra</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>Mot giay bi loi nghiem trong quan sat duoc khitrong mot giay it nhat có mot sai hong dl hoacd2 xay ra.</td></tr></table>

# 6. Tiêu chuẩn cho việc phát hiện một giây bị lỗi nghiêm trọng trong luồng PDH

Bảng 8 liệt $\mathrm { k } \hat { \mathrm { e } }$ giá trị ‘x’ gây ra một giây bị lỗi nghiêm trọng (SES) trong khi kiểm tra hệ thống đang khai thác.

Bảng 8 - Tiêu chuẩn có SES trên các tuyến PDH



<table><tr><td rowspan=1 colspan=1>Tóc do bit (kbit/s)</td><td rowspan=1 colspan=1>2 048</td></tr><tr><td rowspan=1 colspan=1>Kiéu EDC</td><td rowspan=1 colspan=1>CRC-4</td></tr><tr><td rowspan=1 colspan=1>S6 khoi/1 giay</td><td rowspan=1 colspan=1>1000</td></tr><tr><td rowspan=1 colspan=1>S6 bit/1 khói</td><td rowspan=1 colspan=1>2 048</td></tr><tr><td rowspan=1 colspan=1>Nguong SES truoc Khuyén nghi G.826</td><td rowspan=1 colspan=1>x = 805</td></tr><tr><td rowspan=1 colspan=1>Nguong ISM dua tren SES cua Khuyénnghi G.826</td><td rowspan=1 colspan=1>X = 30% khoi bi 1oi</td></tr></table>
