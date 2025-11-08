# Public_373

# 1. Khái quát

Trong các phép thử này, EUT phải tuân thủ theo cấu hình hoạt động, thủ tục lắp đặt và nối đất bình thường, trừ khi có thay đổi được chỉ rõ, và được khai thác trong điều kiện đo kiểm bình thường. Giao diện riêng biệt của EUT với môi trường điện từ bên ngoài là các cổng. Giới hạn vật lý của EUT mà ở đó có phát xạ hay tác động của điện từ trường là cổng vỏ.

Các phép thử chế độ chênh lệch là các phép thử giữa nguồn điện, tín hiệu và đường dây điều khiển.

Các phép thử chế độ chung là các phép thử giữa các nhóm đường dây và điểm tham chiếu chung, thường là đất.

Đối với các phép thử miễn nhiễm, các kết quả được đánh giá theo các tiêu chí chất lượng phụ thuộc và các điều kiện được khai thác và các chức năng đã gán của EUT, và được định nghĩa như sau:

- Tiêu chí chất lượng A: EUT phải tiếp tục hoạt động bình thường trong và sau khi thử. Không xảy ra suy giảm chất lượng hay mất chức năng như đã định nghĩa trong tiêu chuẩn thiết bị và chỉ tiêu kỹ thuật do nhà sản xuất cung cấp.

- Tiêu chí chất lượng B: EUT phải tiếp tục hoạt động bình thường sau khi thử. Không xảy ra suy giảm chất lượng hay mất chức năng như đã định nghĩa trong tiêu chuẩn thiết bị và chỉ tiêu kỹ thuật do nhà sản xuất cung cấp. Trong khi thử, suy giảm chất lượng hay mất chức năng nhưng có thể tự phục hồi mà không được phép thay đổi trạng thái hoạt động thực sự và số liệu lưu trữ.

- Tiêu chí chất lượng C: Suy giảm tạm thời và mất chức năng cho phép trong khi thử, với điều kiện chức năng có thể tự phục hồi, hoặc phục hồi lại sau khi kết thúc phép thử bằng các bộ phận điều khiển, như đã định nghĩa trong tiêu chuẩn thiết bị và chỉ tiêu kỹ thuật do nhà sản xuất cung cấp.



Các điều kiện và phép thử được tóm tắt trong Bảng 4. Bảng 4 cũng cung cấp các yêu cầu chỉ tiêu chất lượng cho thiết bị sóng vô tuyến và thiết bị định vị khác nhau. Với các loại thiết bị khác, tiêu chí chất lượng phải được cung cấp trong tiêu chuẩn thiết bị tương ứng và các chỉ tiêu kỹ thuật do nhà sản xuất cung cấp, tuy nhiên, tối thiểu EUT phải tuân thủ chỉ tiêu chất lượng C.

# Bảng 4 - Miễn nhiễm điện từ

<table>
  
  <tbody>
    <tr>
      <td>Điều kiện</td>
      <td>Xách tay</td>
      <td>Bảo vệ</td>
      <td>Mở</td>
      <td>Chìm</td>
    </tr>
    <tr>
      <td>Nhiễu dẫn tần số vô tuyến</td>
      <td>*</td>
      <td>3 V r.m.s e.m.f 150 kHz - 80 MHz, 10 V r.m.s e.m.f tại các tần số điểm quy định Các cổng nguồn a.c và d.c, cổng điều khiển và tín hiệu, chế độ chung Tiêu chí chất lượng A</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Nhiễu phân tán</td>
      <td>10 V/m 80 MHz - 2 GHz Cổng vỏ Tiêu chí chất lượng A</td>
      <td></td>
      <td></td>
      <td>*</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>Điều kiện</td>
      <td>Xách tay</td>
      <td>Bảo vệ</td>
      <td>Mở</td>
      <td>Chìm</td>
    </tr>
    <tr>
      <td>Chuyển tiếp nhanh</td>
      <td>*</td>
      <td>Điện áp 2 kV trên các cổng nguồn a.c. Điện áp 1 kV chế độ chung trên các cổng điều khiển và tín hiệu. Tiêu chí chất lượng B</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chuyển tiếp chậm</td>
      <td>*</td>
      <td>1 kV cổng/đất, 0,5 kV cổng/cổng Cổng nguồn AC Tiêu chí chất lượng B</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Biến đổi nguồn ngắn hạn</td>
      <td>*</td>
      <td>Điện áp  20% cho 1,5 s, tần số  10% cho 5 s Cổng nguồn AC. Tiêu chí chất lượng B</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Hỏng nguồn</td>
      <td>*</td>
      <td>Ngắt 60 s Cổng nguồn a.c và d.c. Tiêu chí chất lượng C</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Phóng tĩnh điện</td>
      <td>Tiếp xúc 6 kV Không gian 8 kV Tiêu chí chất lượng B</td>
      <td></td>
      <td></td>
      <td>*</td>
    </tr>
  </tbody>
</table>

# 2. Thiết bị thu sóng vô tuyến

Nếu EUT có gắn thiết bị thu sóng vô tuyến, các tần số trong băng loại trừ, cùng với các đáp ứng của thiết bị thu băng hẹp (đáp ứng giả), phải không nằm trong các phép thử miễn nhiễm với nhiễu bức xạ và nhiễu dẫn.

# 2.1 Băng loại trừ

Băng loại trừ của thiết bị thu được định nghĩa là băng tần được khai thác của thiết bị thu, do nhà sản xuất công bố, mở rộng tại các giới hạn thêm $5 \%$ giá trị.

# 2.2 Đánh giá đáp ứng thiết bị thu

Đáp ứng băng hẹp cho phép (đáp ứng giả) được xác định bằng phương pháp sau:

Nếu tín hiệu thử (tín hiệu không mong muốn) làm suy giảm chất lượng tại một tần số riêng, tần số tín hiệu thử phải được tăng thêm một lượng gấp đôi độ rộng băng tần của bộ lọc IF máy thu nằm ngay trước bộ giải điều chế, theo như công bố của nhà sản xuất. Tín hiệu thử sau đó được giảm một lượng tương đương.

Nếu không có suy giảm chất lượng tại cả hai tần số này thì đáp ứng ở đây được gọi là đáp ứng băng hẹp cho phép. Nếu vẫn có suy giảm chất lượng, thì có thể do phần thay đổi đã làm cho tần số của tín hiệu thử tương ứng với một đáp ứng băng hẹp khác. Điều này được xác định bằng cách lặp lại các thủ tục trên bằng cách tăng và giảm tần số tín hiệu thử thêm 2,5 lần độ rộng băng tần ở trên.

Nếu vẫn có suy giảm chất lượng thì đáp ứng ở đây không được coi là đáp ứng băng hẹp cho phép.



# 3. Miễn nhiễm đối với nhiễu dẫn tần số vô tuyến

# 3.1 Mục đích

Mô phỏng ảnh hưởng của nhiễu gây ra bởi nguồn, tín hiệu và đường dây điều khiển từ các thiết bị phát sóng vô tuyến trên tàu tại các tần số dưới 80 MHz.

# 3.2 Quy trình đo

EUT được đặt trên một tấm đỡ cách điện có độ cao 0,1 m so với mặt phẳng tham chiếu đất. Thiết bị phụ trợ (AE) cần thiết cung cấp nguồn cho EUT và các tín hiệu cần thiết để được khai thác bình thường và kiểm tra chất lượng phải được kết nối với nhau bằng dây cáp, sẽ được cung cấp bởi các thiết bị ghép và tách thích hợp (CDNs) tại khoảng cách $^ { 0 , 1 \mathrm { ~ m ~ } }$ và $^ { 0 , 3 \mathrm { ~ m ~ } }$ từ EUT (Hình 7). TCVN 8241-4-6: 2009 chỉ rõ thiết kế của CDNs và các kẹp phun thay thế nếu không thể sử dụng CDN.

|<image_1>|

CHÚ THÍCH: T - Đầu cuối $5 0 \Omega$

<table>
  
  <tbody>
    <tr>
      <td>Điều kiện</td>
      <td>Xách tay</td>
      <td>Bảo vệ</td>
      <td>Mở</td>
      <td>Chìm</td>
    </tr>
    <tr>
      <td>CHÚ THÍCH: “*” - Không quy định</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

T2 - Khuyếch đại công suất (6 dB)

CDN - Mạng ghép/ tách

# Hình 7 - Sơ đồ thiết lập thử miễn nhiễm đối với nhiễu dẫn tần số vô tuyến

|<image_2>|

CHU THICH:CDN-M3, $C _ { 1 } \left( { \sf t y p } \right) = 1 0 \mathsf { n F }$ $C _ { 2 } \ ( \mathsf { t y p } ) = 4 7$ nF, $R = 3 0 0$ Ω,L≥280 $\mu \mathsf { H }$ tai150 kHz. CDN-M2, $C _ { 1 } \left( { \sf t y p } \right) = 1 0 \mathsf { n F }$ $C _ { 2 } \left( \mathrm { t y p } \right) = 4 7$ nF, $R = 2 0 0 ~ \Omega$ Ω, $L \geq 2 8 0 ~ \mu \ H$ tai150kHz. CDN-M1, $C _ { 1 } \left( { \sf t y p } \right) = 2 2 { \sf n F }$ $C _ { 2 } \left( \mathsf { t y p } \right) = 4 7$ nF, $R = \ d _ { 1 } 0 0 \Omega$ $L \geq 2 8 0 ~ \mu \ H$ tai150kHz.

# Hình 8 - Ví dụ minh họa sơ đồ đơn giản của CDN sử dụng với các nguồn cung cấp có lớp che chắn, trong phép thử nhiễu dẫn tần số vô tuyến

Phép thử phải được thực hiện với thiết bị phát thử nối lần lượt với các CDN, trong khi các cổng vào RF không kích thích đến CDN được nối với trở kháng $5 0 \Omega$ .

Thiết bị phát thử phải được thiết lập cho mỗi CDN và ngắt các kết nối AE và EUT thay bằng trở kháng $1 5 0 \Omega$ . Thiết bị phát thử phải cung cấp e.m.f không điều chế tại cổng EUT với mức thử yêu cầu.

Phép thử được tiến hành như trong TCVN 8241-4-6: 2009 với các mức thử sau:

- Biên độ 3 V r.m.s quét trong dải tần số từ $1 5 0 \mathrm { k H z }$ đến 80 MHz



- Biên độ $1 0 \mathrm { ~ V ~ }$ r.m.s tại tần số: 2 MHz, 3 MHz, 4 MHz, 6,2 MHz, 8,2 MHz, 12,6 MHz, $1 6 { , } 5 \mathrm { M H z }$ , 18,8 MHz, 22 MHz và 25 MHz.

Trong khi thử, điều chế biên độ tại $4 0 0 ~ \mathrm { H z } \pm 1 0 ~ \%$ với độ sâu $8 0 \% \pm 1 0 \%$ sẽ được sử dụng.

Tốc độ quét tần số không được vượt quá $1 , 5 \times 1 0 ^ { - 3 }$ decade/s để cho phép phát hiện lỗi của EUT.

Tín hiệu trên được đặt lên nguồn, tín hiệu và đường dây điều khiển của EUT. Phép kiểm tra chất lượng EMC sẽ được trực hiện trong và sau mỗi phép thử.

# 3.3 Yêu cầu kết quả

Các yêu cầu kiểm tra chất lượng EMC phải được thoả mãn trong và sau phép thử tương ứng với Tiêu chí chất lượng A.

# 4. Miễn nhiễm đối với phát xạ tần số vô tuyến

# 4.1 Mục đích

Mô phỏng ảnh hưởng của các thiết bị phát sóng vô tuyến tần số trên 80 MHz, như các thiết bị phát VHF đặt trên tàu, thiết bị radio cầm tay, đặt gần thiết bị.

# 4.2 Quy trình đo

Thiết bị phải được đặt trong một phòng che thích hợp hay buồng không có tiếng vọng và có kích thước tương xứng với EUT.

EUT cần đặt ở khu vực cường độ trường đồng nhất và cách điện với đất bằng giá đỡ phi kim. Khu vực đồng nhất được hiệu chuẩn khi phòng đo trống. Cấu hình của EUT và các cáp đi cùng sẽ được ghi trong biên bản thử nghiệm.

<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

|<image_3>|

# Hình 9 - Ví dụ điều kiện thử nghiệm thích hợp miễn nhiễmđối với tần số vô tuyến phân tán

Các dây dẫn song song sẽ được sử dụng nếu đường dây từ và đến EUT không được chỉ rõ, và để trần trong trường điện từ cách EUT $1 \textrm { m }$ .

Phép thử được tiến hành như trong TCVN 8241-4-3: 2009, tại mức nghiêm ngặt 3, với anten phát đặt đối diện với một trong bốn mặt của EUT. Khi thiết bị có thể được sử dụng theo các hướng khác nhau (thẳng đứng và nằm ngang), phép thử được tiến hành ở tất cả các mặt. EUT ban đầu được đặt sao cho một mặt trùng với mặt phẳng hiệu chuẩn. Dải tần được quét với tốc độ theo thứ tự là $1 , 5 \times 1 0 ^ { - 3 }$ decade/s với dải tần từ 80 MHz đến 1 GHz và $0 { , } 5 \times 1 0 ^ { - 3 }$ decade/s với dải tần từ 1 GHz đến 2 GHz, và đủ nhỏ để cho phép phát hiện bất kỳ lỗi chức năng nào của EUT. Bất kỳ tần số nhạy cảm hay có tính vượt trội nào cũng cần được phân tích riêng.

EUT được đặt trong điện trường điều chế với cường độ $1 0 \ \mathrm { V / m }$ quét trong dải tần từ 80 MHz đến 2 GHz. Điều chế tại $4 0 0 \mathrm { \ : H z } \pm 1 0 \%$ đến độ sâu $8 0 \% \pm 1 0 \%$ .

# 4.3 Yêu cầu kết quả



Các yêu cầu kiểm tra chất lượng EMC phải được thoả mãn trong và sau phép thử tương ứng với Tiêu chí chất lượng A .

# 5. Miễn nhiễm đối với đột biến nhanh nguồn AC, tín hiệu và đường điều khiển

# 5.1 Mục đích

Mô phỏng đột biến năng lượng thấp, nhanh gây ra do chuyển mạch thiết bị tạo nên cung lửa điện tại chỗ tiếp xúc.

# 5.2 Quy trình đo

Phép thử được tiến hành như trong IEC 61000-4-4, tại mức nghiêm ngặt 3, sử dụng thiết bị phát thử tuân thủ theo 6.1.1 của IEC 61000-4-4, mạng ghép/tách tuân thủ theo 6.2 của IEC 61000-4-4 cho các đường điện, và thiết bị kẹp ghép điện dung tuân thủ theo 6.3 của IEC 61000-4-4 cho tín hiệu và đường điều khiển (Hình 10).

|<image_4>|

CHÚ THÍCH: I - Khoảng cách giữa giá kẹp và EUT (không lớn hơn 1 m) (A) - Vị trí ghép đường nguồn

<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

(B) - Vị trí ghép đường tín hiệu

Hình 10 - Thiết lập thử nghiệm chung cho miễn nhiễm đối với đột biến nhanh Xung với các đặc tính sau được sử dụng cho nguồn, tín hiệu và đường điều khiển: - Thời gian quá độ: 5 ns (Giá trị nằm giữa $10 \%$ và $90 \%$ ). - Độ rộng: 50 ns ( $50 \%$ giá trị). - Biên độ: $2 \mathrm { k V }$ chế độ chênh lệch trên các đường điện AC, $1 \ \mathrm { k V }$ chế độ chênh lệch trên tín hiệu và đường điện. - Tốc độ lặp: 5 kHz (1 kV), 2,5 kHz (2 kV). - Ứng dụng: $1 5 \mathrm { m s }$ burst trong $3 0 0 \mathrm { m s }$ . - Chu trình: 3 phút đến 5 phút cho mỗi xung cực tính dương và âm.

# 5.3 Yêu cầu kết quả

Các yêu cầu kiểm tra chất lượng EMC phải được thoả mãn trong và sau phép thử tương ứng với Tiêu chí chất lượng B.
