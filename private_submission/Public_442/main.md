# Public_442

<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>1.1</td>
      <td>Xử lý theo danh sách khách hàng : - Có chức năng xử lý theo danh sách các nhóm KH - Có chức năng xử lý theo gói cước (vd gói dân tộc) được phép gọi vào</td>
      <td></td>
      <td>1. Đầu số 1789: nhóm danh sách: - Khi khách hàng gọi lên đầu số 1789, hệ thống kiểm tra xem đầu số KH đang gọi thuộc nhóm nào thì định tuyến về nhóm đó. - Kênh điểm bán, KH nội bộ - 2 nguồn nhóm: Lấy từ các hệ thống khác (WS trả về mã nhóm), Hoặc tạo thủ công, có thể add thủ công các khách hàng - Màn hình quản lý nhóm khách hàng : Thêm mới các nhóm khách hàng + Cấu hình mã nhóm + Luật ưu tiên nhóm khách hàng (1 khách hàng thuộc nhiều nhóm, nhưng sẽ xử lý theo kịch bản ưu tiên) - Tích hợp API check nhóm + check gói cước (line dân tộc)</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>1.2</td>
      <td>Xử lý theo vị trí khách hàng gọi lên : Phát nhac theo tỉnh trên IVR, VIP theo tỉnh</td>
      <td></td>
      <td>* Các bất cập hiện có: - Khi khai báo IVR lên thì phải có người thực hiện lại test âm báo cho từng 63CN, khi có bão lũ không sử dụng được,… các nhiều trường hợp không sử dụng được. (anh Tungtt2 gửi lại các tài liệu mô tả bất cập hiện có của hệ thống cũ về các tính năng này) -> Cải thiện những vấn đề bất cập - Mong muốn 1: Công cụ để test âm báo cho từng tỉnh thành khi cấu hình file audio tương ứng với các tỉnh - Giải pháp: sử dụng 3cx để thực hiện test cuộc gọi, khai báo suxfix lên 3cx và thực hiện cuộc gọi test lên hệ thống để test âm báo - Mong muốn 2: Phát âm báo theo tỉnh, theo hạng (từ nhiều nguồn, cả tự động và thủ công) , theo nhóm khách hàng (nguời dùng chủ động định nghĩa nhóm trên hệ thống) Chú ý*: Nhóm định nghĩa: Mỗi nhóm được tạo và gắn mã code, khi có cuộc gọi thì check mã nhóm của KH và tự động add KH vào nhóm + add thủ công vào nhóm Nhóm thủ công: Tạo nhóm và add khách hàng thủ công vào nhóm</td>
    </tr>
  </tbody>
</table>







<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>1.6</td>
      <td>Tự động check ngưỡng nghẽn : - Xử lý theo ngưỡng, hỗ trợ nhiều ngưỡng - và SMS điều hướng KH sử dụng kênh tương tác khác</td>
      <td></td>
      <td>1 ( KH gọi lên hệ thống, khi queue có 100 TVV, VD: queue 100% TVV đang gặp KH - Ngưỡng 1 queue 90% TVV đang gặp KH - Ngưỡng 2 ,... => Hệ thống đánh giá có tạo thêm cuộc gọi hay không, với mỗi ngưỡng có thể cấu hình hành động là gì (chuyển node, ivr, gửi tin nhắn cảnh báo,...) . Khi gọi vào IVR, cho phép so sánh ngưỡng nghẽn của 1 Queue ACD. - Có thể cấu hình ngưỡng nghẽn - Có thể cấu hình IVR, Tại 1 node IVR, có thể: + Kiểm tra ngưỡng nghẽn 1 queue -> Đưa ra kết quả -> Cấu hình các bước xử lý tiếp theo + So sánh ngưỡng nghẽn của các queue -> Đưa ra kết quả -> Cấu hình các bước xử lý tiếp theo 2. Gửi SMS điều hướng KH sử dụng kênh tương tác khác (khi đạt ngưỡng nghẽn, ...). Cho phép KH nhập nội dung tin nhắn tài liệu IBM - anh Tungtt2 gửi lại)</td>
    </tr>
    <tr>
      <td>1.7</td>
      <td>Cho phép định tuyến cuộc gọi vào IVR theo thời gian</td>
      <td>Bổ xung mới : - Định tuyến vào cây IVR tương ứng theo các khoảng thời gian KH gọi vào theo từng đầu số - Mỗi đầu số có thể đặt tối thiểu 10 khoảng thời gian</td>
      <td>1. Hiện tại: KH gọi vào ACD thì cấu hình thời gian này cho gặp TVV, tgian này cho vào IVR 2. Mong muốn: Với cây IVR, KH gọi vào giờ A thì thực hiện hành động gì, giờ B thì thực hiện hành động gì</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>1.8</td>
      <td>Nhận diện giọng nói qua IVR (voice - eKYC)</td>
      <td>Bổ xung mới : - HD khách hàng đọc đoạn âm theo hướng dẫn để thực hiện nhận dạng - Cấu hình được việc chuyển file ghi âm của KH đến hệ thống so sánh nhận diện khác nhau tùy theo dịch vụ Cụ thể: 1. Luồng selfcare trên IVR (đã mô tả bên cạnh) 2. Luồng kiểm tra trong lúc đàm thoại: - ĐTV click button xác minh KH trên giao diện nghiệp vụ BCCS -> BCCS check ht eKYC xem SĐT này đăng kí eKYC chưa-> Nếu có thì BCCS thực hiện gửi yc sang IPCC để IPCC lấy 1 phần ghi âm cuộc gọi hiện tại gửi sang ht eKYC -> eKYC so sánh dữ liệu trả về kết quả xác minh trên giao diện BCCS cho</td>
      <td>1. Khi KH gọi lên mong muốn tra cứu thông tin, thực hiện thao tác nghiệp vụ - Hệ thống thực hiện Check đã đăng ký eKYC hay chưa (KH bấm phím chọn) - Hệ thống kiểm tra KH đã có đăng ký trên eKYC hay chưa (kiểm tra trên hệ thống eKYC), trả kết quả về hệ thống, nếu đúng khách hàng thì thực hiện nghiệp vụ 2. Nghiệp vụ Đăng ký eKYC 3. Hỗ trợ cho phép kết nối tới nhiều hệ thống eKYC khác nhau</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>M - ĐTV -> ĐTV dựa vào KQ để thực hiện nghiệp vụ cho KH mà KH không bị hỏi han nhiều. ô tả thêm: 1. LUỒNG CHUNG trên IVR KH gọi -> Ipcc -> IVR -> : + VAS connector check các điều kiện bài toán AI , + VAS connector Check sang hệ thống Voicebiometric xem KH đã đăng kí chưa + Phát âm HD bấm phím (tr hợp đã đăng kí và TH chưa đăng kí có âm HD riêng) + Check xem KH có bấm nhánh đến nhánh nào (nhánh đăng kí API/nhánh tra cứu API/ nhánh đăng kí & tra cứu qua voice eKYC/ nhánh chuyển</td>
      <td></td>
    </tr>
  </tbody>
</table>







<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>eKYC (Để đăng kí các dịch vụ A,B,C dùng voice eKYC quý khách vui lòng bấm phím X) + IPCC check sang ht Voice eKYC xem KH đã đăng kí chưa : Đã đăng kí -> check xem có đúng chính chủ không - > đúng chính chủ -> Báo lại IPCC -> IPCC tác động sang các HT khác để đăng kí. () Đã đăng kí -> check xem có đúng chính chủ không - > Không chính chủ -> Báo lại IPCC -> Hd khách hàng dùng chức năng gặp ĐTV hoặc đăng kí lại. () Đã đăng kí -> check xem có đúng chính chủ không - > Không chính chủ nhiều lần trong ngày -> Báo lại IPCC -> Hd khách hàng dùng chức năng</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>gặp ĐTV hoặc đăng kí lại. Chưa đăng kí -> Chuyển sang hd đăng kí như ở case 1 Case 3: KH đăng kí lại voice eKYC như thế nào + Cần có nghiệp vụ vhi tiết để bảo đảm không bị giả mạo??? 2. Luồng trên BCCS:</td>
      <td></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Xử lý phím bấm</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2.1</td>
      <td>Bấm phím để chọn nhánh Trả lời tự động</td>
      <td></td>
      <td>Bấm phím để chọn nhánh Trả lời tự động</td>
    </tr>
    <tr>
      <td>2.2</td>
      <td>Phím #, *</td>
      <td></td>
      <td>Phím #, *</td>
    </tr>
    <tr>
      <td>2.3</td>
      <td>Phát âm khi bấm phím sai</td>
      <td></td>
      <td>Phát âm khi bấm phím sai</td>
    </tr>
    <tr>
      <td>2.4</td>
      <td>Cấu hình phát lặp</td>
      <td></td>
      <td>1. Cấu hình động số lần phát lặp lại file media 2. Cấu hình động thời gian chờ khách hàng bấm phím</td>
    </tr>
    <tr>
      <td>2.5</td>
      <td>Bấm phím lớn hơn hoặc bằng 2 chữ số</td>
      <td></td>
      <td>Bấm phím lớn hơn hoặc bằng 2 chữ số</td>
    </tr>
    <tr>
      <td>2.6</td>
      <td>Xử lý khi không bấm phím (chuyển vào nhánh IVR, chuyển queue...)</td>
      <td>- Cho phép cấu hình trên bất kì Node IVR nào nếu KH không thao tác sẽ chuyển đến ĐTV (hiện tại đã đáp ứng, muốn chuyển đến node nào thì dựng link đến node cần chuyển, trên link đó khai điều kiện thực hiện link, có thể là Noaudio (không bấm phím), Mã phím (bấm phím), defaule (defaule chuyển đến node nào đó)</td>
      <td>1. Cấu hình file NoAudio, khi phát hết file media, khách hàng không bấm gì thì lập tức thực hiện chuyển tiếp tới các hành động khác đã cấu hình</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2.7</td>
      <td>Hỗ trợ DTMF inband và outband</td>
      <td></td>
      <td>2 1. DTMF: Dual tall frequency: hỗ trợ gửi các phím bấm lên tổng đài. Khi KH bấm phím, DTMF hỗ trợ mã hóa các phím bấm và gửi lên tổng đài, tổng đài thực hiện giải mã các tín hiệu phím bấm được gửi lên . Hệ thống MyCC có hỗ trợ cấu hình chọn inband hoặc outband được không?</td>
    </tr>
    <tr>
      <td>2.8</td>
      <td>Bấm phím gặp điện thoại viên</td>
      <td></td>
      <td>Bấm phím gặp điện thoại viên</td>
    </tr>
    <tr>
      <td>2.9</td>
      <td>Node phát nhiều file nhạc. Node play music hỗ trợ phát nhạc thay đổi theo khung giờ.</td>
      <td></td>
      <td>1. Mong muốn: Cấu hình được nhiều file phát trong 1 lần 2. Cấu hình theo luật phát (VD: xoay vòng, ngẫu nhiên,…)</td>
    </tr>
    <tr>
      <td>2.10</td>
      <td>Âm báo riêng với từng mã lỗi dịch vụ của thuê bao</td>
      <td></td>
      <td>- Tổng đài báo lỗi dịch vụ cố định 18008119: phát thông báo tình trạng lỗi liên quan đến dịch vụ cố định băng rộng(CĐBR) theo số gọi lên để khách hàng có thể tự seflcare hoặc có thể biết tình trạng lỗi thuê bao của mình ở tình trạng như thế nào. Thông tin lỗi do tư vấn viên(TVV) cung cấp(tất cả các cuộc gọi phản ánh dịch vụ: chất lượng kém, chập chờn, mất dịch vụ...). - Tổng đài báo lỗi dịch vụ di động</td>
    </tr>
    <tr>
      <td>2.11</td>
      <td>Smart IVR 1 – tra cứu/ đăng kí gói data/VAS</td>
      <td></td>
      <td>- Xây dựng Smart IVR đăng ký gói cước theo từng kịch bản nghiệp vụ</td>
    </tr>
    <tr>
      <td>2.12</td>
      <td>Smart IVR 1 – tra cứu/ đăng kí gói data/VAS - Báo cáo thông kê cho phép chủ động khai báo để thông kê gói mới mà ko cần nâng câp báo cáo</td>
      <td></td>
      <td>- Xây dựng báo cáo thống kê phím bấm, tổng hợp đăng ký, chi tiết với từng gói cước</td>
    </tr>
    <tr>
      <td>2.13</td>
      <td>Smart IVR 2 - thông báo lỗi nợ cước</td>
      <td></td>
      <td>Smart IVR 2 - thông báo lỗi nợ cước</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2.14</td>
      <td>Smart IVR 3 - thông báo sự cố (cố định/di động)/tạo phản ánh tự động về BCCS</td>
      <td>Lưu ý luồng tạo phản ánh tự động</td>
      <td>Smart IVR 3 - thông báo sự cố (cố định/di động)/tạo phản ánh tự động về BCCS</td>
    </tr>
    <tr>
      <td>2.15</td>
      <td>Smart IVR 4 - tạm mở nợ cước</td>
      <td></td>
      <td>Khi KH gọi lên tổng đài di động và có yêu cầu, TVV có thể tạm mở chặn một chiều cho khách hàng nếu khách hàng yêu cầu, thời gian tạm mở đến hết chu kỳ cước.</td>
    </tr>
    <tr>
      <td>2.16</td>
      <td>Smart IVR 5 - tích điểm, đổi điểm</td>
      <td></td>
      <td>Smart IVR 5 - tích điểm, đổi điểm</td>
    </tr>
    <tr>
      <td>2.17</td>
      <td>Smart IVR 6 - tra cứu thông tin, gói cước đang sử dụng</td>
      <td></td>
      <td>Tra cứu gói data trên 191 - 1228</td>
    </tr>
    <tr>
      <td>2.18</td>
      <td>Smart IVR 8 – đăng kí đổi SIM</td>
      <td></td>
      <td>- Cho phép khai báo động các kịch bản Smart IVR (dự kiến bổ sung Smart IVR đăng ký đổi SIM 5G) - Hệ thống IVR 197 xây dựng thêm 01 phím bấm cho KH thao tác đăng ký đổi sim 4G. Khi KH bấm phím đổi sim, hệ thống IVR gửi yêu cầu sang hệ thống quản lý đơn hàng, tự động tạo thành thành 01 yêu cầu đổi sim trên hệ thống Order, nhân viên địa bàn tiếp nhận và liên hệ đổi sim tại nhà cho KH. Khi KH đổi sim 4G thà nh công, hệ thống tự động cộng các ưu đãi cho KH theo chính sách hiện hành tương tự như khi KH đổi sim 4G qua SMS. - Báo cáo: Báo cáo tổng hợp thuê bao đăng ký đổi sim qua IVR, Báo cáo chi tiết thuê bao đăng ký đổi sim qua IVR (đây chính là các tác động đăng ký đổi sim, hệ thống gửi</td>
    </tr>
  </tbody>
</table>











<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2.24</td>
      <td>Cho phép nhập thông tin từ IVR để xử lý kịch bản (đối thủ có)</td>
      <td>- Bổ xung mới: - Cho phép nhập vd SDT/CMND/CCCD - Cho phép nhập mã số thuế, nhập số ID dịch vụ, mã nhập đơn hàng (cả số và chữ)... vd : KH -> Phát âm hỏi tra cho số nào -> chọn số đang gọi, số khác -> Nhập số khác -> yc nhập thông tin xác minh -> OK -> check đơn hàng liên quan -> đọc lại mã đơn hàng cho KH xác nhận -> OK thì báo lại lịch trình cho KH Cho phép khai báo cấu hình node IVR với mã Node ID nào đó: + Node này cho phép cấu hình khai báo chuyển các thông tin INPUT sang 1 hoặc nhiều Webservice nào đó + Với các giá trị trả về thì xử lý các kịch bản tương ứng (phát file, chuyển node</td>
      <td>- 1. Đáp ứng nhập số 2. Xây dựng API Gateway 3. Xây dựng WS kiểm tra thông tin cho KH Bổ xung mới: - Cho phép nhập vd SDT/CMND/CCCD - Cho phép nhập mã số thuế, nhập số ID dịch vụ, mã nhập đơn hàng (cả số và chữ)... vd : KH -> Phát âm hỏi tra cho số nào -> chọn số đang gọi, số khác -> Nhập số khác -> yc nhập thông tin xác minh -> OK -> check đơn hàng liên quan -> đọc lại mã đơn hàng cho KH xác nhận -> OK thì báo lại lịch trình cho KH Cho phép khai báo cấu hình node IVR với mã Node ID nào đó: + Node này cho phép cấu hình khai báo chuyển các thông tin INPUT sang 1 hoặc nhiều Webservice nào đó + Với các giá trị trả về thì xử lý các kịch bản tương ứng (phát file, chuyển node khác...) + Khai báo kết nối được đến các WS của các Doanh nghiệp có Puplic internet dễ dàng qua giao diện (tham khảo Mitek : giao dịch nhập đơn hàng/tra đơn hàng..</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>khác...) + Khai báo kết nối được đến các WS của các Doanh nghiệp có Puplic internet dễ dàng qua giao diện (tham khảo Mitek : giao dịch nhập đơn hàng/tra đơn hàng...)</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2.25</td>
      <td>Việc cấu hình khai báo kết nối đến các ht khác lấy thông tin có thể thực hiện qua giao diện thay vì phải làm thủ tục UPCODE</td>
      <td>- Cấu hình qua giao diện, tham khảo thêm yêu cầu ở 10.3 - Có giao diện báo cáo tình hình trao đổi thông tin giữa IPCC và các WS hệ thống IPCC kết nối đến để đánh giá tình trạng WS : + Số lượng bản tin bị timeout của từng WS + Số lượng cuộc gọi báo lỗi kết nối WS : vd sai định dạng đầu vào, sai đầu ra...</td>
      <td>Tương tự bài toán API gateway Liệt kê danh sách các chuẩn của API đang được hỗ trợ (REST và SOAP) - Liệt kê và gửi lại thông tin cho VTT</td>
    </tr>
    <tr>
      <td>2.26</td>
      <td>Cảnh báo up âm báo IVR</td>
      <td></td>
      <td>Cảnh báo up âm báo IVR</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Phân phối đến ĐTV</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3.1</td>
      <td>Thiết lập hàng đợi và phân phối các cuộc gọi thoại</td>
      <td></td>
      <td>1. Các tham số trên cấu hình queue (anh Tungtt2 gửi lại) 2. VTNET xuất trên DB các tham số cấu hình queue</td>
    </tr>
    <tr>
      <td>3.2</td>
      <td>Phân phối theo số dịch vụ Khách hàng bấm gọi</td>
      <td></td>
      <td>Phân phối theo số dịch vụ Khách hàng bấm gọi</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3.2.1</td>
      <td>Ngoài chức năng phân phối như hiện tại bổ xung thêm: - KH gọi lại n lần sẽ vào queue riêng, Tham số trong cấu hình queue</td>
      <td>Ngoài chức năng phân phối như hiện tại bổ xung thêm: - KH gọi lại n lần sẽ vào queue riêng, Tham số trong cấu hình queue</td>
      <td>1. - Cấu hình số lần khách hàng gọi lại (n lần bao gồm cả cuộc gọi gặp TVV và cuộc gọi nhỡ - n cấu hình được) - Thời điểm bắt đầu đếm số lần gọi, đếm trong khoảng thời gian đã cấu hình, sang giờ đó của ngày hôm sau thì thực hiện reset lại số lần gọi 2. Cấu hình queue route tới khi khách hàng gọi n lần (gồm cả gặp và không gặp) 3. Nếu khách hàng gọi lại n lần (thỏa mãn điều kiện cấu hình), thì thực hiện phân bổ tới queue đã được cấu hình</td>
    </tr>
    <tr>
      <td>3.2.2</td>
      <td>Quản lý theo cả extent và AgentID</td>
      <td>Quản lý theo cả extent và AgentID - Khi tạo ID cho phép tạo ID theo các nhóm ( đặt tên theo đơn vị hay theo vị trí...) - Khi tạo user thì bắt buộc user phải được gắn với ID hoặc nhóm ID thì mới hoạt động được'</td>
      <td>D 1. Mong muốn: trên hệ thống, Agent A sử dụng đầu số A để thực hiện gọi ra, Agent B sử dụng đầu số B để gọi ra 2. Thêm hàng loạt theo file, thủ công (Thêm Device User gọi ra) 3. Gán device hàng loạt theo file, thủ công (Gán Device cho User gọi ra) 4. Đồng bộ dữ liệu device và user giữa các hệ thống IPCC giữa các miền (2 hệ thống khác nhau). Khi thao tác dữ liệu trên 1 hệ thống, hệ thống còn lại sẽ thực hiện đồng bộ về 5. Phân quyền gọi ra: - Phân trên device, cho phép chỉ được gọi ra đầu số nào - Phân quyền hàng loạt (phân theo list trên form và theo file) 6. Anh Tungtt2 tạo mã IBM và gửi lại theo phiếu Nâng cấp AgentID Callout (Phiếu Minhtd2 trình ký) anh sách tính năng</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3.3</td>
      <td>Phân phối theo số ĐT của KH (giống case khách hàng roaming)</td>
      <td></td>
      <td>1. Hiện tại: Phân phối theo đầu số khách hàng gọi lên 2. Mong muốn: Phân phối theo số thuê bao của khách hàng - Cấu hình các định dạng thuê bao, và các hành động xử lý khi đầu số thuê bao tương ứng gọi lên</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3.4</td>
      <td>Routeing dự phòng khi DB lỗi</td>
      <td></td>
      <td>T C Yêu cầu KH: - DB lỗi - Check DB mà chết thì định tuyến sang khu vực khác , thực hiện nhắn tin cảnh báo theo danh sách số thuê bao (cấu hình danh sách số thuê bao) - Xử lý trường hợp mất mạng, TVV không đăng nhập được vào hệ thống thì sẽ thực hiện chuyển sang khu vực khác (Site DB khác) - Xử lý trường hợp TVV đăng nhập vào hệ thống, nhưng mất mạng thực hiện chuyển sang khu vực khác - VD: + Đầu số 1800, do TVV ở Hà Nội và Hải Phòng, mất mạng ở HN -> Không định tuyến - Trường hợp chung queue + Đầu số 198 gán Hà Nội, 199 gán Hải Phòng, 198 mất mạng -> Queue 198 chuyển site khác (VTS đánh giá lại) - Khi 1 queue không có điện thoại viên trực trong giờ làm việc ính năng: - Service check trường hợp DB lỗi, mất mạng (trước và sau khi đăng nhập) - Luồng xử lý thực hiện chuyển sang khu vực khác (Site khác) - Cấu hình template tin nhắn (cấu hình chủ động) - Cấu hình danh sách nhận tin nhắn (cấu hình chủ động) - Tích hợp SMSgateway thực hiện gửi tin nhắn khi định tuyến chuyển sang khu vực khác hú ý: tất cả các tính năng giám sát đều có tính năng nhắn tin và gửi mail (khi thỏa mãn điều kiện, có thể cấu hình điều kiện)</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3.5</td>
      <td>Phân phối theo thâm niên và trình độ Agent (Skill), Gán độ ưu tiên trực nhiều queue</td>
      <td></td>
      <td>D Yêu cầu KH: - Cấu hình độ ưu tiên (phạm vi từ mức độ 1 - mức độ 10), khách hàng chủ động cấu hình trên queue (khi gán Agent) - Phân quyền: Tương tự cách phân quyền trên VSA anh sách tính năng: - Gán Agent vào queue (gán đơn lẻ và gán theo file) - Gán độ ưu tiên cho Agent trên queue (gán đơn lẻ và gán theo file) - Xử lý tìm kiếm và phân phối Agent có độ ưu tiên cao nhất khi có cuộc gọi đến</td>
    </tr>
    <tr>
      <td>3.6</td>
      <td>Phân phối theo đối tác Outsource (chi tiết xem PYC)</td>
      <td>Trước đã làm giải pháp nhưng có bất cập trưởng ca phải nhập danh sách liên tục mất thời gian</td>
      <td>KH cần đánh giá lại</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3.7</td>
      <td>Phân phối theo vùng miền - theo định dạng user (xem PYC)</td>
      <td>Với chức năng theo vùng miền , tìm hiểu thêm tổng đài Mobile phone: Bên Mobile Phone dùng giải pháp tràn tự động nên TLPV luôn ổn định ở mức 98% ngày thường. Mobile Phone cho tràn theo khu vực, và có Call Center ở 6 miền. Khu vực phía Bắc thì HN và HP backup cho nhau. Do vậy, khi lưu lượng cao thì : + Vẫn tăng cường nhân sự đi đáp ứng được, vì có thể huy động ở cả HN và HP để điều phối cho nhau. + Với giải pháp tràn tự động, thì cứ tràn đi tràn lại và do IVR (trả lời tự động trên menu) trả lời KH, không cho đến ĐTV nên về mặt chỉ số vẫn OK</td>
      <td>KH cần đánh giá lại</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3.8</td>
      <td>Xử lý ưu tiên khách hàng VIP cho phép cấu hình tham số “Ngưỡng Agent rảnh tràn queue”</td>
      <td></td>
      <td>D Yêu cầu KH: - Cho phép Cấu hình tràn queue (Cấu hình được queue Đích), đánh giá - Điều kiện tràn queue: check Ngưỡng nghẽn - Mong muốn xây dựng tính năng tràn từ queue VIP (Kim cường, Vàng, Bạc) sang queue Thường - Mong muốn xây dựng tính năng tràn từ queue Thường -> Queue VIP anh sách tính năng: - Cấu hình hạng khách hàng - Xử lý route cuộc gọi vào queue tương ứng hạng khách hàng - Cấu hình đội ưu tiên tràn queue (VD: Kim cương thì tràn queue trước, đến Vàng) - Xử lý tràn sang queue có độ ưu tiên cao nhất</td>
    </tr>
  </tbody>
</table>

# Public_442

<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3.11</td>
      <td>Nhận diện khách hang theo tỉnh</td>
      <td></td>
      <td>D Yêu cầu KH: - Kiểm tra KH ở tỉnh nào thì vào queue ACD nào - Cho phép phát nhạc chờ riêng theo các tỉnh - Phát nhạc chờ theo danh sách khách hàng được add lên hệ thống anh sách tính năng: 1.Cho phép nhận diện thông tin khách hàng theo tỉnh. + Dựa vào suxfix GMSC cấu hình để nhận diện thống tin khách hàng theo tỉnh. + Cho phép phát nhạc chờ riêng đối với mỗi khách hàng thuộc tỉnh tương ứng. 2. Xây dựng báo cáo ghi nhận thông tin cuộc gọi/ khách hàng theo tỉnh hệ thống ghi nhận được. + Xem/ tìm kiếm . + Xuất báo cáo.</td>
    </tr>
    <tr>
      <td>3.12</td>
      <td>Cấu hình định tuyến thông minh</td>
      <td></td>
      <td>Chức năng này cho phép cấu hình ngưỡng định tuyến thông minh theo từng queue + Cho phép cấu hình ngưỡng định tuyến + Ngưỡng tin nhắn cảnh báo. + Cấu hình định tuyến sang khu vực khác cùng đầu số. + Cấu hình định tuyến từ ACD sang IVR</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3.13</td>
      <td>Nhận diện cuộc gọi đc định tuyến thông minh trên giao diện Web</td>
      <td></td>
      <td>Chức năng này cho phép hiển thị thông tin khách hàng được định tuyến theo khu vực trên popup up màn hình điện thoại viên. + Hiển thị thông tin chi tiết khách hàng. + Hiển thị thông tin khách hàng được định tuyến từ vùng miền nào</td>
    </tr>
    <tr>
      <td>3.14</td>
      <td>Định tuyến cuộc gọi theo từng đầu số, từng khu vực.</td>
      <td></td>
      <td>Định tuyến cuộc gọi theo từng đầu số, từng khu vực. Tham khảo nội dung PYC mã 4078954</td>
    </tr>
    <tr>
      <td>3.15</td>
      <td>Người dùng chủ động cấu hình ngưỡng định tuyến.</td>
      <td></td>
      <td>Người dùng chủ động cấu hình ngưỡng định tuyến. Tham khảo nội dung PYC mã 4078954</td>
    </tr>
    <tr>
      <td>3.16</td>
      <td>Người dùng chủ động cấu hình các điều kiện định tuyến bao gồm khu vực, kênh, số lượng cuộc gọi định tuyến đi, số lượng cuộc gọi định tuyến tiếp nhận.</td>
      <td></td>
      <td>Người dùng chủ động cấu hình các điều kiện định tuyến bao gồm khu vực, kênh, số lượng cuộc gọi định tuyến đi, số lượng cuộc gọi định tuyến tiếp nhận. Tham khảo nội dung PYC mã 4078954</td>
    </tr>
    <tr>
      <td>3.17</td>
      <td>Người dùng chủ động trong công tác cảnh báo: Tự cập nhật danh sách nhắn tin theo các ngưỡng nghẽn khác nhau.</td>
      <td></td>
      <td>Người dùng chủ động trong công tác cảnh báo: Tự cập nhật danh sách nhắn tin theo các ngưỡng nghẽn khác nhau. Tham khảo nội dung PYC mã 4078954</td>
    </tr>
    <tr>
      <td>3.18</td>
      <td>Xử lý ưu tiên khách hàng VIP - Có chức năng xử lý VIP, SVIP, Tràn queue trên ACD</td>
      <td></td>
      <td>Yêu cầu KH: - Queue SVIP: Chọn hạng phục vụ - Hạng Kim cương và Vàng - Queue VIP: Chọn hạng Bạc, Thân thiết - Xử lý tràn queue (Tương tự tính năng 3.8)</td>
    </tr>
  </tbody>
</table>











<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3.21</td>
      <td>Xử lý Last agent nâng cao "Recently Agent": KH chọn gặp ĐTV gần nhất hoặc trước đó</td>
      <td></td>
      <td>Tương tự mô tả 3.19</td>
    </tr>
    <tr>
      <td>3.22</td>
      <td>Xử lý Last agent nâng cao "Recently Agent": Phát ấm HD khách hàng chọn gặp ĐTV trước đó hay không</td>
      <td></td>
      <td>Tương tự mô tả 3.19</td>
    </tr>
    <tr>
      <td>3.23</td>
      <td>Cấu hình thời gian áp dụng Last/recently agent</td>
      <td></td>
      <td>Tương tự mô tả 3.19</td>
    </tr>
    <tr>
      <td>3.24</td>
      <td>Cấu hình chọn chuyển BOT hay không</td>
      <td></td>
      <td>1. Tìm kiếm cấu hình chuyển bot 2. Quản lý cấu hình chuyển bot: Thêm danh sách, sửa danh sách, xóa danh sách, xóa hàng loạt 3. Cấu hình chọn điều hướng BOT/ ACD 4. Xuất file excel báo cáo danh sách cấu hình chuyển bot</td>
    </tr>
    <tr>
      <td>3.25</td>
      <td>Cho phép chọn BOT chuyển từ IPCC đến BOT</td>
      <td></td>
      <td>Yêu cầu của KH: - Với mỗi queue cho phép chọn Bot để gặp KH - Cho phép cấu hình queue ACD chọn BOT chuyển đến - Bổ sung thông tin BOT trong báo cáo trạng thái kết thúc cuộc gọi Danh sách tính năng: - Cấu hình chọn bot trên queue - Xử lý KH gặp Bot đã được cấu hình trên queue - Tích hợp các Bot vào hệ thống</td>
    </tr>
    <tr>
      <td>3.26</td>
      <td>Chuyển BOT theo tập danh sách</td>
      <td></td>
      <td>Chuyển BOT theo tập danh sách</td>
    </tr>
    <tr>
      <td>3.27</td>
      <td>Nhận cuộc gọi từ BOT chuyển đến IPCC</td>
      <td>Hỗ trợ cả luồng call in ( KH -> IPCC -> BOT -> ĐTV) và luồng call BOT out từ HT khác chuyển đến ĐTV</td>
      <td>Nhận cuộc gọi từ BOT chuyển đến IPCC</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3.28</td>
      <td>Xử lý blacklist - Có chức năng xử lý blacklist chuyển IVR</td>
      <td></td>
      <td>1 .Thêm mới màn hình blaclist danh sách khách hàng theo từng kênh + Cho phép cấu hình thêm mới danh sách blacklist theo kênh, ngày giờ chặn, mở chặn blaclist + Loại chặn: có kỳ hạn, không kỳ hạn, vĩnh viên theo từng danh sách được cấu hình. + Sửa/ xóa thông tin khách hàng. + Xuất báo cáo. 2. Cấu hình Blacklist chuyển IVR 3. Thêm mới báo cáo lịch sử chặn thuê bao: + Xem/ tìm kiếm. + Xuất báo cáo. 4. Thêm mới báo cáo thống kê khách hàng bị chặn vẫn gọi lên hệ thống. + Xem/ tìm kiếm. + Xuất báo cáo</td>
    </tr>
    <tr>
      <td>3.29</td>
      <td>Xử lý blacklist - Có chức năng xử lý blacklist, chặn gọi vào có kì hạn, không kì hạn, chặn vĩnh viễn, áp riêng cho từng kênh</td>
      <td></td>
      <td>Tương tự tính năng Blacklist đã mô tả</td>
    </tr>
    <tr>
      <td>3.30</td>
      <td>Xử lý blacklist - Nâng cấp tính năng kiểm tra danh sách thuê bao có nằm trong danh sách từ chối nhận tin nhắn 197, 199 trước khi thực hiện survey khách hàng qua các hình thức hiện có trên tổng đài trên HT IPCC</td>
      <td></td>
      <td>Xử lý blacklist - Nâng cấp tính năng kiểm tra danh sách thuê bao có nằm trong danh sách từ chối nhận tin nhắn 197, 199 trước khi thực hiện survey khách hàng qua các hình thức hiện có trên tổng đài trên HT IPCC Tham khảo PYC mã IBM 4079613</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3.31</td>
      <td>ACD theo danh sách nhóm khách hàng - Cho phép nhóm nào đc gọi vào ht</td>
      <td></td>
      <td>- Cấu hình danh sách số điện được được phép gọi theo queue - Add thủ công hoặc import danh sách số thuê bao - Cho phép on/off chức năng</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Tiền xử lý khi gặp ĐTV</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>4.1</td>
      <td>Nhạc chờ mặc định khi tạo queue</td>
      <td></td>
      <td>Nhạc chờ cho từng queue: Chức năng này cho phép khách hàng gọi lên nghe nhạc chờ riêng được cậu hình trong queue: 1. Tại màn hình cấu hình queue: + Thêm mới param_id: Nhạc chờ trong queue: Cho phép/ thêm sửa xóa + Khách hàng gọi lên hệ thống với đầu số queue được cấu hình sẽ nghe nhạc chờ tương ứng được cấu hình trong queue</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>4.2</td>
      <td>Thời gian bắt buộc nghe Nhạc chờ</td>
      <td></td>
      <td>Thời gian nghe nhạc chờ: Đây là khoảng cấu hình phát nhạc chờ trong queue khi khách hàng gọi lên hệ thống mà TVV chưa nhấc máy: + Khi cuộc gọi lên hệ thống check file thông tin file nhạc cấu hình, thời gian phát nhạc để xử lý. + Nếu khách hàng gọi lên hệ thống, hết thời gian phát nhạc chờ trong queue mà TVV không nhấc máy thì sẽ kết thúc cuộc gọi. + Báo cáo Điều kiện đảm bảo: + Thêm mới một tham số: Cấu hình thời gian chờ trong queue. - Luồng xử lý: + Tách thành 2 luồng nghe: nghe nhạc truyền thông + nghe nhạc chờ + Nghe hết 1 file nhạc truyền thông, sau đó vào queue + Cấu hình thời gian chờ trong queue + Cấu hình thời gian nghe file truyền thông + Cấu hình file truyền thông</td>
    </tr>
    <tr>
      <td>4.3</td>
      <td>Nhạc chờ cuộc gọi ưu tiên riêng</td>
      <td></td>
      <td>Yêu cầu KH: - Với các khách hàng ưu tiên, sẽ phát nhạc chờ riêng cho khách hàng nghe. - Nếu không để file nhạc ưu tiên thì sẽ xử lý ưu tiên như bình thường - Cho phép chọn file media từ list trong màn hình cấu hình queue Danh sách tính năng: - Cấu hình nhạc chờ ưu tiên</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>4.4</td>
      <td>Phát nhiều file nhạc chờ khác nhau</td>
      <td></td>
      <td>Yêu cầu KH: - Các chế độ play tuần tự, random - Cấu hình được nhiều file nhạc chờ trong queue</td>
    </tr>
    <tr>
      <td>4.5</td>
      <td>Cấu hình luật phát : lặp lại, random, xoay vòng...</td>
      <td></td>
      <td>Yêu cầu KH: - Cấu hình thuật toán phát file media - Cấu hình chọn file media (trường hợp phát lặp lại 1 file) - Cấu hình chọn nhiều file media (trường hợp phát xoay vòng, random)</td>
    </tr>
    <tr>
      <td>4.6</td>
      <td>Nhạc chờ riêng cho từng queue</td>
      <td></td>
      <td>Cho phép cấu hình nhạc chờ riêng cho từng kênh</td>
    </tr>
    <tr>
      <td>4.7</td>
      <td>Nhạc chờ theo mã tỉnh</td>
      <td></td>
      <td>Nhạc chờ theo mã tỉnh Đã mô tả ở tính năng 3.11</td>
    </tr>
    <tr>
      <td>4.8</td>
      <td>Nghe truyền thông cuộc gọi</td>
      <td></td>
      <td>Yêu cầu KH - Bắt buộc nghe âm báo (tương tự 4.2)</td>
    </tr>
    <tr>
      <td>4.9</td>
      <td>Popup theo danh sách khách hang</td>
      <td></td>
      <td>Popup theo danh sách khách hang Tương tự 4.16 -> 4.22 đã được mô tả chi tiết</td>
    </tr>
    <tr>
      <td>4.10</td>
      <td>Đáp ứng như ht hiện tại với đầu sô 1789, line dân tộc</td>
      <td></td>
      <td>Đáp ứng như hệ thống hiện tại với đầu sô 1789 (nhận biết nhóm khách hàng dựa trên các mã kênh được code trên hệ thống), line dân tộc (nhận diện theo gói cước)</td>
    </tr>
    <tr>
      <td>4.11</td>
      <td>Nghe nhạc chờ theo danh sách</td>
      <td></td>
      <td>Cấu hình danh sách số thuê bao Cấu hình được file nhạc chờ cho danh sách Cấu hình được nhiều danh sách trên queue Mỗi danh sách là 1 file nhạc chờ</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>4.12</td>
      <td>Chức năng IVR ảo</td>
      <td></td>
      <td>Cấu hình phát âm báo Tách nhánh gặp điện thoại viên Không bấm phím -> Có thể chuyển được đến queue ACD cấu hình Cấu hình được thời gian bắt buộc nghe âm báo Chỉ tính phí khi gặp điện thoại viên</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>4.13</td>
      <td>Xử lý nghẽn thông minh - Nhắn tin điều hướng chuyển kênh tương tác khác</td>
      <td></td>
      <td>= Yêu cầu: - Hệ thống căn cứ vào tần suất kh gọi lên tổng đài/ ngày - Cấu hình (số lần) - Căn cứ vào thời gian chờ (tối thiểu bao nhiêu s) - Cấu hình Khung giờ nhắn tin - Cấu hình khung giờ tính toán tham số - Hệ thống thực hiện nhắn tin cho người dùng khi đạt điều kiện cấu hình - Cấu hình nội dung tin nhắn - KH có xu hướng gọi lại nhiều lần vào hệ thống khi ko gọi được TVV -> mục tiêu để giảm tải cho hệ thống - Xử lý trên luồng cuộc gọi (khi đang gọi thì thực hiện kiểm tra thuê bao xem có thỏa mãn điều kiện không) => Định hướng cuộc gọi khi nghẽn - Check theo tỉ lệ nghẽn: Tổng số cuộc gọi đang chờ / tổng số điện thoại viên rảnh (cấu hình số tỉ lệ nghẽn trong khoảng thời gian được cấu hình, cho phép cấu hình nhiều khung giờ) ngưỡng nghẽn được tính toán và cập nhật liên tục -> Gửi hết các khách hàng đang chờ và thỏa mãn điều kiện - Check KH gọi lên hệ thống nhiều lần và gửi đơn lẻ + Check số lần KH gọi lên bị lỡ và nguy cơ lỡ (đang chờ >= n s - n cấu hình được) trong khoảng thời gian lùi so với thời điểm quét (VD: trước thời điểm quét bao nhiêu lâu) + Check khung giờ gửi tin nhắn - nhiều khung giờ (cấu hình được) + Không check KH đã gặp TVV hay chưa trước khi nhắn tin - Với trường hợp định tuyến thông minh thì không nhắn tin - Cấu hình thời gian tối thiểu từ thời điểm khách hàng gọi vào để nhắn tin - Tính ngưỡng nghẽn theo từng queue</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>4.14</td>
      <td>Pop up sang BCCS (và các UD khác)</td>
      <td>Popup dữ liệu từ CCAI sang: - Nếu queue có cấu hình chọn hiển thị lịch sử phân tích KH từ nguồn dữ liệu là ht CCAI thì : + Chức năng hiển thị danh sách trang web khách hàng tham quan + Nguồn khách hàng chính là lịch sử truy cập website của khách hàng trước khi tìm đến sự hỗ trợ của ĐTV. ĐTV sẽ biết được khách hàng đến từ trang nào, họ dừng lại ở chủ đề nào lâu nhất,… Từ đó cơ bản nắm bắt được những _x005finsight mà khách hàng quan tâm ở doanh nghiệp. Agent lúc này có thể tư vấn đúng trọng tâm nhu cầu của khách hàng, khiến cuộc trò chuyện trực tuyến trở nên thoải mái và gần gũi hơn.</td>
      <td>1. Yêu cầu khách hàng - Ví dụ: Popup dữ liệu từ CCAI sang: - Nếu queue có cấu hình chọn hiển thị lịch sử phân tích KH từ nguồn dữ liệu là ht CCAI thì : + Chức năng hiển thị danh sách trang web khách hàng tham quan + Nguồn khách hàng chính là lịch sử truy cập website của khách hàng trước khi tìm đến sự hỗ trợ của ĐTV. ĐTV sẽ biết được khách hàng đến từ trang nào, họ dừng lại ở chủ đề nào lâu nhất,… Từ đó cơ bản nắm bắt được những insight mà khách hàng quan tâm ở doanh nghiệp. Agent lúc này có thể tư vấn đúng trọng tâm nhu cầu của khách hàng, khiến cuộc trò chuyện trực tuyến trở nên thoải mái và gần gũi hơn. - Chuyển thông tin sang ứng dụng khác: SĐT, Mã hoá đơn, mã lịch sử chuyển tiền,vv. Chọn theo từng queue, từng kênh và thông tin theo queue</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>4.14.1</td>
      <td>Popup để MAP cuộc gọi với ID nhập trên BCCS (hoặc UD khác của doanh nghiệp)</td>
      <td>- Cho phép tạo ngay ID tương tác và loại kênh và hiển thị trên Popup cho ĐTV, cho phép copy ID - Tự động chuyển ID tương tác này vào bộ nhớ giao diện để các UD khác có thể lấy thông tin ID này - Khi ĐTV vào CRM riêng của doanh nghiệp (vd BCCS) để tạo TICKET mới thì trước khi bấn nút SAVE thì ht CRM sẽ tự động lấy giá trị ID tương tác của ĐTV trên trình duyệt, view lên cho ĐTV kiểm tra, nếu ĐTV so sánh ID/Kênh ht CRM lấy về đúng với ID?kênh do IPCC tạo ra thì ĐTV sẽ click để LƯU ID và kênh vào TICKET trên CRM (nếu sai cho phép ĐTV copy từ IPCC để paste sang BCCS trước khi lưu) => Mục đích để lưu được thông tin IPCC trên CRM từ đó</td>
      <td>1. Yêu cầu nghiệp vụ '- Cho phép tạo ngay ID tương tác và loại kênh và hiển thị trên Popup cho ĐTV, cho phép copy ID - Tự động chuyển ID tương tác này vào bộ nhớ giao diện để các UD khác có thể lấy thông tin ID này - Khi ĐTV vào CRM riêng của doanh nghiệp (vd BCCS) để tạo TICKET mới thì trước khi bấn nút SAVE thì ht CRM sẽ tự động lấy giá trị ID tương tác của ĐTV trên trình duyệt, view lên cho ĐTV kiểm tra, nếu ĐTV so sánh ID/Kênh ht CRM lấy về đúng với ID?kênh do IPCC tạo ra thì ĐTV sẽ click để LƯU ID và kênh vào TICKET trên CRM (nếu sai cho phép ĐTV copy từ IPCC để paste sang BCCS trước khi lưu) => Mục đích để lưu được thông tin IPCC trên CRM từ đó MAP ping việc tiếp nhận và xử lý của ĐTV. Tương tự với các cuộc gọi ra cho KH, cũng như các kênh tương tác khác như mail, chat... Lưu ý: - Vẫn tạo TICKET riêng trên IPCC , trường hợp doanh nghiệp không có CRM vẫn có thê sd TICKET của IPCC</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>MAP ping việc tiếp nhận và xử lý của ĐTV. Tương tự với các cuộc gọi ra cho KH, cũng như các kênh tương tác khác như mail, chat... Lưu ý: - Vẫn tạo TICKET riêng trên IPCC , trường hợp doanh nghiệp không có CRM vẫn có thê sd TICKET của IPCC</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>4.14.2</td>
      <td>Cấu hình động để IPCC chuyển hay không chuyển các giá trị này lịn hoạt</td>
      <td>- Cấu hình chuyển hay không chuyển các thông tin này ra catche theo từng kênh - Cho phép cấu hình ngoài việc lưu ra biến trên cache thì có thể khai đường link để gửi thông tin sang các ht CRM khác như kiểu gửi SĐT sang BCCS hiện tại để hỗ trợ các UD khác link hoạt, cho phép khai theo từng kênh, mỗi kênh có thể cấu hình >2 link (ngoài số ĐT có thể chuyển cả các dữ liệu khác đã có trên CRM của IPCC (xem mục 4.17.1)</td>
      <td>1. Yêu cầu nghiệp vụ '- Cấu hình chuyển hay không chuyển các thông tin này ra catche theo từng kênh - Cho phép cấu hình ngoài việc lưu ra biến trên cache thì có thể khai đường link để gửi thông tin sang các ht CRM khác như kiểu gửi SĐT sang BCCS hiện tại để hỗ trợ các UD khác link hoạt, cho phép khai theo từng kênh, mỗi kênh có thể cấu hình >2 link (ngoài số ĐT có thể chuyển cả các dữ liệu khác đã có trên CRM của IPCC (xem mục 4.17.1)</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>4.15</td>
      <td>Pop up thông tin KH, nhóm KH (nâng cao)</td>
      <td>Chức năng popup nhóm khách hàng: 1. Cho phép chọn một hoặc nhiều nguồn dữ liệu để POPUP 2. Với mỗi nguồn cho phép : - Cho phép hiện thị tối thiểu 20 trường ( 20 hay hơn nên tham khảo ht Customer 360 hoặc ht khác) - Cho phép cấu hình hiển thị theo Queue - Cho phép cấu hình ĐTV được/không được COPY dữ liệu từng trường trên cửa sổ POP up - Cho phép cấu hình FONT chữ, MÀU sắc từng trường - Cho phép cấu hình chuyển thông tin trong trường nào đến 1 link/ hoặc nhiều link nào đó theo từng Queue để POPUP thông tin KH trên UD link đến - Cho phép lựa chọn thứ tự ưu tiên hiển thị các trường, số</td>
      <td>1. Yêu cầu nghiệp vụ "Chức năng popup nhóm khách hàng: 1. Cho phép chọn một hoặc nhiều nguồn dữ liệu để POPUP 2. Với mỗi nguồn cho phép : - Cho phép hiện thị tối thiểu 20 trường ( 20 hay hơn nên tham khảo ht Customer 360 hoặc ht khác) - Cho phép cấu hình hiển thị theo Queue - Cho phép cấu hình ĐTV được/không được COPY dữ liệu từng trường trên cửa sổ POP up - Cho phép cấu hình FONT chữ, MÀU sắc từng trường - Cho phép cấu hình chuyển thông tin trong trường nào đến 1 link/ hoặc nhiều link nào đó theo từng Queue để POPUP thông tin KH trên UD link đến - Cho phép lựa chọn thứ tự ưu tiên hiển thị các trường, số trường cần hiển thị tùy thời điểm và tùy queue - Năng lực add khoảng 100 tr thuê bao - Cho phép ĐTV thực hiện gửi yêu cầu cập nhật thông tin cho KH nếu phát hiện thông tin Popup bị sai, các yc này sẽ được gửi đến cho giám sát viên, gs viên sẽ là người cập nhật, ht ghi log lại các yc, ng yc, tình trạng đã đc cập nhật, chưa cập nhật, thời điểm cập nhật (phân quyền gs queue nào chỉ nhìn đc yc & sửa queue đó). - Có thể cấu hình ON/OFF các trường nào ĐTV có thể tự cập nhật trong khi KH gọi lên - Mỗi trường đều có chức năng cấu hình : hiện rõ hay hiện 1 phần thông tin để bảo đảm BMATTT - Phần quyền cho user nào có thể cập nhật nhóm KH nào...Tham khảo giao diện quản lý của Strxxx (với các trường cấu hình hiển thị cho queue, nếu KH nào mà thiếu thông tin trường nào thì sẽ hiển thị chữ mờ để ĐTV biết)"</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>trường cần hiển thị tùy thời điểm và tùy queue - Năng lực add khoảng 100 tr thuê bao - Cho phép ĐTV thực hiện gửi yêu cầu cập nhật thông tin cho KH nếu phát hiện thông tin Popup bị sai, các yc này sẽ được gửi đến cho giám sát viên, gs viên sẽ là người cập nhật, ht ghi log lại các yc, ng yc, tình trạng đã đc cập nhật, chưa cập nhật, thời điểm cập nhật (phân quyền gs queue nào chỉ nhìn đc yc & sửa queue đó). - Có thể cấu hình ON/OFF các trường nào ĐTV có thể tự cập nhật trong khi KH gọi lên - Mỗi trường đều có chức năng cấu hình : hiện rõ hay hiện 1 phần thông tin để bảo đảm BMATTT - Phần quyền cho user nào có thể cập</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>nhật nhóm KH nào...Tham khảo giao diện quản lý của Strxxx (với các trường cấu hình hiển thị cho queue, nếu KH nào mà thiếu thông tin trường nào thì sẽ hiển thị chữ mờ để ĐTV biết)</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>4.16</td>
      <td>Popup lịch sử thống kê (thống kê tự động trên BCCS)</td>
      <td></td>
      <td>Tương tự hệ thống cũ. 1. Yêu cầu nghiệp vụ: Truyền thông tin sang ứng dụng khác</td>
    </tr>
    <tr>
      <td>4.17</td>
      <td>View được Lịch sử tương tác qua các kênh</td>
      <td>Có 2 chức năng : - Hiển thị lịch sử tương tác: + Hiển thị lịch sử tương tác trong 1 khoảng thời gian gần nhất (cấu hình được khoảng thời gian này theo từng kênh) + Lịch sử tương tác gồm các kênh và các hướng inbound/outbound - Hiện thị thói quen tương tác của KH theo kênh nào : + Sắp sếp kênh tương tác KH thực hiện nhiều nhất lên đầu + số lần tương tác + Làm nổi bật kênh KH hay tương tác nhất với tổng đài + Số lượng tương tác theo các kênh của KH được cấu hình khoảng thời gian đếm theo từng queue + Hiển thị tên Agent/queue/kênh</td>
      <td>1. Yêu cầu nghiệp vụ Có 2 chức năng : - Hiển thị lịch sử tương tác: + Hiển thị lịch sử tương tác trong 1 khoảng thời gian gần nhất (cấu hình được khoảng thời gian này theo từng kênh) + Lịch sử tương tác gồm các kênh và các hướng inbound/outbound - Hiện thị thói quen tương tác của KH theo kênh nào : + Sắp sếp kênh tương tác KH thực hiện nhiều nhất lên đầu + số lần tương tác + Làm nổi bật kênh KH hay tương tác nhất với tổng đài + Số lượng tương tác theo các kênh của KH được cấu hình khoảng thời gian đếm theo từng queue + Hiển thị tên Agent/queue/kênh tương tác trước đó KH gọi lên (khi KH liên hệ lên tổng đài ở tất cả các kênh)</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>tương tác trước đó KH gọi lên (khi KH liên hệ lên tổng đài ở tất cả các kênh)</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>4.18</td>
      <td>Popup thời gian KH phải chờ đợi và cảnh báo cho ĐTV (chức năng đối thủ có)</td>
      <td>Popup số giây cụ thể KH đã phải chờ từ khi vào queue và cảnh báo cho ĐTV Cấu hình số giây trong khoảng nào sẽ hiển thị thêm cảnh bảo kh chờ "LÂU", "RẤT LÂU" và hiển thị màu chữ khác, nổi bật</td>
      <td>1. Yêu cầu nghiệp vụ - Popup số giây cụ thể KH đã phải chờ từ khi vào queue và cảnh báo cho ĐTV. - Cấu hình số giây trong khoảng nào sẽ hiển thị thêm cảnh bảo kh chờ "LÂU", "RẤT LÂU" và hiển thị màu chữ khác, nổi bật - Cấu hình màu sắc theo khoảng thời gian chờ đợi, theo queue</td>
    </tr>
    <tr>
      <td>4.19</td>
      <td>Pop up nhận diện tích cách, cảm xúc khách hàng</td>
      <td>Chức năng popup tính cách của KH (nếu là KH đã liên hệ tổng đài): - Lấy thông tin tính cách KH từ hệ thống nhận diện cảm xúc KH với KH vừa gọi lại trong vòng x giờ (cấu hình được, vd 48h) - Nếu cảm xúc KH là cáu giận, Không hài lòng cần có cảnh báo (cảnh báo ntn?) cho ĐTV biết - Cấu hình được để có thể kết nối đến các hệ thống nhận diện tích cách KH khác nhau của các nhà cung cấp dv khác nhau (đi bán cho các</td>
      <td>1. Yêu cầu nghiệp vụ Chức năng popup tính cách của KH theo queue (nếu là KH đã liên hệ tổng đài): - Lấy thông tin tính cách KH từ hệ thống nhận diện cảm xúc KH với KH vừa gọi lại trong vòng x giờ (cấu hình được, vd 48h) - Nếu cảm xúc KH là cáu giận, Không hài lòng cần có cảnh báo (cảnh báo ntn?) cho ĐTV biết - Cấu hình được để có thể kết nối đến các hệ thống nhận diện tích cách KH khác nhau của các nhà cung cấp dv khác nhau (đi bán cho các KH khác nhau có ht nhận diện khác nhau</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>KH khác nhau có ht nhận diện khác nhau)</td>
      <td></td>
    </tr>
    <tr>
      <td>4.20</td>
      <td>Thay đổi màu sắc nền giao diện cửa sổ POP UP</td>
      <td>Hỗ trợ tự động hiển thị 3 màu sắc : - Nền popup màu XANH với các cuộc gọi thông thường - Nền popup màu VÀNG với các cuộc KH thỏa mãn 1 trong các đk sau : + KH phải chờ lâu + Khách hàng gọi lại , tương tác lại trên các kênh + Khách hàng có cảm xúc cáu gắt trong các kênh tương tác khác - Nền popup màu ĐỎ</td>
      <td>Hỗ trợ tự động hiển thị 3 màu sắc : - Nền popup màu XANH với các cuộc gọi thông thường - Nền popup màu VÀNG với các cuộc KH thỏa mãn 1 trong các đk sau : + KH phải chờ lâu + Khách hàng gọi lại , tương tác lại trên các kênh + Khách hàng có cảm xúc cáu gắt trong các kênh tương tác khác - Nền popup màu ĐỎ với các KH thỏa mãn 2 trong 3 điều kiện nêu trên - Nếu khách hàng là VIP của 1 trong 2 công ty thì coi là VIP chung của queue đó</td>
    </tr>
  </tbody>
</table>

# Public_442

<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5.10</td>
      <td>Tranfer từ kênh voice sang kênh video Facebook messenger/Zalo/mocha: Khi khách hàng đang trên kênh voice, KH muốn chuyển qua kênh video call (vd để ĐTV kiểm tra modem) thì ĐTV có thể click vào chức năng video call cho khách hàng trên Agent desktop, hệ thống tạo cuộc gọi video call đến KH (có thể qua Facebook messenger, zalo, mocha)</td>
      <td></td>
      <td>1. Yêu cầu nghiệp vụ - Bổ sung chuyến sang kênh Video tiktok (Đánh giá lại) - Tạo menu chuyển từ kênh voice sang các kênh video khác (Fb/Zalo/Mocha) 2. Ghi chú - Không chuyển được sang Facebook/Messenger/Tiktok</td>
    </tr>
    <tr>
      <td>5.11</td>
      <td>Tranfer theo lịch, ngày, giờ, thứ</td>
      <td></td>
      <td>1. Yêu cầu nghiệp vụ - Cho phép đặt nhiều khung giờ - Tương tự hệ thống cũ</td>
    </tr>
    <tr>
      <td>5.12</td>
      <td>Nhạc tranfer linh hoạt : khi cấu hình tranfer tự động thì thuê bao ưu tiên kênh nguồn cũng được phát ưu tiên ở kênh tranfer</td>
      <td></td>
      <td>1. Yêu cầu nghiệp vụ - Tương tự phát nhạc nhờ thuê bao ưu tiên</td>
    </tr>
    <tr>
      <td>5.13</td>
      <td>Nhạc tranfer tự động ACD - ACD : cho phép cấu hình phát âm nhạc chờ của queue nguồn, quueue đích hoặc phát âm riêng</td>
      <td></td>
      <td>1. Yêu cầu nghiệp vụ - Khi cấu hình transfer tự động. Cho phép cấu hình phát nhạc chờ theo queue nguồn, queue đích, file riêng (1 file)</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5.14</td>
      <td>Nghe nhạc tranfer chuyên gia : Cấu hình file riêng cho từng nhóm chuyên gia</td>
      <td></td>
      <td>1. Yêu cầu nghiệp vụ - Cấu hình file nhạc chờ (1 file riêng) cho từng nhóm (bằng tay và tự động). Khi một chuyên gia ở trong nhiều nhóm => nhạc phát cho chuyên gia khi nhận transfer sẽ theo nhóm đã chọn (yêu cầu chọn nhóm trước) - Hiện tại transfer sang chuyên gia chỉ nghe đc 1 file (không sửa được)</td>
    </tr>
    <tr>
      <td>5.15</td>
      <td>Nhạc HOLD</td>
      <td></td>
      <td>Cho phép Admin cấu hình 1 file nhạc sẽ phát cho khách hàng nghe khi điện thoại viên thực hiện hold cuộc gọi.</td>
    </tr>
    <tr>
      <td>5.16</td>
      <td>Nghe nhạc HOLD linh hoạt - Chọn chế độ xoay vòng, lặp lại..</td>
      <td></td>
      <td>1. Yêu cầu nghiệp vụ: - Phát được nhiều file nhạc chờ: Xoay vòng + lặp lại</td>
    </tr>
    <tr>
      <td>5.17</td>
      <td>Nghe nhạc HOLD bắt buộc</td>
      <td></td>
      <td>Tương tự hệ thống cũ 1. Yêu cầu nghiệp vụ: - Cấu hình thời gian bắt buộc nghe nhạc chờ => Không cho phép unhold (Phím unhold mờ đi + hiện thời gian đếm ngược)</td>
    </tr>
    <tr>
      <td>5.18</td>
      <td>Cấu hình nhiều file nhạc HOLD</td>
      <td></td>
      <td>Tương tự hệ thống cũ 1. Yêu cầu nghiệp vụ: Cấu hình nhiều file nhạc HOLD</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5.19</td>
      <td>Kết nối đến hệ thống nhận diện VOICE BIOMETRIC</td>
      <td>Luồng kiểm tra nhận diện trong lúc đàm thoại: - ĐTV click button xác minh KH trên giao diện nghiệp vụ BCCS -> BCCS check ht eKYC xem SĐT này đăng kí eKYC chưa-> Nếu có thì BCCS thực hiện gửi yc sang IPCC để IPCC lấy 1 phần ghi âm cuộc gọi hiện tại gửi sang ht eKYC -> eKYC so sánh dữ liệu trả về kết quả xác minh trên giao diện BCCS cho ĐTV -> ĐTV dựa vào KQ để thực hiện nghiệp vụ cho KH mà KH không bị hỏi han nhiều. (luồng trên IVR thì đã mô tả trên mục 1.9)</td>
      <td>1. Yêu cầu nghiệp vụ Luồng kiểm tra nhận diện trong lúc đàm thoại: - ĐTV click button xác minh KH trên giao diện nghiệp vụ BCCS -> BCCS check ht eKYC xem SĐT này đăng kí eKYC chưa-> Nếu có thì BCCS thực hiện gửi yc sang IPCC để IPCC lấy 1 phần ghi âm cuộc gọi hiện tại gửi sang ht eKYC -> eKYC so sánh dữ liệu trả về kết quả xác minh trên giao diện BCCS cho ĐTV -> ĐTV dựa vào KQ để thực hiện nghiệp vụ cho KH mà KH không bị hỏi han nhiều. (luồng trên IVR thì đã mô tả trên mục 1.9)</td>
    </tr>
    <tr>
      <td>5.20</td>
      <td>Trả lời cuộc gọi</td>
      <td></td>
      <td>Tương tự hệ thống cũ Bổ xung thêm : - Đáp ứng mô hinh 1 ĐTV trả lời queue cho 2 cty - 1 Công ty chủ dịch vụ thuê 2 đơn vị Out tiếp nhận phản ánh của khách hàng => VTS đánh giá (tương tự như các kênh khác)</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5.21</td>
      <td>Hold/Unhold cuộc gọi,</td>
      <td></td>
      <td>Cho phép điện thoại viên thực hiện HOLD/ UNHOLD cuộc gọi mà agent đang trả lời khách hàng.</td>
    </tr>
    <tr>
      <td>5.22</td>
      <td>Bắt buộc phát hết nhạc HOLD mới đc Unhold</td>
      <td></td>
      <td>Trùng 5.17</td>
    </tr>
    <tr>
      <td>5.23</td>
      <td>Chuyển cuộc gọi</td>
      <td></td>
      <td>Sau khi tiếp nhận cuộc gọi vào của khách hàng, cho phép điện thoại viên chủ động chuyển cuộc gọi đến các đích khác nhau: ACD (queue khác), IVR nào đó hoặc chuyên gia.</td>
    </tr>
    <tr>
      <td>5.24</td>
      <td>Kết thúc cuộc gọi</td>
      <td></td>
      <td>Cho phép điện thoại viên chủ động kết thúc cuộc gọi.</td>
    </tr>
    <tr>
      <td>5.25</td>
      <td>Mute/Umute cuộc gọi</td>
      <td></td>
      <td>Cho phép điện thoại viên thực hiện MUTE/UNMUTE cuộc gọi mà agent đang trả lời khách hàng.</td>
    </tr>
    <tr>
      <td>5.26</td>
      <td>Chuyển trạng thái Agent</td>
      <td></td>
      <td>Cho phép điện thoại viên chủ động thay đổi trạng thái tiếp nhận cuộc gọi : chọn 1 trong các chế độ sau: - Available - Not Available - Lunch - Meeting - Training - Break. Hệ thống tự động chuyển trạng thái của điện thoại viên thành: - Connecting: khi có cuộc gọi ring đến điện thoại viên - Connected: khi điện thoại viên trả lời cuộc gọi - Wrapup: khi điện thoại viên ở trạng thái after call work</td>
    </tr>
    <tr>
      <td>5.27</td>
      <td>Hiển thị thông tin cá nhân</td>
      <td></td>
      <td>1. Yêu cầu nghiệp vụ - Hiển thị thông tin Agent - Tương tự hệ thống cũ</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5.28</td>
      <td>Hiển thị cảnh báo về thời gian đàm thoại</td>
      <td></td>
      <td>Tương tự hệ thống cũ 1.Yêu cầu nghiệp vụ - Cho phép cấu hình được thời gian cảnh báo - Trong quá trình điện thoại viên trả lời khách hàng, khi thời gian trả lời vượt quá mức cấu hình thời gian trả lời cho phép, hệ thống hiển thị cảnh báo trên màn hình của điện thoại viên</td>
    </tr>
    <tr>
      <td>5.29</td>
      <td>Nghe cuộc gọi online</td>
      <td></td>
      <td>Khi điện thoại viên đang trả lời cuộc gọi inbound của khách hàng, Giám sát viên hoặc Admin của hệ thống có thể thực hiện nghe online cuộc gọi giữa điện thoại viên và khách hàng.</td>
    </tr>
    <tr>
      <td>5.30</td>
      <td>Tham gia vào cuộc gọi</td>
      <td></td>
      <td>Khi điện thoại viên đang trả lời cuộc gọi inbound của khách hàng, Giám sát viên hoặc Admin của hệ thống có thể thực hiện tham gia vào cuộc gọi giữa điện thoại viên và khách hàng -- >cuộc gọi trở thành cuộc gọi 3 bên.</td>
    </tr>
    <tr>
      <td>5.31</td>
      <td>Cướp cuộc gọi</td>
      <td></td>
      <td>Khi điện thoại viên đang trả lời cuộc gọi inbound của khách hàng, Giám sát viên hoặc Admin của hệ thống có thể thực hiện cướp cuộc gọi của điện thoại viên với khách hàng, luồng cuộc gọi của agent bị ngắt</td>
    </tr>
    <tr>
      <td>5.32</td>
      <td>Nghe lén</td>
      <td></td>
      <td>Khi điện thoại viên đang trả lời cuộc gọi inbound của khách hàng, Giám sát viên hoặc Admin của hệ thống có thể thực hiện nghe lén cuộc gọi giữa điện thoại viên và khách hàng. Điện thoại viên, Khách hàng không biết đến hàng động này.</td>
    </tr>
    <tr>
      <td>5.33</td>
      <td>Chuyển trạng thái của Agent từ xa</td>
      <td></td>
      <td>Giám sát viên hoặc Admin của hệ thống có thể thay đổi trạng thái tiếp nhận cuộc gọi của các điện thoại viên.</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5.34</td>
      <td>Hiển thị lịch sử cuộc gọi</td>
      <td></td>
      <td>Hiển thị thông tin lịch sử cuộc gọi: Số gọi từ, Số gọi đến, Tên queue ACD, Thời gian vào ACD, tên agent tiếp nhận, Thời gian bắt đầu cuộc gọi, Thời điểm kết thúc cuộc gọi.</td>
    </tr>
    <tr>
      <td>5.35</td>
      <td>Hiển thị thông tin cuộc gọi</td>
      <td></td>
      <td>Khi điện thoại viên tiếp nhận cuộc gọi inbound ring tới mình, trên màn hình hiển thị các thông tin: số điện thoại khách hàng, tên queue ACD, đếm thời gian trả lời.</td>
    </tr>
    <tr>
      <td>5.36</td>
      <td>Trưởng nhóm ngắt cuộc gọi của điện thoại viên</td>
      <td></td>
      <td>Khi điện thoại viên đang trả lời cuộc gọi inbound của khách hàng, Giám sát viên hoặc Admin của hệ thống có thể chủ động kết thúc cuộc gọi giữa điện thoại viên và khách hàng.</td>
    </tr>
    <tr>
      <td>5.37</td>
      <td>Quản lý Queue</td>
      <td></td>
      <td>Tương tự hệ thống cũ 1. Yêu cầu nghiệp vụ - Cho phép gán ĐTV vào queue - Quản lý agent theo zone và lọc theo zone - Cty=>khu vực => nhóm (theo vị trí, theo quản lý)</td>
    </tr>
    <tr>
      <td>5.38</td>
      <td>Giám sát queue</td>
      <td></td>
      <td>Tương tự hệ thống cũ 1. Yêu cầu nghiệp vụ - Cho phép giám sát nhiều đơn vị - Phân quyền theo queue, đơn vị - Mô hình giám sát: 1 user giám sát đc bản thân, 1 user giám sát các dịch vụ trong cty, 1 user giám sát được cả bên trong cty và bên ngoài cty, 1 user giám sát được nhiều khu vực</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5.39</td>
      <td>Chat nội bộ</td>
      <td>Hiện tại, hệ thống IPCC đã có tính năng Chat cho Điện thoại viên (ĐTV) và nhân viên BO có thể thực hiện Chat trong ca trao đổi thông tin. Tuy nhiên hệ thống chưa có tính năng chặn chiều Chat theo đối tượng người sử dụng, do đó cần thực hiện nâng cấp chức năng để hệ thống đảm bảo quản lý và kiểm soát được các chiều Chat thông tin theo từng đối tượng</td>
      <td>1. Yêu cầu nghiệp vụ - Hiện tại, hệ thống IPCC đã có tính năng Chat cho Điện thoại viên (ĐTV) và nhân viên BO có thể thực hiện Chat trong ca trao đổi thông tin. Tuy nhiên hệ thống chưa có tính năng chặn chiều Chat theo đối tượng người sử dụng, do đó cần thực hiện nâng cấp chức năng để hệ thống đảm bảo quản lý và kiểm soát được các chiều Chat thông tin theo từng đối tượng '- Mới chỉ gửi text (chat thông thường) - Cho phép gửi Media, file, hình ảnh, biểu tượng, emoji</td>
    </tr>
  </tbody>
</table>







<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5.43</td>
      <td>Chat 1-1</td>
      <td></td>
      <td>Giao diện chat Tiếp nhận và hiển thị tin nhắn Lưu trữ xử lý tin nhắn</td>
    </tr>
    <tr>
      <td>5.44</td>
      <td>Chat nhắc nhở</td>
      <td></td>
      <td>1. Yêu cầu nghiệp vụ - Chủ dv chat toàn bộ - Làm thuê chat cho trong nhân sự của đơn vị làm thuê 2. Đề xuất chức năng - Đối tượng phân quyền được gửi gì (ĐTV, TVV, lãnh đạo) - Cho thêm quản lý nhóm chat (Trường nhóm add nhóm) (Trùng với yêu cầu): giám sát viên Nhắn cho nhiều nhóm tuy vào từng quyền - Cấu hình không cho phép ĐTV nhắn với nhau</td>
    </tr>
    <tr>
      <td>5.46</td>
      <td>Chat theo nhóm</td>
      <td></td>
      <td>- Cho phép giám sát tạo nhóm chat trao đổi nghiệp vụ</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5.47</td>
      <td>Yêu cầu trợ giúp</td>
      <td></td>
      <td>2 1. Yêu cầu nghiệp vụ - Có trợ giúp của giám sát chưa có trợ giúp của trưởng ca, trưởng nhóm, agent - Agent xin trợ giúp cấp trên (không xin trợ giúp ngang cấp) - Có màn hình chát hỗ trợ màn hình có vùng dữ liệu (trưởng ca trưởng nhóm, giám sát), nội dung hỗ trợ, hình thức hỗ trợ (chat, điện thoại) - Có hình thức cảnh báo cho ông nhận hỗ trợ biết thông tin trợ - thiết lập 1 luông chat giữa 2 cán bộ hỗ trợ và cán bộ nhân hỗ trợ - Với hỗ trợ theo luồng voice thì cuộc gọi của khách hàng sẽ được hold trong khi chờ trợ giúp . Đề xuất chức năng</td>
    </tr>
    <tr>
      <td>5.48</td>
      <td>Trưởng nhóm tìm kiếm trạng thái agent</td>
      <td></td>
      <td>1. Yêu cầu nghiệp vụ '- Phân quyền chức năng tìm kiếm trạng thái agent - Dữ liệu chỉ hiện thị các ĐTV trong đơn vị tổ chức mà Trưởng ca đó đang thuộc vào (thuộc nhóm vật lý) 2. Đề xuất chức năng - Đề xuất đưa vào giám sát agent và hiển thị theo dữ liệu theo phạm vi quản lý - Các tiêu chí như hệ thống cũ (bỏ IP phone)</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5.49</td>
      <td>Trưởng ca tìm kiếm trạng thái agent</td>
      <td>H Bổ xung thêm ngoài giao diện như tìm kiếm trên AD hiện tại: ệ thống cảnh báo cuộc gọi của NV dài quá thời gian quy định (ví dụ 6 phút) để giám sát có thể nghe song song hỗ trợ. Hệ thống có thể cảnh báo nếu NV để sai chế độ ví dụ away from desk hơn 30 phút. Hệ thống có thể cảnh báo khi số lượng cuộc gọi chờ/số lượng email chưa được xử lý/số tương tác mạng xã hội chưa được xử lý vượt quá số lượng quy định. Số lượng hoặc thời gian có thể chủ động tùy chỉnh.</td>
      <td>H Bổ xung thêm ngoài giao diện như tìm kiếm trên AD hiện tại: ệ thống cảnh báo cuộc gọi của NV dài quá thời gian quy định (ví dụ 6 phút) để giám sát có thể nghe song song hỗ trợ. Hệ thống có thể cảnh báo nếu NV để sai chế độ ví dụ away from desk hơn 30 phút. Hệ thống có thể cảnh báo khi số lượng cuộc gọi chờ/số lượng email chưa được xử lý/số tương tác mạng xã hội chưa được xử lý vượt quá số lượng quy định. Số lượng hoặc thời gian có thể chủ động tùy chỉnh. Đề xuất: - Đã đáp ứng ở chức năng GS thông tin cuộc gọi</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5.50</td>
      <td>Cảnh báo tự động, cảnh báo cưỡng bức, cảnh báo thời gian đàm thoại</td>
      <td>Bổ xung thêm cảnh báo cho ĐTV: Hệ thống cảnh báo (Tạo notification) toàn bộ nhân viên đang login khi cuộc gọi trong hàng chờ vượt quá số lượng cài đặt (số này có thể chủ động cài đặt theo thời gian, theo queue, tần xuất cảnh báo).</td>
      <td>Bổ xung thêm cảnh báo cho ĐTV: Hệ thống cảnh báo (Tạo notification) toàn bộ nhân viên đang login khi cuộc gọi trong hàng chờ vượt quá số lượng cài đặt (số này có thể chủ động cài đặt theo thời gian, theo queue, tần xuất cảnh báo). Đề xuất: - Bổ sung 1 chức năng cảnh bảo khi hệ thống đến ngưỡng thì sẽ cảnh báo, cảnh báo cho TVV, GS - Cho phép cấu hình theo màu cảnh báo - Cảnh báo màn hình: màn hình ĐTV và màn hình của GS - TungTV đề xuất đưa vào bài toán ngẽn</td>
    </tr>
    <tr>
      <td>5.51</td>
      <td>Cảnh báo các chế độ quá thời gian cho ĐTV trên AD</td>
      <td></td>
      <td>- Giữ nguyên như hệ thống 1 - Cảnh báo các chế độ quá thời gian cho ĐTV trên AD (Hiển thị cho từng ĐTV) - Cấu hình theo từng queue</td>
    </tr>
    <tr>
      <td>5.52</td>
      <td>Cảnh báo cho giám sát</td>
      <td></td>
      <td>1. Yêu cầu nghiệp vụ - Cảnh báo của DTV cũng hiện trên màn hình của ông giám sát 2. Đề xuất chức năng</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5.53</td>
      <td>Tinh năng hạn chế người dùng chuyển chế độ trên AgentDesktop</td>
      <td></td>
      <td>1. Yêu cầu nghiệp vụ ' - Căn cứ tỷ lệ ngẽn hệ thống (cấu hình được) - Thỏa mãn tất cả các queue 2. Đề xuất chức năng - Bổ sung tham số % ĐTV avaiable/Tổng số user đăng nhập/Queue - Quá số thì không cho chuyển và cảnh bảo - Cho phép GS mở được trạng thái cho người xin</td>
    </tr>
    <tr>
      <td>5.54</td>
      <td>Transfer AG - AG</td>
      <td></td>
      <td>1. Yêu cầu nghiệp vụ - Giống hệ thống cũ 2. Đề xuất chức năng - Giữ nguyên từ hệ thống cũ - Bổ sung kiểm tra trạng thái avaiable và chỉ chuyển trạng trong queue - Bổ sung trưởng nhóm, trưởng ca có thể chuyển cuộc từ AG này sang AG khác trong cùng queue</td>
    </tr>
    <tr>
      <td>5.55</td>
      <td>Transfer AG - Supervisor</td>
      <td></td>
      <td>2 1. Yêu cầu nghiệp vụ - Lấy được Supervisor quản lý ông AG đó . Đề xuất chức năng Chỉ chuyển được tới Supervíor quản lý nhóm của AG đó</td>
    </tr>
    <tr>
      <td>5.56</td>
      <td>Transfer AG – Chuyên gia (phân biệt với cuộc gọi thông thường)</td>
      <td></td>
      <td>Transfer AG – Chuyên gia (phân biệt với cuộc gọi thông thường). ĐTV chủ động chuyển sang chuyên gia</td>
    </tr>
    <tr>
      <td>5.57</td>
      <td>transfer từ ACD – sang các kênh khác và tranfer giữa các kênh</td>
      <td></td>
      <td>Tham khảo 5.7; 5.8; 5.9; 5.10 -Tranfer từ ACD - sang các kênh khác (Hệ thống đang có )</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5.58</td>
      <td>Đa kênh (voice, video, Email, Chat, Social – Facebook, Mocha, Zalo…)</td>
      <td></td>
      <td>1. Yêu cầu nghiệp vụ - Cho phép xem lịch sử tương tác KH đa kênh (Các kênh trong IPCC, các kênh ngoài IPCC) - Cho phép xem lịch sử xử lý với từng Khách hàng, với nhiều khách hàng, lịch sử tương tác, lịch sử phản ánh - Xem thông tin KH đa kênh - Tương tác với KH trên kênh bất kỳ 2. Đề xuất chức năng</td>
    </tr>
    <tr>
      <td>5.59</td>
      <td>Đa kênh trên cùng giao diện - all in one</td>
      <td></td>
      <td>1. Yêu cầu nghiệp vụ - Hiển thị thông tin theo đặc thù từng kênh 2. Đề xuất chức năng</td>
    </tr>
    <tr>
      <td>5.60</td>
      <td>Nhận diện khách trên các kênh khác nhau - Customer jouney</td>
      <td></td>
      <td>1. Yêu cầu nghiệp vụ - Cho phép cấu hình thông tin hiển thị: Công ty (chủ dịch vụ), kênh tương tác, nguồn dữ liệu: IPCC, mBCCS, app của các nhà cung cấp dịch vụ, tương tác tại cửa hàng.vv - Hiển thị lịch sử tương tác, popup theo kênh tương tác, chủ sở hữu dịch vụ - Cấu hình động theo từng nguồn thông tin - 2. Đề xuất chức năng</td>
    </tr>
    <tr>
      <td>5.61</td>
      <td>Popup lịch sử tương tác với BOT</td>
      <td></td>
      <td>1. Yêu cầu nghiệp vụ - Hiển thị lịch sử tương tác với bot (theo các kênh), tên bot (nguồn nào) 2. Đề xuất chức năng</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5.62</td>
      <td>Popup & TAG khi Transfer (tham khảo Mitek)</td>
      <td>Bổ xung chức năng tag nội dung khi tranfer (tham khảo Mitek): + Chọn loại chủ để KH hỏi theo danh mục sẵn có để TAG khi chuyển tranfer + Cho ô để ĐTV nhập nội dung KH phản ánh chi tiết khi chuyển, nd này có thể copy từ ô ĐTV nhập trên BCCS để tranfer</td>
      <td>Bổ xung chức năng tag nội dung khi tranfer (tham khảo Mitek): - Popup thông tin khi transfer giữa các kênh - Cho phép nhập ghi chú khi transfer</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Xử lý kết thúc tương tác</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>6.1</td>
      <td>( Kết thúc thông thường, tạo TICKET tham khảo thêm phần 12.2.8 - các chức năng phần mạng xã hôi)</td>
      <td>N - Tự động tạo TICKET đối với kênh thoại cũng như các kênh khác cho cả 2 chiều INbound/Outbound - TICKET có thể mapping với 1 bản ghi trên hệ thống CRM của 1 đơn vi khác (BCCS_CC), CRM của VTPost...) - Bổ xung chi tiết danh sách THUỘC TÍNH của 1 TICKET goài ra lưu ý các bất cập ht cũ: Hiện tại khi Giám sát thực hiện giao lại ticket thủ công cho NVCSKH gặp tình trạng: hệ thống Econtact hiển thị toàn bộ NVCSKH bao gồm cả NVCSKH đang online (NVCSKH đi làm) và offline (NVCSKH không đi làm) dẫn đến tình trạng nhầm lẫn trong</td>
      <td>T Đ 1. Yêu cầu nghiệp vụ - Tự động tạo TICKET đối với kênh thoại cũng như các kênh khác cho cả 2 chiều INbound/Outbound - TICKET có thể mapping với 1 bản ghi trên hệ thống CRM của 1 đơn vi khác (BCCS_CC), CRM của VTPost...) - Bổ xung chi tiết danh sách THUỘC TÍNH của 1 TICKET rao đổi : ịnh hướng : 100% các phản ánh phải được tiếp nhận và xử lý, cần có giải pháp cho các trường hợp không dc xử lý trên kênh phi thoại Hiện tại : đối với Voice đã có chức năng gọi lại tự động, đang đề xuất thêm chức năng hẹn gọi lại. Với các kênh khác đề xuất bổ xung Trao đổi : - Với kênh FB đã có định danh, VTS đã hiểu mong muỗn - Với kênh Chat web : cần xử lý với KH không định danh + Xây dựng chức năng cho khách hàng để lại thông tin liên hệ + Xây dựng chức năng phân phối lại phản ánh đến ĐTV với các KH để lại thông tin liên hệ, có ưu tiên xử lý + Khi phân phối lại có hiện thị lịch sử trước đó + Có thể ON/OFF chức năng này chủ động trong quá trình khai thác</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>quá trình giao (hình ảnh bên dưới). -Mong muốn nâng cấp: + Ưu tiên hiển thị danh sách các NVCSKH đang online lên đầu. + Có ký hiệu nhận biết để phân biệt giữa NVCSKH đang online và offline. (tham khảo thêm phần 12.2.8 - các chức năng phần mạng xã hôi)</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>6.2</td>
      <td>Chuyển cuộc gọi sang ht survey tập trung</td>
      <td></td>
      <td>1. Yêu cầu nghiệp vụ - Bổ sung cho tất cả các kênh - Gửi survey sms theo đầu số và sđt khách hàng - Kênh thoại survey qua sms; kênh chat survey trực tiếp</td>
    </tr>
    <tr>
      <td>6.3</td>
      <td>Survey ngay trên IPCC</td>
      <td>( Yêu cầu phân quyền - Queue (các kênh) nghiệp vụ nào thực hiện survey thì chỉ có đơn vị đó được tác động cấu hình, thực hiện survey và xuất báo cáo - Trường hợp 1 đầu số thoại có 2 nhánh ACD, mỗi nhánh thuộc 1 cty thì nhánh của cty nào dc tác động đến các chiến dịch survey của kênh đó bất cập ht IPCC 1.0 là không thể cấp quyên cấu hình servey cho các đơn vị khác như VTP...)</td>
      <td>1. Yêu cầu nghiệp vụ - Survey qua email - Survey qua USSD - Survey qua sms - Survey trực tiếp (chat) - Survey qua IVR</td>
    </tr>
  </tbody>
</table>







<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>6.5.1</td>
      <td>6.5.1 Survey Voice</td>
      <td>Có các lựa chon sau : - Cấu hình được cuộc gọi chỉ voice sang survey - Cấu hình được chỉ gửi survey các cuộc gặp ĐTV - Cấu hình được chỉ gửi survey các cuộc gặp BOT (nếu cuộc gọi KH vào queue nghe hết nhạc chờ sang BOT luôn thì IPCC không gửi survey ACD nữa) Bất cập Hiện tại : - Khi cấu hình queeue chuyển BOT thì mỗi cuộc chuyển BOT hê thống IPCC hiểu đó là ĐTV kết thúc cuộc gọi và thực hiện gửi lệnh sang ht survey tập trung, sau đó BOT lại gửi lần nữa, nếu KH đó lại được chuyển lại IPCC để gặp ĐTV thì lại được survey thêm lần thứ 3</td>
      <td>Có các lựa chon sau : - Cấu hình được cuộc gọi chỉ voice sang survey - Cấu hình được chỉ gửi survey các cuộc gặp ĐTV - Cấu hình được chỉ gửi survey các cuộc gặp BOT (nếu cuộc gọi KH vào queue nghe hết nhạc chờ sang BOT luôn thì IPCC không gửi survey ACD nữa) 1. Yêu cầu nghiệp vụ Lựa chọn được các cấu hình cho survey</td>
    </tr>
    <tr>
      <td>6.6</td>
      <td>Voice mail</td>
      <td></td>
      <td>1. Cho phép để lại voice mail trong TH queue có cấu hình để lại voice mail (hướng dẫn KH để lại Voice mail)</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>6.7</td>
      <td>Nhạc kết thúc cuộc gọi (nhạc peep) khi KH kết thúc trước</td>
      <td></td>
      <td>1. KH kết thúc trước => có nhạc riêng để ĐTV biết được thông tin. Cấu hình theo từng queue</td>
    </tr>
    <tr>
      <td>6.8</td>
      <td>Thăm dò ý kiến Khách hàng qua IVR (đề xuất này GĐ yêu cầu PGS bổ xung nghiệp vụ</td>
      <td></td>
      <td>- Thăm dò ý kiến Khách hàng qua IVR . Tương tự hệ thống cũ - Bổ sung báo cáo</td>
    </tr>
    <tr>
      <td>6.9</td>
      <td>Phát âm để hỏi KH có đồng ý Khảo sát không? Có thì gửi</td>
      <td></td>
      <td>Phát âm để hỏi KH có đồng ý Khảo sát không? Có thì gửi</td>
    </tr>
    <tr>
      <td>6.10</td>
      <td>Khách hàng chọn không đồng ý khảo sát thì không gửi</td>
      <td></td>
      <td>Khách hàng chọn không đồng ý khảo sát thì không gửi</td>
    </tr>
    <tr>
      <td>6.11</td>
      <td>Khách hàng không lựa chọn thì vẫn gửi khảo sát</td>
      <td></td>
      <td>Khách hàng không lựa chọn thì vẫn gửi khảo sát</td>
    </tr>
    <tr>
      <td>6.12</td>
      <td>Thống kê tỉ lệ khao sát theo loại KH đồng ý và hệ thống tự chuyển</td>
      <td></td>
      <td>Thống kê tỉ lệ khao sát theo loại KH đồng ý và hệ thống tự chuyển</td>
    </tr>
    <tr>
      <td>6.13</td>
      <td>Thăm dò ý kiến Khách hàng qua SMS</td>
      <td>Có thể chọn được đầu số SMS để thực hiện survey với mỗi queue. Có thể nhiều queue dùng chung 1 đầu số để survey (Sau này nếu bán dịch vụ cho các đơn vị ngoài, mỗi đơn vị sẽ yêu cầu 1 đầu số SMS riêng để gắn với ALIAS của đơn vị đó khi thực hiện survey trên các kênh dịch vụ của đơn vị đó)</td>
      <td>- Tích hợp với Survey tập trung và xây dựng mới - Có thể chọn được đầu số SMS để thực hiện survey với mỗi queue. - Có thể nhiều queue dùng chung 1 đầu số để survey (Sau này nếu bán dịch vụ cho các đơn vị ngoài, mỗi đơn vị sẽ yêu cầu 1 đầu số SMS riêng để gắn với ALIAS của đơn vị đó khi thực hiện survey trên các kênh dịch vụ của đơn vị đó)</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>6.14</td>
      <td>Chuyển cuộc gọi từ ACD sang IVR</td>
      <td></td>
      <td>- Khi kết thúc cuộc gọi chủ động và tự động (nhỡ) chuyển cuộc gọi từ ACD sang IVR</td>
    </tr>
    <tr>
      <td>6.15</td>
      <td>Chuyển cuộc gọi từ ACD sang ACD</td>
      <td></td>
      <td>- Bao gồm chuyển chủ động và chuyển tự động</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Gọi ra</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>7.1</td>
      <td>Cấu hình dạng số được phép gọi ra</td>
      <td></td>
      <td>Mục đích để chặn gọi quốc tế, ngoại mạng,vv</td>
    </tr>
    <tr>
      <td>7.2</td>
      <td>Cấu hình giờ được gọi ra, theo ngày, theo thứ, hỗ trợ nhiều khoảng giờ Gọi ra theo lịch hẹn (tự động) ( tự điền thêm khách hàng vào danh sách gọi lại )</td>
      <td>- Cấu hình gọi ra theo giờ áp dụng theo từng Queue - Với queue gọi ra cho phép cấu hình mapping với 1 trường thông tin nào đó trên 1 chiến dịch thuộc modun chiến dịch để tự động kích hoạt cuộc gọi ra - Vd : Khi KH hẹn gọi lại, ĐTV nhập thông tin yc gọi lại trên IPCC, hệ thống tự validate thông tin ĐTV nhập, đến thời điểm cần gọi ht tự động make cuộc gọi ra, popup lý do gọi ra cho ĐTV nếu ĐTV O thì make cuộc gọi đến KH , trường hợp KH ko nghe máy thì ht sẽ gọi lại theo QĐ và</td>
      <td>- Cấu hình giờ được gọi ra, theo ngày (ngày cụ thể trong năm dd/mm/yyyy), theo thứ, hỗ trợ nhiều khoảng giờ, cấu hình theo queue - Cấu hình gọi ra theo lịch hẹn tự động: ĐTV có thể nhập thông tin gọi lại cho KH (khoảng thời gian hẹn gọi lại, khoảng cách giữa 2 lần gọi, số lần gọi tối đa, cấu hình queue gọi ra, nội dung cuộc gọi trước). Đến thời gian hẹn gọi lại hệ thống tự động gọi ra cho KH - Đối với khách hàng có Định danh thì phản ánh theo các kênh - Đối với khách hàng không định danh hỗ trợ khách hàng bổ sung thêm thông tin nếu khách hàng cần phản hồi sau khi bị lỡ (chat bạn bị lỡ, bạn cần gặp TVV thì đề nghị để lại thông tin (email, SĐT) để TVV liên lạc, có thể đưa vào chiến dịch HPC. - Đối với các chat lỡ thì có cớ chế cho phân phối lại và cho phép cấu hình để đưa các chat lỡ đưa tới TVV với mức độ ưu tiên. - Bổ sung các chiến dịch cho các kênh khách khi cần truyền thông</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>thông báo cả số lần đã gọi ra trc đó nhưng KH ko nghe máy để ĐTV nắm được (Tương tự trên các kênh khác có thể thiết lập chiến dịch outbound : Zalo broadcast, SMS Broadcast, Email Broadcast ...vd nhắc cm sinh nhat)</td>
      <td></td>
    </tr>
    <tr>
      <td>7.3</td>
      <td>Cấu hình thay đổi số hiển thị gọi ra</td>
      <td></td>
      <td>- Cấu hình thay đổi số hiển thị gọi ra - Có prefix + số đt khách hàng hoặc thay thế gửi sang cho chuyên gia cả 2 hình thức (chủ động, tự động)</td>
    </tr>
    <tr>
      <td>7.4</td>
      <td>Check DNC khi gọi ra</td>
      <td></td>
      <td>- Check hạn nghạch cuộc gọi quảng cáo</td>
    </tr>
  </tbody>
</table>

# Public_442

<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>7.8</td>
      <td>Khi KH gọi lại các số đã gọi ra thì POPUP các thông tin đã gọi ra trước đó</td>
      <td>Cần làm kĩ - Mục tiêu là quản lý được thời gian phản hồi lại cho khách hàng nhanh hay chậm</td>
      <td>1. Yêu cầu nghiệp vụ Cần làm kĩ - Mục tiêu là quản lý được thời gian phản hồi lại cho khách hàng nhanh hay chậm. - Mỗi cuộc gọi và phiên tương tác IPCC sinh ra ID => Hiển thị cho ĐTV + chuyển ID, thời gian giao dịch, kênh giao dịch sang Ứng dụng khác. - Nhận thông tin mã giao dịch từ Ứng dụng khác - Cấu hình thông tin ID cuộc gọi của queue gửi sang hệ thống nào - Sử dụng với các ứng dụng khác có CRM và không có CRM 2. Đề xuất - Hiển thị các cuộc gọi ra theo cùng công ty ( User thuộc công ty) - Bổ sung phân quyền cho phép khai thác cuộc gọi theo mô hình -</td>
    </tr>
    <tr>
      <td>7.8.1</td>
      <td>Popup gọi ra từ BCCS (cũng như các UD khác) xem phần call in</td>
      <td>Cần làm kĩ - Mục tiêu là quản lý được thời gian phản hồi lại cho khách hàng nhanh hay chậm</td>
      <td>Tương tự như trên - Thông tin trên PopUp: số đã gọi ra, kênh gọi ra, người gọi ra, thời gian gọi ra - TT CSKH cần phản hồi lại</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>7.9</td>
      <td>Khi chuyển cuộc gọi tới di động yêu cầu hiển thị đúng số di động của khách hàng à Trường hợp hiển thị đúng số di động của khách hàng thì tổng đài sẽ tính cước cho số khách hàng, đồng thời hệ thống IPCC cũng sẽ tính cước gọi lên tổng đài, khách hàng sẽ bị tính cước hai lần. Cần confirm lại cách làm. Vì vậy đối với luồng này ipcc cho qua sip trunk khác và ko khai cước cho síp trunk này tránh kh bị tính cước 2 lần</td>
      <td></td>
      <td>- Bổ sung luồng sip trunk nếu tranfer chuyên gia thì tùy queue có thể chọn đượcluồng sip trunk - Để khai phí 0 đồng cho sip trunk này (tùy theo quy định)</td>
    </tr>
    <tr>
      <td>7.10</td>
      <td>Luồng tự động gọi lại cấu hình số gốc (tính cước) nhưng vẫn hiển thị số chung 2660198</td>
      <td></td>
      <td>Như hiện tại Luồng tự động gọi lại cấu hình số gốc (tính cước) nhưng vẫn hiển thị số chung 2660198</td>
    </tr>
    <tr>
      <td>7.11</td>
      <td>Popup khi gọi ra</td>
      <td>- Hiển thị các màn hình popup khi gọi ra - Hiển thị các cảnh báo khi gọi ra từ giao diện: + Popup DNC + Popup Quotar</td>
      <td>- Hiển thị các màn hình popup khi gọi ra - Hiển thị các cảnh báo khi gọi ra từ giao diện: + Popup DNC + Popup Quotar - Quota thì đội dự án đề xuất</td>
    </tr>
    <tr>
      <td>7.12</td>
      <td>Gọi ra từ các hệ thống khác: - Gọi ra từ BCCS - Gọi ra từ Happy call - Gọi ra từ hệ thống khác (nâng cấp nếu phát sinh)</td>
      <td></td>
      <td>IPCC cung cấp các API để các hệ thống khác tích hợp để gọi ra</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Xử lý call back</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>8.1</td>
      <td>Voice call back (auto call back)</td>
      <td>Callbacks: https://help.mypure cloud.com/articles/a bout-callbacks/</td>
      <td>Hiện tại có chức năng tự động gọi lại KH nhỡ (có nên xây dựng chức năng để KH đăng kí gọi lại trên queue chờ ACD) - Callback cho Agent: Voice interactions for agents overview Place, transfer, and dismiss a callback Schedule callbacks during a voice interaction Schedule a callback in a script - Callbacks for administrators and contact center managers: Scheduled Callbacks view Add a rule Callbacks in campaigns Schedule callbacks from a website</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>8.2</td>
      <td>Gọi lại KH thường</td>
      <td></td>
      <td>Gọi lại khách hàng thường: cho phép tự động gọi lại khách hàng thường khi bị nhỡ: 1. Cấu hình tham số gọi lại khách hàng thường thỏa mã các tham số mô tả bên dưới-> hệ thống tự động thực hiện cuộc gọi lại cho khách hàng thường khi bị nhỡ 2. Thêm mới màn hình báo cáo/thống kê cuộc gọi lại tự động: Thống kê thông tin cuộc gọi tự động trong ngày + Cho phép tìm kiếm thông tin khách hàng/ queue gọi lại. + Xuất báo cáo chi tiết Điều kiện đảm bảo: 1. Màn hình Cấu hình queue callout + Thêm mới loại callout: Gọi ra tự động khách hàng thường cho phép gọi ra cho khách hàng thường theo giờ cấu hình trong màn cấu hình queue callout + Thêm mới param_id: Cấu hình tham số giá trị agent gọi lại: tất cả agent trong queue/ theo danh sách import. + Thêm mới Tham số cấu hình trạng thái gọi lại tự động: Cho phép on/off khi cần thiết 2. Cấu hình queue: + Đối với queue thường với tham số cho phép gọi lại khách hàng thường. 3. Thêm mới màn hình Quản lý chiến dịch gọi lại: Cho phép quản lý tất cả thông tin queue callout được cấu hình. + Tìm kiếm. + ON/OFF các trạng thái gọi lại các queue. 4. Thêm mới màn hình cấu hình ưu tiên cuộc gọi nhỡ:</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>8.3</td>
      <td>Gọi lại KH VIP</td>
      <td></td>
      <td>4 Gọi lại khách hàng VIP: Cho phép gọi lại khách VIP bị nhỡ khi gọi lên hệ thống theo khoảng khung giờ cấu hình. 1. Màn hình Cấu hình queue callout + Thêm mới loại callout: Gọi ra tự động khách hàng VIP cho phép gọi ra cho khách hàng VIP 2. Cấu hình queue + Đối với queue thường với tham số cho phép gọi lại khách hàng VIP theo các hạng VIP tương ứng. 3. Thêm mới màn hình Quản lý chiến dịch gọi lại: Cho phép quản lý tất cả thông tin queue callout được cấu hình. + Tìm kiếm. + ON/OFF các trạng thái gọi lại các queue. 4. Thêm mới màn hình cấu hình ưu tiên cuộc gọi nhỡ: . Thêm mới màn hình Thống kê cuộc gọi lại tự động trong ngày + Cho phép tìm kiếm thông tin khách hàng/ queue gọi lại. + Xuất báo cáo chi tiết</td>
    </tr>
    <tr>
      <td>8.4</td>
      <td>Cấu hình thời gian gọi lại theo giờ, theo thứ, theo ngày</td>
      <td></td>
      <td>Cấu hình thời gian gọi lại: Hiện tại trên hệ thống cũ chỉ cấu hình khoảng khung giờ gọi lại: 1.Thêm mới màn hình cấu hình thời gian gọi lại khách hàng: + Thêm mới tính năng cấu hình theo thứ, theo giờ. + Xây dựng tiến trình gọi lại cho khách theo khoảng khung giờ, thời gian được cấu hình.</td>
    </tr>
    <tr>
      <td>8.5</td>
      <td>Gọi ra</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>8.6</td>
      <td>Gọi ra chủ động từ IPCC - từ Agentdesktop</td>
      <td></td>
      <td>Gọi ra chủ đổng IPCC: Tính năng này cho phép gọi ra chủ động từ agent Destop cho khách hàng 1. Thêm mới màn hình Cấu hình queue callout: + Tạo mới tất cả param_id dùng gọi lại cho khách hàng: Tỉ lệ rảnh, queue gọi lại, agent gọi lại, trạng thái gọi lại….(tham khảo IPCC1.0). 2. Tạo Agent Destop: Cho phép agent có thể nghe máy, chủ động gọi ra cho khách hàng. + TVV có thể chủ động đăng nhập Agent Destop chuyển trạng thái đăng nhập. + Thực hiện cuộc gọi ra / vao tưowng ứng. 3. Xây dựng báo cáo thông kê thông tin cuộc gọi ra chủ động từ các queue: + Xem chi tiết/ tìm kiếm. + Xuất báo cáo 4. Phân quyền: admin/giám sát/ trưởng ca điều hành có quyenf xem xuất báo cáo.</td>
    </tr>
    <tr>
      <td>8.7</td>
      <td>Gọi ra Từ ud happy call, gọi ra từ BCCS: - Chiến dịch MNP - Chiến dịch CĐBR - BADO…</td>
      <td></td>
      <td>Hiện tại đã có "Gọi ra Từ ud happy call, gọi ra từ BCCS: - Chiến dịch MNP - Chiến dịch CĐBR - BADO…"</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>8.8</td>
      <td>Hỗ trợ 2 chức năng gọi ra thông thường và gọi ra KH nhấc máy mới chuyển đến ĐTV (autocall)</td>
      <td></td>
      <td>T Chức năng này cho phép gọi ra: Trùng nội dung. Gọi ra khách hàng nhấc máy đến DTV: + Hệ thống tính toán lượng agent rảnh. + Tính toán danh sách khách hàng được cấu hình. + Tự động đổ cuộc gọi ra cho khách hàng. + Khách hàng nhấc máy sẽ điều phối cuộc gọi đến TVV. + Tư vấn viên tiếp nhận cuộc gọi và trả lời yêu cầu khách hàng rùng với tính năng chủ động gọi ra 8.6 và tính năng thực hiện cuộc gọi HappyCall</td>
    </tr>
    <tr>
      <td>8.9</td>
      <td>gọi ra từ BCCS</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Vận hành</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.1</td>
      <td>Xây dựng (thêm mới/sửa) kịch bản cây IVR qua giao diện đồ họa</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.2</td>
      <td>Cập nhật kịch bản chủ động không làm gián đoạn hệ thống, không phải làm thủ tục sang đơn vị vận hành hỗ trợ</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.3</td>
      <td>Cấu hình các kết nối API qua giao diện</td>
      <td>- Cho phép cấu hình các kết nối API qua giao diện, - Các API cần được quy hoạch tên để dễ quản lý - Các tham số liên quan API có thể điều chỉnh được qua giao diện như: tăng giảm số lượng threar xử lý, thiết đặt thời gian timeout, số lượng ccu xử lý đồng thời của mỗi API...</td>
      <td></td>
    </tr>
    <tr>
      <td>9.4</td>
      <td>Cây IVR có thể hỗ trợ đón nhiều đầu số</td>
      <td>- Cho phép phân quyền chỉnh sửa từng cây IVR riêng, chỉ được tác động thay đổi, chỉnh sửa cây được phân quyền - Ghi log tác động chỉnh sửa cấu trúc cây và log tác động thay file âm thanh</td>
      <td></td>
    </tr>
    <tr>
      <td>9.5</td>
      <td>Tool xây cây IVR không bị giới hạn số lượng nốt hoặc đáp ứng 100K nốt, số lượng cây IVR không giới hạn hoặc tối thiểu 1000 cây</td>
      <td>- Cho phép phân quyền chỉ được thay đổi file nhạc của cây được phân quyền (tìm kiếm, backup, update, rollback, ...). - Ghi log tác động chỉnh sửa cấu trúc</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>cây và log tác động thay file âm thanh</td>
      <td></td>
    </tr>
    <tr>
      <td>9.6</td>
      <td>Phân quyền trên cây IVR :</td>
      <td>- Cho phép phân quyền chỉnh sửa từng cây IVR riêng, chỉ được tác động thay đổi, chỉnh sửa cây được phân quyền - Ghi log tác động chỉnh sửa cấu trúc cây và log tác động thay file âm thanh</td>
      <td></td>
    </tr>
    <tr>
      <td>9.7</td>
      <td>Cho phép thay đổi âm của riêng từng cây IVR</td>
      <td>- Cho phép phân quyền chỉ được thay đổi file nhạc của cây được phân quyền (tìm kiếm, backup, update, rollback, ...). - Ghi log tác động chỉnh sửa cấu trúc cây và log tác động thay file âm thanh</td>
      <td></td>
    </tr>
    <tr>
      <td>9.8</td>
      <td>Phân quyền báo cáo thống kê phím bấm từng cây, từng đầu số</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.9</td>
      <td>Chức năng cảnh báo up âm IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.10</td>
      <td>Năng lực xử lý của 1 cây IVR đáp ứng >5000 ccu và khả năng mở rộng theo chiều ngang</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.11</td>
      <td>Ghi âm cuộc gọi, 3 file (file gộp và file tách ĐTV và KH),</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.12</td>
      <td>cho phép tắt bật chức năng ghi âm với từng đầu số (gd chỉ đạo chưa cần nếu ht mới chưa đáp ứng)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.13</td>
      <td>Tạo queue mới và tích hợp với các hệ thống khác :</td>
      <td>- Dễ dàng nhúng các kênh tương tác (chat, e mail, FB, Zalo...) trên Web của các đơn vị - Dễ dàng tích hợp video call với các app của các doanh nghiệp - Tạo sẵn nhiều SIP trunk, nhiều danh sách đầu số Callin sẵn để giảm thời gian khai báo khi triển khai - Cho phép tiếp nhận cuộc gọi từ các tổng đài SIP khác qua khai báo đơn giản</td>
      <td></td>
    </tr>
    <tr>
      <td>9.14</td>
      <td>Tạo queue (thoại/video) mới không cần chuyển VTN thực hiện</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.15</td>
      <td>Tạo các queue chat fanpage/group mới không cần chuyển VTN thực hiện</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.16</td>
      <td>Tạo các queue (email, sms ) không cần VTN thực hiện</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.17</td>
      <td>Chủ động cấu hình thêm, chon kết nối đến các kênh CallBOT</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.18</td>
      <td>Chủ động cấu hình thêm, chon kết nối đến các kênh Chat BOT</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.19</td>
      <td>Quy hoạch được các đầu số, nhóm đầu số vào các modun riêng để bảo đảm khi lỗi không ảnh hưởng đến nhau</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.20</td>
      <td>Đồng bộ danh sách KH tự động từ các HT</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>







<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>ngân hàng Đồng bộ với các ht khác nếu có dịch vụ mới 2. Phân quyền : - Trong các màn hình tìm kiếm, cho phép lựa chọn "nguồn dữ liệu VIP" cho tìm kiếm trong tất cả các nguồn, hoặc từng nguồn tùy theo phân quyền - Phân quyền đến từng nút tìm kiếm, xuất báo cáo - Các chức năng xuất báo cáo có 2 loại buton : xuất danh sách không mã hóa số TB và xuất có mã hóa 1 phần số 3. Nghiệp vụ: - Cho phép import danh sách để tìm hạng tương ứng theo file</td>
      <td></td>
    </tr>
  </tbody>
</table>











<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.30</td>
      <td>Partime (xem tài liệu chi tiết)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.31</td>
      <td>Voice to text</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.32</td>
      <td>Chức năng test nhóm ĐTV</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.33</td>
      <td>Phân quyền tác động thay đổi tham số theo queue</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.34</td>
      <td>Ghi log tác động thay đổi tham số queue</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.35</td>
      <td>Cấu hình cho phép đăng nhập theo định dạng user</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.36</td>
      <td>Giám sát gọi ra</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.37</td>
      <td>Thống kê trạng thái cuộc gọi và ĐTV</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.38</td>
      <td>Ghi âm cuộc gọi ra</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.39</td>
      <td>Nhóm kênh cần giám sát cho Trưởng ca</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.40</td>
      <td>Đăng kí và trả lời cuộc gọi trên ĐT di động</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.41</td>
      <td>Agent desktop hỗ trợ 3 giao diện Mobile_app/Web/AgentDesktop</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.42</td>
      <td>Đồng bộ trạng thái hang loạt</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.43</td>
      <td>Đặt lịch khảo sát</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.44</td>
      <td>Import danh sách VIP/Blacklist/Agent từ file</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.45</td>
      <td>Import khách hàng không được phép gọi ra (DNC) từ file</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.46</td>
      <td>Import gán hủy ID theo file</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.47</td>
      <td>Import nhóm khách hàng</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.48</td>
      <td>Tìm kiếm Agent gán cho Queue</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.49</td>
      <td>Gán agent cho queue từ file</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.50</td>
      <td>Gán username trưởng ca vào zone</td>
      <td>Mục đích : - Giám sát được trạng thái nhân viên trên từng Queue trên giao diện theo 2 hình thức: + Giám sát theo vị trí địa lý (từng queue, tất các queue) + Giám sát được theo nhóm nhân sự quản lý</td>
      <td></td>
    </tr>
    <tr>
      <td>9.51</td>
      <td>Gán callout cho agent</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.52</td>
      <td>Nghe lại lịch sử cuộc gọi</td>
      <td>Chính là chức năng tìm kiếm nghe lại cuộc gọi Yêu cầu cho phép tìm kiếm nghe lại từ internet</td>
      <td></td>
    </tr>
    <tr>
      <td>9.53</td>
      <td>Nghe lại lịch sử cuộc gọi từ ngoài internet</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.54</td>
      <td>Gán agent vào zone/cập nhật location cho user ĐTV</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.55</td>
      <td>Quản lý nhạc</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.56</td>
      <td>Quản lý thông tin line-server</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.57</td>
      <td>Cập nhật nhạc chờ ACD</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.58</td>
      <td>Thống kê mã lỗi gọi ra</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.59</td>
      <td>Thống kê tổng hợp thông tin cuộc gọi cuộc gọi (S-001)</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.60</td>
      <td>Thống kê cuộc gọi theo số lần và theo thuê bao</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.61</td>
      <td>Thống kê danh sách thuê bao thực hiện khảo sát</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.62</td>
      <td>Báo cáo tác động</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.63</td>
      <td>Báo cáo tác động âm báo IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.64</td>
      <td>Thống kê tổng hợp cuộc gọi được ĐTV chuyển vào khảo sát IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.65</td>
      <td>Thống kê thời gian chờ và gặp trung bình</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.66</td>
      <td>Thống kê trạng thái disconnect cuộc gọi</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.67</td>
      <td>Thống kê tổng hợp cuộc gọi thực hiện khảo sát SMS, USSD</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.68</td>
      <td>Thống kê tổng hợp phím bấm (kênh IVR)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.69</td>
      <td>Thống kê lịch sử tác động cây IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.70</td>
      <td>Thống kê tổng hợp thông tin cuộc gọi (kênh ACD) (CG-002)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.71</td>
      <td>Thống kê thời gian chờ TB (CG- 001.1)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.72</td>
      <td>Thống kê cuộc gọi vào IVR theo thời gian nghe (CG-004)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.73</td>
      <td>Thống kê cuộc gọi theo phút (CG - 005)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.74</td>
      <td>Thống kê chi tiết cuộc gọi (kênh IVR) (CG - 006)</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.75</td>
      <td>Thống kê cuộc gọi chuyển ACD</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.76</td>
      <td>Thống kế tổng hợp thông tin cuộc gọi VIP</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.77</td>
      <td>Thống kê số lần thay đổi trạng thái của Agent (AG - 001)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.78</td>
      <td>Thống kê trạng thái làm việc của Agent (AG - 003)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.79</td>
      <td>Thống kê tác động của Agent (AG - 005)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.80</td>
      <td>Thống kê thời gian trạng thái (AG - 002)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.81</td>
      <td>Thống kê số cuộc gọi của Agent (AG - 004)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.82</td>
      <td>Thống kê theo đầu số khách hàng (KH - 004)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.83</td>
      <td>Thống kê khách hàng gọi lên hệ thống N lần (KH - 002)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.84</td>
      <td>Thống kê khách hàng rớt và gặp Agent (KH - 003)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.85</td>
      <td>Thống kê thông tin chi tiết khách hàng (KH - 001)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.86</td>
      <td>Thống kê khách hàng bị chặn vẫn gọi lên hệ thống (BL - 001)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.87</td>
      <td>Quản lý Black List</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.88</td>
      <td>Thống kê lịch sử chặn thuê bao</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.89</td>
      <td>Thống kê tổng hợp thuê bao bị chặn theo kênh</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.90</td>
      <td>Quản lý hạng khách hàng VIP</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.91</td>
      <td>Quản lý khách hàng VIP</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.92</td>
      <td>Danh mục đầu số người dùng</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.93</td>
      <td>Quản lý tin nhắn (menu này cho chức năng tạo sms survey)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.94</td>
      <td>Danh mục khảo sát (SMS, USSD)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.95</td>
      <td>Danh mục cây IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.96</td>
      <td>Danh mục kênh</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.97</td>
      <td>Thêm kênh cho người dùng</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.98</td>
      <td>Quản lý mở khóa tài khoản</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.99</td>
      <td>Quản lý nhóm tin nhắn</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.100</td>
      <td>Quản lý chiến dịch (survey KH nhỡ, KH gặp, cho phép KH từ chối)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.101</td>
      <td>Cấu hình tranfer</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.102</td>
      <td>Cấu hình số ĐT tranfer cho ĐTV</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.103</td>
      <td>Cấu hình queue</td>
      <td>T - Yêu cầu phân quyền đến "Từng THAM SỐ" của "từng Queue" để chủ động cấp quyền cho các đơn vị chủ động cấu hình các tham số đơn giản (hiện tại phân quyền chưa linh hoạt nên khó khăn trong việc để các đơn vị chủ động thay đổi một số các tham số đơn giản phục vụ công tác điều hành trong ca trực) ương tự với tất cả các tham số của các loại Queue khác nhau trên hệ thống (Thoại, chat, mail, video...), Queue in/out</td>
      <td></td>
    </tr>
    <tr>
      <td>9.104</td>
      <td>Cấu hình queue Callout</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.105</td>
      <td>Cấu hình cuộc gọi nhỡ</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.106</td>
      <td>Cấu hình định tuyến thông minh</td>
      <td>Có thể cấp quyền cho trưởng ca thực hiện theo từng đơn vị, từng công ty</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.107</td>
      <td>Các báo cáo thống kê được phân quyền từng báo cáo, từng đầu số và phân quyền xuất các định dang sau. được chia làm các 3 dạng xuất báo cáo: - Xuất file excel không mã hoá số thuê bao - Xuất file excel mã hoá số TB - Xuất pdf</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.108</td>
      <td>Các báo cáo thống kê được phân quyền từng báo cáo, từng đầu số có 2 loại báo cáo - Mã hoá số TB - Không mã hoá số TB</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.109</td>
      <td>Báo cáo thống kê đăng kí dịch vụ qua IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.110</td>
      <td>-map ds user gọi ra trên queue gọi ra</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.111</td>
      <td>Cho phép hiển thị avatar của KH trên các queue MXH</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9.112</td>
      <td>Ưu tiên hiển thị ảnh avatar với các kênh không phải MXH như thoại, email</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Phân hệ Monitor</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10.1</td>
      <td>Kênh chat</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>







<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10.1.2</td>
      <td>Báo cáo chat</td>
      <td>-Báo cáo chỉ số kênh Chat+MXH theo ngày, múi giờ: + Lấy dữ liệu các kênh trên hệ thống Econtact. + Nội dung báo cáo bao gồm: Lưu lượng đầu vào; Lưu lượng tiếp nhận; Lưu lượng tiếp nhận trong hạn; Tỷ lệ kết nối; Tỷ lệ phản hồi trong hạn; Thời gian trả lời trung bình (áp dụng với kênh chat).</td>
      <td>-Báo cáo chỉ số kênh Chat+MXH theo ngày, múi giờ: + Lấy dữ liệu các kênh trên hệ thống Econtact. + Nội dung báo cáo bao gồm: Lưu lượng đầu vào; Lưu lượng tiếp nhận; Lưu lượng tiếp nhận trong hạn; Tỷ lệ kết nối; Tỷ lệ phản hồi trong hạn; Thời gian trả lời trung bình (áp dụng với kênh chat).</td>
    </tr>
    <tr>
      <td>10.1.3</td>
      <td>Báo cáo chỉ số kênh</td>
      <td>-Báo cáo chỉ số kênh Chat+MXH theo ngày, múi giờ: + Lấy dữ liệu các kênh trên hệ thống Econtact. + Nội dung báo cáo bao gồm: Lưu lượng đầu vào; Lưu lượng tiếp nhận; Lưu lượng tiếp nhận trong hạn; Tỷ lệ kết nối; Tỷ lệ phản hồi trong hạn; Thời gian trả lời trung bình (áp dụng với kênh chat).</td>
      <td>-Báo cáo chỉ số kênh Chat+MXH theo ngày, múi giờ: + Lấy dữ liệu các kênh trên hệ thống Econtact. + Nội dung báo cáo bao gồm: Lưu lượng đầu vào; Lưu lượng tiếp nhận; Lưu lượng tiếp nhận trong hạn; Tỷ lệ kết nối; Tỷ lệ phản hồi trong hạn; Thời gian trả lời trung bình (áp dụng với kênh chat).</td>
    </tr>
  </tbody>
</table>

# Public_442

<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10.2.1</td>
      <td>View được tỉ lệ kết nối của tất cả các kênh ( thoại + econtact)</td>
      <td>Hiện đang giám sát dựa trên Agent desktop + CCMS + KPI online. Veiw đc các thông tin sau: - Biểu đồ TLKN, hiển thị: (1) Lưu lượng CG theo khoảng giờ và lũy kế ngày vào ACD, BOT (Bot tách riêng chỉ gặp BOT và gặp BOT chuyển agent), Tất cả. (2) Target KPI, --> Hiển thị theo queue - Veiw đc các thông số trên Agent desktop, các tab: + Giám sát queue (Tổng CG vào, CG chờ, CG trả lời, Ag chính/phụ, Các thông tin khác đã có trên Giám sát queue + Tìm kiếm trạng thái agent + Thống kê trạng thái CG và ĐTV (hiển thị theo đối tác, theo tổng đài: ready, not ready, ringing..., tổng) + Các tiện ích khác:</td>
      <td>Vấn đề: - Trùng Trạng thái Agent - Thông tin hệ thống (ít dùng) giống thông tin trong Giám sát Queue 1. Yêu cầu nghiệp vụ - Giám sát queue nhìn thông tin theo queue (không chia nhỏ đến đối tác + khu vực) - Cho phép phân cấp ĐTV theo nhóm, theo khu vực. Phân cấp máy tính (Địa chỉ MAC). Gán người quản lý cho cácc nhóm - View đc các thông số trên Agent desktop, các tab: + Giám sát queue (Tổng CG vào, CG chờ, CG trả lời, Ag chính/phụ, Các thông tin khác đã có trên Giám sát queue + Tìm kiếm trạng thái agent + Thống kê trạng thái CG và ĐTV (hiển thị theo đối tác, theo tổng đài: ready, not ready, ringing..., tổng) - Hiển thị biểu đồ giám sát theo khu : KPI, chỉ số (%), lưu lượng (số tuyệt đối), bảng chi tiết số liệu - Cấu hình KPI : Cấu hình thông tin hiển thị biểu đồ và số liệu theo kênh cố định, di động, theo khu vực, khoảng thời gian và thể loại...</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Quản lý queue (gán queue thủ công), Trạng thái CG (dùng để nghe line), Chat, Gọi ra ngoài (hiện gọi ra trên bccs) => Check đưa sang mục nào + Tiện ích của Giám sát: Nghe online, Gán CG, Nghe online CG ra + Tab không dùng: Trạng thái ag (giống tìm kiếm trạng thái ag), Thông tin HT (giống giám sát queue)</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10.2.2</td>
      <td>SMS báo cáo chỉ số tự động theo múi giờ</td>
      <td>Tham khảo tài liệu KPI Monitor: - Cho phép cấu hình template tin nhắn, xem/thêm/sửa/xóa template tin nhắn - Tự động nhắn tin theo giờ/ngày --> Cho phép ng dùng setup đc các khung giờ nhắn tin (vd: Ngày N lúc 8h nhắn báo cáo ngày N-1 từ 00h-23h59) - Cho phép cấu hình ngưỡng chỉ số cảnh báo - Gửi tin nhắn: Tạo/xem/sửa/xóa nhóm SMS; Tính toán chỉ số tự động, Tích hợp thêm tính năng khác, Gửi tin...</td>
      <td>- Cho phép cấu hình template tin nhắn, xem/thêm/sửa/xóa template tin nhắn: bổ sung cấu thời gian so sánh (option so sánh số liêu VD: cùng kỳ tuần trước, tháng trước, quý trước, năm trước) - Tự động nhắn tin theo giờ/ngày --> Cho phép ng dùng setup đc các khung giờ nhắn tin (vd: Ngày N lúc 8h nhắn báo cáo ngày N-1 từ 00h-23h59) - Cho phép cấu hình ngưỡng chỉ số cảnh báo - Gửi tin nhắn: Tạo/xem/sửa/xóa nhóm SMS; Tính toán chỉ số tự động, Tích hợp thêm tính năng khác, Gửi tin theo nhóm nhận SMS - Tạo nhóm nhận tin nhắn: Import người dùng vào nhóm tin nhắn - Cho phép cấu hình các tham số: Thời gian nhắn,</td>
    </tr>
    <tr>
      <td>10.2.3</td>
      <td>SMS báo cáo chỉ số chủ động theo múi giờ</td>
      <td>Tham khảo tài liệu KPI Monitor => SMS báo cáo (Tương tự SMS mục 11.2 => Ng dùng cấu hình tay</td>
      <td>- Người dùng cấu hình thủ công sms cảnh báo chỉ số - Gộp vào 2 chức năng SMS báo cáo tự động và chủ động và một màn hình cấu hình - Với kênh trực tuyến: Bỏ sms tự động</td>
    </tr>
    <tr>
      <td>10.2.4</td>
      <td>SMS cảnh báo chỉ số theo ngưỡng nghẽn</td>
      <td>Tham khảo tài liệu KPI Monitor Tương tự mục 11.2</td>
      <td>- Người dùng cấu hình thủ công sms cảnh báo theo ngưỡng nghẽn - Mong muốn bổ sung phẩn thay đổi cấu hình các cấp</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10.2.5</td>
      <td>Báo cáo chỉ số cuộc gọi theo ngày theo giờ</td>
      <td>- Tham khảo tài liệu KPI Monitor: Báo cáo theo giờ, theo ngày, Chi tiết theo múi giờ - Gửi kèm nội dung word chi tiết</td>
      <td>- Bổ sung lấy dữ liệu các kênh (bổ sung các kênh) Hiện tại đang lấy dữ liệu kênh hệ thống báo cáo, CCMS, IPCC CG008 - Lấy dữ liệu cuộc gọi CG002 - Đang bắt buộc lấy từng kênh (bổ sung chọn danh sách kênh và ra dữ liệu ra từng kênh không ra số tổng)</td>
    </tr>
    <tr>
      <td>10.2.6</td>
      <td>Báo cáo so sánh chỉ số theo ngày, theo giờ giữa ngày 2 ngày được chọn</td>
      <td>1. Lưu lại thông tin cuộc gọi - Lưu lại thông tin cuộc gọi - Tính toán các chỉ số cuộc gọi theo ngày, giờ 2. So sánh chỉ số cuộc gọi giữa 2 ngày được chọn 3. Phân quyền: - Cho phép admin so sánh chỉ số cuộc gọi giữa 2 ngày được chọn</td>
      <td>1. Lưu lại thông tin cuộc gọi - Lưu lại thông tin cuộc gọi: Thông tin cuộc gọi vào, gặp ĐTV, rớt (do KH, do hệ thống), KH tự ngắt => tỷ lệ kết nối thành công đến ĐTV, tỷ lệ rớt, tỷ lệ ngắt... - Tính toán các chỉ số cuộc gọi theo ngày, giờ: chọn từ giờ đến giờ, ngày 2. So sánh chỉ số cuộc gọi giữa 2 ngày được chọn</td>
    </tr>
  </tbody>
</table>











<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10.2.9</td>
      <td>Cấu hình kênh/ nhóm kênh hiển thị</td>
      <td>- Cấu hình kênh hiển thị (Thêm/ Sửa/ Xóa/ Cập nhật) - Cấu hình nhóm kênh hiển thị (Thêm/ Sửa/ Xóa/ Cập nhật)</td>
      <td>Chức năng đăng có (CN: phân quyền, phân quyền Monitor)</td>
    </tr>
    <tr>
      <td>10.2.10</td>
      <td>cấu hình Danh sách kênh/nhóm kênh để tạo nội dung gửi sms</td>
      <td>1.Cấu hình danh sách kênh để tạo nội dung SMS (Thêm mới, sửa, xóa) 2. Cấu hình danh sách nhóm kênh SMS (Thêm mới, sửa, xóa) 3.Xử lý luồng tạo nội dung gửi SMS từ danh sách kênh/ nhóm kênh</td>
      <td>Là chức năng SMS- Nhóm kênh trên hệ thống Monitor</td>
    </tr>
    <tr>
      <td>10.2.11</td>
      <td>cấu hình danh sách sdt nhận sms</td>
      <td>1. Cấu hình danh sách SDT nhận SMS - Thêm mới - sửa - Xóa 2.'Import danh sách số điện thoại nhận sms Tải file import lỗi</td>
      <td>Cho phép cấu hình danh sách sđt nhận sms</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10.2.12</td>
      <td>cấu hình cấp độ gửi sms theo từng danh sách</td>
      <td>1. Cấu hình cấp độ gửi sms theo từng danh sách - Thêm mới - sửa - Xóa 2. Xử lý gửi tin nhắn theo danh sách số điện thoại đã cấu hình</td>
      <td>Cho phép cấu hình cấp độ gửi sms theo từng danh sách</td>
    </tr>
    <tr>
      <td>10.2.13</td>
      <td>Cấu hình định nghĩa các loại cuộc gọi</td>
      <td></td>
      <td>Cho phép cấu hình định nghĩa loại cuộc gọi: Cuộc gọi nhiều lần, cuộc gọi đầu số lạ…</td>
    </tr>
    <tr>
      <td>10.2.14</td>
      <td>Quản lý account</td>
      <td></td>
      <td>Cho phép quản lý account</td>
    </tr>
    <tr>
      <td>10.3</td>
      <td>Kênh video call</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10.3.1</td>
      <td>View được tỉ lệ kết nối của tất cả các kênh ( thoại + econtact)</td>
      <td>Hiện đang giám sát dựa trên Agent desktop + CCMS + KPI online. Veiw đc các thông tin sau: - Biểu đồ TLKN, hiển thị: (1) Lưu lượng CG theo khoảng giờ và lũy kế ngày vào ACD, BOT (Bot tách riêng chỉ gặp BOT và gặp BOT chuyển agent), Tất cả. (2) Target KPI, --> Hiển thị theo queue - Veiw đc các thông số trên Agent desktop, các tab: + Giám sát queue (Tổng CG vào, CG chờ, CG trả lời, Ag chính/phụ, Các thông tin khác đã có trên Giám sát queue + Tìm kiếm trạng thái agent + Thống kê trạng thái CG và ĐTV (hiển thị theo đối tác, theo tổng đài: ready, not ready, ringing..., tổng) + Các tiện ích khác:</td>
      <td>Vấn đề: - Trùng Trạng thái Agent - Thông tin hệ thống (ít dùng) giống thông tin trong Giám sát Queue 1. Yêu cầu nghiệp vụ - Giám sát queue nhìn thông tin theo queue (không chia nhỏ đến đối tác + khu vực) - Cho phép phân cấp ĐTV theo nhóm, theo khu vực. Phân cấp máy tính (Địa chỉ MAC). Gán người quản lý cho cácc nhóm - View đc các thông số trên Agent desktop, các tab: + Giám sát queue (Tổng CG vào, CG chờ, CG trả lời, Ag chính/phụ, Các thông tin khác đã có trên Giám sát queue + Tìm kiếm trạng thái agent + Thống kê trạng thái CG và ĐTV (hiển thị theo đối tác, theo tổng đài: ready, not ready, ringing..., tổng) - Hiển thị biểu đồ giám sát theo khu : KPI, chỉ số (%), lưu lượng (số tuyệt đối), bảng chi tiết số liệu - Cấu hình KPI : Cấu hình thông tin hiển thị biểu đồ và số liệu theo kênh cố định, di động, theo khu vực, khoảng thời gian và thể loại...</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Quản lý queue (gán queue thủ công), Trạng thái CG (dùng để nghe line), Chat, Gọi ra ngoài (hiện gọi ra trên bccs) => Check đưa sang mục nào + Tiện ích của Giám sát: Nghe online, Gán CG, Nghe online CG ra + Tab không dùng: Trạng thái ag (giống tìm kiếm trạng thái ag), Thông tin HT (giống giám sát queue)</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10.3.2</td>
      <td>SMS báo cáo chỉ số tự động theo múi giờ</td>
      <td>Tham khảo tài liệu KPI Monitor: - Cho phép cấu hình template tin nhắn, xem/thêm/sửa/xóa template tin nhắn - Tự động nhắn tin theo giờ/ngày --> Cho phép ng dùng setup đc các khung giờ nhắn tin (vd: Ngày N lúc 8h nhắn báo cáo ngày N-1 từ 00h-23h59) - Cho phép cấu hình ngưỡng chỉ số cảnh báo - Gửi tin nhắn: Tạo/xem/sửa/xóa nhóm SMS; Tính toán chỉ số tự động, Tích hợp thêm tính năng khác, Gửi tin...</td>
      <td>- Cho phép cấu hình template tin nhắn, xem/thêm/sửa/xóa template tin nhắn: bổ sung cấu thời gian so sánh (option so sánh số liêu VD: cùng kỳ tuần trước, tháng trước, quý trước, năm trước) - Tự động nhắn tin theo giờ/ngày --> Cho phép ng dùng setup đc các khung giờ nhắn tin (vd: Ngày N lúc 8h nhắn báo cáo ngày N-1 từ 00h-23h59) - Cho phép cấu hình ngưỡng chỉ số cảnh báo - Gửi tin nhắn: Tạo/xem/sửa/xóa nhóm SMS; Tính toán chỉ số tự động, Tích hợp thêm tính năng khác, Gửi tin theo nhóm nhận SMS - Tạo nhóm nhận tin nhắn: Import người dùng vào nhóm tin nhắn - Cho phép cấu hình các tham số: Thời gian nhắn,</td>
    </tr>
    <tr>
      <td>10.3.3</td>
      <td>SMS báo cáo chỉ số chủ động theo múi giờ</td>
      <td>Tham khảo tài liệu KPI Monitor => SMS báo cáo (Tương tự SMS mục 11.2 => Ng dùng cấu hình tay</td>
      <td>- Người dùng cấu hình thủ công sms cảnh báo chỉ số - Gộp vào 2 chức năng SMS báo cáo tự động và chủ động và một màn hình cấu hình - Với kênh trực tuyến: Bỏ sms tự động</td>
    </tr>
    <tr>
      <td>10.3.4</td>
      <td>SMS cảnh báo chỉ số theo ngưỡng nghẽn</td>
      <td>Tham khảo tài liệu KPI Monitor Tương tự mục 11.2</td>
      <td>Hiện tại đang đảm bảo - Mong muốn bổ sung phẩn thay đổi cấu hình các cấp</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10.3.5</td>
      <td>Báo cáo chỉ số cuộc gọi theo ngày theo giờ</td>
      <td>- Tham khảo tài liệu KPI Monitor: Báo cáo theo giờ, theo ngày, Chi tiết theo múi giờ - Gửi kèm nội dung word chi tiết</td>
      <td>Đã có báo cáo - Bổ sung lấy dữ liệu các kênh (bổ sung các kênh) Hiện tại đang lấy dữ liệu kênh hệ thống báo cáo, CCMS, IPCC CG008 - Lấy dữ liệu cuộc gọi CG002 - Đang bắt buộc lấy từng kênh (bổ sung chọn danh sách kênh và ra dữ liệu ra từng kênh không ra số tổng)</td>
    </tr>
    <tr>
      <td>10.3.6</td>
      <td>Báo cáo so sánh chỉ số theo ngày, theo giờ giữa ngày 2 ngày được chọn</td>
      <td>1. Lưu lại thông tin cuộc gọi - Lưu lại thông tin cuộc gọi - Tính toán các chỉ số cuộc gọi theo ngày, giờ 2. So sánh chỉ số cuộc gọi giữa 2 ngày được chọn 3. Phân quyền: - Cho phép admin so sánh chỉ số cuộc gọi giữa 2 ngày được chọn</td>
      <td>1. Lưu lại thông tin cuộc gọi - Lưu lại thông tin cuộc gọi: Thông tin cuộc gọi vào, gặp ĐTV, rớt (do KH, do hệ thống), KH tự ngắt => tỷ lệ kết nối thành công đến ĐTV, tỷ lệ rớt, tỷ lệ ngắt... - Tính toán các chỉ số cuộc gọi theo ngày, giờ: chọn từ giờ đến giờ, ngày 2. So sánh chỉ số cuộc gọi giữa 2 ngày được chọn</td>
    </tr>
  </tbody>
</table>











<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10.3.9</td>
      <td>Cấu hình kênh/ nhóm kênh hiển thị</td>
      <td>- Cấu hình kênh hiển thị (Thêm/ Sửa/ Xóa/ Cập nhật) - Cấu hình nhóm kênh hiển thị (Thêm/ Sửa/ Xóa/ Cập nhật)</td>
      <td>Chức năng đăng có (CN: phân quyền, phân quyền Monitor)</td>
    </tr>
    <tr>
      <td>10.3.10</td>
      <td>cấu hình Danh sách kênh/nhóm kênh để tạo nội dung gửi sms</td>
      <td>1.Cấu hình danh sách kênh để tạo nội dung SMS (Thêm mới, sửa, xóa) 2. Cấu hình danh sách nhóm kênh SMS (Thêm mới, sửa, xóa) 3.Xử lý luồng tạo nội dung gửi SMS từ danh sách kênh/ nhóm kênh</td>
      <td>Là chức năng SMS- Nhóm kênh trên hệ thống Monitor</td>
    </tr>
    <tr>
      <td>10.3.11</td>
      <td>cấu hình danh sách sdt nhận sms</td>
      <td>1. Cấu hình danh sách SDT nhận SMS - Thêm mới - sửa - Xóa 2.'Import danh sách số điện thoại nhận sms Tải file import lỗi</td>
      <td>Cho phép cấu hình danh sách sđt nhận sms</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10.3.12</td>
      <td>cấu hình cấp độ gửi sms theo từng danh sách</td>
      <td>1. Cấu hình cấp độ gửi sms theo từng danh sách - Thêm mới - sửa - Xóa 2. Xử lý gửi tin nhắn theo danh sách số điện thoại đã cấu hình</td>
      <td>Cho phép cấu hình cấp độ gửi sms theo từng danh sách</td>
    </tr>
    <tr>
      <td>10.3.13</td>
      <td>Cấu hình định nghĩa các loại cuộc gọi</td>
      <td></td>
      <td>Cho phép cấu hình định nghĩa loại cuộc gọi</td>
    </tr>
    <tr>
      <td>10.3.14</td>
      <td>Quản lý account</td>
      <td></td>
      <td>Cho phép quản lý account</td>
    </tr>
    <tr>
      <td>10.4</td>
      <td>Email</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10.4.1</td>
      <td>Biểu đồ giám sát mail theo khung giờ</td>
      <td>Giám sát số lượng mail trong khung giờ</td>
      <td>Biểu đồ cột bao gồm các chỉ số - Cột 1: Số lượng mail nhận trong khung giờ. Bao gồm mail cần xử lý và mail bỏ qua - Cột 2: Mail hoàn thành: Số lượng mail hoàn thành trong khung giờ của các mail nhận trong khung giờ. Bao gồm trong hạn và quá hạn - Cột 3: Mail tạm đóng: Số lượng mail tạm đóng trong khung giờ của các mail nhận trong khung giờ. Bao gồm trong hạn và quá hạn - Cột 4: Mail chưa xử lý: Số lượng mail chưa xử lý trong khung giờ của các mail nhận trong khung giờ. Bao gồm trong hạn và quá hạn Cột 1 = Mail bỏ qua + Cột 2 + Cột 3 + Cột 4</td>
    </tr>
    <tr>
      <td>10.4.2</td>
      <td>Số liệu mail chưa xử lý và tạm đóng luỹ kế đến thời điểm hiện tại</td>
      <td></td>
      <td>Số liệu mail chưa xử lý (trong hạn và quá hạn) và tạm đóng (trong hạn và quá hạn) luỹ kế đến thời điểm hiện tại</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10.4.3</td>
      <td>8 Báo cáo theo các loại ĐTV, Loại mail, Loại KH, Hệ thống</td>
      <td></td>
      <td>8 Báo cáo theo các loại ĐTV, Loại mail, Loại KH, Hệ thống</td>
    </tr>
    <tr>
      <td>11</td>
      <td>Các chức năng liên quan đến kênh phi thoại</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.1</td>
      <td>Phân hệ email</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.1.1</td>
      <td>Xem nội dung email khách hàng gửi</td>
      <td></td>
      <td>- Chức năng cho phép Agent xem nội dung email khách hàng gửi khi được khi được giao xử lý Ticket Email. - Từ màn hình Danh sách Ticket, Agent click vào xem chi tiết 1 Ticket Email. Hệ thống hiển thị màn hình Ticket Detail Email, trong đó có hiển thị nội dung email khách hàng gửi đến.</td>
    </tr>
    <tr>
      <td>11.1.1.1</td>
      <td>Phản hồi email cho khách hàng</td>
      <td></td>
      <td>- Chức năng cho phép Agent trả lời email khách hàng - Trên màn hình Ticket Detail Email, Agent click vào “Phản hồi” tương ứng với email mà khách hàng gửi đến hệ thống ==> Hiển thị màn hình soạn thảo email</td>
    </tr>
    <tr>
      <td>11.1.1.2</td>
      <td>Chuyển tiếp email</td>
      <td></td>
      <td>Chuyển tiếp email cho một người khác</td>
    </tr>
    <tr>
      <td>11.1.1.3</td>
      <td>Chức năng tiếp nhận email</td>
      <td></td>
      <td>- Chức năng cho phép Agent forward email của khách hàng gửi đến tới 1 hay nhiều địa chỉ email bất kỳ - Trên màn hình Ticket Detail Email, Agent click vào “Chuyển tiếp” tương ứng với email mà khách hàng gửi đến hệ thống ==> Hiển thị màn hình Forward email</td>
    </tr>
    <tr>
      <td>11.1.1.4</td>
      <td>Tiếp nhận email qua nhiều địa chỉ email của khách hàng B2B (không giới hạn địa chỉ email)</td>
      <td>Một khách hàng B2B có thể có nhiều địa chỉ email tiếp nhận dịch vụ. Phục vụ được nhiều khách hàng B2B.</td>
      <td>1. Yêu cầu nghiệp vụ - Một khách hàng B2B có thể có nhiều địa chỉ email tiếp nhận dịch vụ. Phục vụ được nhiều khách hàng B2B. - Mỗi email được cấu hình vào 1 queue</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.1.1.5</td>
      <td>Phân vùng làm việc cho từng địa chỉ email tiếp nhận dịch vụ</td>
      <td>Mỗi địa chỉ email tiếp nhận dịch vụ có 1 inbox riêng.</td>
      <td>1. Yêu cầu nghiệp vụ - Mỗi địa chỉ email tiếp nhận dịch vụ có 1 queue riêng.</td>
    </tr>
    <tr>
      <td>11.1.1.6</td>
      <td>Phân vùng xử lý email cho nhân viên CSKH</td>
      <td>Một nhân viên CSKH có thể được phân vùng xử lý 1 inbox hoặc nhiều inbox</td>
      <td>1. Yêu cầu nghiệp vụ - Một nhân viên CSKH có thể được phân vùng xử lý 1 queue hoặc nhiều queue</td>
    </tr>
    <tr>
      <td>11.1.1.7</td>
      <td>Chức năng báo email mới</td>
      <td>Khi có Email mới, hệ thống eContact sẽ popup cửa sổ thông báo h ở góc cuối bên phải của màn hình (tương tự như thông báo từ Outlook) hoặc thông báo bằng âm thanh để NVCSKH nhận biết</td>
      <td>Popup thông báo đến người được phân phối Email</td>
    </tr>
    <tr>
      <td>11.1.2</td>
      <td>Chức năng xử lý email</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.1.2.1</td>
      <td>Chương trình có đầy đủ các tính năng xử lý email của ứng dụng Outlook như đọc, trả lời, chuyển tiếp, soạn thảo email, chỉnh sửa, đính kèm file. Các thao tác xử lý được thực hiện trực tiếp trên chương trình, không qua công cụ trung gian.</td>
      <td>Người dùng đọc thư gửi đến, soạn thư và chỉnh sửa thư trả lời, chuyển tiếp trực tiếp được thư cho các cá nhân, đơn vị khác, đính kèm và tải được các file đính kèm.</td>
      <td>1. Yêu cầu nghiệp vụ - Người dùng đọc thư gửi đến, soạn thư, chuyển tiếp trực tiếp được thư cho các cá nhân, đơn vị khác, đính kèm và tải được các file đính kèm. - Cho phép cấu hình dung lượng file đính kèm (gửi ra) theo mail - Khi soạn mail + Nếu tích chọn mail nội bộ => Hiển thị chữ ký cá nhân + Nếu khác nội bộ => Không hiển thị chữ ký cá nhân</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.1.2.2</td>
      <td>Thay đổi các trạng thái xử lý của email</td>
      <td>Hệ thống tự động chuyển trạng thái thư khi người dùng thao tác và xử lý thư: Thư chưa đọc, thư đã đọc, thư đã trả lời, thư đã xử lý. Người dùng có thể lựa chọn chuyển trạng thái của thư trong các trường hợp không cần trả lời lại thư khách hàng, tạo ghi chú để đánh dấu phân loại.</td>
      <td>1. Yêu cầu nghiệp vụ - Hệ thống tự động chuyển trạng thái thư khi người dùng thao tác và xử lý thư: Thư chưa đọc (màu), thư đã đọc (màu), thư đã trả lời (trạng thái), thư đã xử lý (trạng thái ticket). Người dùng có thể lựa chọn chuyển trạng thái của thư trong các trường hợp không cần trả lời lại thư khách hàng, phân loại phản ánh</td>
    </tr>
    <tr>
      <td>11.1.2.3</td>
      <td>Có chức năng bàn giao email và lịch sử bàn giao email.</td>
      <td>Người dùng thực hiện được bàn giao email của mình cho người khác, SUP thực hiện bàn giao giữa các nhân viên và lưu được lý do chuyển tiếp email. Nhân viên đọc được lịch sử bàn giao và lý do của việc bàn giao thư.</td>
      <td>1. Yêu cầu nghiệp vụ - Người dùng thực hiện được bàn giao email của mình cho người khác, lưu được lý do chuyển tiếp email. Nhân viên đọc được lịch sử bàn giao và lý do của việc bàn giao thư.</td>
    </tr>
    <tr>
      <td>11.1.2.4</td>
      <td>Có tính năng tạo lưu ý trong email, bàn giao thư từ user này sang user khác.</td>
      <td>Người dùng soạn được lưu ý và lưu vào mail khách gửi đến khi email đang cần theo dõi, đang chờ xử lý.</td>
      <td>1. Yêu cầu nghiệp vụ - Cho phép tạo lưu ý khi bàn giao mail từ user này sang user khác - Cho phép ghi chú riêng tư (chỉ người tạo nhìn thấy) và ghi chú công khai. Cho phép xem danh sách ghi chú</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.1.2.5</td>
      <td>Có tính năng tạo thư mới để gửi cho khách hàng</td>
      <td>Người dùng soạn và tạo được thư mới để gửi cho tập khách hàng nhất định từ các đầu email đã được cài đặt vào chương trình.</td>
      <td>1. Yêu cầu nghiệp vụ - Người dùng soạn và tạo được thư mới để gửi cho tập khách hàng nhất định từ các đầu email đã được cài đặt vào chương trình: Hàng loạt (import theo file) và đơn lẻ - Hàng loạt: Tạo nhiều mail cho 1 danh sách địa chỉ email - Đơn lẻ: Tạo 1 mail (1 hay nhiều địa chỉ trong to)</td>
    </tr>
    <tr>
      <td>11.1.2.6</td>
      <td>Dung lượng mail đính kèm</td>
      <td>Nâng dung lượng file đính kèm khi phản hồi mail tới KH: Hiện tại hệ thống chỉ cho phép gửi file đính kèm có dung lượng <5MB, tuy nhiên với những file mà BO ngửi đến KH có dung lượng lớn hơn 5MB nên sẽ không gửi được, NV CSKH phải tách thành nhiều file để gửi nhiều lần tới mail của KH => / Cần nâng dung lượng file đính kèm lên cao hơn (trên 20MB) để NVCSKH gửi mail phản hồi tới KH</td>
      <td>Nâng dung lượng file đính kèm khi phản hồi mail tới KH: Hiện tại hệ thống chỉ cho phép gửi file đính kèm có dung lượng <5MB, tuy nhiên với những file mà BO ngửi đến KH có dung lượng lớn hơn 5MB nên sẽ không gửi được, NV CSKH phải tách thành nhiều file để gửi nhiều lần tới mail của KH => / Cần nâng dung lượng file đính kèm lên cao hơn (trên 20MB) để NVCSKH gửi mail phản hồi tới KH</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.1.2.7</td>
      <td>Tính năng theo dõi các phản ánh chuyển BO trên ht</td>
      <td>Tính năng theo dõi các phản ánh chuyển BO trên ht. Xây dựng giao diện cho người dùng nhập loại khiếu nại của KH và thời gian xử lý tương ứng của các phản ánh nhập chuyển BO, hệ thống sẽ hiển thị thông báo khi phản ánh hết hạn hoặc quá hạn để người dùng chủ động vào cập nhật thông tin đóng phản ánh đúng hạn; Người quản trị được phép cấu hình thay đổi/thêm/bớt đầu mục nhập và thời gian tương ứng.</td>
      <td>- Chức năng tạo phản ánh trên eContact (cần Người quản trị được phép cấu hình thay đổi/thêm/bớt đầu mục nhập và thời gian tương ứng) hoặc BCCS - Cập nhật hạn phản ánh BO trên eContact (BCCS truyền sang) - Theo dõi hạn, trạng thái xử lý - Quá trình xử lý (VD:có thể mở link sang BCCS => Xem lịch sử xử lý phản ánh)</td>
    </tr>
    <tr>
      <td>11.1.2.8</td>
      <td>Tính năng gửi mail cho KH theo file:</td>
      <td>Tính năng gửi mail cho KH theo file: Hệ thống cho phép người dùng thao tác gửi Email cho KH theo file danh sách mail đính kèm, nhằm mục đích truyền thông, quảng cáo tùy thuộc từng giai đoạn của chiến dịch CSKH:</td>
      <td>Tính năng gửi mail cho KH theo file: Hệ thống cho phép người dùng thao tác gửi Email cho KH theo file danh sách mail đính kèm, nhằm mục đích truyền thông, quảng cáo tùy thuộc từng giai đoạn của chiến dịch CSKH:</td>
    </tr>
    <tr>
      <td>11.1.3</td>
      <td>Chức năng hiển thị</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.1.3.1</td>
      <td>Hiển thị đầy đủ các trường thông tin khi có email gửi đến chương trình</td>
      <td>Người dùng kiểm tra được các trường thông tin tương tác của khách hàng qua email trên màn hình hiển thị: email khách hàng, thời gian gửi đến, thời gian phải trả lời, subject, số thẻ hội viên, hạng thẻ hội viên</td>
      <td>1. Yêu cầu nghiệp vụ: - Người dùng kiểm tra được các trường thông tin tương tác của khách hàng qua email trên màn hình hiển thị: email khách hàng, thời gian gửi đến, thời gian phải trả lời (SLA), subject, các trường thông tin động - Các trường thông tin động: Đồng bộ/gọi API/Import</td>
    </tr>
    <tr>
      <td>11.1.3.2</td>
      <td>Hiển thị trạng thái của email trên chương trình</td>
      <td>Người dùng kiểm tra được tình trạng của email: Đã đọc, đã trả lời, đã xử lý nhưng không cần gửi thư, đã chuyển tiếp cho nhóm xử lý nghiệp vụ.</td>
      <td>- Tương tự trạng thái email</td>
    </tr>
    <tr>
      <td>11.1.3.3</td>
      <td>Hiển thị lịch sử trao đổi mail với KH</td>
      <td>Người dùng kiểm tra và đọc được loop trao đổi thư theo thứ tự thời gian xử lý trong một email.</td>
      <td>- Người dùng kiểm tra và đọc được loop trao đổi thư theo thứ tự thời gian xử lý trong một email. - Hiển thị luồng trao đổi mail</td>
    </tr>
    <tr>
      <td>11.1.3.4</td>
      <td>Hiển thị email gửi đến và gửi đi theo đầu email nhận</td>
      <td>Người dùng kiểm tra được số lượng, nội dung thư đã nhận, đã gửi theo đầu email nhận thư.</td>
      <td>- Xây dựng báo cáo thống kê mail vào, báo cáo mail ra (luồng chủ động)</td>
    </tr>
    <tr>
      <td>11.1.4</td>
      <td>Chức năng phân loại</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.1.4.1</td>
      <td>Nâng cấp tính năng nhập thông</td>
      <td>Cấu hình bộ nhập thống kê cho kênh email trên hệ thống : (1) Cần nâng cấp bổ sung thêm cấp 5 trường nhập thống kê; (2) Cập nhật bộ nhập thống kê mới lên hệ thống ; (3) Cấu hình trường nhập thống kê cho kênh Email - Cho phép phân quyền thêm bớt bộ nhập - Xây dựng cơ chế động bộ tự động sang BCCS</td>
      <td>Hiện tại nhập thống kê theo 4 cấp => Chuyển nhập thống kê theo 5 cấp Hệ thống eContact đã có chức năng nhập thống kê nhu cầu của KH theo 4 cấp tương tự như trên BCCS (đã cấu hình trên kênh Fanpage-MXH). Tuy nhiên bộ nhập đã cũ và không phù hợp với hiện tại (hiện có 5 cấp). Do đó: (1) Cần nâng cấp bổ sung thêm cấp 5 trường nhập thống kê; (2) Cập nhật bộ nhập thống kê mới lên hệ thống eContact; (3) Cấu hình trường nhập thống kê cho kênh Email.</td>
    </tr>
    <tr>
      <td>11.1.4.2</td>
      <td>Đồng bộ dữ liệu nhập thống kê trên hệ thống eContact sang hệ thống BCCS</td>
      <td>Sau khi NVCSKH cập nhật thông tin thống kê nhu cầu trên eContact, hệ thống có tính năng cho phép người dùng có thể đồng bộ dữ liệu nhập lên hệ thống BCCS (mục nhập thống kê). Import dữ liệu theo file.</td>
      <td>Hệ thống có tính năng cho phép người dùng có thể đồng bộ dữ liệu nhập lên hệ thống BCCS (mục nhập thống kê) Đồng bộ phân cấp (5 cấp nhập thống kê) Import dữ liệu theo file: Danh mục bộ nhập thống kê có thể tự định nghĩa được theo file Danh mục loại phản ánh đang được khai báo độc lập cả BCCS và IPCC. Để đồng bộ dữ liệu loại phản ánh ticket sang thì danh mục 2 bên phải đồng bộ</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.1.4.3</td>
      <td>Theo chủ đề.</td>
      <td>Người dùng tiếp nhận email gửi đến và kiểm tra nội dung email có thể chọn chủ đề email theo list chủ đề được cấu hình sẵn trong hệ thống.</td>
      <td>- Phân loại phản ánh email</td>
    </tr>
    <tr>
      <td>11.1.5</td>
      <td>Chức năng tìm kiếm</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.1.5.1</td>
      <td>Có tính năng tìm kiếm email theo các trường thông tin: địa chỉ email khách gửi đến, theo chủ đề, theo từ khóa trong nội dung, theo thời gian nhận, theo số thẻ hội viên</td>
      <td>Người dùng tìm kiếm được luồng email khách gửi đến, luồng email trao đổi với khách thông qua địa chỉ email khách gửi đến, chủ đề khách viết, theo một vài từ khóa trong nội dung, theo thời gian khách gửi đến, theo số thẻ hội viên.</td>
      <td>- Tìm kiếm theo nhiều tiêu chí: Người dùng tìm kiếm được luồng email khách gửi đến, luồng email trao đổi với khách thông qua địa chỉ email khách gửi đến, chủ đề khách viết, theo một vài từ khóa trong nội dung, theo thời gian khách gửi đến, theo số thẻ hội viên.</td>
    </tr>
    <tr>
      <td>11.1.5.2</td>
      <td>Lọc email nhanh theo user, thời gian, chủ đề, wrap up code, trạng thái để theo dõi và xử lý theo thứ tự.</td>
      <td>Agent vào trang Supervisor và tìm kiếm theo các nội dung: user, thời gian, chủ đề, wrap up code, trạng thái</td>
      <td>- Chức năng filter theo các tiêu chí: user (ĐTV đang được giao), thời gian, chủ đề, wrap up code, trạng thái</td>
    </tr>
    <tr>
      <td>11.1.5.3</td>
      <td>Nhận biết email trùng</td>
      <td>Trong quá trình xử lý agent sẽ chủ động phát hiện được email gửi trùng (tiêu chí trùng sẽ do IT cấu hình trên hệ thống) để chọn trả lời hoặc không</td>
      <td>- Cho phép lọc trùng email theo các thuộc tính - Cho phép cấu hình thời gian quét, luật check trùng</td>
    </tr>
  </tbody>
</table>

# Public_442

<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.1.6.1</td>
      <td>Hệ thống cảnh báo được thời gian Email sắp hết hạn xử lý, đã hết hạn xử lý dựa trên thời gian khách gửi thư đến trong số thư được nhận và trong quese</td>
      <td>K T Agent có thể tự xem thư nào sắp hết hạn xử lý, thư nào đã hết hạn xử lý trong số thư nhận được hoặc thư trong Q để biết thời hạn phải xử lý cho đúng hạn hoặc có cảnh báo từ hệ thống. hi phản ánh còn 10 phút ht sẽ popup thông báo lên màn hình phản ánh sắp hết hạn, và đến khi u hết hạn, hệ thống sẽ tiếp tục popup một lần nữa báo đỏ lên cảnh báo cho người dùng i phản ánh đã quá hạn hời gian cảnh báo được cấu hình theo từng queue email riêng</td>
      <td>- Cảnh báo sắp hết hạn: Agent có thể tự xem thư nào sắp hết hạn xử lý, thư nào đã hết hạn xử lý trong số thư nhận được hoặc thư trong queue để biết thời hạn phải xử lý cho đúng hạn hoặc có cảnh báo từ hệ thống. - Cho phép filter mail sắp hết hạn theo thời gian từ đến: Ví dụ email sắp hết hạn trong 20 phút đến 30 phút - Cấu hình màu email sắp hết hạn theo từng email dịch vụ - Cảnh báo sắp hết hạn hoặc quá hạn cho TVV (người được giao xử lý email) và Giám sát viên (hiển thi tất cả cảnh báo) (popup hoặc noti hoặc bảng thông báo) - Cho phép cấu hình người giám sát email (thêm, xoá)</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.1.6.2</td>
      <td>Nhận diện từ khóa có dấu hiệu tiêu cưc, từ khóa chuyên ngành</td>
      <td>Chương trình có thể tự động tìm kiếm và nhận diện từ khóa tiêu cực, từ khóa chuyên ngành… theo bộ từ khóa được cài đặt trong hệ thống để gắn vào email của khách, giúp nhân viên nhận diện và xử lý theo thứ tự ưu tiên</td>
      <td>- Tích hợp với API KGM</td>
    </tr>
    <tr>
      <td>11.1.6.3</td>
      <td>Tính năng thông báo khi có : Email đặc biệt gửi đến</td>
      <td>Hệ thống gửi SMS tới các số TB được cấu hình sẵn trên hệ thống khi KH gửi Email tới Email và có CC/BCC tới các Email đặc biệt (Ví dụ: Email của Ban Tổng Giám đốc, : Hiệp hội người tiêu dùng, Email tới các đơn vị báo chí...). Danh sách Email đặc biệt sẽ do TT CSKH đề xuất. Hệ thống cho phép người quản trị có thể thay đổi/thêm/bớt số điện thoại người nhận SMS, danh sách Email đặc biệt.</td>
      <td>- Nếu có mail đặc biệt nằm trong: To; BCC, CC thì gửi sms đến danh sách thuê bao được cấu hình - Cấu hình sms cảnh báo cho từng mail dịch vụ</td>
    </tr>
    <tr>
      <td>11.1.7</td>
      <td>Chức năng lưu trữ</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>







<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.1.8.1</td>
      <td>Chia email ưu tiên cho user xử lý thư trước đó của khách</td>
      <td>Hệ thống chia mail đều theo vòng lặp theo thứ tự ưu tiên: cho người dùng đã xử lý gần nhất email của khách nếu người dùng đang ở trạng thái sẵn sàng sau đó chia đều mail còn lại cho số lượng nhân viên được khai báo trong ca làm việc</td>
      <td>Hệ thống chia mail đều theo vòng lặp theo thứ tự ưu tiên: cho người dùng đã xử lý gần nhất (người xử lý cuối cùng) email của khách nếu người dùng đang ở trạng thái sẵn sàng sau đó chia đều mail còn lại cho số lượng nhân viên được khai báo trong ca làm việc</td>
    </tr>
    <tr>
      <td>11.1.8.2</td>
      <td>Chia email gửi đến theo nhóm user/user được cài đặt/chỉ định.</td>
      <td>Hệ thống nhận diện và cài đặt được một số phân loại email gửi đến nhóm/cá nhân nhân viên được chỉ định xử lý mà không tuân theo nguyên tắc chia mail đều.</td>
      <td>Hệ thống nhận diện và cài đặt được một số phân loại email gửi đến nhóm/cá nhân nhân viên được chỉ định xử lý mà không tuân theo nguyên tắc chia mail đều.</td>
    </tr>
    <tr>
      <td>11.1.8.3</td>
      <td>Chia email theo trạng thái của nhân viên được khai báo</td>
      <td>Hệ thống chia mail đều theo vòng lặp cho số lượng nhân viên được khai báo có tình trạng sẵn sàng trong ca làm việc.</td>
      <td>Hệ thống chia mail đều theo vòng lặp cho số lượng nhân viên được khai báo có tình trạng sẵn sàng trong ca làm việc. Giống như hiện tại đang xoay vòng</td>
    </tr>
    <tr>
      <td>11.1.9</td>
      <td>Chức năng vận hành</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>















<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.2.4</td>
      <td>Chức năng phân luồng xử lý</td>
      <td>Khi có thông tin cần xử lý, hệ thống sẽ có thông báo có tin nhắn mới (có cảnh báo), nhân viên tích vào mục cần xử lý tương ứng và lần lượt xử lý các tương tác theo thứ tự thời gian. Trong ca làm việc có từ 2 người trở lên cùng tham gia xử lý, để tránh trả lời trùng, một khi nhân viên nhấn vào bài viết/inbox/comment cần xử lý thì item này sẽ bị khóa lại ở ở các user còn lại. Trong trường hợp sau 5 phút người xử lý chưa xử lý xong items, hệ thống mở khóa chuyển sang nhân viên khác xử lý hoặc nhân viên khác có thể chủ động mở khóa để xử lý.</td>
      <td>- Khi có thông tin cần xử lý, hệ thống sẽ có thông báo có tin nhắn mới (có cảnh báo), nhân viên tích vào mục cần xử lý tương ứng và lần lượt xử lý các tương tác theo thứ tự thời gian. Trong ca làm việc có từ 2 người trở lên cùng tham gia xử lý, để tránh trả lời trùng, một khi nhân viên nhấn vào bài viết/inbox/comment cần xử lý thì item này sẽ bị khóa lại ở ở các user còn lại. - Luồng chat: Nếu không có ĐTV tiếp nhận => Rớt. Nếu có ĐTV tiếp nhận mà không phản hồi => Cảnh báo -Sau 5 phút không phản hồi chat + không hold hoặc offline => Transfer (Bỏ nội dung này vì Giám sát có thể transfer thủ công 12.2.1.3) - KH chat bị rớt => Tái phân bổ. Khi phân bổ lại từ thời điểm rớt đến thời điểm quét. Nếu KH đã chat lại và được tiếp nhận thì không tái phân bổ nữa - Áp dụng cho định danh: Với TH chat rớt, kh chat tiếp lên => note hội thoại trc (nhỡ) + xem lịch sử + không tái phân bổ chat nhỡ - Cấu hình được tỷ lệ % ĐTV rảnh tiếp nhận phiên chat phân bổ lại để đảm bảo tỷ lệ ĐTV tiếp nhận KH online - Duration phân bổ = 24h kể từ lúc KH phản ánh (Cấu hình cho inbox từng page) => Áp dụng cho chat, cmt, email</td>
    </tr>
    <tr>
      <td>11.2.5</td>
      <td>- Giám sát: cho phép Transfer chat sang ĐTV khác</td>
      <td></td>
      <td>- Giám sát: cho phép Transfer chat sang ĐTV khác</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.2.6</td>
      <td>Các tác vụ xử lý</td>
      <td>1.Thêm tính năng ngắt dòng (xuống dòng trong 1 lần tương tác) khi NVCSKH phản hồi thông tin tới KH (kênh Chat) -Hiện tại khi NVCSKH tương tác/phản hồi thông tin tới KH qua đoạn hội thoạt chat chưa có tính năng ngắt dòng NVCSKH không thực hiện được việc tách ý trong cùng 1 nội dung tương tác Bổ sung thêm tính năng ngắt dòng trong 1 lần tương tác.</td>
      <td>1.Thêm tính năng ngắt dòng (xuống dòng trong 1 lần tương tác) khi NVCSKH phản hồi thông tin tới KH (kênh Chat) -Hiện tại khi NVCSKH tương tác/phản hồi thông tin tới KH qua đoạn hội thoạt chat chưa có tính năng ngắt dòng NVCSKH không thực hiện được việc tách ý trong cùng 1 nội dung tương tác Bổ sung thêm tính năng ngắt dòng trong 1 lần tương tác.</td>
    </tr>
    <tr>
      <td>11.2.7</td>
      <td>Comment/bài viết: Trả lời, Nhắn tin, Thích, Theo dõi, Xóa, Ẩn, Trung lập, gắn nhãn phân loại, bỏ qua, phân user xử lý.</td>
      <td>Nhân viên tuân thủ quy trình làm việc, nội dung tương tác để lựa chọn các tác vụ xử lý đã nêu.</td>
      <td>- Comment/bài viết: Trả lời, Nhắn tin, Thích, Theo dõi, Xóa, Ẩn, Trung lập, gắn nhãn phân loại, bỏ qua, phân user xử lý.</td>
    </tr>
    <tr>
      <td>11.2.8</td>
      <td>Inbox: Bỏ qua, trả lời, gắn nhãn phân loại, thả icon.</td>
      <td>Nhân viên tuân thủ quy trình làm việc, nội dung tương tác để lựa chọn các tác vụ xử lý đã nêu.</td>
      <td>- Chat: Bỏ qua, trả lời, gắn nhãn phân loại, thả icon.</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.2.9</td>
      <td>Chức năng nhập thống kê</td>
      <td>Cấu hình bộ nhập thống kê cho các kênh trên hệ thống : (1) Cần nâng cấp bổ sung thêm cấp 5 trường nhập thống kê; (2) Cập nhật bộ nhập thống kê mới lên hệ thống ; (3) Cấu hình trường nhập thống kê cho các kênh - Cho phép phân quyền thêm bớt bộ nhập - Xây dựng cơ chế động bộ tự động sang BCCS</td>
      <td>Cấu hình bộ nhập thống kê cho các kênh trên hệ thống : (1) Cần nâng cấp bổ sung thêm cấp 5 trường nhập thống kê; (2) Cập nhật bộ nhập thống kê mới lên hệ thống ; (3) Cấu hình trường nhập thống kê cho các kênh - Cho phép phân quyền thêm bớt bộ nhập - Xây dựng cơ chế động bộ tự động sang BCCS</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.2.10</td>
      <td>Chức năng ticket (tham khảo phần 6.1)</td>
      <td>Giao lại ticket thủ công cho NVCSKH Thêm tính năng đánh giá ticket trong hạn/ngoài hạn trong báo cáo Nâng cấp tính năng đóng ticket hàng loạt Popup thông báo khi có ticket mới được giao Quyền ẩn/xóa/sửa ticket của BO</td>
      <td>- 2 3 1. Hiện tại khi Giám sát thực hiện giao lại ticket thủ công cho NVCSKH gặp tình trạng: hệ thống Econtact hiển thị toàn bộ NVCSKH bao gồm cả NVCSKH đang online (NVCSKH đi làm) và offline (NVCSKH không đi làm) dẫn đến tình trạng nhầm lẫn trong quá trình giao (hình ảnh bên dưới). Mong muốn nâng cấp: + Ưu tiên hiển thị danh sách các NVCSKH đang online lên đầu. + Có ký hiệu nhận biết để phân biệt giữa NVCSKH đang online và offline. . '-Hiện tại trong báo cáo ticket đã có thông tin về tổng thời gian NVCSKH phản hồi, tuy nhiên trong cột Tiến độ vi phạm chưa có mục đánh giá trong hạn, quá hạn để phục vụ công tác kiểm soát của BO. -Mong muốn nâng cấp: cột Tiến độ vi phạm trả dữ liệu bao gồm: (1) Trong hạn, (2) Quá hạn, (3) Không đánh giá. Cụ thể: vDữ liệu trong hạn được đánh giá như sau: üTrong khung giờ từ 6h30-22h hàng ngày (ngày n): các trường hợp NVCSKH giải đáp và phản hồi lại KH, thời gian NV CSKH phản hồi nhỏ hơn hoặc bằng 30 phút (Cột Tổng thời gian TVV phản hồi) Đánh giá: Trong hạn. üTrong khung giờ từ 22h ngày hôm trước (ngày n)-6h30 ngày hôm sau (ngày n+1): các trường hợp NV CSKH giải đáp và phản hồi lại KH trước 08h AM của ngày n+1 Đánh giá: Trong hạn. vDữ liệu quá hạn được đánh giá như sau: üTrong khung giờ từ 6h30-22h hàng ngày (ngày n): các trường hợp NV CSKH giải đáp và phản hồi lại KH, thời gian NV CSKH phản hồi lớn hơn 30 phút (Cột Tổng thời gian TVV phản hồi) Đánh giá: Quá hạn. üTrong khung giờ từ 22h ngày hôm trước (ngày n)-6h30 ngày hôm sau (ngày n+1): các trường hợp NV CSKH giải đáp và phản hồi lại KH sau 08h AM của ngày n+1 Đánh giá: Quá hạn. vDữ liệu KĐG được đánh giá như sau: các trường hợp NVCSKH tích bỏ qua ticket, không giải đáp Đánh giá: Không đánh giá. Hình ảnh chi tiết các cột trong báo cáo . Nâng cấp tính năng đóng ticket hàng loạt -Đối với tính năng đóng ticket hàng loạt: hiện tại hệ thống Econtact chỉ hỗ trợ người dùng</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>- 4 đóng toàn bộ ticket hoặc đóng 1 phần ticket (theo khoảng thời gian từ ngày tới ngày) Chưa hỗ trợ đóng ticket hàng loạt theo bài post hoặc từ khóa… (như hình ảnh bên dưới). ðĐối với các bài post dạng livestream hoặc minigame, số lượng ticket đẩy về hệ thống rất lớn, phần lớn là các ticket không cần giải đáp Người dùng phải thực hiện đóng thủ công trên hệ thống, ảnh hưởng tới tiến độ xử lý đối với các ticket khác. Mong muốn nâng cấp: Bổ sung thêm tính năng đóng ticket hàng loạt theo bài post (theo mã bài post, link bài post) hoặc từ khóa. Người sử dụng có thể chọn từng bài post, hoặc nhập từ khóa tra cứu Hệ thống sẽ hiển thị toàn bộ các ticket có liên quan để người dùng có thể thực hiện đóng ticket. & 5. Xem trong PYC mã IBM đính kèm</td>
    </tr>
  </tbody>
</table>















<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>trường hợp khiếu nại do không xác nhận được SĐT mà KH cung cấp có chính xác hay không?</td>
      <td></td>
    </tr>
  </tbody>
</table>











<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.2.26</td>
      <td>Các tính năng tích hợp với FaceBook</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.2.27</td>
      <td>Quản trị facebook page</td>
      <td></td>
      <td>- Chức năng cho phép người dùng là quản trị hệ thống thực hiện tích hợp page của doanh nghiệp vào hệ thống với các thông tin sau: + Tên trang Facebook + Mô tả + Đường link - Cho phép thêm, sửa xóa thông tin tích hợp</td>
    </tr>
    <tr>
      <td>11.2.28</td>
      <td>Chức năng Ticket facebook.</td>
      <td></td>
      <td>- Chức năng cho phép sau khi đã tích hợp 1 page vào hệ thống thành công, với tất cả các comments/bài post khách hàng để lại trên page của DN - Hệ thống tiếp nhận và tạo thành ticket trên hệ thống IPCC. - Trên chức năng quản lý Tickets, chọn kênh Facebook : người dùng có thể thấy danh sách các tickets</td>
    </tr>
    <tr>
      <td>11.2.29</td>
      <td>Chức năng chat facebook.</td>
      <td></td>
      <td>Khách hàng vào page của doanh nghiệp, gửi chat Inbox page của doạnh nghiệp. Hệ thống get chat và tạo thành hội thoại trên IPCC, phân bổ chat đến tư vấn viên đủ điều kiện</td>
    </tr>
    <tr>
      <td>11.2.30</td>
      <td>Báo cáo facebook</td>
      <td></td>
      <td>- Bổ sung 1 báo cáo facebook với thông tin tìm kiếm: thời gian tiếp nhận, thời gian xử lý, trạng thái, người gửi - Cho phép xuất dữ liệu ra file excel</td>
    </tr>
    <tr>
      <td>11.2.31</td>
      <td>Báo cáo chat</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.2.32</td>
      <td>Báo cáo chat tổng hợp</td>
      <td></td>
      <td>- Bổ sung 1 báo cáo tổng hợp với thông tin tìm kiếm: thời gian tiếp nhận, thời gian xử lý, TVV - Cho phép xuất dữ liệu ra file excel</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.2.33</td>
      <td>Báo cáo chat theo phiên Báo cáo chat theo hội thoại</td>
      <td></td>
      <td>- Bổ sung 1 báo cáo tổng hợp với thông tin tìm kiếm: thời gian tiếp nhận, thời gian xử lý, TVV - Cho phép xuất dữ liệu ra file excel</td>
    </tr>
    <tr>
      <td>11.2.34</td>
      <td></td>
      <td></td>
      <td>- Bổ sung 1 báo cáo tổng hợp với thông tin tìm kiếm: thời gian tiếp nhận, thời gian xử lý, TVV - Cho phép xuất dữ liệu ra file excel</td>
    </tr>
    <tr>
      <td>11.2.35</td>
      <td>IPCC CLOUD BAMBOO - CHAT ON WEB PORTAL</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.2.36</td>
      <td>Cấu hình Domain Chat</td>
      <td></td>
      <td>- Chức năng cho phép khai báo thông tin Chung của Trang web, bao gồm: Tên, Mô tả</td>
    </tr>
    <tr>
      <td>11.2.37</td>
      <td>Tab Thông tin web</td>
      <td></td>
      <td>- Cho phép cập nhật thông tin Tên, mô tả trang web</td>
    </tr>
    <tr>
      <td>11.2.38</td>
      <td>Tab Quản lý dịch vụ</td>
      <td></td>
      <td>- Cho phép thêm/sửa/xóa dịch vụ cho trang web. Mặc định khi thêm mới 1 domain, hệ thống sẽ tự sinh 1 dịch vụ. Admin cũng có thể khai báo thêm dịch vụ</td>
    </tr>
    <tr>
      <td>11.2.39</td>
      <td>Tab Cấu hình hiển thị</td>
      <td></td>
      <td>- Cho phép cấu hình các thông tin hiển thị trên cửa sổ chat như: Tiêu đề, Màu sắc, Nhân viên hỗ trợ, Ngôn ngữ</td>
    </tr>
    <tr>
      <td>11.2.40</td>
      <td>Tab Nhập thông tin</td>
      <td></td>
      <td>- Cho phép cấu hình 1 số thông tin như: Lời chào khách hàng khi khách hàng bắt đầu chat, tin nhắn thông báo giao dịch chat kết thúc, thời gian cảnh báo khi khách hàng để quá lâu không phản hồi Agent, tin nhắn cảnh báo khi khách hàng để quá lâu không phản hồi Agent</td>
    </tr>
    <tr>
      <td>11.2.41</td>
      <td>Tab Script Nhúng</td>
      <td></td>
      <td>- Cho phép xem Script của Domain do hệ thống tự sinh ra. Khi triển khai kênh chat trên Web, cần nhúng Script này vào trang web để hiển thị được Domain</td>
    </tr>
    <tr>
      <td>11.2.42</td>
      <td>Luồng chat</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.2.43</td>
      <td>Gán danh sách agents vào queue chat</td>
      <td></td>
      <td>- Với mỗi dịch vụ của domain, chương trình tự động sinh một queue chat tương ứng. Admin hoặc giám sát viên của doanh nghiệp cần gán agents vào queue để tiếp nhận và xử lý chat</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11.2.44</td>
      <td>Khách hàng gửi yêu cầu chat</td>
      <td></td>
      <td>- Khách hàng có thể gửi yêu cầu chat đến hệ thống từ kênh web chat</td>
    </tr>
    <tr>
      <td>11.2.45</td>
      <td>Hiển thị thông báo có chat đến</td>
      <td></td>
      <td>- Chức năng cho phép hiển thị thông báo tới Agent khi có giao dịch chat phân bổ đến - Khi có giao dịch chat (KH chat từ web), hệ thống sẽ thực hiện tìm kiếm Agent rảnh rỗi kênh chat để phân bổ đến Agent. Agent được phân bổ giao dịch chat, màn hình sẽ hiển thị thông báo</td>
    </tr>
    <tr>
      <td>11.2.46</td>
      <td>Agent tiếp nhận chat / Từ chối chat</td>
      <td></td>
      <td>- Chức năng cho phép hiển Agent tiếp nhận / Từ chối chat khi có chat phân bổ đến</td>
    </tr>
    <tr>
      <td>11.2.47</td>
      <td>Agent thực hiện chat với khách hàng</td>
      <td></td>
      <td>- Chức năng cho phép Agent thực hiện chat với khách hàng sau khi đã tiếp nhận giao dịch web chat</td>
    </tr>
    <tr>
      <td>11.2.48</td>
      <td>Agent hold chat</td>
      <td></td>
      <td>- Khi Agent cần tra cứu hoặc trao đổi với Agent khác, Agent có thể hold chat bằng cách nhấn vào icon hold</td>
    </tr>
    <tr>
      <td>11.2.49</td>
      <td>Kết thúc chat</td>
      <td></td>
      <td>- Giao dịch chat với khách hàng kết thúc bằng 1 trong các cách sau: - Agent kết thúc chat - Agent click vào icon x để thực hiện kết thúc chat è Hệ thống hiển thị confirm</td>
    </tr>
    <tr>
      <td>11.2.50</td>
      <td>Cảnh báo KPI phiên chat đầu tiên</td>
      <td></td>
      <td>Cảnh báo KPI phiên chat đầu tiên</td>
    </tr>
    <tr>
      <td>11.2.51</td>
      <td>Cảnh báo KPI phiên chat tiếp theo</td>
      <td></td>
      <td>Cảnh báo KPI phiên chat tiếp theo</td>
    </tr>
    <tr>
      <td>11.2.52</td>
      <td>Cảnh báo KPI số lần hold chat</td>
      <td></td>
      <td>Cảnh báo KPI số lần hold chat</td>
    </tr>
    <tr>
      <td>11.2.53</td>
      <td>Cảnh báo KPI thời gian hold chat</td>
      <td></td>
      <td>Cảnh báo KPI thời gian hold chat</td>
    </tr>
    <tr>
      <td>12</td>
      <td>HappyCall</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.1</td>
      <td>Cấu hình tham số HT</td>
      <td>Thêm sửa xóa các tham số chung của hệ thống</td>
      <td>Thêm sửa xóa các tham số chung của hệ thống</td>
    </tr>
    <tr>
      <td>12.2</td>
      <td>Quản lý khách hàng</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.2.1</td>
      <td>Quản lý danh sách khách hàng</td>
      <td>- Xem thông tin chi tiết khách hàng: - Thêm sửa xóa danh sách khách hàng - Tìm kiếm theo tên danh sách, mã danh sách. - Xem thông tin chi tiết gồm: + Họ tên + Số điện thoại + Địa chỉ + Loại khiếu nại - Sửa: + Cập nhật theo file, + Xóa bản ghi trong danh sách</td>
      <td>- Xem thông tin chi tiết khách hàng: - Thêm sửa xóa danh sách khách hàng - Tìm kiếm theo tên danh sách, mã danh sách. - Xem thông tin chi tiết gồm: + Họ tên + Số điện thoại + Địa chỉ + Loại khiếu nại - Sửa: + Cập nhật theo file, + Xóa bản ghi trong danh sách</td>
    </tr>
    <tr>
      <td>12.2.2</td>
      <td>Bổ sung tính năng tìm kiếm</td>
      <td>Tìm kiếm theo: - Ngày tạo - Người tạo - Ngày cập nhật - Người cập nhật - Đã được gán vào chiến dịch</td>
      <td>- Nâng cấp tính năng - Bổ sung tiêu chí</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.2.3</td>
      <td>Quản khách hàng(menu con)</td>
      <td>- Thêm sửa xóa nhóm khách hàng - Tìm kiếm theo: + Tên + Giới tính + Số ĐT + Trạng thái chiến dịch + CMND - Xem thông tin danh sách khách hàng - Mở khóa/ khóa khách hàng</td>
      <td>- Thêm sửa xóa nhóm khách hàng - Tìm kiếm theo: + Tên + Giới tính + Số ĐT + Trạng thái chiến dịch + CMND - Xem thông tin danh sách khách hàng - Mở khóa/ khóa khách hàng</td>
    </tr>
    <tr>
      <td>12.2.4</td>
      <td>Xuất danh sách</td>
      <td>Xuất danh sách KH trong Menu Quản lý khách hàng\ Quản lý danh sách khách hàng\ trong cột hành động, khi chọn “Xem thông tin chi tiết khách hàng”</td>
      <td>Tham khảo mã IBM - Bổ sung chính sách an toàn của TĐ (các trường dữ liệu quy định thì có xuất mã hóa) - Bổ sung phân quyền xuất nhìn full dữ liệu hoặc xuất thấy dữ liệu ẩn Bổ sung xuất pdf, excel</td>
    </tr>
  </tbody>
</table>

# Public_442

<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.2.7</td>
      <td>Danh sách khách hàng không liên lạc</td>
      <td>- Cho phép người sử dụng thực hiện nhập các danh sách khách hàng không liên lạc lên hệ thống. Những khách hàng thuộc danh sách không liên lạc sẽ được bỏ qua khi thực hiện chiến dịch - Thêm mới, cập nhật, tìm kiếm, xóa danh sách, xóa khách hàng khỏi danh sách - Tìm kiếm theo: + Mã danh sách + Loại chiến dịch + Loại danh sách + Tên danh sách. - Tải file biểu mẫu, cập nhật trong kết quả tìm kiếm</td>
      <td>C - Bổ xung danh sách KH Vị thế, sẽ không thực hiện gọi ra HappyCall Khi trong chiến dịch gọi ra có thuê bao nằm trong danh sách này thực hiện POPup cảnh báo cho ĐTV biết đang gọi cho KH vị thế - Đồng bộ tự động danh sách KH Vị thế về IPCC ác chiến dịch Campain khác trên IPCC cũng check ds KH Vị thế trước khi thực hiện (không thực hiện các "chiến dịch" gửi mail, sms với KH Vị thế)</td>
    </tr>
    <tr>
      <td>12.2.8</td>
      <td>ĐTV bổ sung KH vào danh sách blacklist</td>
      <td>- Nếu trong Khi đàm thoại, KH yêu cầu TVV dừng mọi liên hệ trong tương lai, TVV có thể chọn ô Blacklist trong kết quả tương tác của chiến dịch đó để đưa KH vào danh sách Blacklist.</td>
      <td>- Bổ sung chức năng mới - Đưa vào backlist đối tượng khách hàng đang tương tác</td>
    </tr>
    <tr>
      <td>12.2.9</td>
      <td>Xuất excel</td>
      <td>- Xuất DS KH blacklist</td>
      <td>- Bổ sung chức năng mới - Bổ sung xuất dữ liệu nhạy cảm</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.2.10</td>
      <td>Bổ sung tính năng tìm kiếm</td>
      <td>- Tìm theo số ĐT khách hàng</td>
      <td>- Bổ sung tiêu chí tìm kiếm: để tìm kiếm được các KH đang nằm trong danh sách Backlist</td>
    </tr>
    <tr>
      <td>12.3</td>
      <td>Quản lý chiến dịch</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.3.1</td>
      <td>Quản lý nhóm Agents</td>
      <td>- Thêm sửa xóa nhóm agent - Cho phép tìm kiếm theo: + Mã danh sách + Loại chiến dịch + Loại danh sách + Tên danh sách. - Trong kết quả tìm kiếm cho phép: + Cập nhật danh sách + Gán trưởng nhóm cho danh sách + Tải danh sách TVV + Gán IP Phone cho user</td>
      <td>- Thêm sửa xóa nhóm agent - Cho phép tìm kiếm theo: + Mã danh sách + Loại chiến dịch + Loại danh sách + Tên danh sách. - Trong kết quả tìm kiếm cho phép: + Cập nhật danh sách + Gán trưởng nhóm cho danh sách + Tải danh sách TVV + Gán IP Phone cho user</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.3.2</td>
      <td>Quản lý thông tin chiến dịch</td>
      <td>- Tím kiếm theo: + Mã chiến dịch + Thời gian bắt đầu + Thời gian kết thúc + Tên chiến dịch + Loại chiến dịch + Kiểu gọi ra + Xuất báo cáo chiến dịch tìm kiếm - Thêm mới chiến dịch: + Chọn HT gọi ra + Kịch bản chiến dịch + Gán danh sách KH + Danh sách TVV Trong kết quả tìm kiếm cho phép chuyển chiến dịch tự động sang thủ công và ngược lại, xem thông tin chiến dịch, xóa chiến dịch, chuyển chiến dịch sang trạng thái chuẩn bị, gia hạn chiến dịch</td>
      <td>- Tím kiếm theo: + Mã chiến dịch + Thời gian bắt đầu + Thời gian kết thúc + Tên chiến dịch + Loại chiến dịch + Kiểu gọi ra + Xuất báo cáo chiến dịch tìm kiếm - Thêm mới chiến dịch: + Chọn HT gọi ra + Kịch bản chiến dịch + Gán danh sách KH + Danh sách TVV Trong kết quả tìm kiếm cho phép chuyển chiến dịch tự động sang thủ công và ngược lại, xem thông tin chiến dịch, xóa chiến dịch, chuyển chiến dịch sang trạng thái chuẩn bị, gia hạn chiến dịch</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.3.3</td>
      <td>Thêm mới chiến dịch</td>
      <td>- Bổ sung Thoại/ Thoại và Video Call/ Video Call - Thời gian nhập kết quả tương tác: + Kết nối: là thời gian nhập kết quả cho các cuộc gọi kết nối thành công được tới KH, hết thời gian nhập kết quả tương tác mà TVV không nhập hệ thống sẽ đóng màn hình nhập kết quả tương tác đồng thời lưu một bản ghi nháp để TVV có thể chỉnh sửa kết quả tương tác + Không kết nối: là thời gian nhập kết quả cho các cuộc gọi kết nối không thành công được tới KH, hết thời gian nhập kết quả tương tác mà TVV không nhập hệ thống sẽ đóng màn hình nhập kết quả tương tác đồng thời lưu một bản ghi nháp để TVV có thể chỉnh sửa kết quả tương tác - Chế độ thực hiện:</td>
      <td>- Áp dụng cho chiến dịch Telesale - Hiển thị các thông từ BCCS CC Bổ sung tích hợp với các API cung cấp thông tin BCCS - Cung cấp các API tạo các chiến dịch HPC - Bổ sung Thoại/ Thoại và Video Call/ Video Call - Thời gian nhập kết quả tương tác: + Kết nối: là thời gian nhập kết quả cho các cuộc gọi kết nối thành công được tới KH, hết thời gian nhập kết quả tương tác mà TVV không nhập hệ thống sẽ đóng màn hình nhập kết quả tương tác đồng thời lưu một bản ghi nháp để TVV có thể chỉnh sửa kết quả tương tác + Không kết nối: là thời gian nhập kết quả cho các cuộc gọi kết nối không thành công được tới KH, hết thời gian nhập kết quả tương tác mà TVV không nhập hệ thống sẽ đóng màn hình nhập kết quả tương tác đồng thời lưu một bản ghi nháp để TVV có thể chỉnh sửa kết quả tương tác - Chế độ thực hiện: Theo múi giờ trong ngày hay khoảng thời gian - Chọn chế độ thực hiện cho chiến dịch: + Manual + Preview + Progressive + Predictive"</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Theo múi giờ trong ngày hay khoảng thời gian - Chọn chế độ thực hiện cho chiến dịch: + Manual + Preview + Progressive + Predictive</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.3.4</td>
      <td>Thêm mới chiến dịch</td>
      <td>Bổ sung thêm trường cấu hình “Số lượng khảo sát thành công tối đa”: được tính theo số lượng dữ liệu KH kết nối thành công. Với những chiến dịch có yêu cầu đặc thù thì khi tạo chiến dịch tích chọn vào trường này và nhập số lượng dữ liệu KH yêu cầu. Khi đếm đủ số lượng tối đa theo chiến dịch -> Chiến dịch tạm dừng (không cho nhận dữ liệu thêm) - > Hệ thống thông báo: “Dữ liệu khảo sát đã đạt tối đa”.</td>
      <td>- Áp dụng cho chiến dịch HPC - Bổ sung thêm trường cấu hình “Số lượng khảo sát thành công tối đa”: được tính theo số lượng dữ liệu KH kết nối thành công. Với những chiến dịch có yêu cầu đặc thù thì khi tạo chiến dịch tích chọn vào trường này và nhập số lượng dữ liệu KH yêu cầu. Khi đếm đủ số lượng tối đa theo chiến dịch -> Chiến dịch tạm dừng (không cho nhận dữ liệu thêm) -> Hệ thống thông báo: “Dữ liệu khảo sát đã đạt tối đa”.</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.3.5</td>
      <td>Cấu hình hiển thị thông tin khi thêm mới chiến dịch</td>
      <td>P Cho lựa chọn cấu hình thông tin hiển thị: thông tin trên BCCS, thông tin từ hệ thống khác có giao tiếp với HPC để phục vụ chiến dịch đặc thù. - Cho lựa chọn cấu hình hiển thị lịch sử tương tác của KH lên các kênh CSKH như: thoại, Video call. chat. - Người tạo chiến dịch cần được phân quyền mới được cấu hình hiển thị các thông tin này hân quyền cho phép tạo chiến dịch happy call, chỉ những người của đơn vị nào mới được cấu hình các trường dữ liệu của đơn vị đó liên quan đến việc hiển thị thông tin khi gọi ra</td>
      <td>P Cho lựa chọn cấu hình thông tin hiển thị: thông tin trên BCCS, thông tin từ hệ thống khác có giao tiếp với HPC để phục vụ chiến dịch đặc thù. - Cho lựa chọn cấu hình hiển thị lịch sử tương tác của KH lên các kênh CSKH như: thoại, Video call. chat. - Người tạo chiến dịch cần được phân quyền mới được cấu hình hiển thị các thông tin này hân quyền cho phép tạo chiến dịch happy call, chỉ những người của đơn vị nào mới được cấu hình các trường dữ liệu của đơn vị đó liên quan đến việc hiển thị thông tin khi gọi ra</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.3.6</td>
      <td>Chiến dịch HPC Sự cố lặp(tự động)</td>
      <td>- Lấy dữ liệu PA từ BCCS của ngày được chọn - Lấy dữ liệu PA từ BCCS của 30 ngày trước ngày được chọn. - Thực hiện đếm trùng theo số thuê bao của ngày được chọn so với danh sách số thuê bao gặp sự cố trong 30 ngày trước đó. Lấy toàn bộ số thuê bao lặp lại từ 3 lần trở lên đẩy vào chiến dịch HPC sự cố lặp. - Đẩy dữ liệu lặp từ 3 lần trở lên vào chiến dịch HPC sự cố lặp - Tự động đồng bộ kết quả HPC trên phần mềm HPC về BCCS, khi ĐTV cập nhật kết quả khảo sát trên tool HPC thì kết quả cũng được cập nhật và đóng trên BCCS. - Xuất báo cáo DL đã đẩy tự động trên 2 chiến dịch. - Xuất được báo cáo</td>
      <td>- Lấy dữ liệu PA từ BCCS của ngày được chọn - Lấy dữ liệu PA từ BCCS của 30 ngày trước ngày được chọn. - Thực hiện đếm trùng theo số thuê bao của ngày được chọn so với danh sách số thuê bao gặp sự cố trong 30 ngày trước đó. Lấy toàn bộ số thuê bao lặp lại từ 3 lần trở lên đẩy vào chiến dịch HPC sự cố lặp. - Đẩy dữ liệu lặp từ 3 lần trở lên vào chiến dịch HPC sự cố lặp - Tự động đồng bộ kết quả HPC trên phần mềm HPC về BCCS, khi ĐTV cập nhật kết quả khảo sát trên tool HPC thì kết quả cũng được cập nhật và đóng trên BCCS. - Xuất báo cáo DL đã đẩy tự động trên 2 chiến dịch. - Xuất được báo cáo tiến độ HPC. - Báo cáo Campaign: Đảm bảo hệ thống cho phép xuất được kết quả đầy đủ thông tin các trường như dữ liệu đồng bộ sang</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>tiến độ HPC. - Báo cáo Campaign: Đảm bảo hệ thống cho phép xuất được kết quả đầy đủ thông tin các trường như dữ liệu đồng bộ sang</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.3.7</td>
      <td>Chiến dịch HPC đóng PA DV Cố định BOT không xử lý</td>
      <td>- Lấy dữ liệu PA từ BCCS - Lọc trùng theo trường số thuê bao với những DL đã đẩy vào chiến dịch HPC sự cố lặp. - Loại bỏ những DL bị trùng với chiến dịch HPC sự cố lặp - Đẩy dữ liệu vào chiến dịch HPC đóng PA DV Cố định. - Tự động đồng bộ kết quả HPC trên phần mềm HPC về BCCS, khi ĐTV cập nhật kết quả khảo sát trên tool HPC thì kết quả cũng được cập nhật và đóng trên BCCS. - Xuất báo cáo DL đã đẩy tự động trên 2 chiến dịch. - Xuất được báo cáo tiến độ HPC. - Báo cáo Campaign: Đảm bảo hệ thống cho phép xuất được kết quả đầy đủ thông tin các trường như dữ liệu đồng bộ sang</td>
      <td>- Lấy dữ liệu PA từ BCCS - Lọc trùng theo trường số thuê bao với những DL đã đẩy vào chiến dịch HPC sự cố lặp. - Loại bỏ những DL bị trùng với chiến dịch HPC sự cố lặp - Đẩy dữ liệu vào chiến dịch HPC đóng PA DV Cố định. - Tự động đồng bộ kết quả HPC trên phần mềm HPC về BCCS, khi ĐTV cập nhật kết quả khảo sát trên tool HPC thì kết quả cũng được cập nhật và đóng trên BCCS. - Xuất báo cáo DL đã đẩy tự động trên 2 chiến dịch. - Xuất được báo cáo tiến độ HPC. - Báo cáo Campaign: Đảm bảo hệ thống cho phép xuất được kết quả đầy đủ thông tin các trường như dữ liệu đồng bộ sang. - Tham khảo PYC mã 4075452 trên hệ thống quản lý sản xuất</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.3.8</td>
      <td>Chiến dịch Manual</td>
      <td>- Agent nhận KH, hệ thống phân phối về KH A => (2) Agent xem thông tin KH và bấm gọi => (3) Agent kết thúc cuộc gọi với KH A => Agent thao tác nhận KH tiếp theo (B) và lặp lại các bước 2-3. - Agent xem được thông tin KH trước khi gọi. - Agent có thể bỏ qua một KH và xử lý tiếp KH khác. - Với dạng chiến dịch này, người quản lý muốn Agent chủ động nhận KH từ list KH sẵn có, xem thông tin và chủ động thao tác gọi khách khi sẵn sàng.</td>
      <td>- AG có thể xem được thông tin KH Chủ động nhận KH từ list khách hàng có sẵn - Chuyển sang menu - Nội dung chi tiết tham khảo PYC có mã IBM 4075458 trên hệ thống quản lý sản xuất</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.3.9</td>
      <td>Chiến dịch Predictive</td>
      <td>- Hệ thống tự động gọi ra nhiều số điện thoại KH, chỉ khi KH nghe máy, cuộc gọi mới được đổ tới agent. + (1) Hệ thống gọi cho KH A trước khi kết nối với Agent => (2) Khách hàng A nghe máy, hệ thống gọi đến agent. Trong lúc chưa được kết nối đến agent, khách hàng nghe nhạc chờ => (3) Agent nghe máy, lúc này KH và Agent được kết nối với nhau. Nếu Agent không nghe máy, cuộc gọi đổ sang Agent khác sau 10s (KH chờ lâu sẽ tắt máy). + Lưu ý: hệ thống tính toán số cuộc gọi cần thực hiện tại một thời điểm để tối ưu trong phạm vi tỷ lệ nhỡ cho phép, có thể KH đã nghe máy rồi nhưng chưa có agent rảnh để đổ cuộc gọi. + Agent không xem</td>
      <td>- Hệ thống tự động gọi ra nhiều số điện thoại KH, chỉ khi KH nghe máy, cuộc gọi mới được đổ tới agent. + (1) Hệ thống gọi cho KH A trước khi kết nối với Agent => (2) Khách hàng A nghe máy, hệ thống gọi đến agent. Trong lúc chưa được kết nối đến agent, khách hàng nghe nhạc chờ => (3) Agent nghe máy, lúc này KH và Agent được kết nối với nhau. Nếu Agent không nghe máy, cuộc gọi đổ sang Agent khác sau 10s (KH chờ lâu sẽ tắt máy). + Lưu ý: hệ thống tính toán số cuộc gọi cần thực hiện tại một thời điểm để tối ưu trong phạm vi tỷ lệ nhỡ cho phép, có thể KH đã nghe máy rồi nhưng chưa có agent rảnh để đổ cuộc gọi. + Agent không xem được thông tin KH trước khi gọi. + Agent không được phép bỏ qua một KH và xử lý tiếp KH khác (Agent chỉ có thể từ chối cuộc gọi đến từ hệ thống). + Với dạng chiến dịch này, người quản lý muốn tối đa nhất công suất gọi điện của Agent, chấp nhận trường hợp có thể KH nghe máy nhưng không gặp được Agent (chưa có Agent rảnh tiếp nhận cuộc gọi, hoặc KH tắt máy trước khi gặp Agent) - Nội dung chi tiết tham khảo PYC có mã IBM 4075458 trên hệ thống quản lý sản xuất</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>được thông tin KH trước khi gọi. + Agent không được phép bỏ qua một KH và xử lý tiếp KH khác (Agent chỉ có thể từ chối cuộc gọi đến từ hệ thống). + Với dạng chiến dịch này, người quản lý muốn tối đa nhất công suất gọi điện của Agent, chấp nhận trường hợp có thể KH nghe máy nhưng không gặp được Agent (chưa có Agent rảnh tiếp nhận cuộc gọi, hoặc KH tắt máy trước khi gặp Agent)</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.3.10</td>
      <td>Chiến dịch Preview</td>
      <td>- Chiến dịch đổ KH về cho agent, cho agent 1 khoảng thời gian để xem trước thông tin KH trước khi quay số. + (1) Hệ thống hiển thị thông tin KH A => (2) Agent có 1 khoảng thời gian nhất định để xem thông tin KH => (3) Hết thời gian trên, hệ thống gọi cho Agent => (4) Khi Agent nghe máy, hệ thống gọi đến KH để kết nối 2 bên => (5) Sau khi cuộc gọi kết thúc, hệ thống hiển thị thông tin KH tiếp theo và lặp lại các bước (2) đến (5). + Agent xem được thông tin KH trước khi gọi. + Agent có thể bỏ qua một KH và xử lý tiếp KH khác (Agent hẹn gọi lại, sau đó hệ thống hiển thị KH tiếp theo). + Với dạng chiến dịch này, người quản</td>
      <td>- Chiến dịch đổ KH về cho agent, cho agent 1 khoảng thời gian để xem trước thông tin KH trước khi quay số. + (1) Hệ thống hiển thị thông tin KH A => (2) Agent có 1 khoảng thời gian nhất định để xem thông tin KH => (3) Hết thời gian trên, hệ thống gọi cho Agent => (4) Khi Agent nghe máy, hệ thống gọi đến KH để kết nối 2 bên => (5) Sau khi cuộc gọi kết thúc, hệ thống hiển thị thông tin KH tiếp theo và lặp lại các bước (2) đến (5). + Agent xem được thông tin KH trước khi gọi. + Agent có thể bỏ qua một KH và xử lý tiếp KH khác (Agent hẹn gọi lại, sau đó hệ thống hiển thị KH tiếp theo). + Với dạng chiến dịch này, người quản lý muốn agent có thời gian nhất định để xem thông tin KH trước khi đàm thoại</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>lý muốn agent có thời gian nhất định để xem thông tin KH trước khi đàm thoại</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.3.11</td>
      <td>Chiến dịch Progressive</td>
      <td>Khi agent sẵn sàng nhận cuộc gọi, chiến dịch liên tục đổ cuộc gọi cho agent: - (1) Hệ thống gọi cho Agent trước khi kết nối với KH A => (2) Khi agent nghe máy, hệ thống gọi đến KH A để kết nối hai bên => (3) Agent kết thúc cuộc gọi với KH A => (4) Hệ thống gọi cho Agent trước khi kết nối với KH tiếp theo (B) và lặp lại các bước (2) đến (4). - Agent không xem được thông tin KH trước khi gọi. - Agent không được phép bỏ qua một KH và xử lý tiếp KH khác (Agent chỉ có thể từ chối cuộc gọi đến từ hệ thống). - Với dạng chiến dịch này, người quản lý muốn Agent thực hiện liên tục các cuộc gọi, không có thời gian xem thông tin KH trước cuộc gọi</td>
      <td>Khi agent sẵn sàng nhận cuộc gọi, chiến dịch liên tục đổ cuộc gọi cho agent: - (1) Hệ thống gọi cho Agent trước khi kết nối với KH A => (2) Khi agent nghe máy, hệ thống gọi đến KH A để kết nối hai bên => (3) Agent kết thúc cuộc gọi với KH A => (4) Hệ thống gọi cho Agent trước khi kết nối với KH tiếp theo (B) và lặp lại các bước (2) đến (4). - Agent không xem được thông tin KH trước khi gọi. - Agent không được phép bỏ qua một KH và xử lý tiếp KH khác (Agent chỉ có thể từ chối cuộc gọi đến từ hệ thống). - Với dạng chiến dịch này, người quản lý muốn Agent thực hiện liên tục các cuộc gọi, không có thời gian xem thông tin KH trước cuộc gọi. - Nội dung chi tiết tham khảo PYC mã 4075458 trên hệ thống quản lý sản xuất</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.3.12</td>
      <td>Tìm kiếm chiến dịch</td>
      <td>- Khi TVV chọn chiến dịch để triển khai, hệ thống sẽ phân bổ các khách hàng cho tư vấn viên trong tập các khách hàng được gán với chiến dịch theo quy tắc sau: + Khách hàng hẹn gọi lại của TVV đang trong khoảng thời gian hẹn gọi lại. + Khách hàng hẹn gọi lại của TVV khác đang trong khoảng thời gian hẹn gọi lại nhưng TVV đó không đăng nhập hoặc không thực hiện chiến dịch. + Khách hàng chưa được gọi.Khách hàng từng được liên lạc nhưng có kết quả kết nối là “Không liên lạc được” hoặc “Không kết nối do hạ tầng viễn thông” hoặc 1 giá trị trạng thái kết nối động được cấu hình cho phép gọi lại cho KH, chưa đạt số lần gọi ra</td>
      <td>- Khi TVV chọn chiến dịch để triển khai, hệ thống sẽ phân bổ các khách hàng cho tư vấn viên trong tập các khách hàng được gán với chiến dịch theo quy tắc sau: + Khách hàng hẹn gọi lại của TVV đang trong khoảng thời gian hẹn gọi lại. + Khách hàng hẹn gọi lại của TVV khác đang trong khoảng thời gian hẹn gọi lại nhưng TVV đó không đăng nhập hoặc không thực hiện chiến dịch. + Khách hàng chưa được gọi.Khách hàng từng được liên lạc nhưng có kết quả kết nối là “Không liên lạc được” hoặc “Không kết nối do hạ tầng viễn thông” hoặc 1 giá trị trạng thái kết nối động được cấu hình cho phép gọi lại cho KH, chưa đạt số lần gọi ra tối đa và khoảng cách từ thời điểm cuộc gọi gần nhất đến thời điểm phân bổ >= tham số khoảng cách giữa 2 lần liên lạc. - Chi tiết tham khảo PYC mã IBM 4075468</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>tối đa và khoảng cách từ thời điểm cuộc gọi gần nhất đến thời điểm phân bổ >= tham số khoảng cách giữa 2 lần liên lạc.</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.3.13</td>
      <td>Quản lý đơn vị</td>
      <td>- Tìm kiếm theo: + Mã đơn vị + Tên đơn vị + Đơn vị cha + Trạng thái đơn vị + Mã tư vấn viên + Thêm, sửa, xóa đơn vị. - Gán danh sách tư vấn viên vào mã cây đơn vị tương ứng</td>
      <td>- Tìm kiếm theo: + Mã đơn vị + Tên đơn vị + Đơn vị cha + Trạng thái đơn vị + Mã tư vấn viên + Thêm, sửa, xóa đơn vị. - Gán danh sách tư vấn viên vào mã cây đơn vị tương ứng</td>
    </tr>
    <tr>
      <td>12.3.14</td>
      <td>Quản lý khách hàng báo đỏ</td>
      <td></td>
      <td>Đề xuất bỏ</td>
    </tr>
    <tr>
      <td>12.3.15</td>
      <td>Chiến dịch tạo tự động Cảnh báo Roaming, BADO</td>
      <td></td>
      <td>Đề xuất bỏ</td>
    </tr>
    <tr>
      <td>12.3.16</td>
      <td>Chiến dịch tự động HappyCall MNP</td>
      <td></td>
      <td>- Áp dụng cho cả chiến dịch tự động thủ công - IPCC 4.0 cung cấp API - Các đơn vị tích hợp các API để truyền sang cho IPCC tạo thông tin dữ liệu cho chiến dịch.</td>
    </tr>
    <tr>
      <td>12.3.17</td>
      <td>Cảnh báo giám sát</td>
      <td>Không hoạt động</td>
      <td>- Đảm bảo chức năng tương tự như chức năng trên hệ thống cũ - Kiểm tra tính năng tại sao chưa hoạt động</td>
    </tr>
    <tr>
      <td>12.3.18</td>
      <td>Đánh giá chiến dịch</td>
      <td>Không hoạt động</td>
      <td>- Đảm bảo chức năng tương tự như chức năng trên hệ thống cũ - Kiểm tra tính năng tại sao chưa hoạt động</td>
    </tr>
    <tr>
      <td>12.4</td>
      <td>Thực hiện chiến dịch</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.4.1</td>
      <td>Nhập kết quả tương tác</td>
      <td>- Thực hiện gọi ra cho khách hàng theo chiến dịch. - Tím kiếm theo: Mã chiến dịch, thời gian bắt đầu, thời gian kết thúc, tên chiến dịch, loại chiến dịch - Chuyển trạng thái chiến dịch từ chuẩn bị sang triển khai - Tư vấn viên nhận KH thực hiện chiến dịch theo kịch bản - Nhập kết quả.</td>
      <td>Đảm bảo chức năng tương tự như chức năng trên hệ thống cũ</td>
    </tr>
    <tr>
      <td>12.4.2</td>
      <td>Sửa đổi, thêm mới kết quả</td>
      <td>- Bổ sung tính năng sửa đổi/ thêm mới kết quả trong “Trạng thái liên lạc với Khách hàng” và áp dụng cho tất cả các loại chiến dịch HPC</td>
      <td>đã upcode ==> đề xuất bỏ yêu cầu này</td>
    </tr>
    <tr>
      <td>12.4.3</td>
      <td>Cảnh báo KH hẹn gọi lại, nhắn tin KH</td>
      <td>- Đối với những khách hàng là khách hàng hẹn gọi lại thì phần kết quả tương tác với KH sẽ hiển thị thêm thông báo “Chú ý đây là khách hàng hẹn gọi lại”. - Trường hợp KH không nghe máy/ KH báo bận, TVV có thể nhấn nút gửi tin nhắn</td>
      <td>- Bổ sung cảnh báo KH hẹn gọi lại - Bổ sung 1 tin nhắn mẫu để nhắn gọi lại cho KH - Cho phép tùy chỉnh template nội dung tin nhắn - Nội dung chi tiết tham khảo nội dung PYC có mã IBM 4075458 trên hệ thống quản lý sản xuất</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>đến KH theo tin nhắn đã được cấu hình trước để xin lịch hẹn gọi lại cho KH</td>
      <td></td>
    </tr>
    <tr>
      <td>12.4.4</td>
      <td>Yêu cầu nhập thông tin</td>
      <td>Trên bảng hỏi HPC phần câu hỏi mặc định “Quest 2” và mục “ Ghi chú” dùng để lấy thông tin về GBOC chỉ cho phép người dùng thực hiện đóng kết quả khi 02 nội dung này được cập nhật thông tin đầy đủ.</td>
      <td>Đã upcode ==> đề xuất bỏ yêu cầu này</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.4.5</td>
      <td>Nhận diện KH gọi thành công chuyển trạng thái sang DNC</td>
      <td>- Hệ thống kiểm tra số lần khách hàng được gọi ra thành công ứng với loại chiến dịch mà khách hàng vừa được gọi ra, tính từ đầu tháng tính đến thời điểm hiện tại. Sau đó sẽ so sánh với số lần kết nối KH thành công/tháng của loại chiến dịch đó (được cấu hình trong mục Cấu hình số lần tham gia chiến dịch của khách hàng). Nếu số kết quả tương tác có trạng thái kết nối là thành công của KH đó theo loại chiến dịch >= Số lần kết nối KH thành công /tháng thì KH đó được cập nhật thành KH DNC. - Khi KH là DNC thì sẽ không được phân bổ gọi ra nếu tồn tại trong các chiến dịch khác. - Đến ngày đầu tiên của tháng mới, tất cả các khách hàng là</td>
      <td>- Hệ thống kiểm tra số lần khách hàng được gọi ra thành công ứng với loại chiến dịch mà khách hàng vừa được gọi ra, tính từ đầu tháng tính đến thời điểm hiện tại. Sau đó sẽ so sánh với số lần kết nối KH thành công/tháng của loại chiến dịch đó (được cấu hình trong mục Cấu hình số lần tham gia chiến dịch của khách hàng). Nếu số kết quả tương tác có trạng thái kết nối là thành công của KH đó theo loại chiến dịch >= Số lần kết nối KH thành công /tháng thì KH đó được cập nhật thành KH DNC. - Khi KH là DNC thì sẽ không được phân bổ gọi ra nếu tồn tại trong các chiến dịch khác. - Đến ngày đầu tiên của tháng mới, tất cả các khách hàng là DNC của tháng cũ sẽ được cập nhật thành khách hàng bình thường, không còn là khách hàng DNC. - Chỉ liên quan đến cuộc gọi Telesale - Nội dung chi tiết tham khảo nội dung PYC có mã IBM 4075458 trên hệ thống quản lý sản xuất</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>DNC của tháng cũ sẽ được cập nhật thành khách hàng bình thường, không còn là khách hàng DNC.</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.4.6</td>
      <td>Hiển thị talktime</td>
      <td>- Hiển thị thông tin talktime (tổng thời gian đàm thoại với KH) lũy kế trong ngày để ĐTV nhìn thấy khi đang thực hiện chiến dịch. Mục đích để ĐTV đảm bảo đủ thời lượng gọi bắt buộc/ngày theo quy định.</td>
      <td>- Hiển thị thông tin talktime (tổng thời gian đàm thoại với KH) lũy kế trong ngày để ĐTV nhìn thấy khi đang thực hiện chiến dịch. Mục đích để ĐTV đảm bảo đủ thời lượng gọi bắt buộc/ngày theo quy định. Thời gian đàm thoại của ĐTV chỉ liên quan đến cuộc gọi Telesale tham gia trong ngày - Nội dung chi tiết tham khảo nội dung PYC có mã IBM 4075458 trên hệ thống quản lý sản xuất</td>
    </tr>
    <tr>
      <td>12.4.7</td>
      <td>Sửa kết quả tương tác</td>
      <td>Chức năng cho 3 nhóm người dùng sử dụng: + Trưởng nhóm: Cho phép sửa kết quả tương tác của tất cả các Agent mình là trưởng nhóm. Thời gian sửa trong vòng 24h tính từ thời điểm lưu bản ghi. + Giám sát viên: Cho phép sửa kết quả tương tác của tất cả các agent. Thời gian sửa không giới hạn. + Tư vấn viên: Cho phép sửa kết quả tương tác của mình. Thời gian sửa trong vòng 12h tính từ thời điểm lưu bản ghi.</td>
      <td>Xây dựng chức năng trên hệ thống mới tương tự chức năng trên hệ thống cũ Chức năng cho 3 nhóm người dùng sử dụng: + Trưởng nhóm: Cho phép sửa kết quả tương tác của tất cả các Agent mình là trưởng nhóm. Thời gian sửa trong vòng 24h tính từ thời điểm lưu bản ghi. + Giám sát viên: Cho phép sửa kết quả tương tác của tất cả các agent. Thời gian sửa không giới hạn. + Tư vấn viên: Cho phép sửa kết quả tương tác của mình. Thời gian sửa trong vòng 12h tính từ thời điểm lưu bản ghi.</td>
    </tr>
  </tbody>
</table>

# Public_442

<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>chỉnh sửa nội dung kịch bản. - Cho phép import kịch bản theo file</td>
      <td></td>
    </tr>
    <tr>
      <td>12.4.10</td>
      <td>Quản lý tin nhắn gửi đến KH</td>
      <td>Cho phép người dùng quản lý và gửi tin nhắn đến khách hàng: - Hệ thống cho phép thêm mới, tìm kiếm, chỉnh sửa, xóa tin nhắn. - Cấu hình tin nhắn vào từng chiến dịch để TVV có thể bấm gửi tin trong trường hợp KH không nghe máy/KH báo bận.</td>
      <td>Cho phép người dùng quản lý và gửi tin nhắn đến khách hàng: - Hệ thống cho phép thêm mới, tìm kiếm, chỉnh sửa, xóa tin nhắn. - Cấu hình tin nhắn vào từng chiến dịch để TVV có thể bấm gửi tin trong trường hợp KH không nghe máy/KH báo bận. - Nội dung chi tiết tham khảo nội dung PYC có mã IBM 4075458 trên hệ thống quản lý sản xuất</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.4.11</td>
      <td>Quản lý cuộc gọi vào của KH</td>
      <td>- ĐTV thực hiện chiến dịch telesales tới KH, KH bị lỡ cuộc gọi & sau đó KH thực hiện gọi lại tổng đài hệ thống tự động hiển thị cuộc gọi đến cho chính Agent đã thực hiện gọi ra trước đó cho KH: + Nếu Agent này không online thì cuộc gọi được chuyển đến Agent khác đang rảnh rỗi. + Nếu Agent này đang bận hoặc không có Agent nào nhận cuộc gọi cho đến Khi hết chuông chờ thì KH Ađược xếp vào hàng gọi nhỡ, được hiển thị cho tất cả các Agent, đến Khi có Agent gọi lại cho KH và nhập kết quả đã xử lý thì KH A được đẩy sang hàng đã xử lý.</td>
      <td>Đề xuất bỏ (từ chị PhuongCT) ==> đề xuất bỏ</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.4.12</td>
      <td>Chuyển sang chiến dịch khác</td>
      <td>Tính năng tự động cho phép người quản lý cấu hình nếu Agent đạt năng suất trên chiến dịch này thì được phép tự động chuyển sang chiến dịch khác để không phải thêm thủ công</td>
      <td>- Tính năng tự động cho phép cấu hình nếu Agent đạt năng suất trên chiến dịch này thì được phép tự động chuyển sang chiến dịch khác để không phải thêm thủ công. - KPI bán hàng thành công trên ngày của chiến dịch - Đạt KPI mới được chuyển - KPI cấu hình trên chiến dịch - Tùy chiến dịch cho phép chuyển và không cho phép chuyển - Nội dung chi tiết tham khảo nội dung PYC có mã IBM 4075458 trên hệ thống quản lý sản xuất</td>
    </tr>
    <tr>
      <td>12.4.13</td>
      <td>Phân quyền VSA</td>
      <td>- Phân hệ VSA của HappyCall các nhóm chức năng hiện tại gán cứng với role nên khi lấy các chức năng con xây nhóm chức năng riêng cho từng đơn vị thì không hoạt động dẫn đến tất cả các đơn vị đều đang dùng chung nhóm chức năng của TTCSKH và quản trị user đơn vị không thể cấp quyền cho người dùng đơn vị mình. - Nâng cấp để có thể cấp quyền riêng cho từng đơn vị.</td>
      <td>- Phân hệ VSA của HappyCall các nhóm chức năng hiện tại gán cứng với role nên khi lấy các chức năng con xây nhóm chức năng riêng cho từng đơn vị thì không hoạt động dẫn đến tất cả các đơn vị đều đang dùng chung nhóm chức năng của TTCSKH và quản trị user đơn vị không thể cấp quyền cho người dùng đơn vị mình. - Nâng cấp để có thể cấp quyền riêng cho từng đơn vị. - Quyền áp dụng đến mức nút chức năng - Nội dung chi tiết tham khảo nội dung PYC có mã IBM 2743689 trên hệ thống quản lý sản xuất</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>- Quyền áp dụng đến mức nút chức năng</td>
      <td></td>
    </tr>
    <tr>
      <td>12.4.14</td>
      <td>Chuyển GBOC</td>
      <td>Khách hàng MNP không kịp níu kéo thì tick chuyển hàng loạt sang GBOC để kịp thời gian gìn giữ</td>
      <td>Đã upcode ==> đề xuất bỏ yêu cầu này</td>
    </tr>
    <tr>
      <td>12.4.15</td>
      <td>Chuyển GBOC</td>
      <td>Tự động hóa luồng giao kết quả HPC sang GBOC để giao kênh đi tiếp xúc giữ gìn</td>
      <td>Đã upcode ==> đề xuất bỏ yêu cầu này</td>
    </tr>
  </tbody>
</table>







<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.4.17</td>
      <td>Tích hợp hệ thống BCCS, CC và hệ thống Order vào hệ thống Happycall .</td>
      <td>- Khi ĐTV nhận KH, màn hình giao diện bổ sung thêm 1 tab “Hệ thống CC”, khi click vào tab này sẽ mở ra trang BCCS_Chăm sóc khách hàng: + Khi click vào Tab “Hệ thống CC” mở ra thông tin TB của KH trên trang BCCS + Khi ĐTV nhận KH, màn hình giao diện bổ sung thêm 1 tab “Hệ thống Hỗ trợ tư vấn”.Khi click vào tab này sẽ mở ra trang BCCS_Hỗ trợ tư vấn (ĐTV không phải thao tác đăng nhập số thuê bao của KH và mã capcha mà màn hình sẽ hiển thị luôn thông tin của thuê bao trên BCCS_Hỗ trợ tư vấn) - Cho phép hiển thị thông tin toàn bộ các gói cước KH đang dùng và tài khoản của KH trên hệ thống HPC.</td>
      <td>Theo mã IBM - Bổ sung link trên hệ thống HappyCall , CC, Orders khi ĐTV nhận KH - ĐTV nhấn vào link vào BCCS, CC, Orders - Khi ĐTV nhận KH, màn hình giao diện bổ sung thêm 1 tab “Hệ thống CC”, khi click vào tab này sẽ mở ra trang BCCS_Chăm sóc khách hàng: + Khi click vào Tab “Hệ thống CC” mở ra thông tin TB của KH trên trang BCCS + Khi ĐTV nhận KH, màn hình giao diện bổ sung thêm 1 tab “Hệ thống Hỗ trợ tư vấn”.Khi click vào tab này sẽ mở ra trang BCCS_Hỗ trợ tư vấn (ĐTV không phải thao tác đăng nhập số thuê bao của KH và mã capcha mà màn hình sẽ hiển thị luôn thông tin của thuê bao trên BCCS_Hỗ trợ tư vấn) - Cho phép hiển thị thông tin toàn bộ các gói cước KH đang dùng và tài khoản của KH trên hệ thống HPC. - Link BCCS, CC, Orders để cấu hình cho phép thay đổi thuận - Nội dung chi tiết tham khảo nội dung PYC có mã IBM 4075458 trên hệ thống quản lý sản xuất</td>
    </tr>
  </tbody>
</table>







<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.5.2</td>
      <td>Báo cáo tổng hợp chiến dịch</td>
      <td>Tìm kiếm theo: - Mã chiến dịch - Từ ngày đến ngày - Đầu số gọi - Xuất excel</td>
      <td>- Bổ sung báo cáo tổng hợp chiến dịch: - Nhập các tiêu chí tìm kiếm: + Mã chiến dịch: chọn mã chiến dịch từ danh sách chiến dịch đang có trên hệ thống + Từ ngày, đến ngày: tìm kiếm theo thời gian tạo bản ghi kết quả tương tác. + Đầu số gọi - Dữ liệu tìm kiếm hiển thị trên màn hình và được xuất excel với các thông tin: Tên chiến dịch Mã chiến dịch Thời gian thực hiện Thời gian kết thúc Trạng thái chiến dịch Số lượng KH của chiến dịch Số lượng KH đã gọi Số lượng KH chưa gọi Số lượng TVV của chiến dịch Số lượng TVV đã tham gia Số lượng TVV không tham gia Kết quả kết nối + KH đồng ý nghe máy + KH hẹn gọi lại + KH yêu cầu không gọi + KH không liên lạc được + KH báo bận + Sai số ĐT Kết quả bán hàng + KH đồng ý mua + KH không đồng ý mua + KH xem xét + KH tự đăng ký - Nội dung chi tiết và mẫu báo cáo tham khảo nội dung PYC với mã IBM là 4075458 trên hệ thống quản lý sản xuất.</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.5.3</td>
      <td>Báo cáo chi tiết theo chiến dịch</td>
      <td>- Tìm kiếm theo: Mã chiến dịch, Từ ngày, đến ngày, đầu số gọi - Dữ liệu tìm kiếm hiển thị trên màn hình và được xuất excel với các thông tin: + Tên chiến dịch + Mã chiến dịch + Thời gian thực hiện + Thời gian kết thúc + Trạng thái chiến dịch + Số lượng KH của chiến dịch + Số lượng KH đã gọi + Số lượng KH chưa gọi + Số lượng TVV của chiến dịch + Số lượng TVV đã tham gia + Số lượng TVV không tham gia - Kết quả kết nối: + KH đồng ý nghe máy + KH hẹn gọi lại + KH yêu cầu không gọi + KH không liên lạc</td>
      <td>- Bổ sung Báo cáo hiệu suất Agent - Tìm kiếm theo: + Mã chiến dịch + Từ ngày đến ngày + Đầu số gọi - Dữ liệu tìm kiếm hiển thị trên màn hình và được xuất excel với các thông tin: + STT + Số điện thoại đã gọi + Số lần liên lạc + Thời gian gọi + Agent + Kết quả kết nối (Agent nhập kịch bản) + Kết quả bán hàng (Agen nhập kịch bản) + Ghi chú (Agent nhập nội dung) - Bổ sung phân quyền báo cáo - Nội dung chi tiết và mẫu báo cáo tham khảo nội dung PYC với mã IBM là 4075458 trên hệ thống quản lý sản xuất.</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>được + KH báo bận + Sai số ĐT Kết quả bán hàng + KH đồng ý mua + KH không đồng ý mua + KH xem xét + KH tự đăng ký</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.5.4</td>
      <td>Báo cáo hiệu quả theo chiến dịch</td>
      <td>- Tìm kiếm theo: + Mã chiến dịch + Từ ngày đến ngày + Đầu số gọi - Dữ liệu tìm kiếm hiển thị trên màn hình và được xuất excel với các thông tin: + STT + Số điện thoại đã gọi + Số lần liên lạc + Thời gian gọi + Agent + Kết quả kết nối (Agent nhập kịch bản) + Kết quả bán hàng (Agen nhập kịch bản) + Ghi chú (Agent nhập nội dung)</td>
      <td>- Bổ sung Báo cáo hiệu suất Agent - Tìm kiếm theo: + Mã chiến dịch + Từ ngày đến ngày + Đầu số gọi - Dữ liệu tìm kiếm hiển thị trên màn hình và được xuất excel với các thông tin: + STT + Số điện thoại đã gọi + Số lần liên lạc + Thời gian gọi + Agent + Kết quả kết nối (Agent nhập kịch bản) + Kết quả bán hàng (Agen nhập kịch bản) + Ghi chú (Agent nhập nội dung) - Bổ sung phân quyền báo cáo - Nội dung chi tiết và mẫu báo cáo tham khảo nội dung PYC với mã IBM là 4075458 trên hệ thống quản lý sản xuất.</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.5.5</td>
      <td>Báo cáo hiệu suất Agent</td>
      <td>- Tìm kiếm theo: + Mã chiến dịch + Từ ngày đến ngày + Đầu số gọi - Dữ liệu tìm kiếm hiển thị trên màn hình và được xuất excel với các thông tin: + STT + Agent + Tổng số cuộc gọi nhỡ + Thời gian chờ TB (giây) + Thời gian chờ tối đa (giây) + Thời gian đàm thoại TB của Agent (giây) + Thời gian đàm thoại tối đa của Agent (giây) + Tổng thời gian đàm thoại của Agent(phút) + Số cuộc kết thúc do Agent</td>
      <td>- Bổ sung Báo cáo hiệu suất Agent - Tìm kiếm theo: + Mã chiến dịch + Từ ngày đến ngày + Đầu số gọi - Dữ liệu tìm kiếm hiển thị trên màn hình và được xuất excel với các thông tin: + STT + Agent + Tổng số cuộc gọi nhỡ + Thời gian chờ TB (giây) + Thời gian chờ tối đa (giây) + Thời gian đàm thoại TB của Agent (giây) + Thời gian đàm thoại tối đa của Agent (giây) + Tổng thời gian đàm thoại của Agent(phút) + Số cuộc kết thúc do Agent - Bổ sung phân quyền báo cáo - Nội dung chi tiết và mẫu báo cáo tham khảo nội dung PYC với mã IBM là 4075458 trên hệ thống quản lý sản xuất.</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.5.6</td>
      <td>Báo cáo tổng hợp KQ HPC</td>
      <td>- Nhóm trường dữ liệu cố định: + Trạng thái kết nối + Nhân viên HPC + Thời gian HPC + Ghi chú + Kết quả Khảo sát các câu hỏi - Nhóm các trường dữ liệu còn lại: Lấy theo dữ liệu đầu vào => Theo cấu hình file import dữ liệu KH ˗ Dữ liệu xuất ra cần đủ các trường câu hỏi trong cả trường hợp dữ liệu KH không có đáp án tương ứng.</td>
      <td>- Bổ sung Báo cáo hiệu suất Agent - Tìm kiếm theo: Mã chiến dịch, Từ ngày, đến ngày, đầu số gọi - Dữ liệu tìm kiếm hiển thị trên màn hình và được xuất excel với các thông tin: + Tên chiến dịch + Mã chiến dịch + Thời gian thực hiện + Thời gian kết thúc + Trạng thái chiến dịch + Số lượng KH của chiến dịch + Số lượng KH đã gọi + Số lượng KH chưa gọi + Số lượng TVV của chiến dịch + Số lượng TVV đã tham gia + Số lượng TVV không tham gia - Kết quả kết nối: + KH đồng ý nghe máy + KH hẹn gọi lại + KH yêu cầu không gọi + KH không liên lạc được + KH báo bận + Sai số ĐT Kết quả bán hàng + KH đồng ý mua + KH không đồng ý mua + KH xem xét + KH tự đăng ký - Bổ sung phân quyền báo cáo - Nội dung chi tiết và mẫu báo cáo tham khảo nội dung PYC với mã IBM là 4075458 trên hệ thống quản lý sản xuất.</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12.5.7</td>
      <td>Báo cáo chi tiết KQ HPC</td>
      <td>- Nhóm trường dữ liệu cố định: + Trạng thái kết nối + Nhân viên HPC + Thời gian HPC + Ghi chú + Kết quả Khảo sát các câu hỏi - Nhóm các trường dữ liệu còn lại: Lấy theo dữ liệu đầu vào => Theo cấu hình file import dữ liệu KH ˗ Dữ liệu xuất ra cần đủ các trường câu hỏi trong cả trường hợp dữ liệu KH không có đáp án tương ứng.</td>
      <td>- Bổ sung báo cáo chi tiết kết quả HPC với các thông tin như sau: ˗ Kết quả báo cáo xuất 2 có 2 nhóm trường: + Nhóm trường dữ liệu cố định: (1) Trạng thái kết nối (2) Nhân viên HPC (3) thời gian HPC (4) Ghi chú (5) Kết quả Khảo sát các Q hỏi + Nhóm các trường dữ liệu còn lại: Lấy theo dữ liệu đầu vào => Theo cấu hình file import dữ liệu KH ˗ Dữ liệu xuất ra cần đủ các trường câu hỏi trong cả trường hợp dữ liệu KH không có đáp án tương ứng. - Cho phép xuất excel báo cáo - Bổ sung phân quyền báo cáo cho các nhóm người dùng khác nhau - Nội dung chi tiết và mẫu báo cáo tham khảo nội dung PYC với mã IBM là 4075452 trên hệ thống quản lý sản xuất.</td>
    </tr>
    <tr>
      <td>13</td>
      <td>Chấm điểm cuộc gọi</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>I</td>
      <td>HT Chấm điểm giám sát</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>







<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.2</td>
      <td>Quản lý Danh sách nhóm chấm</td>
      <td>-Upload thông tin NV CSKH cần đánh giá trong tháng, bao gồm: + Họ tên + Mã NV CSKH + Nhóm + Kênh (line) + Đối tác (công ty) + Thâm niên + User + Trưởng nhóm + Giám sát quản lý + Kiểm định + Số lượng cuộc gọi cần chấm + Số điện thoại NV CSKH + Số điện thoại Trưởng nhóm/Giám sát quản lý + Ghi chú - Upload dữ liệu lên hệ thống dưới dạng file Excel và có thể lấy dữ liệu từ cơ sở dữ liệu Phần mềm Quản lý nhân sự thê ngoài của TT CSKH. - Tìm kiếm theo các đk trên</td>
      <td>- Cho phép quản lý danh sách nhóm chấm: thêm mới, sửa, xóa, import thông tin - Các thông tin tham khảo chức năng quản lý danh sahcs nhóm chấm trên hệ thống cũ - Bổ sung cho phép gán nhóm chấm cho từ 1 đến 2 giám sát - Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.3</td>
      <td>Chức năng lọc cuộc gọi/ lọc mail/ lọc hội thoại chat</td>
      <td>-Lọc cuộc gọi theo các điều kiện: + Độ ngắn dài cuộc gọi + Theo danh sách NV CSKH + Theo giám sát quản lý + Theo đối tác + Theo khoảng thời gian cài đặt + Theo kênh + Theo số thuê bao + Theo user của KH (áp dụng kênh Trực tuyến: Mạng xã hội, chat đa kênh) + Mã cuộc gọi /ghi âm/ hình ảnh (áp dụng kênh Video call) + Địa chỉ email của KH, tiêu đề email (áp dụng với kênh Mail)</td>
      <td>- Bổ sung lọc theo mail, lọc theo hội thoại - Mỗi kênh có điều kiện lọc khác nhau - Bổ sung các điều kiện lọc: -Lọc cuộc gọi theo các điều kiện: + Độ ngắn dài cuộc gọi + Theo danh sách NV CSKH + Theo giám sát quản lý + Theo đối tác + Theo khoảng thời gian cài đặt + Theo kênh + Theo số thuê bao + Theo user của KH (áp dụng kênh Trực tuyến: Mạng xã hội, chat đa kênh) + Mã cuộc gọi /ghi âm/ hình ảnh (áp dụng kênh Video call) + Địa chỉ email của KH, tiêu đề email (áp dụng với kênh Mail) - Các đối tượng cuộc gọi/ mail/ hội thoại được chấm điểm đảm bảo đầy đủ các tiêu chí trên - Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.4</td>
      <td>Chức năng lọc cuộc gọi/ lọc mail/ lọc hội thoại chat</td>
      <td>- Lọc cuộc gọi theo mức cảm xúc cuộc gọi gồm các mức cảm xúc (Lấy theo bộ từ khóa của K.CNTT trên hệ thống GSCG, dữ liệu đích có thể thay đổi theo thực tế): + Cuộc gọi bình thường (OK). + Cuộc gọi cảnh báo cao (NOK). + Cuộc gọi cảnh báo trung bình/cần xem xét (NOK). - Lọc cuộc gọi theo Nhu cầu phản ánh khách hàng gồm 05 cấp nghiệp vụ (lấy theo bộ từ khóa nhập thống kê nhu cầu KH gọi tổng đài trên web GSCG của K.CNTT)</td>
      <td>- Bổ sung tích hợp với phân tích cảm xúc kênh mail, chat tương tự kênh voice nếu có các công cụ phân tích cảm xúc trên mail và chat. - Lọc cuộc gọi theo mức cảm xúc cuộc gọi gồm các mức cảm xúc (Lấy theo bộ từ khóa của K.CNTT trên hệ thống GSCG, dữ liệu đích có thể thay đổi theo thực tế): + Cuộc gọi bình thường (OK). + Cuộc gọi cảnh báo cao (NOK). + Cuộc gọi cảnh báo trung bình/cần xem xét (NOK). - Lọc cuộc gọi theo Nhu cầu phản ánh khách hàng gồm 05 cấp nghiệp vụ (lấy theo bộ từ khóa nhập thống kê nhu cầu KH gọi tổng đài trên web GSCG của K.CNTT) - Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.</td>
    </tr>
  </tbody>
</table>







<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.6</td>
      <td>Chức năng chấm điểm</td>
      <td>- Ràng buộc theo chức năng Quản lý Danh sách nhóm chấm: 1 Giám sát quản lý 1 nhóm NV CSKH do đó mỗi Giám sát quản lý thì xem và chấm được các cuộc gọi của NV CSKH trong nhóm mà mình quản lý - Cho phép người dùng chấm điểm online/offline, chấm theo chủ đích dưới hình thức đẩy excel và import lên phần mềm (lưu ý: đối với chấm offline, sẽ thực hiện chấm các cuộc gọi đã lọc theo điều kiện tại mục 2). - Cho phép Giám sát được phép sửa trong vòng 24 giờ kể từ lúc chấm lần đầu</td>
      <td>- Bổ sung cho phép có 2 giám sát quản lý giám sát ĐTV, cả 2 giám sát đều có quyền chấm điểm cho ĐTV. - Trên 1 cuộc gọi nếu một giám sát đã chấm điểm cho ĐTV viên rồi thì cán bộ giám sát kia sẽ không được phép chấm (nếu chấm rồi thì phải cảnh báo) trên cuộc gọi. - Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.</td>
    </tr>
  </tbody>
</table>







<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>phầm…). o Cấp 3: Phân loại chi tiết theo nhu cầu của KH (cú pháp sử dụng, cách sử dụng, giá cước…). o Cấp 4: Phân loại chi tiết theo tên sản phẩm/ dịch vụ/ chính sách (Economy, V120…). o Cấp 5: Phân loại chi tiết theo hành vi sử dụng dịch vụ và nguyên nhân</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.8</td>
      <td>Chấm điểm Online (chức năng thêm mới vào trong menu Chấm điểm,, hiện menu này đã có chức năng chấm điểm offline, nay bổ xung thêm chấm online)</td>
      <td>-cho phép người chấm xem được danh sách các cuộc gọi đang tiếp nhận của nhóm NV CSKH mà mình quản lý. Giám sát được tích chọn bất kỳ cuộc gọi nào cần đánh giá theo thang điểm quy định. - Có chức năng bỏ cuộc gọi không đánh giá và ghi chú được lý do vì sao không đánh giá theo một số đầu mục quy định (cuộc gọi không có nội dung, cuộc gọi test…các đầu mục này sẽ do người dùng tự động cập nhật lên hệ thống). - Yêu cầu: + Bắt đầu vào chấm - > lưu đánh dấu cuộc gọi ở trạng thái đang chấm. + Kết thúc chấm và lưu dữ liệu -> chuyển sang trạng thái đã chấm. + Đối với cuộc gọi được chấm cùng lúc, lấy kết quả lưu trước,</td>
      <td>- Bổ sung chấm cho kênh: chat, mail, video call. - Cho phép người chấm xem được danh sách các cuộc gọi đang tiếp nhận của nhóm NV CSKH mà mình quản lý. Giám sát được tích chọn bất kỳ cuộc gọi nào cần đánh giá theo thang điểm quy định. - Có chức năng bỏ cuộc gọi không đánh giá và ghi chú được lý do vì sao không đánh giá theo một số đầu mục quy định (cuộc gọi không có nội dung, cuộc gọi test…các đầu mục này sẽ do người dùng tự động cập nhật lên hệ thống). - Yêu cầu: + Bắt đầu vào chấm -> lưu đánh dấu cuộc gọi ở trạng thái đang chấm. + Kết thúc chấm và lưu dữ liệu -> chuyển sang trạng thái đã chấm. + Đối với cuộc gọi được chấm cùng lúc, lấy kết quả lưu trước, người lưu sau sẽ nhận được thông báo “Cuộc gọi này đã chấm”. + Phần phân loại nghiệp vụ: trường hợp xếp loại TB, Yếu bắt buộc chọn phân loại cấp 4,5. + Phần kỹ năng: bắt buộc chọn ít nhất một tiêu chí cha. Nếu chọn tiêu chí cha có tiêu chí con thì bắt buộc chọn ít nhất một tiêu chí con. - Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.</td>
    </tr>
  </tbody>
</table>

# Public_442

<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>gọi ở trạng thái đang chấm. + Kết thúc chấm và lưu dữ liệu -> chuyển sang trạng thái đã chấm. + Đối với cuộc gọi được chấm cùng lúc, lấy kết quả lưu trước, người lưu sau sẽ nhận được thông báo “Cuộc gọi này đã chấm”. + Phần phân loại nghiệp vụ: trường hợp xếp loại TB, Yếu bắt buộc chọn phân loại cấp 4,5. + Phần kỹ năng: bắt buộc chọn ít nhất một tiêu chí cha. Nếu chọn tiêu chí cha có tiêu chí con thì bắt buộc chọn ít nhất một tiêu chí con.</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.10</td>
      <td>Kiểm định lần 1</td>
      <td>- Cho phép người dùng được cấp quyền kiểm định 1 có quyền sửa toàn bộ phần đánh giá của Giám sát/ trưởng nhóm chấm cuộc gọi đó sau 24h kề từ khi Giám sát chấm lần đầu. - Chức năng tra cứu tính năng kiểm định 1: Cho phép người dùng tìm kiếm cuộc gọi cần kiểm định theo thời gian, theo Giám sát/ Trưởng nhóm, theo NV CSKH, số điện thoại KH gọi tổng đài, theo đối tác, theo ngưỡng xếp loại của cuộc gọi</td>
      <td>- Bổ sung kiểm định cho kênh: chat, mail, video call. - Cho phép người dùng được cấp quyền kiểm định 1 có quyền sửa toàn bộ phần đánh giá của Giám sát/ trưởng nhóm chấm cuộc gọi đó sau 24h kề từ khi Giám sát chấm lần đầu. - Chức năng tra cứu tính năng kiểm định 1: Cho phép người dùng tìm kiếm cuộc gọi cần kiểm định theo thời gian, theo Giám sát/ Trưởng nhóm, theo NV CSKH, số điện thoại KH gọi tổng đài, theo đối tác, theo ngưỡng xếp loại của cuộc gọi. - Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.11</td>
      <td>Kiểm định lần 2 (là chức năng thêm vào trong menu Chấm điểm)</td>
      <td>- Cho phép người dùng được cấp quyền kiểm định 1 có quyền sửa toàn bộ phần đánh giá của kiểm định 1 đồng thời sửa được đánh giá của Giám sát/trưởng nhóm chấm cuộc gọi đó - Tính năng tra cứu chức năng kiểm định 2: - Cho phép người dùng tìm kiếm cuộc gọi cần kiểm định theo thời gian, theo kết quả kiểm định 1, theo Giám sát/ trưởng nhóm, theo NV CSKH, số điện thoại KH gọi tổng đài, theo đối tác, theo ngưỡng xếp loại của cuộc gọi, theo lỗi đánh giá của kiểm định lần 1 với Giám sát/trưởng nhóm. - Cho phép tra cứu cuộc gọi đã chấm/ chưa chấm/ cuộc gọi lỗi theo đơn vị đối tác, theo Giám sát/ trưởng nhóm, NV</td>
      <td>- Bổ sung kiểm định cho kênh: chat, mail, video call. - Cho phép người dùng được cấp quyền kiểm định 1 có quyền sửa toàn bộ phần đánh giá của kiểm định 1 đồng thời sửa được đánh giá của Giám sát/trưởng nhóm chấm cuộc gọi đó - Tính năng tra cứu chức năng kiểm định 2: - Cho phép người dùng tìm kiếm cuộc gọi cần kiểm định theo thời gian, theo kết quả kiểm định 1, theo Giám sát/ trưởng nhóm, theo NV CSKH, số điện thoại KH gọi tổng đài, theo đối tác, theo ngưỡng xếp loại của cuộc gọi, theo lỗi đánh giá của kiểm định lần 1 với Giám sát/trưởng nhóm. - Cho phép tra cứu cuộc gọi đã chấm/ chưa chấm/ cuộc gọi lỗi theo đơn vị đối tác, theo Giám sát/ trưởng nhóm, NV CSKH, số điện thoại của KH gọi tổng đài. Đồng thời trong quá trình tra cứu xong có thể thực hiện sửa/ khôi phục cuộc gọi theo yêu cầu. - Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>CSKH, số điện thoại của KH gọi tổng đài. Đồng thời trong quá trình tra cứu xong có thể thực hiện sửa/ khôi phục cuộc gọi theo yêu cầu</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.12</td>
      <td>Hướng dẫn chấm điểm cuộc gọi (Nội dung này là hướng dẫn có tạo thành 1 menu trong chức năng chấm điểm không)?</td>
      <td>- Cần xác định cuộc gọi đầu vào -> Chấm điểm từng tiêu chí - >Xác định mức độ lỗi ảnh hưởng (nếu có)_> nhận xét và chọn bộ lỗi -> Điểm. - Xác định cuộc gọi đầu vào: phân dạng loại cuộc gọi - Chấm điểm từng tiêu chí: khung điểm của từng tiêu chí sẽ được đánh giá là n (OK), n+1 (NOK). Đối với tiêu chí không đạt yêu cầu, Giám sát phải chọn mức lỗi tương ứng. - Xác định mức độ lỗi ảnh hưởng đến KH: + NV CSKH không vi phạm lỗi: mức lỗi trong tham chấm điểm sẽ được để trống và cuộc gọi đạt ngưỡng Xuất sắc. + NV CSKH vi phạm lỗi: áp dụng trừ điểm theo mức lỗi đối với từng nhóm lỗi.</td>
      <td>Bổ sung màn hình hướng dẫn ==> Đề xuất bỏ</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>- Nhận xét và chọn bộ lỗi.</td>
      <td></td>
    </tr>
    <tr>
      <td>13.13</td>
      <td>Hướng dẫn cách tính điểm trung bình nghiệp vụ tháng (tạo thành 1 menu riêng)</td>
      <td>- Điểm trung bình nghiệp vụ của NV CSKH/ tháng = TBC điểm tất cả các cuộc gọi được đánh giá / tháng/ NV CSKH – điểm quy đổi. - điểm quy đổi sẽ</td>
      <td>Bổ sung màn hình hướng dẫn ==> Đề xuất bỏ</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>được cấu hình với điểm trừ.</td>
      <td></td>
    </tr>
    <tr>
      <td>II</td>
      <td>Chức năng cấu hình hệ thống</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.14</td>
      <td>Danh mục cấu hình thang điểm</td>
      <td>- Hệ thống cho phép người dùng khai báo, sửa xóa chỉ tiêu và trọng số tương ứng với từng đầu mục trong khu giải đáp và tỷ trọng. - Hệ thống hiển thị đầy đủ các chức năng sau: + Dạng cuộc gọi + Đầu mục cuộc gọi + Chỉ tiêu đánh giá cuộc gọi (n)/nhóm lỗi (n)/ mức lỗi (n).</td>
      <td>Xem trong menu quản lý tiêu chí chấm điểm, nếu đã đáp ứng thì bỏ mục này ==> đề xuất bỏ</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.15</td>
      <td>Danh mục cấu hình điểm quy đổi</td>
      <td>Hệ thống cho phép người dùng khai báo, sửa xóa điểm trừ tương ứng với từng điểm quy đổi</td>
      <td>- Bổ sung chức năng danh mục cấu hình điểm quy đổi cho phần Đánh giá đa kênh: - Tìm kiếm, sửa xóa, xuất dữ liệu - Cho phép phân quyền chức năng tới admin quản lý cấu hình - Cấu hình theo các tiêu chí : điểm trung bình tất cả các cuộc gọi được đánh giá trên tháng/NV CSKH. - Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.</td>
    </tr>
    <tr>
      <td>III</td>
      <td>Đánh giá Học viên</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.16</td>
      <td>Nhập thông tin học viên</td>
      <td>1 Cần trao đổi: - Dữ liệu thông tin học viên: --> Dữ liệu xuất ra fie hay nhập vào? - Cách thức đánh giá và đầy cuộc gọi về hệ thống: sử dụng cơ chế giống cuộc gọi offline đánh giá NV CKSH đang làm việc (giống như là như nào? ) . Nhập thông tin vào 2. Cách thức đánh giá và đầy cuộc gọi về hệ thống: sử dụng cơ chế giống cuộc gọi offline đánh giá</td>
      <td>Bổ sung 1 chức năng hoặc 1 tab đánh giá học viên - Chọn học viên (User) - Import danh sách học viên, tìm kiếm, sửa xóa hoạc viên, thêm học viên - Các thông tin chấm điểm tương tự đánh giá nhân viên - Bổ sung phân quyền admin có thể nhập thông tin hoặc viên - Cách thức đánh giá và đầy cuộc gọi về hệ thống: sử dụng cơ chế giống cuộc gọi offline đánh giá NV CKSH - Tính điểm trung bình các cuộc gọi theo công thức chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>NV CKSH đang làm việc (gọi dữ liệu từ hệ thống IPCC đẩy lên phần mềm chấm điểm, sử dụng thang điểm chấm offline)</td>
      <td></td>
    </tr>
    <tr>
      <td>13.17</td>
      <td>Báo cáo thống kê kết quả</td>
      <td>Cần trao đổi - Điểm đạt của học viên là trung bình điểm các cuộc gọi được chấm. - Thống kê kết quả theo nhân sự, đối tác - Biểu mẫu tổng hợp điểm các cuộc gọi của học viên như sau: --> Xuất file excel theo mẫu tại Phiếu yêu cầu</td>
      <td>- Điều chỉnh mẫu báo cáo thống kế theo mẫu mới nhất - Điểm đạt của hoặc viên là trung bìn điểm các cuộc gọi được chấm - Thống kê kết quả theo nhân sự, đối tác - Cho phép xuất file excel theo mẫu báo báo - Mẫu báo cáo tham khảo biểu mẫu tại phiếu yêu cầu có mã IBM 4075370 trên hệ thống quản lý sản xuất</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.18</td>
      <td>Test nghiệp vụ</td>
      <td>- Tạo mục nhập lưu dữ liệu NV CSKH toàn trung tâm (dữ liệu sẽ được cập nhật khi có NV CSKH mới, NV CSKH nghỉ). Dữ liệu NV CSKH được đánh giá theo user VSA - Trên giao diện nhập dữ liệu test nghiệp vụ, Giám sát sẽ nhập user NV CSKH tiếp nhận cuộc gọi test và đánh giá kết quả đạt/ không đạt trên các tiêu chí gồm: + Nghiệp vụ + Kỹ năng + Thái độ + Kết thúc cuộc gọi (chào KH) + Đánh giá chung + Phân loại nghiệp vụ + Ghi chú - Mục thống kê, báo cáo kết quả: - Giám sát chọn thời gian xuất file chi tiết các cuộc gọi test. - Chọn thời gian xuất kết quả theo user NV CKSH với các cột:</td>
      <td>- Bổ sung Chức năng (tab) nhập dữ liệu kết quả đánh giá test nghiệp vụ - Nhập đơn lẻ (theo lô) - Import theo file - User ĐTV theo VSA quản lý - Sửa tên thành yêu cầu (quản lý kết quả đánh giá test nghiệp vụ) - Bổ sung 1 báo cáo kết quả</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>tổng test, tổng đạt về đánh giá chung, cột tỷ lệ đạt (Tỷ lệ đạt =Tổng cuộc gọi đạt/ tổng cuộc gọi test). - Thống kê các cuộc gọi không đạt ở các tiêu chí (tùy chọn): trên các tiêu chí Nghiệp vụ, kỹ năng, thái độ, kết thúc cuộc gọi (chào KH), đánh giá chung, phân loại nghiệp vụ… Mẫu tổng hợp: --> Xuất file excel theo mẫu tại Phiếu yêu cầu</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>IV</td>
      <td>Tab chấm điểm cuộc gọi cho kênh chat đa kênh và mạng xã hội</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.19</td>
      <td>Chức năng chấm điểm offline (Chức năng chấm điểm offline đã có nhưng chỉ có duy nhất kênh Voice, chưa có các kênh: chat đã kênh và mạng xã hội--> Dữ liệu tương tác của KH khác với kênh Voice, đề xuất xây tab riêng. Anh /chị kỹ thuật đánh giá thêm có thể lựa chọn 1 trong 2 cách: (1) bổ sung thêm kênh chat đa kênh và mạng xã hội trong chức năng đã có hoặc (2) xây tab mới)</td>
      <td>- Nội dung tương tác của KH: + Nội dung hội thoại: hiển thị nội dung tương tác của KH dưới dạng hộp hội thoại có kèm thanh cuộn (kéo lên-xuống với các hội thoại có nội dung dài). + User của KH: hiển thị user tương tác của KH (dữ liệu lấy trên hệ thống Econtact). - Nhu cầu phản ánh khách hàng gồm 05 cấp nghiệp vụ: (tương tự như kênh Voice) - Thang điểm đánh giá cuộc gọi: Giữ nguyên tỷ trọng các tiêu chí giống như kênh Voice - Thang điểm gồm các tiêu chí: + Tiêu chí chính bao gồm: (1) Kiến thức chuyên môn nghiệp vụ, (2) ý thức trách nhiệm/ thái độ.</td>
      <td>- Chỉnh sửa Chấm điểm Offline, bổ sung kênh chat, video call, mạng xã hội để chấm - Lấy được ghi âm, hội thoại chat từ hệ thống Econtact - Xem được nội dung tương tác của KH: + Nội dung hội thoại: hiển thị nội dung tương tác của KH dưới dạng hộp hội thoại có kèm thanh cuộn (kéo lên-xuống với các hội thoại có nội dung dài). + User của KH: hiển thị user tương tác của KH (dữ liệu lấy trên hệ thống Econtact). - Nhu cầu phản ánh khách hàng gồm 05 cấp nghiệp vụ: (tương tự như kênh Voice) - Thang điểm đánh giá cuộc gọi: Giữ nguyên tỷ trọng các tiêu chí giống như kênh Voice - Thang điểm gồm các tiêu chí: + Tiêu chí chính bao gồm: (1) Kiến thức chuyên môn nghiệp vụ, (2) ý thức trách nhiệm/ thái độ. + Tiêu chí điểm trừ bao gồm: + Kỹ năng nói /viết, + Kỹ năng lắng nghe/ trình bày + Kỹ năng tra cứu + Tiến độ. - Nội dung chi tiết tham khảo nội dung Phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>+ Tiêu chí điểm trừ bao gồm: + Kỹ năng nói /viết, + Kỹ năng lắng nghe/ trình bày + Kỹ năng tra cứu + Tiến độ.</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.20</td>
      <td>Chấm điểm Online (Chức năng chấm điểm online đã có nhưng chỉ có duy nhất kênh Voice, chưa có các kênh: chat đã kênh và mạng xã hội)</td>
      <td>- Lấy được ghi âm, hội thoại chat từ hệ thống Econtact</td>
      <td>- Chỉnh sửa Chấm điểm Online, bổ sung kênh chat, video call, mạng xã hội để chấm - Lấy được ghi âm, hội thoại chat từ hệ thống Econtact - Nội dung chi tiết tham khảo nội dung Phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất</td>
    </tr>
    <tr>
      <td>13.21</td>
      <td>Kiểm định 1 (Chức năng kiểm định 1 đã có nhưng chỉ có duy nhất kênh Voice, chưa có các kênh: chat đã kênh và mạng xã hội)</td>
      <td>- Lấy được ghi âm, hội thoại chat từ hệ thống Econtact</td>
      <td>Chỉnh sửa chức năng kiểm định 1, bổ sung kênh chat, video call để kiểm định - Lấy được ghi âm, hội thoại chat từ hệ thống Econtact - Nội dung chi tiết tham khảo nội dung Phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất</td>
    </tr>
    <tr>
      <td>13.22</td>
      <td>Kiểm định 2(Chức năng kiểm định 2 đã có nhưng chỉ có duy nhất kênh Voice, chưa có các kênh: chat đã kênh và mạng xã hội)</td>
      <td>- Lấy được ghi âm, hội thoại chat từ hệ thống Econtact</td>
      <td>Chỉnh sửa chức năng kiểm định 2, bổ sung kênh chat, video call để kiểm định - Lấy được ghi âm, hội thoại chat từ hệ thống Econtact - Nội dung chi tiết tham khảo nội dung Phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất</td>
    </tr>
    <tr>
      <td>V</td>
      <td>Tạo tab chấm điểm cuộc gọi Videocall</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>







<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.26</td>
      <td>Kiểm định 2</td>
      <td>- Kết quả kiểm định lần 2: Tương tự kênh thoại (Voice) - Bổ sung thêm tiêu chí điểm trừ</td>
      <td>- Bổ sung tính năng Kết quả kiểm định lần 2, Tương tự kênh thoại (Voice) - Bổ sung thêm tiêu chí điểm trừ - Nói/Viết</td>
    </tr>
    <tr>
      <td>VI</td>
      <td>Tạo tab chấm điểm cho kênh Email</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.27</td>
      <td>Chấm điểm offline (Chức năng chấm điểm offline đã có nhưng chỉ có duy nhất kênh Voice, chưa kênh: Mail)</td>
      <td>- Giữ nguyên các tiêu chí và tỷ trọng của các tiêu chí trong thang điểm Email tương tự như kênh voice: + Nghiệp vụ + Ý thức/thái độ + Nói + Nghe + Tra cứu. - Bổ sung thêm tiêu chí Viết (cùng tiêu chí Nói trên thang điểm) - Khi chọn chấm email, hệ thống sẽ đẩy toàn bộ nội dung email lên phần mềm chấm điểm của NV CSKH tới KH theo user trả lời.</td>
      <td>- Giữ nguyên các tiêu chí và tỷ trọng của các tiêu chí trong thang điểm Email tương tự như kênh voice: + Nghiệp vụ + Ý thức/thái độ + Nói + Nghe + Tra cứu. - Bổ sung thêm tiêu chí Viết (cùng tiêu chí Nói trên thang điểm) - Khi chọn chấm email, hệ thống sẽ đẩy toàn bộ nội dung email lên phần mềm chấm điểm của NV CSKH tới KH theo user trả lời. - Nội dung chi tiết tham khảo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.28</td>
      <td>Kết quả chấm điểm cuộc gọi (nội dung này sẽ nằm trong Menu Chấm điểm)</td>
      <td>- Tổng hợp toàn bộ kết quả chấm của giám sát trong các ngày. Thông tin tìm kiếm tương tự kênh thoại (voice)</td>
      <td>- Có tính năng kết quả chấm điểm cuộc gọi (nằm trong menu chấm điểm - Tổng hợp toàn bộ kết quả chấm của giám sát trong các ngày. - Thông tin tìm kiếm tương tự kênh thoại (voice) - Bổ sung phân quyền chức năng cho giám sát viên có quyền thao tác - Nội dung chi tiết tham khảo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất</td>
    </tr>
    <tr>
      <td>13.29</td>
      <td>Kết quả kiểm định lần 1(Chức năng kiểm định 1 đã có nhưng chỉ có duy nhất kênh Voice, chưa kênh: Mail)</td>
      <td>- Tương tự kênh thoại (Voice) - Bổ sung thêm tiêu chí điểm trừ - Nói/Viết</td>
      <td>- Tương tự kênh thoại (Voice) - Bổ sung thêm tiêu chí điểm trừ - Nói/Viết - Bổ sung phân quyền chức năng cho giám sát viên có quyền thao tác - Nội dung chi tiết tham khảo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất</td>
    </tr>
    <tr>
      <td>13.30</td>
      <td>Kết quả kiểm định lần 2</td>
      <td>- Tương tự kênh thoại (Voice), (tương tự là như thế nào) - Bổ sung thêm tiêu chí điểm trừ - Nói/Viết</td>
      <td>- Bổ sung tính năng Kết quả kiểm định lần 2 cho kênh Email, Tương tự kênh thoại (Voice) - Bổ sung thêm tiêu chí điểm trừ - Nói/Viết - Chi tiết nội dung tham khảo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất</td>
    </tr>
    <tr>
      <td>VII</td>
      <td>Báo cáo</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.31</td>
      <td>Báo cáo đánh giá cảm xúc cuộc gọi</td>
      <td>- Bổ sung: - Thời gian: Từ ngày xxx- đến ngày xxx - User: chọn 1 hoặc tất cả - Kênh: chọn 1 hoặc tất cả - Đối tác: chọn 1 hoặc tất cả - Khu vực: chọn 1 hoặc tất cả - Thâm niên: chọn 1 hoặc tất cả</td>
      <td>Bổ sung báo cáo theo mẫu : - Cho phép tìm kiếm theo tiêu chí: + Thời gian: Từ ngày xxx- đến ngày xxx + User: chọn 1 hoặc tất cả + Kênh: chọn 1 hoặc tất cả + Đối tác: chọn 1 hoặc tất cả + Khu vực: chọn 1 hoặc tất cả + Thâm niên: chọn 1 hoặc tất cả - Cho phép xuất dữ liệu ra file excel theo tiêu chí tìm kiếm đã chọn. - Cho phép thể hiện dữ liệu dưới dạng biểu đồ - Mẫu báo cáo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất</td>
    </tr>
    <tr>
      <td>13.32</td>
      <td>Báo cáo “Chi tiết đánh giá cảm xúc cuộc gọi”:</td>
      <td>- Bổ sung: - Thời gian: Từ ngày xxx- đến ngày xxx - User: chọn 1 hoặc tất cả - Kênh: chọn 1 hoặc tất cả - Đối tác: chọn 1 hoặc tất cả - Khu vực: chọn 1 hoặc tất cả - Thâm niên: chọn 1 hoặc tất cả</td>
      <td>Bổ sung báo cáo theo mẫu : - Cho phép tìm kiếm theo tiêu chí: + Thời gian: Từ ngày xxx- đến ngày xxx + User: chọn 1 hoặc tất cả + Kênh: chọn 1 hoặc tất cả + Đối tác: chọn 1 hoặc tất cả + Khu vực: chọn 1 hoặc tất cả + Thâm niên: chọn 1 hoặc tất cả - Cho phép xuất dữ liệu ra file excel theo tiêu chí tìm kiếm đã chọn. - Cho phép thể hiện dữ liệu dưới dạng biểu đồ - Mẫu báo cáo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.33</td>
      <td>Báo cáo “Tỉ lệ đánh giá cảm xúc cuộc gọi”</td>
      <td>Xem được tỉ lệ đánh giá chính xác cảm xúc cuộc gọi</td>
      <td>Bổ sung báo cáo theo mẫu (như hiện tại đang dùng trên IPCC 1.0 cập nhật biểu mẫu mới nhất): - Cho phép tìm kiếm theo tiêu chí - Cho phép xuất dữ liệu ra file excel theo tiêu chí tìm kiếm đã chọn. - Cho phép thể hiện dữ liệu dưới dạng biểu đồ - Mẫu báo cáo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất</td>
    </tr>
    <tr>
      <td>13.34</td>
      <td>Báo cáo Tỷ lệ nhận diện của hệ thống</td>
      <td>- Tìm kiếm theo tiêu chí đã chọn và vẽ biểu đồ - Xuất excel - Tỷ lệ cuộc gọi đã đánh giá ngày/ tháng/ năm: vẽ biểu đồ hình tròn</td>
      <td>Bổ sung báo cáo theo mẫu (như hiện tại đang dùng trên IPCC 1.0 cập nhật biểu mẫu mới nhất): - Cho phép tìm kiếm theo tiêu chí - Cho phép xuất dữ liệu ra file excel theo tiêu chí tìm kiếm đã chọn. - Cho phép thể hiện Biểu đồ tỷ lệ cuộc gọi đã đánh giá ngày/tháng/năm (biểu đồ hình tròn) - Mẫu báo cáo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.35</td>
      <td>Báo cáo nhu cầu Phản ánh Khách hàng</td>
      <td>- Thời gian: Từ ngày - đến ngày (ngày tiếp nhận PAKH). - User tiếp nhận. - Mã cuộc gọi. - Số điện thoại gọi lên. - Nghiệp vụ các cấp 1,2,3,4,5 - Nội dung nhu cầu KH - Cho phép xuất dữ liệu ra file excel theo tiêu chí tìm kiếm đã chọn. - Biểu đồ nhu cầu PAKH</td>
      <td>Bổ sung báo cáo theo mẫu (như hiện tại đang dùng trên IPCC 1.0) - Thời gian: Từ ngày - đến ngày (ngày tiếp nhận PAKH). + User tiếp nhận. + Mã cuộc gọi. + Số điện thoại gọi lên. + Nghiệp vụ các cấp 1,2,3,4,5 + Nội dung nhu cầu KH - Cho phép xuất dữ liệu ra file excel theo tiêu chí tìm kiếm đã chọn. - Cho phép thể hiện Biểu đồ nhu cầu PAKH - Mẫu báo cáo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13.36</td>
      <td>Báo cáo kết quả chấm điểm (29 mẫu)</td>
      <td></td>
      <td>Bổ sung xây dựng 29 mẫu báo cáo theo mẫu báo cáo cập nhật mới nhât: - Danh sách báo cáo: 1. Báo cáo chất lượng giải đáp đối tác theo xếp loại 2. Báo cáo chất lượng giải đáp đơn vị đối tác theo thâm niên 3. Báo cáo chất lượng giải đáp theo thâm niên tổng hợp các đối tác 4. Báo cáo so sánh chất lượng giải đáp theo thâm niên của 2 tháng liền nhau 5. Báo cáo chất lượng giải đáp theo ngày (không phân biệt đối tác) 6. Báo cáo chất lượng giải đáp theo line 7. Báo cáo chất lượng giải đáp đối tác theo xếp loại 8. Báo cáo chất lượng giải đáp theo dạng cuộc gọi 9. Báo cáo chất lượng nhân sự tổng hợp đối tác theo thâm niên 10. Báo cáo chất lượng nhân sự theo thâm niên 2 tháng liền nhau theo khu vực 11. Báo cáo chất lượng nhân sự theo line 12. Báo cáo chất lượng nhân sự đối tác theo thâm niên 13. Báo cáo xu hướng Khách hàng và khả năng đáp ứng của ĐTV theo line 14. Báo cáo chi tiết lỗi nghiệp vụ theo line 15. Báo cáo chi tiết lỗi tiêu chí 16. Báo cáo chi tiết cơ cấu chấm điểm theo thời lượng cuộc gọi của từng đối tác 17. Báo cáo chi tiết cơ cấu chấm điểm theo dạng cuộc gọi của từng đối tác 18. Báo cáo chi tiết cơ cấu chấm điểm trên từng ĐTV 19. Báo cáo cơ cấu kiểm định theo dạng cuộc gọi 20. Báo cáo cơ cấu kiểm định theo xếp loại cuộc gọi theo đối tác 21. Báo cáo cơ cấu kiểm định theo thời lượng cuộc gọi theo đối tác 22. Báo cáo cơ cấu kiểm định chi tiết theo ĐTV 23. Báo cáo cơ cấu kiểm định theo đối tác (lũy kế) 24. Báo cáo chi tiết chất lượng chấm điểm Của kiểm định VT 25. Báo cáo chi tiết lỗi sai (nguyên nhân sai) của từng đối tác 26. Báo cáo chi tiết lỗi sai của từng giám sát 27. Báo cáo chi tiết lỗi sai (nguyên nhân sai) của từng đối tác 28. Báo cáo kết quả chấm điểm cuộc gọi kênh Videocall 29. Báo cáo tổng hợp chẩm điểm. - Mẫu báo cáo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất</td>
    </tr>
    <tr>
      <td>14</td>
      <td>Mobile Call(CG tư vấn bán hàng)</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>14.1</td>
      <td>Bổ sung cung cấp quyền VSA cho quyền chức năng lích sử cuộc gọi</td>
      <td></td>
      <td>- GD tra cứu cuộc gói bổ sung thông tin: loại kênh bán, user kênh bán trên chức năng nghe lịch sử cuộc gọi. - Bổ sung ma trận phân quyền cho chức năng gửi VSA để cấp quyền, cấp quyền cho các user có quyền thao tác</td>
    </tr>
    <tr>
      <td>14.2</td>
      <td>Khi login mất kết nối AG server Khi call log CG không có file ghi âm</td>
      <td></td>
      <td>- Kiểm tra lỗi khi login mất kết AG Server - Bổ sung trường hiển thị đường link đến file ghi âm - Cho phép kích vào file ghi âm có thể nghe lại</td>
    </tr>
    <tr>
      <td>14.3</td>
      <td>trên GD cuộc gọi tư vấn thể hiện thời gian cuộc gọi bao nhiêu thời gian</td>
      <td></td>
      <td>Trên GD cuộc gọi tư vấn thể hiện thời gian cuộc gọi bao nhiêu thời gian</td>
    </tr>
    <tr>
      <td>14.4</td>
      <td>Triển khai trên MAriaDB</td>
      <td></td>
      <td>Hệ thống mới sẽ triển khai trên MariaDB</td>
    </tr>
    <tr>
      <td>14.5</td>
      <td>Hiển thị một số các trường thông tin của khách hàng để ông tư vấn biết (như</td>
      <td></td>
      <td>Bổ sung màn hình thông tin key KH: đang dùng gói thuê bao gì, có đang dùng VTPay và một số thông tin key khác… trên giao dịch giao diện cuộc gọi</td>
    </tr>
    <tr>
      <td>15</td>
      <td>Video Call Quản lý bán hàng mới</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>15.1</td>
      <td>Tích hợp với CN giám sát cửa hàng, gám sát điểm bán để gọi được Video call đến một người trong đó</td>
      <td></td>
      <td>- Tích hợp với CN giám sát cửa hàng, gám sát điểm bán để gọi được Video call đến một người trong đó</td>
    </tr>
    <tr>
      <td>15.2</td>
      <td>Khi gọi videocall đến cửa hàng và điểm bán mà không kết nối có lựa chọn để chuyển cuộc gọi sang số tổng đài và điểm bán</td>
      <td></td>
      <td>Khi gọi videocall đến cửa hàng và điểm bán mà không kết nối có lựa chọn để chuyển cuộc gọi sang số tổng đài và điểm bán</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>15.3</td>
      <td>Bổ sung các mẫu báo cáo, các màn hình giám sát theo mẫu</td>
      <td></td>
      <td>- Bổ sung các mẫu báo cáo, các màn hình giám sát theo mẫu</td>
    </tr>
    <tr>
      <td>16</td>
      <td>Video Call xác minh khách hàng</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>16.1</td>
      <td>Bổ sung chức năng đánh giá cuộc gọi</td>
      <td>Chưa có chức năng đánh giá cuộc gọi (ĐTV hiện tại phải thống kê thủ công qua file excel rất bất tiện)</td>
      <td>- Hệ thống bổ sung báo cáo đánh giá cuộc gọi cho phép xuất dữ liệu ra file excel - Nâng cấp hệ thống cũ bổ sung báo cáo đánh giá cuộc gọi (có nhiều báo cáo)</td>
    </tr>
    <tr>
      <td>16.2</td>
      <td>Chức năng tra cứu lịch sử cuộc gọi</td>
      <td>Chưa nghe lại được cuộc gọi có hình ảnh, chỉ nghe đc âm thanh</td>
      <td>- Kiểm tra lại trên hệ thống cũ - Trên hệ thống mới phải đáp ứng được vấn đề này</td>
    </tr>
    <tr>
      <td>16.3</td>
      <td>Chức năng tra cứu lịch sử cuộc gọi</td>
      <td>3. Nhiều cuộc gọi ko tìm kiếm lại được (NN do đang bị đầy bộ nhớ)</td>
      <td>- Hệ thống hiện tại đang bị đầy bộ nhớ ==> thực hiện nâng cấp bộ nhớ theo kế hoạch thống nhất để giải quyết vấn đề này (phụ thuộc vào kế hoạch hạ tầng) - Trên hệ thống mới sẽ tự động đáp ứng vấn đề này</td>
    </tr>
    <tr>
      <td>16.4</td>
      <td>Quản lý cuộc gọi</td>
      <td>4. Thỉnh thoảng tại 1 thời điểm cuộc gọi bị rớt nhiều (ví dụ 16h ngày 14/6)</td>
      <td>- Kiểm tra tại sao tự dưng rớt và rớt hàng loạt - Khi rớt hàng loạt bên CSKH báo lại cho VTS để phối hợp kiểm tra tìm nguyên nhân</td>
    </tr>
    <tr>
      <td>16.5</td>
      <td>Quản lý cuộc gọi</td>
      <td>5 . Lỗi cuộc gọi đang tiếp nhận bị mất tín hiệu (TB tiếp nhận 80c/ngày)</td>
      <td>- Hiện tại hệ thống vẫn đáp ứng KPI - Khi có lỗi thì bên CSKH báo lại cho VTS để phối hợp kiểm tra - Trên hệ thống xây mới đảm bảo được KPI và giảm thiểu các lỗi này</td>
    </tr>
  </tbody>
</table>

# Public_442

<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.16</td>
      <td>Login hệ thống MyCC: 1 account chỉ được phép đăng nhập duy nhất trên 1 máy tính</td>
      <td>Login hệ thống MyCC: 1 account chỉ được phép đăng nhập duy nhất trên 1 máy tính => Hiện tại 1 user đăng nhập đồng thời trên nhiều vị trí (Khi cg đổ đến acc của ĐTV sẽ đổ đồng thời trên các thiết bị, ĐTV không thao tác để tiếp nhận, CG rớt)</td>
      <td>Login hệ thống MyCC: 1 account chỉ được phép đăng nhập duy nhất trên 1 máy tính => Hiện tại 1 user đăng nhập đồng thời trên nhiều vị trí (Khi cg đổ đến acc của ĐTV sẽ đổ đồng thời trên các thiết bị, ĐTV không thao tác để tiếp nhận, CG rớt)</td>
    </tr>
    <tr>
      <td>17.17</td>
      <td>Cuộc gọi đến ĐTV videocall chưa tự link sang BCCS</td>
      <td>Cuộc gọi đổ đến ĐTV trên Mycc => Khi ĐTV click nhận sẽ tự bung giao diện BCCS hiển thị thông tin thuê bao</td>
      <td>Cuộc gọi đổ đến ĐTV trên Mycc => Khi ĐTV click nhận sẽ tự bung giao diện BCCS hiển thị thông tin thuê bao</td>
    </tr>
    <tr>
      <td>17.18</td>
      <td>hiển thị thông tin cuộc gọi video 1 chiều, video 2 chiều, voice</td>
      <td>Khi có cuộc gọi đổ đến ĐTV, trên giao diện MyCC hiển thị thông báo loại cuộc gọi của KH là Videocall 1 chiều, 2 chiều, voice</td>
      <td>Khi có cuộc gọi đổ đến ĐTV, trên giao diện MyCC hiển thị thông báo loại cuộc gọi của KH là Videocall 1 chiều, 2 chiều, voice</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.19</td>
      <td>Tool thống kê dữ liệu Agent (dành cho BO): Tổng tiếp nhận, tổng rớt, thời gian nhấc máy, thời gian đàm thoại, thời gian các trạng thái làm việc/ Log chi tiết thay đổi trạng thái của Agent/ BC lưu lượng theo khoảng giờ (tổng vào, tổng rớt, tổng gặp)/</td>
      <td>TC chưa thực hiện được công tác cảnh báo đánh giá hiệu quả, ý thức làm việc củ NV CSKH</td>
      <td>Tool thống kê dữ liệu Agent (dành cho BO): Tổng tiếp nhận, tổng rớt, thời gian nhấc máy, thời gian đàm thoại, thời gian các trạng thái làm việc/ Log chi tiết thay đổi trạng thái của Agent/ BC lưu lượng theo khoảng giờ (tổng vào, tổng rớt, tổng gặp)/</td>
    </tr>
    <tr>
      <td>17.20</td>
      <td>Tool thống kê dữ liệu năng suất, thời gian Avaiable của Agent (dành cho Agent)</td>
      <td>TVV không nắm được hiệu suất công việc trong ca để đảm bảo năng suất và thời gian làm việc theo quy định</td>
      <td>Tool thống kê dữ liệu năng suất, thời gian Avaiable của Agent (dành cho Agent)</td>
    </tr>
    <tr>
      <td>17.21</td>
      <td>Cấu hình kết thúc cuộc gọi và chat chưa đồng bộ dẫn đến kéo dài thời gian xử lý (KH đã kết thúc call nhưng phiên chat vẫn để thời gian timeout theo cấu hình kênh chat, một số TH khách hàng lại gọi lại khi chat chưa out sẽ làm tăng lưu lượng vào)</td>
      <td>Cấu hình khi KH kết thúc Video call hệ thống sẽ kết thúc Chat (đảm bảo đúng tính chất tương tác, rút ngắn thời gian CG)</td>
      <td>Cấu hình kết thúc cuộc gọi và chat chưa đồng bộ dẫn đến kéo dài thời gian xử lý (KH đã kết thúc call nhưng phiên chat vẫn để thời gian timeout theo cấu hình kênh chat, một số TH khách hàng lại gọi lại khi chat chưa out sẽ làm tăng lưu lượng vào)</td>
    </tr>
    <tr>
      <td>17.22</td>
      <td>Tình trạng gửi tin báo "Gửi lỗi" do KH đã thoát tính năng Chat, tuy nhiên phía TVV không có nhận biết, phải chờ KH, hết thời gian time out mới được ngắt kết nối</td>
      <td>kéo dài thời gian xử lý, YC đối với TH khách hàng tự ngắt phiên chat, thoát khỏi tính năng => Hệ thống cần cấu hình kết thúc phiên chat, có thông báo cho</td>
      <td>Tình trạng gửi tin báo "Gửi lỗi" do KH đã thoát tính năng Chat, tuy nhiên phía TVV không có nhận biết, phải chờ KH, hết thời gian time out mới được ngắt kết nối</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>TVV, giải phóng kênh</td>
      <td></td>
    </tr>
    <tr>
      <td>17.23</td>
      <td>Hệ thống chưa hiển thị số thuê bao trên giao diện chat phía KH</td>
      <td>Hiển thị số thuê bao trên giao diện chat phía KH theo đúng cấu hình trên kênh chat 4G</td>
      <td>Hệ thống chưa hiển thị số thuê bao trên giao diện chat phía KH</td>
    </tr>
    <tr>
      <td>17.24</td>
      <td>Xuất file chi tiết kênh Call me back chưa có thời gian KH đặt lịch hẹn</td>
      <td>chưa có số liệu ảnh hưởng đến công tác báo cáo thống kê nhu cầu KH</td>
      <td>Xuất file chi tiết kênh Call me back chưa có thời gian KH đặt lịch hẹn</td>
    </tr>
    <tr>
      <td>17.25</td>
      <td>Tính năng tự động gọi ra trên CMB</td>
      <td>Ảnh hưởng đến hoạt động giải dáp KH</td>
      <td>Tính năng tự động gọi ra trên CMB</td>
    </tr>
    <tr>
      <td>17.26</td>
      <td>Tool dành cho BO vận hành thực hiện các thao tác: Add thêm user nghe line cho Agent, user BO; reset mật khẩu đăng nhập hệ thống; gán/thay đổi queue giải đáp cho Agent</td>
      <td>Chưa hỗ trợ được kịp thời trong ca trực ảnh hưởng đến hoạt động giải đáp</td>
      <td>Tool dành cho BO vận hành thực hiện các thao tác: Add thêm user nghe line cho Agent, user BO;khoá/mở khoá mật khẩu đăng nhập hệ thống ; gán/thay đổi queue giải đáp cho Agent</td>
    </tr>
    <tr>
      <td>17.27</td>
      <td>Tool báo cáo số liệu https://10.60.96.72:8692/report chưa chính xác, tình trạng đăng nhập hệ thống chập chờn thường xuyên báo lỗi</td>
      <td>YC hoàn thiện và bàn giao tài liệu cho các tool lấy số liệu, thống nhất cách lấy SL.</td>
      <td>Tool báo cáo số liệu https://10.60.96.72:8692/report chưa chính xác, tình trạng đăng nhập hệ thống chập chờn thường xuyên báo lỗi - Bổ sung kiểm tra tình trạng đăng nhập hệ thống báo cáo số liệu - Chỉnh sửa lại các lỗi sau khi xác định được nguyên nhân lỗi</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.28</td>
      <td>Hệ thống chưa tối ưu, user của người dùng không vào được đủ các link của hệ thống eContact; hệ thống đang phân quyền 1 user chỉ vào được 1 trong 2 trang eContact Chat đa kênh hoặc Videp call đa kênh => bất cập trong công tác điều hành do nhân sự có thể dùng chung</td>
      <td>YC tạo lại quyền truy cập hệ thống</td>
      <td>- Trên hệ thống mới sẽ tập trung chức năng và việc phân quyền theo nhóm sẽ đảm bảo được các tài khoản sẽ có đầy đủ các chức năng theo phân quyền.</td>
    </tr>
    <tr>
      <td>17.29</td>
      <td>Bộ đếm thời gian khi chạy clip chờ trên Video call.</td>
      <td>KH không nắm được thời gian chờ kết nối</td>
      <td>Hiển thị bộ đếm thời gian video chờ</td>
    </tr>
    <tr>
      <td>17.30</td>
      <td>ĐTV, TC phải xác thực 10 link mới vào được hệ thống mỗi lần chuyển máy tính khác hoặc xóa cache lại phải xác thực lại => khó khăn, mới thời gian</td>
      <td>Bất cập, mất thời gian</td>
      <td>ĐTV, TC phải xác thực 10 link mới vào được hệ thống mỗi lần chuyển máy tính khác hoặc xóa cache lại phải xác thực lại => khó khăn, mới thời gian</td>
    </tr>
    <tr>
      <td>17.31</td>
      <td>Tính năng nghe cuộc gọi Offline hiện file ghi âm đang bị chia thành 2 cửa sổ KH và TVV, giám sát không sử dụng được chế độ tua ghi âm</td>
      <td>Tối ưu gộp thành 1 cửa sổ để GS thực hiện chế độ tua</td>
      <td>Tính năng nghe cuộc gọi Offline hiện file ghi âm đang bị chia thành 2 cửa sổ KH và TVV => Gộp thành 1 file ghi âm (voice của cả KH và ĐTV)</td>
    </tr>
    <tr>
      <td>17.32</td>
      <td>Hiển thị thời gian phiên chat trên giao diện KH đến giây</td>
      <td>ĐTV chưa xác định được thời gian chat. YC hiện thị chính xác đến giây</td>
      <td>Hiển thị thời gian phiên chat (giây)</td>
    </tr>
    <tr>
      <td>17.33</td>
      <td>Tính năng Tổng đài 4G chưa được tích hợp lên web Portal</td>
      <td>Theo bài toán ban đầu</td>
      <td>- Bổ sung tính năng tổng đài 4G lên web Portal - Đưa thành webview (nhúng link web)</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.34</td>
      <td>Chưa có tính năng chấm điểm cuộc gọi.</td>
      <td>GS chấm thủ công trên file excel, khó kiểm soát => tính năng theo Theo bài toán ban đầu</td>
      <td>- Bổ sung chức năng cấu hình chấm điểm cuội gọi - Bổ sung tự động tính điểm cuộc gọi sau khi cuộc gọi kết thúc - Bổ sung giao diện xem thông tin chấm điểm cuộc gọi</td>
    </tr>
    <tr>
      <td>17.35</td>
      <td>Chưa có hệ thống đánh giá hài lòng</td>
      <td>Chưa đánh giá được ý kiến của KH. YC bổ sung hiện đã có tính năng này trên Chat đa kênh- eContact</td>
      <td>- Bổ sung chức năng đánh giá hài lòng khi kết thúc luồng gọi</td>
    </tr>
    <tr>
      <td>17.36</td>
      <td>Hiện tại hệ thống chưa có tool thống kê các cuộc gọi ĐTV tự kết thúc khi cuộc gọi đã đổ đến agent</td>
      <td>YC bổ sung tool thống kê</td>
      <td>Bổ sung tool thống kê các cuộc gọi ĐTV tự kết thúc khi cuộc gọi đã đổ đến agent</td>
    </tr>
    <tr>
      <td>17.37</td>
      <td>Khi kết thúc cuộc gọi VideoCall có các chức năng SMS, play quảng cáo…</td>
      <td>- Khi kết thúc cuộc gọi VideoCall có các chức năng SMS, play quảng cáo…</td>
      <td>- Khi kết thúc cuộc gọi VideoCall có các chức năng SMS, play quảng cáo… - Phát video quảng cáo: Khi ĐTV kết thúc trước - Gửi sms quảng cáo đến thuê bao sau khi kết thúc - Hệ thống tự phát được video/ gửi sms</td>
    </tr>
    <tr>
      <td>17.38</td>
      <td>Giao diện có các khu vực header và footer dành cho quảng cáo, khu vực này có thể cấu hình text chạy hoặc ảnh động hoặc cảnh báo dịch vụ của khách hàng</td>
      <td>Cho phép hình text chạy hoặc cảnh báo dịch vụ của KH ở khu vực header và footer dành cho quảng cáo</td>
      <td>Giao diện có các khu vực header và footer dành cho quảng cáo, khu vực này có thể cấu hình text chạy hoặc ảnh động hoặc cảnh báo dịch vụ của khách hàng</td>
    </tr>
    <tr>
      <td>17.39</td>
      <td>+ Hiển thị cảnh báo chất lượng sóng trực quan bằng biểu tượng và màu sắc hiển thị realtime, có 3-5 mức độ chất lượng.</td>
      <td>Hiển thị cảnh báo chất lượng sóng trực quan bằng biểu tượng và màu sắc hiển thị realtime, có 3-5 mức độ chất lượng</td>
      <td>Hiển thị cảnh báo chất lượng sóng trực quan bằng biểu tượng và màu sắc hiển thị realtime, có 3-5 mức độ chất lượng. (Sóng thoại)</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.40</td>
      <td>Thời gian chờ trong Queue sẽ do bộ phận kỹ thuật tự cấu hình. Khi KH chờ hết thời gian timeout, hệ thống tự động bật ra cửa sổ Đặt lịch hẹn gọi lại để KH thiết lập lịch hẹn gọi lại sau.</td>
      <td>Thời gian chờ trong Queue sẽ do bộ phận kỹ thuật tự cấu hình. Khi KH chờ hết thời gian timeout, hệ thống tự động bật ra cửa sổ Đặt lịch hẹn gọi lại để KH thiết lập lịch hẹn gọi lại sau.</td>
      <td>Thời gian chờ trong Queue sẽ do bộ phận kỹ thuật tự cấu hình. Khi KH chờ hết thời gian timeout, hệ thống tự động bật ra cửa sổ Đặt lịch hẹn gọi lại để KH thiết lập lịch hẹn gọi lại sau.</td>
    </tr>
    <tr>
      <td>17.41</td>
      <td>Chức năng cấu hình bắt buộc khách hàng xem hết video chờ trong khoảng x giây mới chuyển đến ĐTV rảnh (ĐTV rảnh cũng ko tiếp nhận ngay mà KH phải xem hết đoạn video)</td>
      <td>- chức năng cấu hình bắt buộc khách hàng xem hết video chờ trong khoảng x giây mới chuyển đến ĐTV rảnh (ĐTV rảnh cũng ko tiếp nhận ngay mà KH phải xem hết đoạn video)</td>
      <td>- chức năng cấu hình bắt buộc khách hàng xem hết video chờ trong khoảng x giây mới chuyển đến ĐTV rảnh (ĐTV rảnh cũng ko tiếp nhận ngay mà KH phải xem hết đoạn video)</td>
    </tr>
    <tr>
      <td></td>
      <td>Nghe offline</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.42</td>
      <td>Link với phần đánh giá cuộc gọi</td>
      <td>Khi nghe lại cuộc gọi, nếu muốn đánh giá chấm điểm cuộc gọi đó GS sẽ tích vào nút Chấm điểm (bên cạnh nút Nghe offline), khi đó hệ thống sẽ link sang phần chấm điểm để đánh giá các tiêu chí như quy định.</td>
      <td>Khi nghe lại cuộc gọi, nếu muốn đánh giá chấm điểm cuộc gọi đó GS sẽ tích vào nút Chấm điểm (bên cạnh nút Nghe offline), khi đó hệ thống sẽ link sang phần chấm điểm để đánh giá các tiêu chí như quy định.</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.43</td>
      <td>Lưu dữ liệu ghi âm và phiên chat</td>
      <td>Cho phép GS/TC xuất và tải file ghi âm (voice call, video call, call back) và dữ liệu chi tiết phiên chát về máy tính.</td>
      <td>Cho phép GS/TC xuất và tải file ghi âm (voice call, video call, call back) và dữ liệu chi tiết phiên chát về máy tính.</td>
    </tr>
    <tr>
      <td>17.44</td>
      <td>Nhận diện chế độ hold,mute máy trong cuộc gọi của ĐTV</td>
      <td>Khi nghe lại cuộc gọi, GS có thể nhận diện được ĐTV đã hold máy hay mute máy.</td>
      <td>Khi nghe lại cuộc gọi, GS có thể nhận diện được ĐTV đã hold máy hay mute máy.</td>
    </tr>
    <tr>
      <td></td>
      <td>Nghe online</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.45</td>
      <td>Đánh dấu lỗi sai</td>
      <td>Khi GS/TC nghe online,GS có thể note vào file ghi âm đoạn ĐTV bị sai. Phần này GS sẽ tích vào nút Nhắc nhở.( cạnh với nút Nghe online và nút Chấm điểm)</td>
      <td>Khi GS/TC nghe online,GS có thể note vào file ghi âm đoạn ĐTV bị sai. Phần này GS sẽ tích vào nút Nhắc nhở.( cạnh với nút Nghe online và nút Chấm điểm) Cho phép đánh dấu vào thời điểm cần nhắc nhở => Xuất file biết được thời điểm bị nhắc nhở</td>
    </tr>
    <tr>
      <td>17.46</td>
      <td>Nói thầm với ĐTV</td>
      <td>Khi ĐTV trả lời cuộc gọi nhưng cần hỗ trợ, GS/TC nghe online có thể nhắc ĐTV trực tiếp trong cuộc gọi, nội dung nhắc này chỉ ĐTV nghe thấy- không làm ảnh hưởng tới KH</td>
      <td>Khi ĐTV trả lời cuộc gọi nhưng cần hỗ trợ, GS/TC nghe online có thể nhắc ĐTV trực tiếp trong cuộc gọi, nội dung nhắc này chỉ ĐTV nghe thấy- không làm ảnh hưởng tới KH</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.47</td>
      <td>Đàm thoại nhóm</td>
      <td>Khi GS/TC nghe online, nếu KH yêu cầu gặp GS hoặc nội dung cuộc gọi cần can thiệp, GS có thể sử dụng chức năng này để đàm thoại 3 bên: KH- ĐTV- GS</td>
      <td>- Khi GS/TC nghe online, nếu KH yêu cầu gặp GS hoặc nội dung cuộc gọi cần can thiệp, GS có thể sử dụng chức năng này để đàm thoại 3 bên: KH- ĐTV- GS - ĐTV không thể nói (tự động mute), Không hiển thị hình giám sát</td>
    </tr>
    <tr>
      <td>17.48</td>
      <td>Chat hỗ trợ</td>
      <td>Khi ĐTV trả lời cuộc gọi / phiên chat nhưng cần hỗ trợ, GS/TC chat tới ĐTV nội dung cần nhắc nhở. Nội dung này sẽ hiển thị trên màn hình ĐTV</td>
      <td>Khi ĐTV trả lời cuộc gọi / phiên chat nhưng cần hỗ trợ, GS/TC chat tới ĐTV nội dung cần nhắc nhở. Nội dung này sẽ hiển thị trên màn hình ĐTV</td>
    </tr>
    <tr>
      <td>17.49</td>
      <td>Gọi điện hỗ trợ</td>
      <td>Khi ĐTV trả lời phiên chat nhưng cần hỗ trợ, GS/TC có thể gọi trực tiếp tới ID ĐTV để nhắc nhở.</td>
      <td>Khi ĐTV trả lời phiên chat (Không áp dụng với kênh thoại) nhưng cần hỗ trợ, GS/TC có thể gọi trực tiếp tới ID ĐTV để nhắc nhở (Không cho chiều ngược lại, hoặc ĐTV gọi cho ĐTV)</td>
    </tr>
    <tr>
      <td>17.50</td>
      <td>Add danh sách nghe online</td>
      <td>Cho phép GS/TC nghe online toàn bộ nhân viên có trong ca trực, hoặc add danh sách nghe online theo chủ đích( vd: nhân sự yếu, nhân sự mới lên line, nhân sự vi phạm thái độ)</td>
      <td>Cho phép GS/TC nghe online toàn bộ nhân viên có trong ca trực, hoặc add danh sách nghe online theo chủ đích( vd: nhân sự yếu, nhân sự mới lên line, nhân sự vi phạm thái độ)</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.51</td>
      <td>Cảnh báo cuộc gọi dài</td>
      <td>Trong ca, nếu có cuộc gọi của ĐTV kéo dài >5p, hệ thống sẽ có cảnh báo (cảnh báo dạng pop up hoặc màu sắc) để GS/TC dễ phát hiện, dễ can thiệp cắt cuộc gọi khi cần.</td>
      <td>Trong ca, nếu có cuộc gọi của ĐTV kéo dài >5p, hệ thống sẽ có cảnh báo (cảnh báo dạng pop up hoặc màu sắc) để GS/TC dễ phát hiện, dễ can thiệp cắt cuộc gọi khi cần.</td>
    </tr>
    <tr>
      <td>17.52</td>
      <td>Link với phần đánh giá chấm điểm</td>
      <td>Khi nghe online CG/ xem online phiên chát nếu muốn đánh giá chấm điểm CG/phiên chát đó GS sẽ tích vào nút Chấm điểm (bên cạnh nút Nghe online), khi đó hệ thống sẽ link sang phần chấm điểm để đánh giá các tiêu chí như quy định.</td>
      <td>Khi nghe online CG/ xem online phiên chát nếu muốn đánh giá chấm điểm CG/phiên chát đó GS sẽ tích vào nút Chấm điểm (bên cạnh nút Nghe online), khi đó hệ thống sẽ link sang phần chấm điểm để đánh giá các tiêu chí như quy định.</td>
    </tr>
    <tr>
      <td>17.53</td>
      <td>Nhận diện chế độ hold,mute máy trong cuộc gọi của ĐTV</td>
      <td>Khi nghe online cuộc gọi, GS có thể nhận diện được ĐTV đã hold máy hay mute máy.</td>
      <td>Khi nghe online cuộc gọi, GS có thể nhận diện được ĐTV đã hold máy hay mute máy.</td>
    </tr>
    <tr>
      <td></td>
      <td>Quản lý cuộc gọi ra của ĐTV</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.54</td>
      <td>Thống kê offline chi tiết cuộc gọi ra</td>
      <td>1. Điều kiện chọn: + Chọn kênh (Không chọn sẽ thống kê tất cả các kênh) + Chọn thời gian 2. Kết quả thống kê: + Tổng cuộc gọi thành công, Tổng thất bại (nguyên nhân: KH không nghe máy, KH từ chối), Thời gian chờ, Tổng thời gian đàm thoại, Thời gian chờ TBinh, Tổng nhân sự.</td>
      <td>1. Điều kiện chọn: + Chọn kênh (Không chọn sẽ thống kê tất cả các kênh) + Chọn thời gian 2. Kết quả thống kê: + Tổng cuộc gọi thành công, Tổng thất bại (nguyên nhân: KH không nghe máy, KH từ chối), Thời gian chờ, Tổng thời gian đàm thoại, Thời gian chờ TBinh, Tổng nhân sự.</td>
    </tr>
    <tr>
      <td>17.55</td>
      <td>Theo dõi Online</td>
      <td>Tính năng này sẽ theo dõi cả kênh Call back và các cuộc HPC khác trên tổng đài: 1. Điều kiện chọn: + Kênh cần theo dõi: ví dụ Call back/ happy call 2. Kết quả Online: Kênh, Số thuê bao, thời gian gọi ra thời lượng cuộc gọi</td>
      <td>Tính năng này sẽ theo dõi cả kênh Call back và các cuộc HPC khác trên tổng đài: 1. Điều kiện chọn: + Kênh cần theo dõi: ví dụ Call back/ happy call 2. Kết quả Online: Kênh, Số thuê bao, thời gian gọi ra thời lượng cuộc gọi</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.56</td>
      <td>Thống kê chi tiết theo Agent gọi ra</td>
      <td>1. Điều kiện chọn: + Chọn ĐTV; Chọn kênh (nếu không chọn kênh sẽ xuất chi tiết ĐTV trên tất cả các kênh) + Ô tìm kiếm nâng cao để search nhiều ĐTV + Ô nhập thời gian 2. Kết quả: + Xuất chi tiết theo ĐTV gồm: kênh, số TB, thời gian gọi ra + Trạng thái kết thúc cuộc gọi.</td>
      <td>1. Điều kiện chọn: + Chọn ĐTV; Chọn kênh (nếu không chọn kênh sẽ xuất chi tiết ĐTV trên tất cả các kênh) + Ô tìm kiếm nâng cao để search nhiều ĐTV + Ô nhập thời gian 2. Kết quả: + Xuất chi tiết theo ĐTV gồm: kênh, số TB, thời gian gọi ra + Trạng thái kết thúc cuộc gọi.</td>
    </tr>
    <tr>
      <td></td>
      <td>Call me back</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.57</td>
      <td>Tần suất</td>
      <td>Thống kê số lần gọi ra cho các thuê bao</td>
      <td>Thống kê số lần gọi ra cho các thuê bao</td>
    </tr>
    <tr>
      <td>17.58</td>
      <td>Thống kê tổng hợp đánh giá chỉ số kết nối của kênh call me back</td>
      <td>Thống kê chi tiết tương tác có đánh giá NOK và OK đối với từng tương tác</td>
      <td>Thống kê chi tiết tương tác có đánh giá NOK và OK đối với từng tương tác</td>
    </tr>
    <tr>
      <td>17.59</td>
      <td>Thống kê nhu cầu thực KH (căn cứ trên nội dung ĐTV gọi lại cho KH)</td>
      <td>Thống kê nhu cầu KH theo nội dung thực tế ĐTV tick khi gọi lại cho KH</td>
      <td>Thống kê nhu cầu KH theo nội dung thực tế ĐTV tick khi gọi lại cho KH</td>
    </tr>
  </tbody>
</table>











<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.62</td>
      <td>Cơ chế gọi lại của hệ thống</td>
      <td>Khi KH đặt lịch hẹn gọi lại thành công, hệ thống sẽ thiết lập thông tin đặt lịch của KH trong queue chờ (hàng đợi) theo nguyên tắc như sau: - Thiết lập cuộc gọi trong hàng đợi theo khung thời gian mà KH đặt lịch. Trường hợp 2 cuộc gọi đặt lịch cùng 1 khung giờ thì KH nào đặt lịch trước sẽ được thiết lập trước. - Trường hợp cùng 1 khung giờ, có quá nhiều lịch hẹn được thiết lập, hệ thống gọi lần lượt. - Nếu KH không chọn khoảng giờ gọi lại, hệ thống sẽ thiết lập thời gian gần nhất, khi có Agent rảnh sẽ kết nối ngay</td>
      <td>Khi KH đặt lịch hẹn gọi lại thành công, hệ thống sẽ thiết lập thông tin đặt lịch của KH trong queue chờ (hàng đợi) theo nguyên tắc như sau: - Thiết lập cuộc gọi trong hàng đợi theo khung thời gian mà KH đặt lịch. Trường hợp 2 cuộc gọi đặt lịch cùng 1 khung giờ thì KH nào đặt lịch trước sẽ được thiết lập trước. - Trường hợp cùng 1 khung giờ, có quá nhiều lịch hẹn được thiết lập, hệ thống gọi lần lượt. - Nếu KH không chọn khoảng giờ gọi lại, hệ thống sẽ thiết lập thời gian gần nhất, khi có Agent rảnh sẽ kết nối ngay</td>
    </tr>
  </tbody>
</table>











<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Theo dõi thuê bao quấy rối</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.67</td>
      <td>Tra cứu lịch sử thuê bao bị chặn vì quấy rối</td>
      <td>1. Điều kiện chọn: + Chọn tool Quấy rối + Nhập số thuê bao + Khoảng thời gian muốn tra cứu * Cơ chế chặn QR tự động: + Thống kê lịch sử thuê bao, thời gian chặn, nguyên nhân chặn (system, hoặc user chặn nếu bị chặn thủ công)</td>
      <td>1. Điều kiện chọn: + Chọn tool Quấy rối + Nhập số thuê bao + Khoảng thời gian muốn tra cứu * Cơ chế chặn QR tự động: + Thống kê lịch sử thuê bao, thời gian chặn, nguyên nhân chặn (system, hoặc user chặn nếu bị chặn thủ công)</td>
    </tr>
    <tr>
      <td>17.68</td>
      <td>Quản lý thuê bao quấy rối</td>
      <td>1. Thống kê + Chọn tool Quấy rối + Ấn nút thống kê => Hệ thống hiển thị danh sách thuê bao đang bị chặn trên hệ thống gồm cả chặn tự động và chặn thủ công gồm số liệu: Số thuê bao, thời gian chặn, nguyên nhân chặn (system, hoặc user chặn nếu bị chặn thủ công), nút tick để tác động mở. Khi tác động mở chiều hệ thống có trường ghi rõ nguyên nhân). 2. Tác động chặn thuê bao quấy rối:</td>
      <td>1. Thống kê + Chọn tool Quấy rối + Ấn nút thống kê => Hệ thống hiển thị danh sách thuê bao đang bị chặn trên hệ thống gồm cả chặn tự động và chặn thủ công gồm số liệu: Số thuê bao, thời gian chặn, nguyên nhân chặn (system, hoặc user chặn nếu bị chặn thủ công), nút tick để tác động mở. Khi tác động mở chiều hệ thống có trường ghi rõ nguyên nhân). 2. Tác động chặn thuê bao quấy rối: + Chọn tool Quấy rối + Nhập số thuê bao + import danh sách (chặn/mở) + Ấn nút tác động chặn, Nhập trường: ghi rõ nguyên nhân chặn</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>+ Chọn tool Quấy rối + Nhập số thuê bao + Ấn nút tác động chặn, Nhập trường: ghi rõ nguyên nhân chặn</td>
      <td></td>
    </tr>
    <tr>
      <td>17,69</td>
      <td>Tính năng chặn quấy rối</td>
      <td>Tình trạng KH quấy rối hình ảnh liên tục xảy ra ảnh hưởng đến tâm lý ĐTV, chưa có hướng xử KH không có nhu cầu thực</td>
      <td>Tình trạng KH quấy rối hình ảnh liên tục xảy ra ảnh hưởng đến tâm lý ĐTV, chưa có hướng xử KH không có nhu cầu thực</td>
    </tr>
    <tr>
      <td></td>
      <td>Nhắn tin</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.70</td>
      <td>nhắn tin cho Agent hoặc 1 nhóm Agent</td>
      <td>1. Điều kiện chọn: + Chọn tool Nhắn tin + Ô nhập mã Agent, hoặc danh sách Agent + Ô chọn nhóm: Hệ thống gom sẵn theo nhóm ĐTV đã được chia sẵn. + Ô nhập nội dung tin nhắn => Nút gửi, hiển thị Alias + Trường loại bỏ thuê bao/ nhiều TB ra khỏi danh sách nhắn tin: Nhập số thuê bao => Ấn thực hiện 2. Kết quả: + Trưởng ca nhắn tin thông báo đến nhóm nhân sự ĐTV GS, TC.. điều kiện là số thuê bao đã được add trên hệ thống, không nhắn được các số ngoài DS + Trưởng ca loại bỏ các số thuê bao ra khỏi danh sách nhắn tin</td>
      <td>- Bổ sung Popup cảnh báo IPCC cho Agent hoặc 1 nhóm Agent</td>
    </tr>
    <tr>
      <td></td>
      <td>Thông tin agent</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.71</td>
      <td>Tổng hợp thông tin tiếp nhận giải đáp trong ca</td>
      <td>ĐTV có thể nhìn được tổng cuộc gọi/phiên chát đã tiếp nhận trong ca trực đó, ví dụ: số cuộc gọi được phục vụ, số cuộc gọi rớt do KH, số cuộc gọi rớt do ĐTV, tổng thời gian trả lời</td>
      <td>ĐTV có thể nhìn được tổng cuộc gọi/phiên chát đã tiếp nhận trong ca trực đó, ví dụ: số cuộc gọi được phục vụ, số cuộc gọi rớt do KH, số cuộc gọi rớt do ĐTV, tổng thời gian trả lời</td>
    </tr>
    <tr>
      <td></td>
      <td>Nhóm tính năng tiếp nhận giải đáp dành cho NV CSKH</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.72</td>
      <td>Tiếp nhận cuộc gọi</td>
      <td>Sau khi cuộc gọi kết nối thành công với NV CSKH, giao diện tiếp nhận cuộc gọi của NV CSKH sẽ có các tính năng sau: Pick up trả lời cuộc gọi vào/Cuộc gọi ra; Hold máy; Mute máy; Tranfer cuộc gọi sang Agent khác; Bật/tắt hình ảnh phía KH; Kết thúc cuộc gọi.</td>
      <td>Sau khi cuộc gọi kết nối thành công với NV CSKH, giao diện tiếp nhận cuộc gọi của NV CSKH sẽ có các tính năng sau: Pick up trả lời cuộc gọi vào/Cuộc gọi ra; Hold máy; Mute máy; Tranfer cuộc gọi sang Agent khác; Bật/tắt hình ảnh phía KH; Kết thúc cuộc gọi.</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.73</td>
      <td>Chuyển trạng thái Agent và thông tin agent trong ca trực</td>
      <td>Đây là tính năng cho phép NV CSKH chọn/chuyển các trạng thái trong ca trực. Trên hệ thống có hiển thị thời lượng của chế độ hiện tại, cảnh báo đỏ khi quá thời gian chế độ cho phép. Hệ thống sẽ có 08 trạng thái gồm: Availble; Not Availble; Availble - No ACD; Meeting; Typing; At lunch; No Answer; Go out</td>
      <td>Đây là tính năng cho phép NV CSKH chọn/chuyển các trạng thái trong ca trực. Trên hệ thống có hiển thị thời lượng của chế độ hiện tại, cảnh báo đỏ khi quá thời gian chế độ cho phép. Hệ thống sẽ có 08 trạng thái gồm: Availble; Not Availble; Availble - No ACD; Meeting; Typing; At lunch; No Answer; Go out</td>
    </tr>
    <tr>
      <td>17.74</td>
      <td>Tính năng tương tác song song</td>
      <td>Cho phép NV CSKH sử dụng song song 2 tính năng để hỗ trợ KH. Ví dụ: NV CSKH tiếp nhận cuộc gọi video, trong quá trình tương tác, NV CSKH có thể bật thêm tính năng Chat hoặc ngược lại</td>
      <td>Cho phép NV CSKH sử dụng song song 2 tính năng để hỗ trợ KH. Ví dụ: NV CSKH tiếp nhận cuộc gọi video, trong quá trình tương tác, NV CSKH có thể bật thêm tính năng Chat hoặc ngược lại</td>
    </tr>
    <tr>
      <td>17.75</td>
      <td>Gọi ra cho KH</td>
      <td>Tính năng này cho phép NV CSKH thực hiện cuộc gọi ra cho KH từ hệ thống bằng cách nhập số điện thoại cần gọi,</td>
      <td>Tính năng này cho phép NV CSKH thực hiện cuộc gọi ra cho KH từ hệ thống bằng cách nhập số điện thoại cần gọi, nhấn nút gọi ra. Cuộc gọi ra sẽ được ghi âm</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>nhấn nút gọi ra. Cuộc gọi ra sẽ được ghi âm</td>
      <td></td>
    </tr>
    <tr>
      <td>17.76</td>
      <td>Hủy lịch hẹn gọi lại khi KH yêu cầu</td>
      <td>NV CSKH có nút bấm hủy lịch hẹn cho KH.</td>
      <td>NV CSKH có nút bấm hủy lịch hẹn cho KH.</td>
    </tr>
    <tr>
      <td>17.77</td>
      <td>Tổng hợp thông tin tiếp nhận giải đáp</td>
      <td>NV CSKH có thể nhìn được tổng cuộc gọi/phiên Chat đã tiếp nhận trong ca trực đó, ví dụ: số cuộc gọi được phục vụ, số cuộc gọi rớt do KH, số cuộc gọi rớt do NV CSKH, tổng thời gian trả lời, thời điểm đăng nhập, tổng cuộc gọi đến, tổng phiên Chat đến</td>
      <td>NV CSKH có thể nhìn được tổng cuộc gọi/phiên Chat đã tiếp nhận trong ca trực đó, ví dụ: số cuộc gọi được phục vụ, số cuộc gọi rớt do KH, số cuộc gọi rớt do NV CSKH, tổng thời gian trả lời, thời điểm đăng nhập, tổng cuộc gọi đến, tổng phiên Chat đến</td>
    </tr>
    <tr>
      <td></td>
      <td>Nhóm tính năng giám sát và đánh giá chất lượng.</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.78</td>
      <td>Giám sát chất lượng online</td>
      <td>Tính năng này cho phép giám sát nghe online cuộc gọi VideoCall (1 chiều/2 chiều/âm thanh), cuộc gọi Callmeback, xem online phiên Chat và tương tác với NV CSKH và KH trong cuộc gọi. Giám sát có thể online song song 1 cuộc gọi và nhiều phiên Chat của các NV CSKH khác nhau</td>
      <td>Tính năng này cho phép giám sát nghe online cuộc gọi VideoCall (1 chiều/2 chiều/âm thanh), cuộc gọi Callmeback, xem online phiên Chat và tương tác với NV CSKH và KH trong cuộc gọi. Giám sát có thể online song song 1 cuộc gọi và nhiều phiên Chat của các NV CSKH khác nhau</td>
    </tr>
    <tr>
      <td>17.79</td>
      <td>Giám sát chất lượng offline</td>
      <td>Tính năng này cho phép GS tìm kiếm, nghe lại cuộc gọi, xem lại phiên Chat, xuất và lưu dữ liệu chi tiết cuộc gọi/phiên Chat</td>
      <td>Tính năng này cho phép GS tìm kiếm, nghe lại cuộc gọi, xem lại phiên Chat, xuất và lưu dữ liệu chi tiết cuộc gọi/phiên Chat</td>
    </tr>
    <tr>
      <td>17.80</td>
      <td>Tính năng đánh giá chất lượng giải đáp của NV CSKH, chất lượng Giám sát viên:</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.81</td>
      <td>Tính năng điều hành ca trực.</td>
      <td>Theo dõi chỉ số, số liệu Online: cho phép Trưởng ca theo dõi trực tiếp tình trạng, lưu lượng tương tác vào tổng đài, mức độ đáp ứng để có quyết định điều chỉnh nhân sự trong ca, đảm bảo hiệu quả tương tác và chỉ số kết nối toàn tổng đài</td>
      <td>Theo dõi chỉ số, số liệu Online: cho phép Trưởng ca theo dõi trực tiếp tình trạng, lưu lượng tương tác vào tổng đài, mức độ đáp ứng để có quyết định điều chỉnh nhân sự trong ca, đảm bảo hiệu quả tương tác và chỉ số kết nối toàn tổng đài</td>
    </tr>
    <tr>
      <td>17.82</td>
      <td>Thống kê số liệu offline</td>
      <td>tính năng cho phép thống kê số liệu theo các trường thời gian, kênh tương tác, Agent để phục vụ cho công tác báo cáo phân tích</td>
      <td>tính năng cho phép thống kê số liệu theo các trường thời gian, kênh tương tác, Agent để phục vụ cho công tác báo cáo phân tích</td>
    </tr>
  </tbody>
</table>

# Public_442

<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.83</td>
      <td>Tính năng điều hành khác</td>
      <td>Chat: cho phép trưởng ca Chat với nhóm NV CSKH, GS và Trưởng ca khác để thông báo, đưa tin nóng hoặc cảnh báo nhân sự Nhắn tin: cho phép trưởng ca nhắn tin theo số thuê bao đến nhóm NV CSKH, GS và Trưởng ca khác để thông báo, đưa tin nóng hoặc cảnh báo nhân sự, tính năng đảm bảo đối với cả nhân sự không có ca trực. Quản lý thuê bao quấy rối: cho phép trưởng ca theo dõi, tác động chặn/ mở thuê bao quấy rối tổng đài. Quản lý cuộc gọi ra của NV CSKH: cho phép quản lý cuộc gọi ra của NV CSKH</td>
      <td>Chat: cho phép trưởng ca Chat với nhóm NV CSKH, GS và Trưởng ca khác để thông báo, đưa tin nóng hoặc cảnh báo nhân sự Nhắn tin: cho phép trưởng ca nhắn tin theo số thuê bao đến nhóm NV CSKH, GS và Trưởng ca khác để thông báo, đưa tin nóng hoặc cảnh báo nhân sự, tính năng đảm bảo đối với cả nhân sự không có ca trực. Quản lý thuê bao quấy rối: cho phép trưởng ca theo dõi, tác động chặn/ mở thuê bao quấy rối tổng đài. Quản lý cuộc gọi ra của NV CSKH: cho phép quản lý cuộc gọi ra của NV CSKH</td>
    </tr>
    <tr>
      <td>17.84</td>
      <td>Dashboard</td>
      <td></td>
      <td>Hiển thị các các thông tin giám sát. Call > 5min chưa có dữ liệu</td>
    </tr>
    <tr>
      <td>17.85</td>
      <td>Giám sát queue</td>
      <td></td>
      <td>Hiển thị thông tin: Connecting, Avg call length, >5min, <30sec, waiting calls, available/ log_in agent</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17,86</td>
      <td>Báo cáo kết nối</td>
      <td></td>
      <td>Bổ sung báo cáo kết nối theo template mới</td>
    </tr>
    <tr>
      <td>17.87</td>
      <td>Báo cáo năng suất agent</td>
      <td></td>
      <td>Bổ sung Báo cáo năng suất agent theo template mới</td>
    </tr>
    <tr>
      <td>17.88</td>
      <td>Báo cáo trạng thái TVV</td>
      <td></td>
      <td>Bổ sung Báo cáo trạng thái TVV theo template mới</td>
    </tr>
    <tr>
      <td>17.89</td>
      <td>Báo cáo năng suất và trạng thái agent</td>
      <td></td>
      <td>Bổ sung Báo cáo năng suất và trạng thái agent theo template mới</td>
    </tr>
    <tr>
      <td>17.90</td>
      <td>Tìm kiếm cuộc gọi</td>
      <td></td>
      <td>- Tìm kiếm theo khoảng thời gian bất kì - Có nút download file ghi âm hoặc nghe trực tiếp, xem video cuộc gọi theo ứng dụng</td>
    </tr>
    <tr>
      <td>17.91</td>
      <td>Xuất file lịch sử cuộc gọi</td>
      <td>1. Làm rõ cột: THỜI LƯỢNG trên báo cáo 2. BS thêm cột thời gian hold 3. Cột nhiều đầu mục tiếng anh</td>
      <td>1. Làm rõ cột: THỜI LƯỢNG trên báo cáo 2. BS thêm cột thời gian hold 3. Cột nhiều đầu mục tiếng anh</td>
    </tr>
    <tr>
      <td>17.92</td>
      <td>Chi tiết tương tác các kênh Chat</td>
      <td>1. Điều kiện chọn: + Chọn tool Chát + Ô nhập thời gian cần search 2. Kết quả: + Xuất chi tiết theo số thuê bao, ĐTV tiếp nhận, thời lượng từng tương tác, nội dung chi tiết</td>
      <td>1. Bổ sung điều kiện chọn tìm kiếm: + Chọn tool Chát + Ô nhập thời gian cần search 2. Kết quả tìm kiếm bổ sung thêm các thông tin sau: + Xuất chi tiết theo số thuê bao, ĐTV tiếp nhận, thời lượng từng tương tác, nội dung chi tiết</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.93</td>
      <td>Thống kê lịch sử gọi lại cho KH theo lịch hẹn</td>
      <td>1. Điều kiện chọn: + Chọn tool Call me back + Ô nhập thời gian cần search 2. Kết quả: + Xuất chi tiết theo số thuê bao, ĐTV gọi ra, thời lượng từng tương tác, nội dung/ nhu cầu KH, số lần gọi ra (tự động đếm theo thuê bao)</td>
      <td>1. Bổ sung điều kiện chọn tìm kiếm: + Chọn tool Call me back + Ô nhập thời gian cần search 2. Kết quả tìm kiếm bổ sung thêm các thông tin sau: + Xuất chi tiết theo số thuê bao, ĐTV gọi ra, thời lượng từng tương tác, nội dung/ nhu cầu KH, số lần gọi ra (tự động đếm theo thuê bao)</td>
    </tr>
    <tr>
      <td>17.94</td>
      <td>Chi tiết tương tác theo các kênh Video call</td>
      <td>1. Điều kiện chọn: + Chọn kênh + Ô nhập thời gian cần search 2. Kết quả: + Xuất chi tiết theo kênh gồm: STB, kênh, ngày, giờ, thời lượng, trạng thái kết thúc, phân biệt tương tác có 2 kênh song song</td>
      <td>1. Bổ sung thêm điều kiện chọn tìm kiếm: + Chọn kênh + Ô nhập thời gian cần search 2. Kết quả tìm kiếm bổ sung thêm các thông tin sau: + Xuất chi tiết theo kênh gồm: STB, kênh, ngày, giờ, thời lượng, trạng thái kết thúc, phân biệt tương tác có 2 kênh song song</td>
    </tr>
    <tr>
      <td>17.95</td>
      <td>Năng suất ĐTV</td>
      <td>1. Điều kiện chọn: + Chọn kênh + Ô nhập thời gian cần search 2. Kết quả: + ĐTV, Tổng năng suất - Theo từng kênh, Tổng thời gian trả lời, Năng suất</td>
      <td>- Bổ sung thêm điều kiện chọn tìm kiếm: + Chọn kênh + Ô nhập thời gian cần search - Kết quả tìm kiếm bổ sung thêm các thông tin sau: + ĐTV, Tổng năng suất - Theo từng kênh, Tổng thời gian trả lời, Năng suất chuẩn, cảnh bảo nhân sự không đạt năng suất</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>chuẩn, cảnh bảo nhân sự không đạt năng suất</td>
      <td></td>
    </tr>
    <tr>
      <td>17,96</td>
      <td>Báo cáo điểm trung bình nghiệp vụ</td>
      <td>Báo cáo điểm trung bình nghiệp vụ '- Cho phép xuất báo cáo chi tiết điểm trung bình nghiệp vụ tháng theo khu vực, đối tác, phân lớp, theo kênh, theo Giám sát, theo NV CSKH và theo thời gian (ngày, tuần, tháng, quý, năm) theo biểu mẫu 9_Báo cáo điểm trung bình nghiệp vụ Cách tính điểm trung bình cuộc gọi: theo quy định của thang điểm đánh giá NVCSKH</td>
      <td>Báo cáo điểm trung bình nghiệp vụ</td>
    </tr>
    <tr>
      <td>17,97</td>
      <td>Báo cáo chất lượng giải đáp</td>
      <td>Báo cáo chất lượng giải đáp</td>
      <td>Bổ sung Báo cáo chất lượng giải đáp</td>
    </tr>
    <tr>
      <td>17,98</td>
      <td>Báo cáo chất lượng nhân sự</td>
      <td>Báo cáo chất lượng nhân sự</td>
      <td>Bổ sung Báo cáo chất lượng nhân sự</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.99</td>
      <td>Báo cáo tổng hợp dữ liệu đã đánh giá theo NV CSKH</td>
      <td>Báo cáo tổng hợp dữ liệu đã đánh giá theo NV CSKH</td>
      <td>Bổ sung Báo cáo tổng hợp dữ liệu đã đánh giá theo NV CSKH</td>
    </tr>
    <tr>
      <td>17.100</td>
      <td>Cấu hình hệ thống</td>
      <td>Cấu hình thang điểm đánh giá '- Hệ thống cho phép người dùng khai báo, sửa, xóa chỉ tiêu và trọng số tương ứng với từng đầu mục trong khung giải đáp và tỷ trọng theo thang điểm áp dụng hiện hành - Hệ thống hiển thị đầy đủ chức năng sau: Dạng cuộc gọi/ đầu mục cuộc gọi/chỉ tiêu đánh giá cuộc gọi / nhóm lỗi /mức độ lỗi / kênh giải đáp. Hệ thống cho phép người dùng cấu hình KI nhân sự: khai báo, sửa, xóa công thức tính KI nhân sự; import dạng file các tiêu chí khác ngoài điểm trung bình cuộc gọi_ Biểu mẫu 12_file import KI nhân sự</td>
      <td>- Bổ sung Cấu hình thang điểm đánh giá '- Hệ thống cho phép người dùng khai báo, sửa, xóa chỉ tiêu và trọng số tương ứng với từng đầu mục trong khung giải đáp và tỷ trọng theo thang điểm áp dụng hiện hành - Hệ thống hiển thị đầy đủ chức năng sau: Dạng cuộc gọi/ đầu mục cuộc gọi/chỉ tiêu đánh giá cuộc gọi / nhóm lỗi /mức độ lỗi / kênh giải đáp. Hệ thống cho phép người dùng cấu hình KI nhân sự: khai báo, sửa, xóa công thức tính KI nhân sự; import dạng file các tiêu chí khác ngoài điểm trung bình cuộc gọi_ Biểu mẫu 12_file import KI nhân sự</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.101</td>
      <td>Báo cáo kết quả đánh giá chất lượng giải đáp</td>
      <td>Báo cáo kết quả đánh giá chất lượng giải đáp: ' - Cho phép người dùng xuất chi tiết kết quả dữ liệu đánh giá online/ offline theo Biểu mẫu 4_báo cáo kết quả dữ liệu đánh giá - Chỉ cho phép Giám sát viên xuất được dữ liệu đã đánh giá của chính mình - Kiểm định 1 xuất được dữ liệu đã đánh giá của tất cả giám sát viên</td>
      <td>- Điều chỉnh nâng cấp báo cáo kết quả đánh giá chất lượng giải đáp theo biểu mẫu mới (bổ sung thay đổi các tiếu chí và dữ liệu hiển thị)</td>
    </tr>
    <tr>
      <td></td>
      <td>Đánh giá</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.102</td>
      <td>Lọc dữ liệu đánh giá</td>
      <td>Lọc dữ liệu đánh giá theo điều kiện lọc - Cho phép người dùng lọc dữ liệu đánh giá theo các điều kiện sau: thời lượng phiên tương tác, theo danh sách NV CSKH, theo đối tác, theo khoảng thời gian . Kết quả lọc sẽ đẩy về cho Giám sát quản lý. - Cho phép người dùng lọc dữ liệu đánh giá theo file dữ</td>
      <td>- Bổ sung tiêu chí Lọc dữ liệu đánh giá: ..</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>liệu dưới dạng import file dữ liệu ( Biểu mẫu 2), kết quả lọc sẽ đẩy về cho giám sát quản lý</td>
      <td></td>
    </tr>
    <tr>
      <td>17.103</td>
      <td>Đánh giá chất lượng giải đáp</td>
      <td>Đánh giá offline/ Online chất lượng giải đáp</td>
      <td>- Đánh giá chất lượng giải đáp bổ sung điều chỉnh lại theo PYC</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.104</td>
      <td>Kiểm định và báo cáo dữ liệu đã đánh giá</td>
      <td>Kiểm định lần 1 ( Kiểm định ==> Giám sát) ' - Cho phép người dùng được cấp quyền kiểm định 1 có quyền đánh giá chất lượng chấm điểm của giám sát viên: sửa toàn bộ phần đánh giá của Giám sát đã đánh giá dữ liệu đó. Kết quả của dữ liệu kiểm định 1 đánh giá sẽ thay thế kết quả của Giám sát. - Các điều kiện tìm kiếm dữ liệu kiểm định: thời gian, Giám sát, NV CSKH, số điện thoại của Khách hàng gọi lên, đối tác, ngưỡng xếp loại của cuộc gọi ( dữ liệu tìm kiếm này không cần chọn đầy đủ các điều kiện)</td>
      <td>Kiểm định và báo cáo dữ liệu đã đánh giá</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>17.105</td>
      <td>Kiểm định 2 dữ liệu đã đánh giá</td>
      <td>Kiểm định lần 2 (Kiểm định lần2 ==> Kiểm định lần 1 ==> Giám sát) '- Cho phép người dùng được cấp quyền kiểm định 2 có quyền đánh giá chất lượng chấm điểm của kiểm định 1: sửa toàn bộ phần đánh giá của Kiểm định lần 1 đồng thời sửa được đánh giá của Giám sát dữ liệu đó. Kết quả dữ liệu của kiểm định 2 sẽ thay thế kết quả đánh giá của kiểm định 1/ giám sát đã đánh giá trước đó - Các điều kiện tìm kiếm dữ liệu để kiểm định 2: thời gian, tài khoản của kiểm định lần 1, tài khoản của Giám sát, NV CSKH, số điện thoại của Khách hàng gọi lên, theo đối tác, theo ngưỡng xếp loại của cuộc gọi, theo lỗi đánh giá của kiểm định lần 1 với Giám sát</td>
      <td>Kiểm định 2 dữ liệu đã đánh giá</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tên tính năng</td>
      <td>Mô tả của khách hàng</td>
      <td>Làm rõ yêu cầu</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tiền xử lý khi vào IVR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>+ Cho phép tra cứu và xuất cuộc gọi chưa chấm/đã chấm/cuộc gọi lỗi theo đơn vị đối tác, theo Giám sát, NV CSKH, số điện thoại của Khách hàng gọi lên. Đồng thời trong quá trình tra cứu xong có thể thực hiện sửa, khôi phục cuộc gọi theo yêu cầu (lưu ý: khôi phục chỉ dùng khi Giám sát tích bỏ sai cuộc gọi lỗi).</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Giám sát Online</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

