# Public_470

# 1. Cấu trúc dữ liệu đặc tả dùng cho lưu trữ dữ liệu

Dữ liệu đặc tả dùng cho lưu trữ dữ liệu liên quan đến:

thông tinh hành chính về quá trình số hóa 3D: ngày tháng, thời gian, địa điểm, vật thể, chủng loại, cơ quan quét 3D,… các dữ liệu bao gồm các tài liệu tạo ra từ các phần mềm quét 3D, phần mềm mô hỉnh, xử lý thông tin, phân tích, xử lý đám mây điểm và hình ảnh 3D. Dữ liệu cũng có thể là tập hợp các trường dữ liệu trong một hệ thống cơ sở dữ liệu; tập hợp các dữ liệu bao gồm tập hợp các tệp tin (vật lý hoặc ảo), chuỗi các dữ liệu lưu trữ và hệ thống lưu trữ dữ liệu.

Các thuộc tính của dữ liệu đặc tả dùng cho lưu trữ dữ liệu với dữ liệu 3D dữ liệu được thể hiện trong bảng 1 dưới đây:

<table>
  
  <tbody>
    <tr>
      <td>Thuộc tính</td>
      <td>Đối chiếu TCVN 7980: 2008</td>
      <td>Đối chiếu AGRMS</td>
    </tr>
    <tr>
      <td>1. Phân loại bề mặt</td>
      <td></td>
      <td>Face Category</td>
    </tr>
    <tr>
      <td>2. Phân loại vật thể</td>
      <td></td>
      <td>Category</td>
    </tr>
    <tr>
      <td>3. Định danh</td>
      <td>Định danh (bổ sung thêm thuộc tính con chuỗi định danh, giá trị định danh)</td>
      <td>Identifier</td>
    </tr>
    <tr>
      <td>4. Tiêu đề</td>
      <td>Tiêu đề (tương thích toàn bộ)</td>
      <td>Name</td>
    </tr>
    <tr>
      <td>5. Tác giả</td>
      <td>Tác giả (tương thích toàn bộ)</td>
      <td></td>
    </tr>
    <tr>
      <td>6. Chủ đề</td>
      <td>Chủ đề (tương thích toàn bộ)</td>
      <td>Keyword</td>
    </tr>
    <tr>
      <td>7. Mô tả</td>
      <td>Mô tả (tương thích toàn bộ) Description</td>
      <td></td>
    </tr>
    <tr>
      <td>8. Ngày</td>
      <td>Ngày tháng (bổ sung thêm thuộc tính con ngày bắt đầu, ngày kết thúc)</td>
      <td>Date Range</td>
    </tr>
    <tr>
      <td>9. Loại bảo mật</td>
      <td>Security Classification</td>
      <td></td>
    </tr>
    <tr>
      <td>10. Quyền</td>
      <td>Quyền (bổ sung thêm thuộc tính con kiểu quyền, trạng thái quyền)</td>
      <td>Rights</td>
    </tr>
  </tbody>
</table>



|<image_1>|

2. Xác định dữ liệu đặc tả

<table>
  
  <tbody>
    <tr>
      <td>11. Ngôn ngữ</td>
      <td>Ngôn ngữ (tương thích toàn bộ)</td>
      <td>Language</td>
    </tr>
    <tr>
      <td>12. Phạm vi</td>
      <td>Phạm vi (bổ sung thêm thuộc tính con phạm vi thẩm quyền, phạm vi thời gian, phạm vi không gian)</td>
      <td>Coverage</td>
    </tr>
    <tr>
      <td>13. Loại bỏ</td>
      <td>Disposal</td>
      <td></td>
    </tr>
    <tr>
      <td>14. Định dạng</td>
      <td>Định dạng (bổ sung thêm thuộc tính con tên định dạng, phiên bản định dạng, tên ứng dụng, phiên bản ứng dụng)</td>
      <td>Format</td>
    </tr>
    <tr>
      <td>15. Độ lớn</td>
      <td></td>
      <td>Extent</td>
    </tr>
    <tr>
      <td>16. Phương tiện lưu trữ</td>
      <td></td>
      <td>Medium</td>
    </tr>
    <tr>
      <td>17. Vị trí</td>
      <td></td>
      <td>Location</td>
    </tr>
    <tr>
      <td>18. Kiểu</td>
      <td>Kiểu (tương thích toàn bộ)</td>
      <td>Document Form</td>
    </tr>
    <tr>
      <td>19. Loại máy quét 3D</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>20. Chất liệu đối tượng</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

Dữ liệu đặc tả được sử dụng $\tt d \hat { e } \ m \hat { o }$ tả các đối tượng, các thông tin cần thiết để lưu trữ.

Tất cả hình ảnh được số hóa 3D nên được chỉ định dữ liệu đặc tả cho quá trình số hóa tài liệu và hỗ trợ các quy trình nghiệp vụ đang diễn ra. Các tổ chức, cơ quan có thể đưa ra các yêu cầu cụ thể và để tối đa hóa sự kế thừa các giá trị dữ liệu từ các hệ thống và thiết bị hiện có. Quy trình quản lý dữ liệu đặc tả nên tối đa hóa tự động chụp dữ liệu đặc tả, giảm thiểu việc xử lý thủ công. Bất kỳ việc sử dụng, áp dụng dữ liệu đặc tả nên được thực hiện có sự tham khảo tiêu chuẩn ISO 23081-1: 2006.

Dữ liệu đặc tả kết hợp với hình ảnh là một thành phần thiết yếu trong việc quản lý và truy vấn các hình ảnh.

Hai loại dữ liệu đặc tả nên được bắt:

- dữ liệu đặc tả cụ thể cho các vật thể 3D, hình ảnh quét cụ thể và quá trình xử lý ảnh; dữ liệu đặc tả về dữ liệu 3D công việc đang được giao dịch và đại lý liên quan đến nghiệp vụ. Phần lớn các dữ liệu đặc tả này có thể được tự động sinh ra bởi các phần mềm phân tích đám mây điểm, xử lý mô hình 3D và các phần cứng như máy quét 3D được sử dụng để quản lý quá trình số hóa. Cần được giảm thiểu càng nhiều càng tốt việc xử lý thủ công.

Dữ liệu đặc tả có thể được nhúng với các nguồn tài nguyên tại thông tin tiêu đề, hoặc có thể được quản lý trong một hệ thống riêng biệt, hoặc cả hai, nhưng trong cả hai trường hợp đó phải có một mối quan hệ trực tiếp hoặc liên hệ giữa chúng; tức là khi dữ liệu đặc tả nằm trong một hệ thống riêng biệt, nó có liên kết trực tiếp đến các dữ liệu 3D. Dữ liệu đặc tả cũng có thể được đóng gói trong các định dạng hình ảnh 3D.

# 3. Tạo lập dữ liệu đặc tả

Quá trình số hóa bao gồm bảy giai đoạn mà dữ liệu đặc tả phải được áp dụng. Các giai đoạn này là:

- lên kế hoạch; chuẩn bị quét đối tượng 3D; xử lý dữ liệu 3D; dung sai số hóa dữ liệu 3D; lập chỉ mục và dữ liệu đặc tả; quản lý, lưu trữ dữ liệu.



Có hai loại thông tin đánh chỉ số: Thông tin tiểu sử và thông tin thư mục. Thông tin tiểu sử giao dịch với vòng đời của các tập tin dữ liệu 3D, các hình ảnh 3D và liên quan đến bối cảnh của các thuộc tính dữ liệu 3D và tập tin đó phải được giữ lại, đăng nhập và xác nhận trong quá trình số hóa 3D.

Các định nghĩa về nghĩa vụ trong đánh chỉ số bao gồm:

bắt buộc – thuộc tính phải có; bắt buộc nếu có - thuộc tính phải được cung cấp, nếu phù hợp với bối cảnh công việc và / hoặc các nguồn lực (đối tượng nghiệp vụ); đề nghị - nên được sử dụng nếu phù hợp với bối cảnh kinh doanh và / hoặc các nguồn lực (đối tượng kinh doanh) ;   
tùy chọn – tùy thuộc vào yêu cầu mà có lựa chọn cụ thể.

# 4. Dữ liệu đặc tả về quy luật nghiệp vụ, chính sách và ủy nhiệm tại thời điểm quét 3D

Các thông tin liên quan đến số hóa nghiệp vụ, chính sách và ủy nhiệm được mô tả trong bảng 2.

Bảng 2 – Đánh chỉ số tiểu sử   

<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



Một số hoặc tất cả các thông tin này có thể được lấy tự động bởi máy quét và phần mềm số hóa 3D. Trong trường hợp chuyển giao để đảm bảo lưu trữ, điều quan trọng là phải biết ngày chuyển giao để xác định bất kỳ sự chậm trễ nào đó có hợp lý không.Tổ chức cần thực hiện các thủ tục để ngăn chặn bất kỳ hình thức sửa đổi sau khi hình ảnh đã được lấy một cách phù hợp và lập chỉ mục.
