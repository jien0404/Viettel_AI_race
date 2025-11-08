# Public_320

1. Quan điểm, mục đích $^ +$ Quan điểm:

✓ Đơn vị cần tuân thủ việc đánh giá đầy đủ qua các bước với các tiêu chí được nêu và căn cứ vào kết quả đánh giá để ra quyết định lựa chọn công nghệ phù hợp với yêu cầu.   
✓ Quy trình này hỗ trợ đưa ra căn cứ lựa chọn công trong các chỉ tiêu kỹ thuật cho các dự án mua sắm, đầu tư tài nguyên lưu trữ mới.   
✓ Các đơn vị có trách nhiệm cung cấp use cases thường xuyên để quy trình này được cập nhật các tri thức mới. Đánh giá liên tục để đánh giá mức độ phù hợp với thực tế.

$^ +$ Mục đích: Quy trình này nhằm quy định thống nhất phương pháp lựa chọn hạ tầng lưu trữ dữ liệu tại các đơn vị.

# 2. Phạm vi, đối tượng áp dụng

Phạm vi: Áp dụng cho hoạt động đánh giá, lựa chọn hạ tầng lưu trữ dữ liệu. Đối tượng áp dụng: Các cơ quan, đơn vị trong Tập đoàn

3. Tài liệu liên quan

<table>
  
  <tbody>
    <tr>
      <td>TT</td>
      <td>Tài liệu</td>
      <td>Ngày ban hành</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Bộ tiêu chuẩn Lưu trữ và Vận hành dữ liệu TC.CNVTQĐ.CNTT.40</td>
      <td>3/2021</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Quy định xây dựng và áp dụng chỉ tiêu kỹ thuật cho sản phẩm hàng hóa phục vụ hoạt động của Tập đoàn CNVTQĐ mã hiệu 3208/QyĐ-CNVTQĐ-VTNet</td>
      <td>9/2020</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Guideline định cỡ cấp phát tài nguyên CNTT mã hiệu GL.CNVTQĐ.CNTT.18.514</td>
      <td>09/2021</td>
    </tr>
  </tbody>
</table>

4. Giải thích thuật ngữ và từ viết tắt Thuật ngữ o Dữ liệu (Data): là thông tin được máy tính lưu trữ, xử lý hoặc truy xuất theo yêu cầu của người dùng hoặc theo tiến trình hoạt động của máy tính.



o Hạ tầng lưu trữ dữ liệu: gồm hệ thống vật lý và logic có nhiệm vụ quản lý và lưu trữ dữ liệu có thể bao gồm SAN (Storage Area Network), NAS (Network Attached Storage), DAS (Direct Attached System), Object Storage và (SDS) Software Define Storage.   
o Retention: Lưu giữ dữ liệu đảm bảo luôn sẵn sàng phục vụ nhu cầu truy xuất của dữ liệu ngay khi có yêu cầu.   
o Archive: Lưu trữ dữ liệu lâu dài. Khi lưu trữ lâu dài, dữ liệu được chuyển từ phân vùng lưu trữ tốc độ truy xuất cao sang phân vùng có hiệu năng thấp hơn. Khi dữ liệu chuyển từ giai đoạn “Retention” sang “Archive” được còn được gọi là “backup offline”.   
o Backup dự phòng: Là việc sao lưu dữ liệu để dự phòng khi có sự cố xảy ra, dữ liệu vẫn đảm bảo tính sẵn sàng phục vụ cho nghiệp vụ.   
o Node: Một máy tính/ máy chủ vật lý lưu trữ và xử lý dữ liệu như một phần của cơ sở dữ liệu phân tán.

Từ viết tắt

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
      <td>Non Relational hoặc Not Only SQL: Là loại DBMS dành cho dữ liệu có cấu trúc linh hoạt</td>
    </tr>
    <tr>
      <td>4.</td>
      <td>CNTT</td>
      <td>Công nghệ thông tin</td>
    </tr>
    <tr>
      <td>5.</td>
      <td>QHĐC</td>
      <td>Quy hoạch định cỡ</td>
    </tr>
    <tr>
      <td>6.</td>
      <td>VHKT</td>
      <td>Vận hành khai thác</td>
    </tr>
  </tbody>
</table>

# 5. Nội dung quy trình lựa chọn Hạ tầng lưu trữ dữ liệu

• Sự kiện bắt đầu và kết thúc

Sự kiện bắt đầu: Khi có nhu cầu đầu tư hạ tầng lưu trữ dữ liệu mới. Sự kiện kết thúc: Lựa chọn được hạ tầng lưu trữ dữ liệu phù hợp cho nhu cầu, đưa vào CTKT phục vụ các dự án quy hoạch định cỡ và mua sắm tài nguyên hạ tầng lưu trữ dữ liệu mới. Đầu vào: Khi có yêu cầu mua sắm, đầu tư tài nguyên hạ tầng lưu trữ mới.



Đầu ra: Loại hạ tầng lưu trữ phù hợp với nhu cầu nghiệp vụ và tối ưu chi phí, tài nguyên và nỗ lực vận hành khai thác.

• Lưu đồ tổng thể quy trình • Diễn giải chi tiết • Vai trò của các bên liên quan

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
    <tr>
      <td>1.</td>
      <td>Phân tích, đánh giá các tiêu chí công nghệ về lựa chọn</td>
      <td>Khi có nhu cầu đầu tư tài nguyên lưu trữ dữ liệu từ các đơn vị có yêu cầu, đơn vị QHĐC thực hiện phân tích, đánh giá theo các tiêu chí công nghệ sau: - Kiến trúc lưu trữ</td>
      <td>Đơn vị yêu cầu Đơn vị QHĐC</td>
      <td>Phân tích yêu cầu về hạ tầng cần đầu tư</td>
      <td>Các nhận định về loại hạ tầng phù hợp với từng tiêu chí sau khi</td>
    </tr>
  </tbody>
</table>







<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>sản phẩm và chi phí</td>
      <td>tại các cộng đồng công nghệ trên thế giới. Xem xét chi phí cho 1 đơn vị lưu trữ trên từng loại hạ tầng để chọn loại tối ưu về TCO.</td>
      <td></td>
      <td>báo cáo công nghệ của đơn vị và Tập đoàn. Các nguồn thông tin đáng tin cậy.</td>
      <td>chí về chi phí và mức độ phổ biến của sản phẩm.</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Đánh giá năng lực làm chủ sản phẩm, các sản phẩm DBMS và hệ điều hành hỗ trợ</td>
      <td>Đơn vị triển khai cài đặt và Đơn vị vận hành hạ tầng lưu trữ đánh giá năng lực làm chủ sản phẩm. Ưu tiên chọn sản phẩm mà đội dự án am hiểu và thành thạo nhất và vận hành đơn giản, ít lỗi. Trường hợp là hạ tầng lưu trữ mới thì cần phải có đánh giá thử nghiệp trước khi ra quyết định lựa chọn. Biểu mẫu đánh giá lựa chọn từ Bước 1,2,3,4 xem trong Phụ lục 04.</td>
      <td>ĐV QHĐC</td>
      <td>Các use cases đội dự án đã triển khai hoặc tham khảo từ các đơn vị khác. Biên bản đánh giá kết quả thử nghiệp theo các tiêu chí công nghệ được ưu tiên.</td>
      <td>Kết quả lựa chọn hạ tầng lưu trữ được Lãnh đạo đơn vị QHĐC và Lãnh đạo đơn vị vận hành hạ tầng lưu trữ phê duyệt.</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Xây dựng CTKT về Hạ tầng lưu trữ</td>
      <td>Đội dự án đưa đưa kết quả lựa chọn hạ tầng lưu trữ ở Bước 4 vào CTKT mua sắm đầu tư mới hạ tầng lưu trữ theo QĐ 3208/QyĐ- CNVTQĐ-VTNet.</td>
      <td>ĐV QHĐC</td>
      <td>Căn cứ vào kết quả phê duyệt lựa chọn hạ tầng lưu trữ</td>
      <td>CTKT hạ tầng lưu trữ</td>
    </tr>
  </tbody>
</table>

<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Hoạt động chính</td>
      <td>ĐV yêu cầu</td>
      <td>ĐV QHĐC</td>
      <td>ĐV VHKT hạ tầng lưu trữ</td>
    </tr>
  </tbody>
</table>



Giải thích:   

<table>
  
  <tbody>
    <tr>
      <td>1.</td>
      <td>Đưa ra yêu cầu về tài nguyên lưu trữ</td>
      <td>A/R</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2.</td>
      <td>Đánh giá, phân tích các tiêu chí về công nghệ, chi phí, và khả năng làm chủ công nghệ</td>
      <td>I</td>
      <td>A/R</td>
      <td>R</td>
    </tr>
    <tr>
      <td>3.</td>
      <td>Thẩm định và phê duyệt lựa chọn hạ tầng lưu trữ</td>
      <td>R</td>
      <td>A</td>
      <td>R</td>
    </tr>
    <tr>
      <td>4.</td>
      <td>Đưa kết quả lựa chọn hạ tầng lưu trữ vào CTKT phần mềm</td>
      <td>I</td>
      <td>A/R</td>
      <td>C</td>
    </tr>
  </tbody>
</table>

# 6. Tiêu chí, chỉ số đánh giá việc thực hiện quy trình

<table>
  
  <tbody>
    <tr>
      <td>Chữ viết tắt</td>
      <td>Ý nghĩa</td>
    </tr>
    <tr>
      <td>A</td>
      <td>Đơn vị/vai trò chịụ trách nhiệm giải trình kết quả của hoạt động</td>
    </tr>
    <tr>
      <td>R</td>
      <td>Đơn vị/vai trò chịu trách nhiệm thực hiện hoạt động</td>
    </tr>
    <tr>
      <td>S</td>
      <td>Đơn vị/vai trò cung cấp nguồn lực và hỗ trợ thực hiện hoạt động</td>
    </tr>
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

<table>
  
  <tbody>
    <tr>
      <td>Miêu tả KPI</td>
      <td>Công thức tính: Tỉ lệ tuân thủ quy trình = Tổng số dự án có báo cáo lựa chọn hạ tầng lưu trữ đúng quy trình trước khi xây dựng CTKT/ Tổng số dự án. Cách tính: Hàng quý đơn vị chịu trách nhiệm rà soát và lấy số lượng trên hệ thống để tính tỉ lệ.</td>
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
      <td>ĐV QHĐC</td>
    </tr>
  </tbody>
</table>



# 7. Phụ lục đính kèm

<table>
  
  <tbody>
    <tr>
      <td>Đơn vị rà soát việc thực hiện KPI</td>
      <td>Bộ phận Quản trị dữ liệu</td>
    </tr>
  </tbody>
</table>
