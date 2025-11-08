# Public_371

# 1. Khái niệm

|<image_1>|

Hình 1.Giới hạn miền phát xạ ngoài băng, miền phát xạ giả

# 2. Giới hạn dải tần đo phát xạ không mong muốn (ITU-REC SM.329-12 [3])

<table>
  
  <tbody>
    <tr>
      <td>Dải tần cơ sở</td>
      <td>Dải tần đo</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Giới hạn dưới</td>
      <td>Giới hạn trên (Phép đo phải bao gồm toàn bộ băng tần hài và không được cắt tại các giới hạn trên được chỉ ra)</td>
    </tr>
    <tr>
      <td>9 kHz ÷ 100 MHz</td>
      <td>9 kHz</td>
      <td>1 GHz</td>
    </tr>
    <tr>
      <td>100 MHz ÷ 300 MHz</td>
      <td>9 kHz</td>
      <td>Hài bậc 10</td>
    </tr>
  </tbody>
</table>



# 3. Xác định ranh giới miền phát xạ ngoài băng và miền phát xạ giả

Ranh giới miền phát xạ ngoài băng và phát xạ giả tại giá trị tần số cách tần số trung tâm của phát xạ được đưa ra trong Bảng C.1, Bảng C.2, Bảng C.3 sau đây.

Trong phần lớn các hệ thống, tần số trung tâm của phát xạ $( f _ { c } )$ là tần số trung tâm của băng thông cần thiết $( B _ { N } )$ .

Đối với máy phát/bộ phát đáp sử dụng đa kênh truyền hoặc đa sóng mang, khi một vài sóng mang có thể được truyền đồng thời từ bộ khuếch đại cuối cùng của lối ra hoặc từ anten tích cực, tần số trung tâm của phát xạ được lấy từ tần số trung tâm của băng thông 3 dB của máy phát hoặc bộ phát đáp đó và băng thông của máy phát hay bộ phát đáp đó được sử dụng thay thế cho băng thông cần thiết trong việc quyết định ranh giới.

Đối với hệ thống vệ tinh đa sóng mang, hướng dẫn về cách xác định ranh giới miền phát xạ ngoài băng và phát xạ giả được nêu trong khuyến nghị ITU-R SM.1541 [6] mới nhất.

Một số hệ thống chỉ rõ các phát xạ không mong muốn phụ thuộc vào băng thông của kênh hay độ rộng kênh. Các giá trị này có thể được sử dụng thay thế cho băng thông cần thiết trong Bảng C.1 sau đây nếu chúng được đề cập trong các Khuyến nghị của ITU.

Bảng C.1 - Ranh giới miền phát xạ giả và phát xạ ngoài băng

<table>
  
  <tbody>
    <tr>
      <td>300 MHz ÷ 600 MHz</td>
      <td>30 MHz</td>
      <td>3 GHz</td>
    </tr>
    <tr>
      <td>600 MHz ÷ 5,2 GHz</td>
      <td>30 MHz</td>
      <td>Hài bậc 5</td>
    </tr>
    <tr>
      <td>5,2 GHz ÷ 13 GHz</td>
      <td>30 MHz</td>
      <td>26 GHz</td>
    </tr>
    <tr>
      <td>13 GHz ÷ 150 GHz</td>
      <td>30 MHz</td>
      <td>Hài bậc 2</td>
    </tr>
    <tr>
      <td>150 GHz ÷ 300 GHz</td>
      <td>30 MHz</td>
      <td>300 GHz</td>
    </tr>
  </tbody>
</table>



CHÚ THÍCH: $\mathrm { B v }$ là băng thông cần thiết; $( f _ { c } )$ là tần số trung tâm của $\mathrm { B v }$

Trong một số nghiệp vụ, ranh giới miền phát xạ ngoài băng và phát xạ giả được tính theo Bảng C.2 (thay thế cho Bảng C.1):

<table>
  
  <tbody>
    <tr>
      <td>Dải tần</td>
      <td>Trường hợp băng hẹp</td>
      <td></td>
      <td>Khoảng cách thông thường</td>
      <td>Trường hợp băng rộng</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Với BN <</td>
      <td>Khoảng cách</td>
      <td></td>
      <td>Với BN ></td>
      <td>Khoảng cách</td>
    </tr>
    <tr>
      <td>9 kHz < fc  150 kHz</td>
      <td>250 Hz</td>
      <td>625 Hz</td>
      <td>2,5 BN</td>
      <td>10 kHz</td>
      <td>1,5 BN + 10 kHz</td>
    </tr>
    <tr>
      <td>150 kHz < fc  30 MHz</td>
      <td>4 kHz</td>
      <td>10 kHz</td>
      <td>2,5 BN</td>
      <td>100 kHz</td>
      <td>1,5 BN + 100 kHz</td>
    </tr>
    <tr>
      <td>30 MHz < fc  1 GHz</td>
      <td>25 kHz</td>
      <td>62,5 kHz</td>
      <td>2,5 BN</td>
      <td>10 MHz</td>
      <td>1,5 BN + 10 MHz</td>
    </tr>
    <tr>
      <td>1 GHz < fc  3 GHz</td>
      <td>100 kHz</td>
      <td>250 kHz</td>
      <td>2,5 BN</td>
      <td>50 MHz</td>
      <td>1,5 BN + 50 MHz</td>
    </tr>
    <tr>
      <td>3 GHz < fc  10 GHz</td>
      <td>100 kHz</td>
      <td>250 kHz</td>
      <td>2,5 BN</td>
      <td>100 MHz</td>
      <td>1,5 BN + 100 MHz</td>
    </tr>
    <tr>
      <td>10 GHz < fc  15 GHz</td>
      <td>300 kHz</td>
      <td>750 kHz</td>
      <td>2,5 BN</td>
      <td>250 MHz</td>
      <td>1,5 BN + 250 MHz</td>
    </tr>
    <tr>
      <td>15 GHz < fc  26 GHz</td>
      <td>500 kHz</td>
      <td>1,25 MHz</td>
      <td>2,5 BN</td>
      <td>500 MHz</td>
      <td>1,5 BN + 500 MHz</td>
    </tr>
    <tr>
      <td>fc > 26 GHz</td>
      <td>1 MHz</td>
      <td>2,5 MHz</td>
      <td>2,5 BN</td>
      <td>500 MHz</td>
      <td>1,5 BN + 500 MHz</td>
    </tr>
  </tbody>
</table>

Bảng C.2 - Trường hợp băng hẹp và rộng với một số nghiệp vụ   



<table>
  
  <tbody>
    <tr>
      <td>Hệ thống hoặc nghiệp vụ</td>
      <td>Dải tần số</td>
      <td></td>
      <td>Trường hợp băng hẹp</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>Với BN</td>
      <td>Khoảng cách</td>
    </tr>
    <tr>
      <td>Trường hợp băng hẹp với một số nghiệp vụ</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Nghiệp vụ cố định</td>
      <td>14 kHz – 1,5 MHz</td>
      <td></td>
      <td>< 20 kHz</td>
      <td>50 kHz</td>
    </tr>
    <tr>
      <td></td>
      <td>1,5 MHz – 30 MHz</td>
      <td>PT  50 W</td>
      <td>< 30 kHz</td>
      <td>75 kHz</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>PT > 50 W</td>
      <td>< 80 kHz</td>
      <td>200 kHz</td>
    </tr>
    <tr>
      <td>Trường hợp băng rộng với một số nghiệp vụ</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Nghiệp vụ cố định</td>
      <td>14 Hz ÷ 150 kHz</td>
      <td></td>
      <td>> 20 kHz</td>
      <td>1,5 BN + 20 kHz</td>
    </tr>
    <tr>
      <td>Nghiệp vụ cố định qua vệ tinh (FSS)</td>
      <td>3,4 GHz ÷ 4,2 GHz</td>
      <td></td>
      <td>> 250 MHz</td>
      <td>1,5 BN + 250 MHz</td>
    </tr>
    <tr>
      <td>FSS</td>
      <td>5,725 GHz ÷ 6,725 GHz</td>
      <td></td>
      <td>> 500 MHz</td>
      <td>1,5 BN + 500 MHz</td>
    </tr>
    <tr>
      <td>FSS</td>
      <td>7,25 GHz ÷ 7,75 GHz và 7,9 GHz ÷ 8,4 GHz</td>
      <td></td>
      <td>> 250 MHz</td>
      <td>1,5 BN + 250 MHz</td>
    </tr>
  </tbody>
</table>



CHÚ THÍCH: $\mathrm { P r }$ là công suất phát; $\mathrm { B _ { N } }$ là băng thông cần thiết
