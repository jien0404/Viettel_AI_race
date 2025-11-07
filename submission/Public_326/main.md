# Public_326

# 1. Mục đích

Hướng dẫn các bước thực hiện, trách nhiệm của các đơn vị trong công tác đảm bảo tài nguyên IP phục vụ cho sản xuất kinh doanh. Bao $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ : - Hướng dẫn nghiệp vụ cấp phát tài nguyên IP.   
- Hướng dẫn nghiệp vụ thu hồi tài nguyên IP.

# 2. Phạm vi áp dụng

Hướng dẫn này áp dụng cho các hoạt động liên quan tới công tác đảm bảo tài nguyên CNTT và hạ tầng viễn thông phục vụ cho hoạt động phát triển và sản xuất kinh doanh.

# 3. Đối tượng áp dụng

Hướng dẫn này áp dụng cho các đơn vị trong công ty.

4. Giải thích thuật ngữ, định nghĩa, khái niệm

4.1 Giải thích thuật ngữ, định nghĩa, khái niệm

- Tài nguyên địa chỉ IP: Bao gồm địa chỉ IPv4 public, IPv4 private, IPv6.

- Hạ tầng viễn thông bao gồm các hệ thống: Truyền dẫn quốc tế, Truyền dẫn trong nước, mạng cố định, mạng di động, WIFI, mạng viễn thông vệ tinh.

- Hạ tầng CNTT: Hạ tầng phần cứng (Hệ thống máy chủ, thiết bị lưu trữ, các thiết bị hỗ trợ phần mềm khác), hệ điều hành, cơ sở dữ liệu, hệ thống các phần mềm phục vụ sản xuất kinh doanh nội bộ và bên ngoài.

- Hệ thống quản lý tài nguyên: Hệ thống công cụ cấp phát tài nguyên IP tự động trên NIMS, hệ thống giám sát lưu lượng dịch vụ IP (Netflow).

- Đơn vị sử dụng (ĐVSD): Là đơn vị có nhu cầu về việc sử dụng tài nguyên IP.



- Đơn vị cấp phát (ĐVCP): Là đơn vị cấp phát hoặc phân phối địa chỉ IP cho các đơn vị có nhu cầu sử dụng.

- Quản lý, cấp phát tài nguyên cấp 1: Là đơn vị đầu tiên trong một tổ chức chịu trách nhiệm cấp phát địa chỉ cho các đơn vị khác - Quản lý, cấp phát tài nguyên cấp 2: Là đơn vị tiếp nhận IP cấp phát từ các đơn vị cấp 1 và có trách nhiệm cấp phát cho các đơn vị có nhu cầu sử dụng khác.

# 4.2 Từ viết tắt

<table>
  
  <tbody>
    <tr>
      <td>S TT</td>
      <td>Từ viết tắt</td>
      <td>Giải thích</td>
    </tr>
    <tr>
      <td>1.</td>
      <td>BGĐ</td>
      <td>Ban Giám Đốc</td>
    </tr>
    <tr>
      <td>2.</td>
      <td>TCT</td>
      <td>Tổng công ty</td>
    </tr>
    <tr>
      <td>3.</td>
      <td>TT</td>
      <td>Trung tâm</td>
    </tr>
    <tr>
      <td>4.</td>
      <td>CNTT</td>
      <td>Công nghệ thông tin</td>
    </tr>
    <tr>
      <td>5.</td>
      <td>ĐVSD</td>
      <td>Đơn vị sử dụng</td>
    </tr>
    <tr>
      <td>6.</td>
      <td>ĐVCP</td>
      <td>Đơn vị cấp phát tài nguyên</td>
    </tr>
    <tr>
      <td>7.</td>
      <td>BP QLTN</td>
      <td>Bộ phận Quản lý tài nguyên (cấp phòng)</td>
    </tr>
  </tbody>
</table>



# 5. Trách nhiệm các bên liên quan

- Đơn vị cấp phát: Chịu trách nhiệm cấp phát, quản lý tài nguyên cấp 1: Bộ phận quản lý, cấp phát trực thuộc Bộ phận Cấp phát tài nguyên (cấp phòng); cấp phê duyệt lãnh đạo TT   
- Đơn vị VHKT chịu trách nhiệm sử dụng, cấp phát, quản lý cấp 2.

<table>
  
  <tbody>
    <tr>
      <td>8.</td>
      <td>Đơn vị VHKT</td>
      <td>Bộ phận Vận hành khai thác</td>
    </tr>
    <tr>
      <td>9.</td>
      <td>GNOC</td>
      <td>Global Network Operations Center: Hệ thống quản lý và điều hành mạng lưới toàn cầu</td>
    </tr>
    <tr>
      <td>10.</td>
      <td>BM</td>
      <td>Biểu mẫu</td>
    </tr>
    <tr>
      <td>11.</td>
      <td>SR</td>
      <td>Service Request - Yêu cầu dịch vụ cần đáp ứng</td>
    </tr>
    <tr>
      <td>12.</td>
      <td>CR</td>
      <td>Change Request: Phiếu yêu cầu tác động mạng lưới</td>
    </tr>
    <tr>
      <td>13.</td>
      <td>PYC</td>
      <td>Phiếu yêu cầu</td>
    </tr>
    <tr>
      <td>14.</td>
      <td>PAKD</td>
      <td>Phương án kinh doanh</td>
    </tr>
  </tbody>
</table>

- ĐVCP: Chịu trách nhiệm cấp phát đúng tài nguyên yêu cầu, không bị trùng lặp.

ĐVSD: Chịu trách nhiệm trong việc sử dụng tài nguyên: Dùng đúng mục đích, không lãng phí, thất thoát.

6. Nội dung hướng dẫn quản lý cấp phát, thu hồi tài nguyên IP

6.1 Hướng dẫn cấp phát tài nguyên IP   



<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Hoạt động chính</td>
      <td>Công việc thực hiện</td>
      <td>ĐV thực hiện</td>
      <td>Phối hợp</td>
      <td>Công cụ thực hiện</td>
      <td>Đầu vào</td>
      <td>Đầu ra</td>
      <td>Thời gian thực hiện</td>
    </tr>
    <tr>
      <td>1 .</td>
      <td>Trình ký phiếu yêu cầu cấp phát tài nguyên</td>
      <td>- Thực hiện theo biểu mẫu BM01 (tài nguyên IP có 2 loại IP public và IP private) khi thực hiện phải ghi rõ yêu cầu.</td>
      <td>ĐVSD</td>
      <td>ĐVCP Voffice</td>
      <td></td>
      <td>Nhu cầu tài nguyên cho việc triển khai mới</td>
      <td>PYC cấp phát tài nguyên được trình ký</td>
      <td>Theo thời gian thực tế</td>
    </tr>
    <tr>
      <td>2 .</td>
      <td>Phê duyệt phiếu yêu cầu cấp phát tài nguyên</td>
      <td>- Thực hiện phê duyệt yêu cầu của đơn vị yêu cầu cấp phát tài nguyên trên hệ thống VOFFICE.</td>
      <td>Lãnh đạo phòng ĐVSD</td>
      <td>ĐVCP Voffice</td>
      <td></td>
      <td>PYC, PAKD/hợp đồng/tờ trình đề xuất cung cấp tài nguyên được phê duyệt</td>
      <td>PYC được phê duyệt</td>
      <td>Theo thời gian thực tế</td>
    </tr>
    <tr>
      <td>3 .</td>
      <td>Tạo SR cấp phát</td>
      <td>- ĐVSD tạo SR đính kèm PYC đã được phê duyệt.</td>
      <td>ĐVSD</td>
      <td>ĐVCP GNOC</td>
      <td></td>
      <td>PYC được phê duyệt, sở cứ liên quan</td>
      <td>SR được tạo trên GNOC</td>
      <td>Theo thời gian thực tế</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Hoạt động chính</td>
      <td>Công việc thực hiện</td>
      <td>ĐV thực hiện</td>
      <td>Phối hợp</td>
      <td>Công cụ thực hiện</td>
      <td>Đầu vào</td>
      <td>Đầu ra</td>
      <td>Thời gian thực hiện</td>
    </tr>
    <tr>
      <td>4 .</td>
      <td>Tiếp nhận SR cấp phát</td>
      <td>ĐV CPTN tiếp nhận và đánh giá SR: - Trường hợp SR đảm bảo theo yêu cầu: Chuyển sang Bước 5 - Trường hợp SR không đảm bảo theo yêu cầu: Từ chối SR, yêu cầu ĐVYC bổ sung thông tin còn thiếu và quay lại Bước 3. Thời gian tiếp nhận: 01 ngày làm việc tính từ thời điểm SR được tạo.</td>
      <td>ĐVCP</td>
      <td>ĐVSD GNOC</td>
      <td></td>
      <td>SR trên GNOC</td>
      <td>SR được tiếp nhận</td>
      <td>10 ngày làm việc</td>
    </tr>
    <tr>
      <td>5 .</td>
      <td>Cấp phát tài nguyên</td>
      <td>BP CPTN thực hiện: - Cấp phát tài nguyên theo PYC tự động thực hiện trên phần mềm. - Có thể bổ sung các ghi chú vào phần mục tài nguyên cấp phát trên hệ thống.</td>
      <td>ĐVCP</td>
      <td>ĐVSD Trang</td>
      <td>quản trị tài nguyên</td>
      <td>Yêu cầu về tài nguyên trên SR đã tiếp nhận</td>
      <td>Kết quả thực hiện cấp phát</td>
      <td></td>
    </tr>
    <tr>
      <td>5.1</td>
      <td>Cập nhật cơ sở dữ liệu</td>
      <td>Cập nhật cơ sở dữ liệu quản lý tài nguyên IP</td>
      <td>Hệ thống, ĐVCP</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>Ngay khi cấp phát xong</td>
    </tr>
  </tbody>
</table>



# 6.2 Hướng dẫn thu hồi tài nguyên IP

<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Hoạt động chính</td>
      <td>Công việc thực hiện</td>
      <td>ĐV thực hiện</td>
      <td>Phối hợp</td>
      <td>Công cụ thực hiện</td>
      <td>Đầu vào</td>
      <td>Đầu ra</td>
      <td>Thời gian thực hiện</td>
    </tr>
    <tr>
      <td>6 .</td>
      <td>Đóng SR cấp phát trên GNOC</td>
      <td>ĐVSD thực hiện kiểm tra thông tin tài nguyên được cấp phát và thực hiện đóng SR. Thời gian đóng SR là 01 ngày làm việc.</td>
      <td>ĐVSD</td>
      <td>ĐVCP GNOC</td>
      <td></td>
      <td>Kết quả thực hiện cấp phát</td>
      <td>SR ở trạng thái Closed</td>
      <td></td>
    </tr>
  </tbody>
</table>

<table>
  
  <tbody>
    <tr>
      <td>S TT</td>
      <td>Hoạt động chính</td>
      <td>Công việc thực hiện</td>
      <td>ĐV thực hiện</td>
      <td>Phối hợp</td>
      <td>Công cụ thực hiện</td>
      <td>Đầu vào</td>
      <td>Đầu ra</td>
      <td>Thời gian thực hiện</td>
    </tr>
    <tr>
      <td>1 .</td>
      <td>Trình ký phiếu yêu cầu thu hồi tài nguyên</td>
      <td>Căn cứ vào nhu cầu sử dụng tài nguyên, ĐVCP tạo PYC (theo biểu mẫu BM02) thu hồi tài nguyên IP trong các trường hợp sau: - Tài nguyên IP được cấp phát nhưng không có CR khai báo trên mạng lưới (trong thời hạn một quý, các đơn vị sử dụng có trách nhiệm cập nhật CR khai báo dải IP mới và thông báo cho đơn vị cấp phát hàng quý). - Hiệu suất sử dụng tài nguyên IP (dải IP) được cấp thấp (0% trong một quý). Không tính dải IP khai báo</td>
      <td>ĐVCP</td>
      <td>ĐVSD</td>
      <td>Voffice</td>
      <td>Nhu cầu thu hồi tài nguyên của ĐVCP</td>
      <td>PYC thực hiện thu hồi tài nguyên không sử dụng</td>
      <td>Theo thời gian thực tế</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Hoạt động chính</td>
      <td>Công việc thực hiện</td>
      <td>ĐV thực hiện</td>
      <td>Phối hợp</td>
      <td>Công cụ thực hiện</td>
      <td>Đầu vào</td>
      <td>Đầu ra</td>
      <td>Thời gian thực hiện</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>dự phòng hoặc quy hoạch cho các trường hợp đặc biệt khác. - Đơn vị sử dụng (ĐVSD) thông báo không còn nhu cầu.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2 .</td>
      <td>Phê duyệt phiếu yêu cầu thu hồi tài nguyên</td>
      <td>Phê duyệt phiếu yêu cầu</td>
      <td>Lãnh đạo phòng ĐVSD, ĐV CP</td>
      <td>Voffice</td>
      <td>PYC thu hồi tài nguyên</td>
      <td>PYC được phê duyệt</td>
      <td>Theo thời gian thực tế</td>
      <td>Theo thời gian thực tế</td>
    </tr>
    <tr>
      <td>3 .</td>
      <td>Tạo SR thu hồi</td>
      <td>ĐVCP thực hiện tạo SR đính kèm PYC được phê duyệt về việc thu hồi tài nguyên.</td>
      <td>ĐVCP</td>
      <td>ĐVSD</td>
      <td>GNOC</td>
      <td>PYC được phê duyệt</td>
      <td>SR được tạo trên GNOC</td>
      <td>01 ngày làm việc (tính từ thời điểm PYC được phê duyệt)</td>
    </tr>
    <tr>
      <td>4 .</td>
      <td>Tiếp nhận SR thu hồi</td>
      <td>ĐVSD tiếp nhận SR, kiểm tra các tài liệu đính kèm và thông tin liên quan về việc thu hồi tài nguyên. Thời gian thực hiện công việc: - Tiếp nhận SR: 01 ngày làm việc tính từ thời điểm ĐVCP tạo SR. - Thực hiện SR: Lập kế hoạch để thu hồi trả lại tài nguyên đơn vị cấp phát.</td>
      <td>BP CPTN</td>
      <td>ĐVCP</td>
      <td>GNOC</td>
      <td>SR trên GNOC</td>
      <td>SR được tiếp nhận</td>
      <td>Tiếp nhận SR: 01 ngày làm việc. Thực hiện SR: Theo thời gian thực tế thực hiện kế hoạch, tối đa 01 tháng</td>
    </tr>
  </tbody>
</table>
