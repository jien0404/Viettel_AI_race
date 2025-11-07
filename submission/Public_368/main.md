# Public_368

# 1. Kích cỡ khối để thử luồng PDH

Kích cỡ khối để thử luồng PDH trong hệ thống đang khai thác được cho trong Bảng 6.

# Bảng 6 - Kích cỡ khối PDH

<table>
  
  <tbody>
    <tr>
      <td>Tốc độ bit của luồng PDH kbit/s</td>
      <td>Kích cỡ khối PDH bit</td>
      <td>EDC/không có EDC</td>
    </tr>
    <tr>
      <td>2048 8448 34368 139264</td>
      <td>2048 4224 4296 17408</td>
      <td>CRC-4 Không có EDC Không có EDC Không có EDC</td>
    </tr>
  </tbody>
</table>

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

<table>
  
  <tbody>
    <tr>
      <td>Kiểu luồng</td>
      <td>Các thông số</td>
      <td>Tiêu chuẩn đo</td>
    </tr>
    <tr>
      <td>1</td>
      <td>ESR</td>
      <td>Một giây bị lỗi quan sát được khi trong một giây ít nhất có một bất bình thường a1 hoặc a2 hoặc một sai hỏng d1 đến d3 xảy ra.</td>
    </tr>
    <tr>
      <td></td>
      <td>SESR</td>
      <td>Một giây bị lỗi nghiêm trọng quan sát được khi trong một giây ít nhất có ‘x’ bất bình thường a1 hoặc a2, hoặc một sai hỏng d1 đến d3 xảy ra.</td>
    </tr>
  </tbody>
</table>



# 6. Tiêu chuẩn cho việc phát hiện một giây bị lỗi nghiêm trọng trong luồng PDH

Bảng 8 liệt $\mathrm { k } \hat { \mathrm { e } }$ giá trị ‘x’ gây ra một giây bị lỗi nghiêm trọng (SES) trong khi kiểm tra hệ thống đang khai thác.

Bảng 8 - Tiêu chuẩn có SES trên các tuyến PDH

<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>BBER</td>
      <td>Một lỗi khối cơ bản quan sát được khi: một bất bình thường a1 hoặc a2 xảy ra trong một khối nhưng không thuộc phần giây bị lỗi nghiêm trọng.</td>
    </tr>
    <tr>
      <td>2</td>
      <td>ESR</td>
      <td>Một giây bị lỗi quan sát được khi trong một giây ít nhất có một bất bình thường a1 hoặc một sai hỏng d1 đến d3 xảy ra</td>
    </tr>
    <tr>
      <td></td>
      <td>SESR</td>
      <td>Một giây bị lỗi nghiêm trọng quan sát được khi trong một giây ít nhất có ‘x’ bất bình thường a1 hoặc một sai hỏng d1 hoặc d2 xảy ra.</td>
    </tr>
    <tr>
      <td>3</td>
      <td>ESR</td>
      <td>Một giây bị lỗi quan sát được khi trong một giây ít nhất có một bất bình thường a1 hoặc một sai hỏng d1 hoặc d2 xảy ra.</td>
    </tr>
    <tr>
      <td></td>
      <td>SESR</td>
      <td>Một giây bị lỗi nghiêm trọng quan sát được khi trong một giây có ít nhất ‘x’ bất bình thường a1 hoặc một sai hỏng d1 hoặc d2 xảy ra</td>
    </tr>
    <tr>
      <td>4</td>
      <td></td>
      <td>Một giây bị lỗi nghiêm trọng quan sát được khi trong một giây ít nhất có một sai hỏng d1 hoặc d2 xảy ra.</td>
    </tr>
  </tbody>
</table>
