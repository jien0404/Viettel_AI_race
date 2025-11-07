# Public_300

# 1. GIỚI THIỆU

# 1.1 Mục đích

VTP bổ sung đối tượng bưu tá thuê ngoài vào đội ngũ giao nhận để đảm bảo đủ nguồn lực vận hành Phát triển chính sách lương khoán riêng cho đối tượng này $\to \mathrm { H } \hat { \mathrm { e } }$ thống tính lương khoán cần điều chỉnh để đáp ứng việc tính lương cho những đối tượng bưu tá khác nhau.

# 1.2 Phạm vi

Hệ thống SCS, FICO

1.3 Danh mục khái niệm, từ viết tắt

1.4 Tài liệu liên quan

<table>
  
  <tbody>
    <tr>
      <td>#</td>
      <td>Tài liệu</td>
      <td>Người tạo</td>
      <td>Ngày cập nhật</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Phụ lục lỗi</td>
      <td>NhungPAC</td>
      <td>22/03/2024</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Phụ lục phân quyền</td>
      <td>NhungPAC</td>
      <td>22/03/2024</td>
    </tr>
    <tr>
      <td>3</td>
      <td>QLNVVP-2393 Tính lương cho bưu tá thuê ngoài (Bản chốt)</td>
      <td>NhungPAC</td>
      <td>15/11/2023</td>
    </tr>
  </tbody>
</table>

1.5 Tóm tắt tài liệu

# 2. ĐẶC TẢ YÊU CẦU

2.1 Yêu cầu chức năng

# 2.1.1 Đặc tả use case:

<table>
  
  <tbody>
    <tr>
      <td>#</td>
      <td>Nhóm</td>
      <td>UCID</td>
      <td>Use Case</td>
      <td>Priority</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Kỳ lương</td>
      <td>UC1.1</td>
      <td>Tra cứu kỳ lương</td>
      <td>High</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>UC1.2</td>
      <td>Tạo kỳ lương</td>
      <td>High</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>UC1.3</td>
      <td>Chỉnh sửa kỳ lương</td>
      <td>Low</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>UC1.4</td>
      <td>Xóa kỳ lương</td>
      <td>Low</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Dữ liệu đầu vào</td>
      <td>UC2.1</td>
      <td>Lấy dữ liệu đầu vào</td>
      <td>High</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>UC2.2</td>
      <td>Xuất dữ liệu đầu vào</td>
      <td>Medium</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Bảng chi</td>
      <td>UC3.1</td>
      <td>Tra cứu bảng chi</td>
      <td>High</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>UC3.2</td>
      <td>Tạo bảng chi</td>
      <td>High</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>UC3.3</td>
      <td>Chỉnh sửa bảng chi</td>
      <td>Low</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>UC3.4</td>
      <td>Xóa bảng chi</td>
      <td>Low</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>UC3.5</td>
      <td>Yêu cầu chi</td>
      <td>High</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Biên bản</td>
      <td>UC4.1</td>
      <td>Tổng hợp biên bản</td>
      <td>High</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>UC4.2</td>
      <td>Xem danh sách biên bản</td>
      <td>High</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>UC4.3</td>
      <td>Loại/Bỏ loại biên bản</td>
      <td>High</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>UC4.5</td>
      <td>Theo dõi tiến độ chi lương</td>
      <td>Low</td>
    </tr>
  </tbody>
</table>

2.1.1.1. Kỳ lương:

2.1.1.2. UC1.1 - Tra cứu kỳ lương



<table>
  
  <tbody>
    <tr>
      <td>Use Case</td>
      <td>Tra cứu kỳ lương</td>
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
      <td>Use Case ID</td>
      <td>UC1.1</td>
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
      <td>Description</td>
      <td>Cho phép người dùng tìm kiếm danh sách các kỳ lương đã tạo theo bộ lọc tự thiết lập để sử dụng.</td>
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
      <td>Actor(s)</td>
      <td>SCS, TTVH, TCLĐ</td>
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
      <td>Priority</td>
      <td>High</td>
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
      <td>Trigger</td>
      <td>Người dùng truy cập vào SCS → Hợp đồng thuê khoán → Quản lý kỳ lương.</td>
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
    </tr>
    <tr>
      <td>Pre-Condition(s)</td>
      <td></td>
      <td>• Người dùng đăng nhập thành công vào web SCS. • Người dùng đang ở màn hình SCS → Hợp đồng thuê khoán</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Post-Condition(s)</td>
      <td></td>
      <td>Người dùng chọn thành công 1 kỳ lương để sử dụng.</td>
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

(5) Yes - Kết quả tìm kiếm có bao gồm kỳ lương người dùng muốn sử dụng.   
(6) Người dùng chọn kỳ lương và chọn button "Sử dụng".



<table>
  
  <tbody>
    <tr>
      <td>Main Flow</td>
      <td>(1) SCS hiển thị giao diện tra cứu kỳ lương và thiết lập bộ lọc mặc định. (2) SCS tìm kiếm theo bộ lọc đã thiết lập. (3) Yes - Tìm kiếm thành công. (4) SCS hiển thị kết quả tìm kiếm. (5) Yes - Kết quả tìm kiếm có bao gồm kỳ lương người dùng muốn sử dụng. (6) Người dùng chọn kỳ lương và chọn button "Sử dụng". (7) Hệ thống đóng giao diện tra cứu + fill tên kỳ lương muốn sử dụng vào mục kỳ lương tại trang chủ Hợp đồng thuê khoán. Use Case hoàn thành.</td>
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
    </tr>
    <tr>
      <td>Alternative Flow</td>
      <td>(5) No - Kết quả tìm kiếm KHÔNG bao gồm kỳ lương người dùng muốn sử dụng. (8) Người dùng thiết lập bộ lọc và chọn tìm kiếm. Use Case tiếp tục ở bước (2).</td>
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
      <td>Exception Flow</td>
      <td>(3) No - Tìm kiếm thất bại. (6) Hệ thống báo lỗi tương ứng, tham chiếu phụ lục lỗi. Use Case kết thúc.</td>
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

1. Người dùng có thể thiết lập bộ lọc bao gồm:

1.1. Mã hoặc tên chu kỳ:

Không bắt buộc Nhập chuỗi tối đa 100 ký tự Tự động loại bỏ khoảng trắng ở đầu chuỗi nhập trước khi tìm kiếm. Thỏa mãn chuối đã nhập trùng với ít nhất $1 \mathrm { k } \tilde { \mathrm { y } }$ tự với tên hoặc mã của kỳ lương (không phân biệt có dấu/ không dấu, hoa thường). Chuỗi nhập trống (Mặc định) Luôn thỏa mãn.

1.2. Thời gian

# Business rule

• Bắt buộc   
0 ngày ≤ Ngày kết thúc - Ngày bắt đầu $\leq 3 6 5$ ngày Mặc định: Ngày hiện tại trừ 365 ngày Ngày hiện tại.   
Thỏa mãn khi Ngày bắt đầu kỳ lọc ≤ Ngày kết thúc của kỳ ≤ Ngày kết thúc kỳ lọc

1.3 Loại chu kỳ

Không bắt buộc Chọn 1 hoặc nhiều trong danh sách: Tuần; Tháng Không chọn (Mặc định) Luôn thỏa mãn.

2. Mỗi kỳ lấy ra các thông tin sau: Tên kỳ lương; Mã kỳ lương; Tên loại kỳ lương; Ngày bắt đầu kỳ lương (dd/MM/yyyy); Ngày kết thúc kỳ lương (dd/MM/yyyy); Người cập nhật kỳ lương gần nhất (Họ và tên $^ +$ username); Thời gian cập nhật kỳ lương gần nhất (HH:MM dd/MM/yyyy); Kỳ hiện tại (Có/Không?)

3. Người dùng có thể trích xuất dữ liệu tra cứu dưới định dạng .xlsx theo template sau: Danh+sách+kỳ+lương+thuê+khoán.xlsx   
4. Phân quyền (Tham chiếu phụ lục phân quyền).

# 2.1.1.3. UC1.2 Tạo kỳ lương



<table>
  
  <tbody>
    <tr>
      <td>Business rule</td>
      <td>1. Người dùng có thể thiết lập bộ lọc bao gồm: 1.1. Mã hoặc tên chu kỳ: • Không bắt buộc • Nhập chuỗi tối đa 100 ký tự • Tự động loại bỏ khoảng trắng ở đầu chuỗi nhập trước khi tìm kiếm. • Thỏa mãn chuối đã nhập trùng với ít nhất 1 ký tự với tên hoặc mã của kỳ lương (không phân biệt có dấu/ không dấu, hoa thường). • Chuỗi nhập trống (Mặc định) → Luôn thỏa mãn. 1.2. Thời gian • Bắt buộc • 0 ngày ≤ Ngày kết thúc - Ngày bắt đầu ≤ 365 ngày • Mặc định: Ngày hiện tại trừ 365 ngày → Ngày hiện tại. • Thỏa mãn khi Ngày bắt đầu kỳ lọc ≤ Ngày kết thúc của kỳ ≤ Ngày kết thúc kỳ lọc 1.3 Loại chu kỳ • Không bắt buộc • Chọn 1 hoặc nhiều trong danh sách: Tuần; Tháng • Không chọn (Mặc định) → Luôn thỏa mãn. 2. Mỗi kỳ lấy ra các thông tin sau: Tên kỳ lương; Mã kỳ lương; Tên loại kỳ lương; Ngày bắt đầu kỳ lương (dd/MM/yyyy); Ngày kết thúc kỳ lương (dd/MM/yyyy); Người cập nhật kỳ lương gần nhất (Họ và tên + username); Thời gian cập nhật kỳ lương gần nhất (HH:MM dd/MM/yyyy); Kỳ hiện tại (Có/Không?) 3. Người dùng có thể trích xuất dữ liệu tra cứu dưới định dạng .xlsx theo template sau: Danh+sách+kỳ+lương+thuê+khoán.xlsx 4. Phân quyền (Tham chiếu phụ lục phân quyền).</td>
    </tr>
  </tbody>
</table>

<table>
  
  <tbody>
    <tr>
      <td>Use Case</td>
      <td>Tạo kỳ lương</td>
    </tr>
    <tr>
      <td>Use Case ID</td>
      <td>UC1.2</td>
    </tr>
  </tbody>
</table>



2. Phân quyền: (Tham chiếu phụ lục phân quyền).
