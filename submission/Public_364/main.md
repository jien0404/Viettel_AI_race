# Public_364

# 1. Khái niệm mới về đối tượng của bài toán định vị

Mỗi đối tượng, mục tiêu định vị đều có thể sử dụng nhiều thiết bị di động 4G hoạt động trong nhiều môi trường mạng khác nhau. Do đó, đối tượng của bài toán định vị được qui về một thiết bị di động 4G, nó có thể là máy điện thoại di động, máy tính bảng, máy tính xách tay,… có gắn modul kết nối 4G/LTE/Wifi/Bluetooth. Các thiết bị đó hoạt động trên môi trường mạng 4G và chủ yếu được sử dụng để liên lạc (như gọi điện thoại, nhắn tin, kết nối truy cập Internet, giao tiếp mạng xã hội…) hay các hành động khác (như chụp ảnh, ghi âm, quay phim và truyền về nơi khác …). Đối tượng có thể sử dụng liên lạc bằng các dịch vụ gọi điện, nhắn tin truyền thống hoặc bằng các dịch vụ trên nền Internet. Do vậy, nếu thông qua theo dõi hoạt động của thiết bị di động 4G mà đối tượng mang theo, có thể xác định được thông tin về đối tượng (danh tính, vị trí hiện tại, vị trí sắp đến, liên hệ/quan hệ với ai,.. Trong đó, việc định vị, truy vết được đối tượng đó là quan trọng và thường xuyên nhất. Việc truy vết được đối tượng cũng sẽ xác định được các thông tin về đối tượng.

Nếu đã biết được đối tượng đó đăng ký và đang sử dụng một thuê bao di động 4G, thì có thể tìm được đối tượng thông qua việc định vị thuê bao đó. Cũng có thể thực hiện một cách dễ dàng hơn là hỏi nhà mạng di động thuê bao đó đang ở đâu (như trường hợp dịch vụ cứu hộ E911). Nhưng nếu không biết được đối tượng đang sử dụng thuê bao nào hoặc đối tượng sử dụng thiết bị di động 4G nhưng không phát sinh một cuộc gọi di động nào mà chỉ dùng để truy cập Internet, mạng xã hội hay đơn giản là liên lạc qua mạng thì bài toán định vị trở lên hết sức khó khăn. Khó khăn đầu tiên chính là làm thế nào để xác định được đối tượng đó. Do vậy, bài toán định vị đối tượng không còn thông thường là triển khai định vị ngay một thiết bị hay một số thuê bao di động 4G hoặc một thiết bị di động 4G nào đó mà trước tiên phải xác định được đối tượng, sau đó mới có được các dữ kiện chính xác cho bài toán định vị phù hợp sẽ áp dụng. Một đối tượng có thể được xác định chính xác bằng một tập các đặc điểm của nó. Qua thời gian, còn có các thông tin khác có thể xuất hiện như đối tượng đang ở đâu, làm việc gì, đi xe gì, xe của đối tượng đã xuất hiện những chỗ nào, đang truy cập Internet, mạng xã hội ở đâu.



(Lưu ý rằng ban đầu, việc xác định ở đâu là tương đối, ví như đang $\acute { o }$ nước nào/ thành phố nào/ khu vực nào bằng cách thông qua xác định địa chỉ IP mà đối tượng đang online trên Internet, mạng xã hội).

Về mặt kỹ thuật và dịch vụ di động, một con người thường được gắn với một số thuê bao di động nào đó (và ngược lại, từ một số thuê bao di động có thể truy vấn dữ liệu thuê bao của nhà mạng ra một con người nào đó đăng ký thuê bao). Khi thuê bao phát sinh một cuộc gọi, dữ liệu liên quan đến cuộc gọi đó (CDR) có nhiều thông tin như: mã nước, mã mạng di động, mã vùng di động, Cell-ID và Cell-LAC di động phục vụ, số bị gọi v.v…Từ các thông tin này, nếu trong trường hợp thuê bao gọi trên nền mạng 2G, có thể xác định được thuê bao tức đối tượng đó ở đâu (một cách tương đối) và đang liên hệ với ai (tức mối liên hệ của đối tượng đó). Nhưng nếu số thuê bao đó xuất hiện cuộc gọi nhưng đó là cuộc gọi trên nền mạng 3G/4G hay đơn thuần chỉ truy cập Internet/ Facebook…, mà User Name của dịch vụ đó lại được đăng ký từ một số thuê bao di động khác đồng thời lại ẩn danh thì việc xác định đó có là đối tượng cần truy tìm hay không là bài toán nan giải. Từ đây, việc định vị một đối tượng không thể chỉ thực hiện bằng cách định vị một số thuê bao di động nào đó mà đối tượng sử dụng như các nguyên lý định vị thông thường. Muốn định vị được một đối tượng hoạt động trên nền mạng 4G với đa dạng dịch vụ, đa dạng thiết bị như nói ở trên, trước tiên phải tìm kiếm một loạt thông tin khác nhau, từ đó xác định ra thông tin chính xác về đối tượng rồi mới có dữ kiện đưa vào bài toán định vị.

Gần đây, các nước tiên tiến đã mở rộng, đổi mới khái niệm về đối tượng, mục tiêu khi tiến hành định vị. Khái niệm này khá trừu tượng, cũng gần giống như nguyên lý triết học mà một con người bao giờ cũng nằm trong mối quan hệ tổng hòa của xã hội. Có thể nói tóm tắt, khái niệm về đối tượng đã được đổi mới, mở rộng sang khái niệm về mối liên hệ của nó, đối tượng không chỉ là ai như khi xác định đối tượng là một con người (hay số thuê bao di động của nó) mà chính là một tập đặc trưng của câu hỏi trên: ai, ở đâu, đi đâu, quan hệ với ai, làm gì, làm thế nào và mở rộng hơn là đi xe gì, sở thích gì, khám bệnh gì, hay đến đâu, mục đích và xu hướng của nó.



Đồng thời, với sự phát triển của công nghệ và dịch vụ số, mỗi đối tượng có hàng loạt thông tin xã hội liên quan có sẵn. Các thông tin liên quan đến nhau sẽ cùng xuất hiện và phải xác minh khi thực hiện một giao dịch trực tuyến nào đó. Tương tự đó, với mỗi đối tượng cần định vị, mà lại sử dụng thiết bị di động hoạt động trong môi trường mạng 4G thì việc xác định đối tượng đó không chỉ là dựa trên một dữ kiện mà phải là hàng loạt, hay một tập dữ kiện đặc trưng của nó và các dữ kiện liên quan đến nó. Tập dữ kiện đó được định nghĩa bằng một khái niệm mới mang các đặc trưng của đối tượng nằm trong mối liên hệ của nó và được gọi là một “Thực thể”, trong tiếng Anh là “Entity”.

Chẳng hạn, khi cần tìm kiếm một đối tượng, họ không chỉ định vị một đối tượng hay một số thuê bao di động cụ thể mà họ sẽ phân tích một loạt các dữ liệu, sự kiện liên quan của nó, tức phân tích, tìm kiếm một “thực thể”. Các dữ kiện “thực thể” đó có thể được phân tích từ các nguồn khác nhau có thể có như dữ liệu điện thoại di động/điện thoại vệ tinh/vị trí IP/facebook/GPS được trích xuất từ hình ảnh..., và loại của nó (IMSI/MSISDN/IMEI/TMSI/IP,...). Ngoài ra, cũng cần truy vấn, phân tích bổ sung trên các cơ sở dữ liệu tham chiếu, đã được làm giàu và từ đó sẽ tự động cảnh báo được các chỉ dẫn, hành vi đáng ngờ, hay đơn giản là xu hướng của nó.



# 2. Mô tả yêu cầu kỹ thuật cụ thể

Yêu cầu kỹ thuật cụ thể của bài toán định vị thiết bị di động thế hệ thứ tư được mô tả chi tiết trong bảng 2.1.

Bảng 2. 1. Yêu cầu kỹ thuật cụ thể của bài toán định vị   

<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Mô tả</td>
      <td>Yêu cầu kỹ thuật, tham số, trị số</td>
    </tr>
    <tr>
      <td>1. Yêu cầu chung</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>1.1. Xác định đối tượng định vị</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Loại đối tượng</td>
      <td>“Thực thể”</td>
    </tr>
    <tr>
      <td></td>
      <td>Mô tả thực thể</td>
      <td>Tập dữ liệu đặc trưng và dữ liệu liên quan đến đối tượng</td>
    </tr>
    <tr>
      <td></td>
      <td>Tên người</td>
      <td>Có</td>
    </tr>
    <tr>
      <td></td>
      <td>Số thuê bao điện thoại MSISDN</td>
      <td>Có</td>
    </tr>
    <tr>
      <td></td>
      <td>Địa chỉ địa lý</td>
      <td>Có</td>
    </tr>
    <tr>
      <td></td>
      <td>Địa chỉ IP sở hữu hoặc sử dụng</td>
      <td>Có</td>
    </tr>
    <tr>
      <td></td>
      <td>Thuê bao (account) Internet</td>
      <td>Có</td>
    </tr>
    <tr>
      <td></td>
      <td>Nick Name mạng xã hội</td>
      <td>Có</td>
    </tr>
    <tr>
      <td></td>
      <td>Các thông tin xã hội khác</td>
      <td>Có</td>
    </tr>
    <tr>
      <td>1.2. Định vị đối tượng</td>
      <td></td>
      <td>Các trị số yêu cầu (tính khả dụng, độ chính xác… tương ứng với các số liệu nguyên lý kỹ thuật đã phân tích, so sánh ở Chương 1.</td>
    </tr>
    <tr>
      <td></td>
      <td>Đối tượng của bài toán</td>
      <td>Thiết bị di động mà đối tượng mang theo</td>
    </tr>
    <tr>
      <td></td>
      <td>Loại thiết bị di động</td>
      <td>Điện thoại di động, máy tính bảng, máy tính xách tay, modul di động</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>Định vị phạm vi rộng của đối tượng</td>
      <td>Quốc gia, vùng lãnh thổ</td>
    </tr>
    <tr>
      <td></td>
      <td>Định vị phạm vi tương đối của đối tượng</td>
      <td>Tỉnh, thành phố</td>
    </tr>
    <tr>
      <td></td>
      <td>Định vị phạm vi hẹp của đối tượng</td>
      <td>Ô di động (Cell-ID/ Cell LAC), Sector BTS/eNB</td>
    </tr>
    <tr>
      <td></td>
      <td>Định vị vị trí chính xác của đối tượng</td>
      <td>Tọa độ địa lý, số nhà, đường phố, tòa nhà, căn phòng…</td>
    </tr>
    <tr>
      <td></td>
      <td>Truy vết đối tượng</td>
      <td>Lịch sử vị trí, đường đi</td>
    </tr>
    <tr>
      <td></td>
      <td>Xác định mối quan hệ của đối tượng</td>
      <td>Mối quan hệ liên lạc, biểu đồ quan hệ</td>
    </tr>
    <tr>
      <td>2. Thu thập dữ liệu đầu vào của bài toán định vị</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Dữ liệu từ mạng di động và mạng báo hiệu</td>
      <td>- Cell-ID, Cell LAC phục vụ, số gọi, số bị gọi, thời gian cuộc gọi, loại cuộc gọi …được lập thành cơ sở dữ liệu chi tiết cuộc gọi (CDR). - Dữ liệu của mạng di động: MCC, MNC, Cell-ID database - Dữ liệu của mạng báo hiệu: SPC…</td>
    </tr>
    <tr>
      <td></td>
      <td>Dữ liệu từ máy cầm tay</td>
      <td>IMSI, IMEI và các tham số vô tuyến, tham số GNSS</td>
    </tr>
    <tr>
      <td></td>
      <td>Dữ liệu từ SIM</td>
      <td>MSISDN và các tham số định danh</td>
    </tr>
    <tr>
      <td></td>
      <td>Dữ liệu từ Wifi</td>
      <td>Các tham số của Wifi Access Point và các tham số vô tuyến</td>
    </tr>
    <tr>
      <td></td>
      <td>Dữ liệu môi trường mạng mở</td>
      <td>-Tất cả dữ liệu liên quan đến truy cập Internet, sử dụng mạng xã hội, sử dụng dịch vụ OTT như IP Address, Iternet Account, FB Acount, Nick Name, Media….</td>
    </tr>
  </tbody>
</table>



3. Thu thập dữ liệu tham chiếu của bài toán định vị

<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>- Dữ liệu Cell-ID toàn cầu từ nguồn mở - Dữ liệu Wifi toàn cầu từ nguồn mở</td>
    </tr>
    <tr>
      <td>3. Thu thập dữ liệu tham chiếu của bài toán định vị</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Dữ liệu thuê bao di động</td>
      <td>Cơ sở dữ liệu thuê bao của nhà mạng</td>
    </tr>
    <tr>
      <td></td>
      <td>Dữ liệu địa lý</td>
      <td>Bản đồ số, bản đồ hành chính, bản đồ Google Maps.</td>
    </tr>
    <tr>
      <td></td>
      <td>Dữ liệu khác liên quan</td>
      <td>Những dữ liệu liên quan đến hoạt động xã hội khác như mô tả ở khái niệm đối tượng</td>
    </tr>
    <tr>
      <td>4. Đầu ra của bài toán định vị</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Số liệu vị trí phạm vi rộng</td>
      <td>Có, theo phạm vị quốc gia, vùng lãnh thổ</td>
    </tr>
    <tr>
      <td></td>
      <td>Số liệu vị trí phạm vi tương đối</td>
      <td>Có, theo phạm vi tỉnh, thành phố</td>
    </tr>
    <tr>
      <td></td>
      <td>Số liệu vị trí phạm vi hẹp</td>
      <td>Có, theo bán kính Cell di động</td>
    </tr>
    <tr>
      <td></td>
      <td>Số liệu vị trí chính xác</td>
      <td>Có</td>
    </tr>
    <tr>
      <td></td>
      <td>Truy vết lịch sử vị trí và đường đi</td>
      <td>Có, theo độ chính xác của bản đồ số Google Map (trực tuyến hoặc không trực tuyến) hoặc theo độ chính xác của bản đồ số chuyên dụng (nếu cài đặt và sử dụng)</td>
    </tr>
    <tr>
      <td></td>
      <td>Xác định đồ thị mối quan hệ</td>
      <td>Có, đồ thị GraphTech mối quan hệ.</td>
    </tr>
  </tbody>
</table>

4. Đầu ra của bài toán định vị
