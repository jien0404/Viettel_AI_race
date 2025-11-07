# Public_299

# 1. Tổng quan

# 1.1 Mục đích tài liệu

- Tài liệu này được xây dựng nhằm mục đích mô tả thiết $\mathrm { k } \acute { \mathrm { e } }$ các chức năng đáp ứng yêu cầu nghiệp vụ đăng ký tuyển dụng cho bưu tá, nhân viên lái xe trên website: viettelpost.com.vn

# 1.2 Phạm vi

- Luồng nghiệp vụ được áp dụng cho chức năng đăng ký tuyển dụng trên web: https://viettelpost.com.vn/

# 1.3 Thuật ngữ và chữ viết tắt



# 1.4 Danh mục chức năng



# 2. THIẾT KẾ CHỨC NĂNG

# 2.1 Mô tả chung





<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>2. Chọn ứng tuyển nhanh 3. Nhập thông tin ứng tuyển 4. Click Đăng ký 5. Hiển thị popup đăng ký thành công</td>
    </tr>
    <tr>
      <td>Post- Condition(s)</td>
      <td>1. Người dùng đăng ký thông tin ứng tuyển thành công 2. Dữ liệu người dùng đăng ký đẩy về hệ thống tuyển dụng</td>
    </tr>
  </tbody>
</table>

# 2.2 Mô tả nghiệp vụ









<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>Không tiếp nhận hồ sơ có cùng thông tin tương tự)</td>
    </tr>
    <tr>
      <td>15</td>
      <td>Hiển thị danh sách ứng viên</td>
      <td>Hệ thống quản lý nhân sự</td>
      <td>Hệ thống</td>
      <td>Hiển thị danh sách hồ sơ ứng viên được đẩy về từ VTP kèm các trạng thái: • Tạo mới • Đang xử lý • Đạt • Không đạt</td>
    </tr>
    <tr>
      <td>16</td>
      <td>Cập nhật trạng thái hồ sơ ứng viên</td>
      <td>Hệ thống quản lý nhân sự</td>
      <td>Người dùng</td>
      <td>Người dùng cập nhật trạng thái hồ sơ ứng viên, chuyển trạng thái hồ sơ trên danh sách ứng viên</td>
    </tr>
    <tr>
      <td>17</td>
      <td>Trả kết quả ứng tuyển qua SMS/ Mocha</td>
      <td>Hệ thống quản lý nhân sự</td>
      <td>Hệ thống</td>
      <td>Hệ thống gửi thông báo về tiến trình xử lý hồ sơ: • Đang xử lý: Hồ sơ đã được tiếp nhận • Đạt: Hồ sơ ứng tuyển đạt yêu cầu, bộ phận tuyển dụng thực hiện quy trình tuyển dụng thủ công • Không đạt: Hồ sơ bị từ chối, người dùng có thể ứng tuyển lại</td>
    </tr>
  </tbody>
</table>

# 2.3 Mô tả màn hình





<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>Nhập họ và tên</td>
      <td>Để trống trường thông tin > Hiển thị message:</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Năm sinh</td>
      <td>Textbox</td>
      <td>Có</td>
      <td>Hint text: Nhập năm sinh</td>
      <td>Chỉ cho phép nhập số, tối đa 4 số Message: Để trống trường thông tin > Hiển thị message:</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Số điện thoại</td>
      <td>Textbox</td>
      <td>Có</td>
      <td>Hint text: Nhập số điện thoại</td>
      <td>Chỉ cho phép nhập số, tối đa 10 số, không chứa ký tự đặc biệt Message: - Nhập sai định dạng > Hiển thị message: “Số điện thoại không hợp lệ.” - Để trống trường thông tin > Hiển thị message:</td>
    </tr>
    <tr>
      <td>Vị trí ứng tuyển</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>1</td>
      <td>Vị trí ứng tuyển</td>
      <td>Check box Có</td>
      <td></td>
      <td>N/A</td>
      <td>Chọn 1 trong 3 vị trí ứng tuyển: - Nhân viên bưu tá - Nhân viên khai thác - Tài xế xe tải Message: Để trống trường thông tin > Hiển thị message:</td>
    </tr>
    <tr>
      <td>Khu vực ứng tuyển</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>1</td>
      <td>Tỉnh</td>
      <td>Dropdown list</td>
      <td>Có</td>
      <td>Hint text: Chọn tỉnh</td>
      <td>Chọn tỉnh từ danh sách Hệ thống quản lý nhân sự trả về Message: Để trống trường thông tin > Hiển thị message:</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Bưu cục</td>
      <td>Dropdown list</td>
      <td>Có</td>
      <td>Hint text: Chọn bưu cục</td>
      <td>Chọn bưu cục theo tỉnh từ danh sách Hệ thống quản lý nhân sự trả về. Chỉ được chọn bưu cục khi đã chọn tỉnh Message: Để trống trường thông tin > Hiển thị message:</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Điều khoản quy định</td>
      <td>Check box Có</td>
      <td></td>
      <td>N/A</td>
      <td>Mặc định tích điều khoản quy định Message: Bỏ tích điều khoản quy định > Hiển thị message:</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Đăng ký</td>
      <td>Button</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>Click on => Hiển thị popup Message: Trong vòng 7 ngày: Cùng thông tin cá nhân, cùng vị trí ứng tuyển, cùng khu vực ứng tuyển, cùng trạng thái Chưa xử lý => Không tiếp nhận hồ sơ tương tự. Khi click on button => Hiển thị message: “Bạn đã ứng tuyển cho vị trí này, vui lòng đợi xét duyệt" Click hủy => Giữ nguyên màn ứng tuyển Click Xác nhận => Điều hướng màn hình</td>
    </tr>
  </tbody>
</table>
