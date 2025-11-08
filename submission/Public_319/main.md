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

<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tài liệu</td>
      <td>Thời gian ban hành</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Bộ tiêu chuẩn Lưu trữ và Vận hành dữ liệu TC.CNVTQĐ.CNTT.40</td>
      <td>09/2022</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Quy định thiết lập, quản lý, lưu trữ, khai thác log hệ thống CNTT số 4137/QĐ-CNVTQĐ-CNTT.</td>
      <td>9/2021</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Quy định xây dựng, nâng cấp, bảo trì các sản phẩm phần mềm trong Tập đoàn Công nghiệp – Viễn thông Quân đội (3388/QĐ-CNVQTĐ-CNTT)</td>
      <td>7/2021</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Bộ tiêu chuẩn lưu trữ và vận hành dữ liệu (TC.CNVTQĐ.CNTT.40)</td>
      <td>9/2022</td>
    </tr>
  </tbody>
</table>

# 4. Giải thích thuật ngữ và từ viết tắt

# Thuật ngữ

o Dữ liệu (Data): là thông tin được máy tính lưu trữ, xử lý hoặc truy xuất theo yêu cầu của người dùng hoặc theo tiến trình hoạt động của máy tính. o Cơ sở dữ liệu: Chỉ mọi tập hợp dữ liệu được lưu trữ, bất $\mathrm { k } \mathring { \mathrm { e } }$ cấu trúc hoặc nội dung. Trong một số cơ sở dữ liệu lớn CSDL được nhắc đến như là instances và schema.



o Instance: Là một triển khai phần mềm cơ sở dữ liệu (DBMS) có nhiệm vụ kiểm soát quyền truy cập vào một khu vực lưu trữ nhất định. Thường tổ chức có nhiều instance chạy đồng thời, độc lập nhau và mỗi instance kiểm soát truy cập vào các khu vực lưu trữ khác nhau.   
o Hệ quản trị CSDL hay DBMS (Database Management System): Là phần mềm tương tác với người dùng cuối, ứng dụng và chính cơ sở dữ liệu để thu thập và phân tích dữ liệu. Phần mềm DBMS bao gồm các tiện ích cốt lõi được cung cấp để quản trị cơ sở dữ liệu.   
o Node: Một máy tính/ máy chủ vật lý lưu trữ và xử lý dữ liệu như một phần của cơ sở dữ liệu phân tán.

Từ viết tắt:

<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Thuật ngữ và từ viết tắt</td>
      <td>Giải thích</td>
    </tr>
    <tr>
      <td>1.</td>
      <td>CSDL</td>
      <td>Cơ sở dữ liệu</td>
    </tr>
    <tr>
      <td>2.</td>
      <td>RDBMS</td>
      <td>Relational Database Management System (Hệ quản trị CSDL quan hệ)</td>
    </tr>
    <tr>
      <td>3.</td>
      <td>NoSQL</td>
      <td>NonRelational hoặc Not Only SQL: Là loại DBMS dành cho dữ liệu có cấu trúc linh hoạt, không cố định.</td>
    </tr>
    <tr>
      <td>4.</td>
      <td>ĐV PTPM</td>
      <td>Đơn vị Phát triển phần mềm</td>
    </tr>
    <tr>
      <td>5.</td>
      <td>ĐV Nghiệp vụ</td>
      <td>Đơn vị đặt hàng xây dựng phần mềm, am hiểu về nghiệp vụ.</td>
    </tr>
    <tr>
      <td>6.</td>
      <td>ĐV VHKT</td>
      <td>Đơn vị vận hành khai thác cơ sở dữ liệu</td>
    </tr>
  </tbody>
</table>

5. Nội dung quy trình lựa chọn Hệ quản trị cơ sở dữ liệu cho các dự án xây mới, nâng cấp phần mềm

# • Sự kiện bắt đầu và kết thúc

Sự kiện bắt đầu: Khi có nhu cầu lựa chọn DBMS cho các dự án xây mới, nâng cấp phần mềm.   
Sự kiện kết thúc: Lựa chọn được DBMS phù hợp với yêu cầu của bài toán nghiệp vụ, đưa vào CTKT và tài liệu giải pháp của phần mềm được xây mới hoặc nâng cấp.   
Đầu vào: Khi có yêu cầu xây mới/ nâng cấp phần mềm.   
Đầu ra: DBMS được lựa chọn trong CTKT phần mềm và tài liệu giải pháp.

• Lưu đồ tổng thể quy trình • Diễn giải chi tiết



|<image_1>|

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
    </tr>
  </tbody>
</table>

<table>
  
  <tbody>
    <tr>
      <td>Bước</td>
      <td>Hoạt động chính</td>
      <td>Công việc thực hiện</td>
      <td>Phụ trách thực hiện</td>
      <td>Đầu vào</td>
      <td>Đầu ra</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>Đưa ra yêu cầu về dữ liệu</td>
      <td>Khi đơn vị nghiệp vụ đưa ra yêu cầu về xây dựng, nâng cấp phần mềm (theo biểu mẫu được quy định trong Phụ lục 01), đơn vị PTPM phối hợp với đơn vị nghiệp vụ phân tích, làm rõ các yêu cầu về quản lý, lưu trữ và xử lý dữ liệu của ứng dụng theo các tiêu chí sau: - Cấu trúc dữ liệu - Kiểu tổ chức dữ liệu - Kiểu xử lý dữ liệu - Yêu cầu đảm bảo tính ACID/BASE, các ưu tiên trong định luật CAP - Nhu cầu đọc ghi dữ liệu - Quy mô dữ liệu Chi tiết về các tiêu chí công nghệ cần phân tích, đánh giá theo Phụ lục 02.</td>
      <td>ĐV nghiệp vụ; ĐV PTPM</td>
      <td>Phân tích yêu cầu xây dựng, nâng cấp phần mềm</td>
      <td>Các nhận định về loại DBMS phù hợp với từng tiêu chí sau khi đánh giá yêu cầu</td>
    </tr>
    <tr>
      <td>2.</td>
      <td>So sánh các nhận định sau đánh giá ở Bước 1 với các loại</td>
      <td>Sau khi đưa ra nhận định về loại DBMS phù hợp với các tiêu chí đánh giá ở Bước 1, đơn vị PTPM đưa ra các đề xuất về các sản phẩm DBMS có khả năng đáp ứng yêu cầu bài toán</td>
      <td>ĐV PTPM</td>
      <td>Các loai DBMS phù hợp với các tiêu chí công nghệ riêng lẻ</td>
      <td>Tổng hợp các DBMS phù hợp với tất cả các tiêu</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>DBMS phổ biến trên thị trường</td>
      <td>về mặt công nghệ, các ưu tiên cần đáp ứng cho bài toán. Thông tin về đặc trưng, so sánh các loại DBMS phổ biến xem trong Phụ lục 03.</td>
      <td></td>
      <td></td>
      <td>chí của bài toán.</td>
    </tr>
    <tr>
      <td>3.</td>
      <td>Đánh giá vấn đề chi phí và bản quyền</td>
      <td>Chọn DBMS thương mại khi: Khách hàng có yêu cầu chọn 1 hoặc loại DBMS và đảm bảo có ngân sách của dự án đủ chi trả, hiệu quả kinh doanh vượt trội so với chi phí bỏ ra. Các trường hợp còn lại: Phải ưu tiên chọn DBMS mã nguồn mở và tuân theo HD về sử dụng mã nguồn mở của Tập đoàn. Các lưu ý về chi phí và license cho DBMS xem trong Phụ lục 04.</td>
      <td>ĐV PTPM</td>
      <td>Các căn cứ lựa chọn sản phẩm thương mại</td>
      <td>Danh sách sản phẩm đáp ứng được tiêu chí về chi phí/ bản quyền.</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Đánh giá năng lực làm chủ sản phẩm của đội dự án</td>
      <td>Đội dự án của ĐV PTPM và Đơn vị VHKT dữ liệu (dự kiến) đánh giá năng lực làm chủ của mình đối với sản phẩm được chọn qua 3 bước trên. Ưu tiên chọn sản phẩm mà đội dự án am hiểu và thành thạo nhất và vận hành đơn giản, ít lỗi. Trường hợp là DBMS mới đối với đơn vị thì cần phải</td>
      <td>ĐV PTPM ĐV VHKT</td>
      <td>Các use cases đội dự án đã triển khai hoặc tham khảo từ các đơn vị khác. Biên bản đánh giá kết quả thử nghiệp theo</td>
      <td>Kết quả lựa chọn sản phẩm DBMS tối ưu cho dự án được Trưởng dự án và Lãnh đạo đơn vị vận hành CSDL.</td>
    </tr>
  </tbody>
</table>



# • Vai trò của các bên liên quan



Giải thích:   

<table>
  
  <tbody>
    <tr>
      <td>STT Hoạt động chính</td>
      <td></td>
      <td>ĐV Nghiệp vụ</td>
      <td>ĐV PTPM ĐV VHKT</td>
      <td></td>
    </tr>
    <tr>
      <td>1.</td>
      <td>Đưa ra yêu cầu về dữ liệu</td>
      <td>A/R</td>
      <td>S</td>
      <td></td>
    </tr>
    <tr>
      <td>2.</td>
      <td>Lựa chọn sản phẩm có khả năng đáp ứng yêu cầu theo các tiêu chí công nghệ</td>
      <td>R</td>
      <td>A/R</td>
      <td>I</td>
    </tr>
    <tr>
      <td>3.</td>
      <td>Đánh giá vấn đề chi phí và bản quyền</td>
      <td>I</td>
      <td>A/R</td>
      <td>R</td>
    </tr>
    <tr>
      <td>4.</td>
      <td>Đánh giá khả năng làm chủ công nghệ</td>
      <td>R</td>
      <td>A</td>
      <td>R</td>
    </tr>
    <tr>
      <td>5.</td>
      <td>Báo cáo, phê duyệt, thẩm định và đưa vào CTKT</td>
      <td>I</td>
      <td>A/R</td>
      <td>I</td>
    </tr>
  </tbody>
</table>

<table>
  
  <tbody>
    <tr>
      <td>Chữ viết tắt</td>
      <td>Ý nghĩa</td>
    </tr>
    <tr>
      <td>A</td>
      <td>Đơn vị/vai trò chịu trách nhiệm giải trình kết quả của hoạt động</td>
    </tr>
    <tr>
      <td>R</td>
      <td>Đơn vị/vai trò chịu trách nhiệm thực hiện hoạt động</td>
    </tr>
    <tr>
      <td>S</td>
      <td>Đơn vị/vai trò cung cấp nguồn lực và hỗ trợ thực hiện hoạt động</td>
    </tr>
  </tbody>
</table>



# 6. Tiêu chí, chỉ số đánh giá việc thực hiện quy trình

<table>
  
  <tbody>
    <tr>
      <td>C</td>
      <td>Đơn vị/vai trò cung cấp thông tin và tư vấn hỗ trợ trước và trong quá trình thực hiện hoạt động</td>
    </tr>
    <tr>
      <td>I</td>
      <td>Đơn vị/vai trò được thông báo/cung cấp thông tin sau khi hoạt động được thực hiện</td>
    </tr>
  </tbody>
</table>

# 7. Phụ lục đính kèm

<table>
  
  <tbody>
    <tr>
      <td>Miêu tả KPI</td>
      <td>Công thức tính: Tỉ lệ tuân thủ quy trình = Tổng số dự án có báo cáo lựa chọn DBMS đúng quy trình trước khi xây dựng CTKT/ Tổng số dự án. Cách tính: Hàng quý đơn vị chịu trách nhiệm rà soát và lấy số lượng trên hệ thống để tính tỉ lệ.</td>
    </tr>
    <tr>
      <td>Mục đích KPI</td>
      <td>Quản lý việc tuân thủ quy trình.</td>
    </tr>
    <tr>
      <td>Ngưỡng KPI mục tiêu</td>
      <td>>=90% (Kiểm tra thử nghiệm sau 3 tháng sau đó sẽ điều chỉnh ngưỡng KPI theo thực tế)</td>
    </tr>
    <tr>
      <td>Đơn vị chịu trách nhiệm thực hiện KPI</td>
      <td>ĐV PTPM</td>
    </tr>
    <tr>
      <td>Đơn vị rà soát việc thực hiện KPI</td>
      <td>Bộ phận Quản trị dữ liệu</td>
    </tr>
  </tbody>
</table>
