# Public_328

# 1. Mục đích

“Hướng dẫn lựa chọn kỹ thuật AI” cung cấp một khuôn khổ tư duy có hệ thống, giúp các tổ chức và doanh nghiệp nhận diện đúng bản chất bài toán AI, đồng thời lựa chọn chính xác các kỹ thuật phù hợp với mục tiêu và điều kiện triển khai. Việc chuẩn hóa cách phân loại bài toán và kỹ thuật AI không chỉ giúp tối ưu nguồn lực đầu tư mà còn đảm bảo tính nhất quán, minh bạch và hiệu quả trong toàn bộ vòng đời phát triển và vận hành giải pháp AI.

# Đối tượng áp dụng

Hướng dẫn áp dụng với các dự án phát triển sản phẩm ứng dụng học máy, trí tuệ nhân tạo tại các đơn vị trong Tập đoàn.

3. Định nghĩa, thuật ngữ và viết tắt

<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Thuật ngữ & viết tắt</td>
      <td>Giải thích</td>
    </tr>
    <tr>
      <td>1</td>
      <td>CNTT</td>
      <td>Công nghệ thông tin</td>
    </tr>
    <tr>
      <td>2</td>
      <td>AI</td>
      <td>Artificial Intelligence: Lĩnh vực khoa học máy tính nghiên cứu và phát triển các hệ thống có khả năng thực hiện những tác vụ đòi hỏi trí tuệ tương đương con người.</td>
    </tr>
    <tr>
      <td>3</td>
      <td>GPU</td>
      <td>Graphics Processing Unit: Vi xử lý chuyên dụng tối ưu cho tính toán song song cường độ cao,</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Thuật ngữ & viết tắt</td>
      <td>Giải thích</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>thường được sử dụng trong huấn luyện mô hình DL.</td>
    </tr>
    <tr>
      <td>4</td>
      <td>TPU</td>
      <td>Tensor Processing Unit: Vi xử lý do Google phát triển, tối ưu cho các phép toán tensor thường dùng trong huấn luyện và suy luận DL.</td>
    </tr>
    <tr>
      <td>5</td>
      <td>GAN</td>
      <td>Generative Adversarial Network: Mô hình Generative AI gồm hai mạng (generator, discriminator) thi đua nhau để sinh dữ liệu có phân phối giống dữ liệu thật.</td>
    </tr>
    <tr>
      <td>6</td>
      <td>VAE</td>
      <td>Variational Autoencoder: Mô hình Generative AI học phân phối tiềm ẩn để sinh dữ liệu mới qua cơ chế mã hóa–giải mã với chuẩn hóa xác suất.</td>
    </tr>
    <tr>
      <td>7</td>
      <td>GPT</td>
      <td>Generative Pre-trained Transformer: Mô hình</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Thuật ngữ & viết tắt</td>
      <td>Giải thích</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>transformer tiền huấn luyện trên khối lượng lớn văn bản, có khả năng sinh ngôn ngữ tự nhiên.</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Stable Diffusion</td>
      <td>Kỹ thuật tạo ảnh từ nhiễu dựa trên quá trình khuếch tán ngược, kiểm soát chất lượng và phong cách.</td>
    </tr>
    <tr>
      <td>9</td>
      <td>Whisper</td>
      <td>Mô hình nhận diện giọng nói của OpenAI, chuyển đổi âm thanh giọng nói thành văn bản.</td>
    </tr>
    <tr>
      <td>1 0</td>
      <td>MusicGen</td>
      <td>Mô hình DL sinh nhạc tự động theo phong cách và cấu trúc đầu vào.</td>
    </tr>
    <tr>
      <td>1 1</td>
      <td>CNN</td>
      <td>Convolutional Neural Network: Mạng nơ-ron tích chập, chuyên xử lý dữ liệu lưới (ảnh, video) bằng lớp tích chập để trích xuất đặc trưng.</td>
    </tr>
    <tr>
      <td>1 2</td>
      <td>RNN</td>
      <td>Recurrent Neural Network: Mạng nơ-ron hồi tiếp, phù hợp xử lý dữ liệu tuần tự nhờ liên</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Thuật ngữ & viết tắt</td>
      <td>Giải thích</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>kết trạng thái qua thời gian.</td>
    </tr>
    <tr>
      <td>1 3</td>
      <td>LSTM</td>
      <td>Long Short-Term Memory: Biến thể của RNN, giúp duy trì thông tin dài hạn qua cổng nhớ.</td>
    </tr>
    <tr>
      <td>1 4</td>
      <td>GRU</td>
      <td>Gated Recurrent Unit: Biến thể RNN tích hợp cổng cập nhật và khôi phục, đơn giản hóa cấu trúc so với LSTM.</td>
    </tr>
    <tr>
      <td>1 5</td>
      <td>Transformer</td>
      <td>Kiến trúc mạng dựa trên cơ chế self-attention, xử lý song song và đạt hiệu quả cao trong NLP.</td>
    </tr>
    <tr>
      <td>1 6</td>
      <td>ResNet</td>
      <td>Residual Network: Mạng nơ-ron với kết nối tắt (skip connection), giảm thiểu mất mát thông tin khi mô hình sâu tầng.</td>
    </tr>
    <tr>
      <td>1 7</td>
      <td>EfficientNet</td>
      <td>Kiến trúc CNN tự động cân chỉnh độ sâu, độ rộng và độ phân giải để tối ưu hiệu suất.</td>
    </tr>
  </tbody>
</table>

# Các kỹ thuật AI

Các kỹ thuật AI được chia thành $3 \mathrm { k } \tilde { \mathrm { y } }$ thuật chính: (1) Học máy (Machine Learning – ML); (2) Học sâu (Deep Learning – DL); (3) Trí tuệ nhân tạo tạo sinh (Generative AI – GenAI). Mỗi kỹ thuật sở hữu những ưu điểm và hạn chế đặc thù — từ khả năng giải thích rõ ràng, hiệu suất cao của ML, đến sức mạnh xử lý dữ liệu phi cấu trúc của DL và khả năng sáng tạo của GenAI. Cụ thể như sau:

- Bảng 1. Các kỹ thuật AI



<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Thuật ngữ & viết tắt</td>
      <td>Giải thích</td>
    </tr>
    <tr>
      <td>1 8</td>
      <td>SVM</td>
      <td>Support Vector Machine: thuật toán học có giám sát, phân loại bằng cách tìm siêu phẳng tối ưu phân tách các lớp dữ liệu.</td>
    </tr>
    <tr>
      <td>1 9</td>
      <td>KNN</td>
      <td>k-Nearest Neighbors: thuật toán học máy có giám sát, phân loại dựa trên nhãn của k mẫu gần nhất trong không gian đặc trưng.</td>
    </tr>
    <tr>
      <td>2 0</td>
      <td>DBSCAN</td>
      <td>Density-Based Spatial Clustering of Applications with Noise: thuật toán học máy không giám sát, phân nhóm dữ liệu dựa trên mật độ, tự động phát hiện điểm nhiễu.</td>
    </tr>
    <tr>
      <td>21</td>
      <td>XGBoost</td>
      <td>Extreme Gradient Boosting: Thuật toán học máy có giám sát dựa trên kỹ thuật tăng cường (boosting), sử dụng nhiều cây quyết định liên tiếp</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Thuật ngữ & viết tắt</td>
      <td>Giải thích</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>để tối ưu độ chính xác. Thuật toán tập trung vào khả năng xử lý dữ liệu bị thiếu, kiểm soát tình trạng quá khớp (overfitting) tốt.</td>
    </tr>
    <tr>
      <td>2 2</td>
      <td>LightGBM</td>
      <td>Light Gradient Boosting Machine: Thuật toán học máy có giám sát dựa trên kỹ thuật boosting, sử dụng nhiều cây quyết định liên tiếp để tối ưu độ chính xác. Thuật toán tập trung vào các kỹ thuật giúp tăng tốc độ huấn luyện, giảm bộ nhớ tiêu thụ.</td>
    </tr>
    <tr>
      <td>2 3</td>
      <td>K-means</td>
      <td>Thuật toán phân cụm không giám sát, nhóm dữ liệu thành k cụm để tối thiểu hoá khoảng cách tới tâm cụm.</td>
    </tr>
    <tr>
      <td>2 4</td>
      <td>PCA</td>
      <td>Principal Component Analysis: Phương pháp giảm chiều bằng cách</td>
    </tr>
  </tbody>
</table>

1 Lưu ý: ML là khái niệm tổng quát bao gồm tất cả các phương pháp cho phép hệ thống học từ dữ liệu, bao $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ cả học sâu. Tuy nhiên trong tài liệu này, khi đề cập tới ML, ngầm hiểu là ML cổ điển, bao gồm lớp thuật toán thống kê, không bao gồm kiến trúc mạng nơ-ron sâu đặc trưng của học sâu.

2 Lưu ý: DL là tập hợp các kỹ thuật học dựa trên kiến trúc mạng nơ-ron sâu, bao gồm cả mô hình dự đoán và mô hình sinh. Tuy nhiên trong tài liệu này, trí tuệ nhân tạo tạo sinh được tách riêng khỏi học sâu để nhấn mạnh nhóm mô hình có mục tiêu sinh dữ liệu mới (văn bản, hình ảnh, âm thanh…). Vì vậy, khi đề cập tới học sâu, ngầm hiểu là nhóm mô hình học sâu với mục tiêu dự đoán, nhận diện, không bao gồm nhóm mô hình sinh dữ liệu.

# Bộ tiêu chí đánh giá mức độ phù hợp của các kỹ thuật AI

Để lựa chọn kỹ thuật AI phù hợp với từng bài toán cụ thể trong doanh nghiệp, cần thiết lập một bộ tiêu chí đánh giá rõ ràng. Các tiêu chí này giúp tổ chức hiểu đúng bản chất bài toán, đặc điểm dữ liệu, cũng như yêu cầu triển khai thực tế, từ đó giới hạn và đề xuất phạm vi kỹ thuật có thể áp dụng.

Để đánh giá mức độ phù hợp của các kỹ thuật AI với từng tiêu chí, tài liệu áp dụng thang đo 3 mức như sau:

• Phù hợp (P): Kỹ thuật được thiết kế và hoạt động hiệu quả nhất cho tiêu chí này.   
• Cân nhắc (C): Kỹ thuật có thể đáp ứng tiêu chí trong một số điều kiện nhất định, hoặc khi được kết hợp với các kỹ thuật khác, nhưng không phải là lựa chọn hàng đầu.   
• Không phù hợp (K): Kỹ thuật không phù hợp hoặc hoạt động kém hiệu quả cho tiêu chí này.

- Bảng 2. Bảng đánh giá mức độ phù hợp của các kỹ thuật AI theo từng tiêu chí



<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Thuật ngữ & viết tắt</td>
      <td>Giải thích</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>chiếu dữ liệu lên trục chính có phương sai lớn nhất.</td>
    </tr>
    <tr>
      <td>2 5</td>
      <td>t-SNE</td>
      <td>t-Distributed Stochastic Neighbor Embedding: Phương pháp giảm chiều phi tuyến, giữ cấu trúc không gian cục bộ khi trực quan hóa dữ liệu cao chiều.</td>
    </tr>
    <tr>
      <td>2 6</td>
      <td>Isolation Forest</td>
      <td>Thuật toán phát hiện bất thường, cô lập điểm dữ liệu khác biệt qua mô hình rừng cây ngẫu nhiên.</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Kỹ thuật</td>
      <td>Định nghĩa</td>
      <td>Ưu điểm</td>
      <td>Nhược điểm</td>
      <td>Ứng dụng điển hình</td>
      <td>Thuật toán điển hình</td>
    </tr>
    <tr>
      <td>1</td>
      <td>ML1</td>
      <td>- Kỹ thuật AI sử dụng thuật toán thống kê để học từ dữ liệu quá khứ và đưa ra dự đoán mà không cần lập trình tường minh.</td>
      <td>- Xử lý tốt dữ liệu có cấu trúc. - Một số thuật toán có khả năng giải thích được và tốt hơn học sâu. - Chi phí tính toán thấp hơn học sâu. - Mạnh với dữ liệu vừa và nhỏ.</td>
      <td>- Hiệu suất kém với dữ liệu phi cấu trúc (ảnh, video, âm thanh, văn bản). - Cần bước trích chọn đặc trưng thủ công. - Độ chính xác giới hạn với bài toán có mẫu phức tạp. - Giới hạn khả năng khai thác tương tác giữa các đặc trưng phức tạp (phi tuyến).</td>
      <td>- Dự báo nhu cầu, dự báo doanh thu. - Phân loại tín dụng, rủi ro. - Phát hiện gian lận. Dự đoán khách hàng rời mạng.</td>
      <td>- Linear Regression, Logistic Regression. - Decision Tree, Random Forest. - Gradient Boosting, XGBoost, LightGBM. - SVM, KNN, - Naive Bayes. - K-means, DBSCAN</td>
    </tr>
    <tr>
      <td>2</td>
      <td>DL2</td>
      <td>Nhánh của ML sử dụng mạng nơ-ron sâu (Deep Neural Networks – DNN) có khả năng tự động học biểu diễn từ dữ liệu.</td>
      <td>- Tự động trích xuất đặc trưng từ dữ liệu. - Xử lý mạnh dữ liệu phi cấu trúc (ảnh, âm thanh, văn bản, video). - Hỗ trợ học đa phương thức bao gồm ảnh, văn bản, dữ liệu bảng... - Tối ưu hóa tốt cho các bài toán có dữ liệu lớn, phức tạp. - Đạt độ chính xác rất</td>
      <td>- Yêu cầu dữ liệu rất lớn và tài nguyên phần cứng mạnh (GPU/TPU). - Tính đóng, khó giải thích. - Chi phí tính toán cao, độ trễ cao khi suy luận. - Dễ bị quá khớp(overfitting) nếu không có dữ liệu hoặc kỹ thuật chính quy hóa (regularization) tốt. - Quá trình huấn luyện phức tạp, nhạy với các siêu tham số, do đó cần tinh chỉnh kỹ lưỡng.</td>
      <td>- Nhận diện khuôn mặt, y tế chẩn đoán hình ảnh. - Phân tích văn bản, phân tích cảm xúc. - Dịch máy, nhận dạng tiếng nói. - Phát hiện đối tượng trong video.</td>
      <td>- CNN - RNN, LSTM, GRU - Transformer - ResNet, EfficientNet</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Kỹ thuật</td>
      <td>Định nghĩa</td>
      <td>Ưu điểm</td>
      <td>Nhược điểm</td>
      <td>Ứng dụng điển hình</td>
      <td>Thuật toán điển hình</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>cao trong thị giác máy tính, xử lý ngôn ngữ tự nhiên.</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3</td>
      <td>GenAI</td>
      <td>Nhánh của học sâu sử dụng các mô hình có khả năng sinh ra dữ liệu mới (văn bản, hình ảnh, âm thanh, video, code, nhạc).</td>
      <td>- Sinh nội dung sáng tạo (văn bản, ảnh, video, nhạc, code). - Học biểu diễn phức tạp từ dữ liệu phi cấu trúc. - Tăng tốc quy trình sáng tạo, lập trình, nghiên cứu và phát triển (R&D). - Hỗ trợ xây dựng dữ liệu tổng hợp (synthetic data) để huấn luyện mô hình khác. - Kết hợp mạnh với tạo sinh dựa trên truy xuất tăng cường (RAG), hỗ trợ bài toán doanh nghiệp phức tạp.</td>
      <td>- Chi phí tính toán rất cao. - Đầu ra có thể chứa thông tin sai lệch, thiên kiến (bias), ảo giác (hallucination). - Độ tin cậy phụ thuộc mạnh vào prompt, chất lượng tinh chỉnh mô hình (fine tune). - Vấn đề về bản quyền, đạo đức và kiểm duyệt nội dung. - Khó kiểm soát chính xác logic nội tại của mô hình.</td>
      <td>- Sinh nội dung truyền thông - Trợ lý lập trình: sinh mã nguồn, sinh tài liệu phân tích. - Trợ lý ảo cho doanh nghiệp. - Tạo dữ liệu tổng hợp trong nghiên cứu y học, sản xuất.</td>
      <td>- GPT. - Stable Diffusion - Whisper. - MusicGen. - GAN, VAE</td>
    </tr>
  </tbody>
</table>



# 6. Các bài toán AI phổ biến

- Theo Viện tiêu chuẩn và Công nghệ Quốc gia của Hoa Kỳ (National Institute of Standards and Technology – NIST), bài toán AI được phân loại theo 14 bài toán phổ biến như sau:

<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Tiêu chí</td>
      <td>Thuộc tính đánh giá</td>
      <td>Định nghĩa</td>
      <td>Đánh giá chi tiết</td>
      <td>ML</td>
      <td>DL</td>
      <td>Gen AI</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Mục tiêu bài toán</td>
      <td>D ự đoán</td>
      <td>Dự báo biến liên tục (regression) hoặc phân loại nhãn (classification) dựa trên tập dữ liệu có nhãn.</td>
      <td>- ML, DL phù hợp: bản chất của ML và DL là xây dựng mô hình học ánh xạ từ dữ liệu đầu vào tới một kết quả xác định. - GenAI cân nhắc: vì GenAI không được thiết kế cho bài toán dự đoán, tuy nhiên có thể sử dụng trong một số trường hợp đặc biệt như sinh kết quả dự đoán dựa trên ngữ cảnh, nhưng không phải là lựa chọn tối ưu cho các bài toán dự đoán hoặc phân loại nhãn rõ ràng.</td>
      <td>P</td>
      <td>P</td>
      <td>C</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Tiêu chí</td>
      <td>Thuộc tính đánh giá</td>
      <td>Định nghĩa</td>
      <td>Đánh giá chi tiết</td>
      <td>ML</td>
      <td>DL</td>
      <td>Gen AI</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Loại dữ liệu</td>
      <td>Tạo sinh</td>
      <td>Tạo mới dữ liệu phi cấu trúc như văn bản, hình ảnh, video, âm thanh hoặc mã nguồn.</td>
      <td>- GenAI phù hợp: Đây là mục tiêu chính của GenAI - DL cân nhắc: Các mô hình DL truyền thống không linh hoạt và hiệu quả bằng các mô hình sinh hiện đại, tuy nhiên có thể cân nhắc trong trường hợp dữ liệu không quá lớn. - ML không phù hợp: Các thuật toán ML không có khả năng sinh dữ liệu mới.</td>
      <td>K</td>
      <td>C</td>
      <td>P</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>D ữ liệu có cấu trúc</td>
      <td>Dữ liệu dạng bảng, gồm hàng và cột với kiểu dữ liệu rõ ràng.</td>
      <td>- ML phù hợp: Các thuật toán ML được tối ưu hóa để xử lý và tìm ra các mối quan hệ trong dữ liệu có cấu trúc - DL cân nhắc: DL có thể xử lý được có cấu trúc nhưng thường không mang lại kết quả vượt trội so với ML mà lại tốn kém tài nguyên hơn. Do đó DL không phải lựa chọn ưu tiên. - GenAI không phù hợp: GenAI không được thiết kế để làm việc với dữ liệu có cấu trúc.</td>
      <td>P</td>
      <td>C</td>
      <td>K</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>D ữ liệu phi cấu trúc</td>
      <td>Dữ liệu không có cấu trúc bảng định sẵn, bao gồm ảnh, văn bản tự do, âm thanh, video…</td>
      <td>- ML không phù hợp: ML không xử lý trực tiếp dữ liệu phi cấu trúc, cần phải trích xuất các đặc trưng thủ công trước khi áp dụng mô hình, điều này rất tốn thời gian và không hiệu quả. - DL và GenAI phù hợp: DL và GenAI đều được thiết kế để xử lý dữ liệu phi cấu trúc thông qua các kiến trúc mạng nơ-ron sâu, có khả năng học các đặc trưng phức tạp một cách tự động.</td>
      <td>K</td>
      <td>P</td>
      <td>P</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Nhãn dữ liệu</td>
      <td>Có nhãn rõ ràng</td>
      <td>Tập dữ liệu đã gán nhãn đầu ra (supervised).</td>
      <td>- ML và DL phù hợp: Các kỹ thuật đều dựa trên dữ liệu có nhãn để học các mẫu và mối quan hệ. - GenAI cân nhắc:</td>
      <td>P</td>
      <td>P</td>
      <td>C</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Tiêu chí</td>
      <td>Thuộc tính đánh giá</td>
      <td>Định nghĩa</td>
      <td>Đánh giá chi tiết</td>
      <td>ML</td>
      <td>DL</td>
      <td>Gen AI</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Không nhãn</td>
      <td>Tập dữ liệu chưa có nhãn, cần khám phá cấu trúc tiềm ẩn (unsupervised).</td>
      <td>- GenAI phù hợp: Kỹ thuật này học và tạo ra cấu trúc từ dữ liệu thô, không cần nhãn. - ML và DL cân nhắc: Trong trường hợp các bài toán unsupervised, các kỹ thuật này có thể sử dụng để khám phá các cấu trúc từ dữ liệu.</td>
      <td>C</td>
      <td>C</td>
      <td>P</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Số chiều dữ liệu</td>
      <td>Số chiều dữ liệu nhỏ</td>
      <td>Dữ liệu có số lượng đặc trưng (feature) nhỏ.</td>
      <td>- ML phù hợp: ML hoạt động hiệu quả với dữ liệu có ít feature - DL và GenAI cân nhắc: Có thể cân nhắc sử dụng nhưng thường không cần thiết và có nguy cơ overfitting.</td>
      <td>P</td>
      <td>C</td>
      <td>C</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Số chiều dữ liệu lớn</td>
      <td>Dữ liệu có số lượng feature rất lớn</td>
      <td>- DL và GenAI phù hợp: Kiến trúc mạng nơ-ron sâu được thiết kế để xử lý và trích xuất đặc trưng từ dữ liệu có số chiều lớn một cách tự động. - ML không phù hợp: ML có hiệu suất kém và khó xử lý khi số lượng đặc trưng tăng lên.</td>
      <td>K</td>
      <td>P</td>
      <td>P</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Số lượng dữ liệu</td>
      <td>Khối lượng dữ liệu nhỏ</td>
      <td>Tập dữ liệu nhỏ</td>
      <td>- ML phù hợp: ML hoạt động tốt trên các tập dữ liệu nhỏ, yêu cầu ít tài nguyên tính toán và thường cho kết quả tốt. - DL và GenAI cân nhắc: DL và GenAI đòi hỏi lượng lớn dữ liệu để học các đặc trưng phức tạp. Với dữ liệu nhỏ, DL dễ bị overfitting và kém hiệu quả. Tuy nhiên có thể cân nhắc nếu sử dụng các mô hình đã được huấn luyện sẵn hoặc tinh chỉnh trên dữ liệu nhỏ.</td>
      <td>P</td>
      <td>C</td>
      <td>C</td>
    </tr>
  </tbody>
</table>

# Đánh giá mức độ phù hợp của các kỹ thuật AI theo từng bài toán phổ biến

Để đánh giá mức độ phù hợp của các kỹ thuật AI theo từng bài toán, thực hiện như sau:

- Thực hiện đánh giá các đặc điểm và yêu cầu của bài toán dựa trên bộ tiêu chí đã được xây dựng.   
- Tham chiếu bảng đánh giá đã xây dựng, với mỗi tiêu chí xác định mức độ phù hợp của từng kỹ thuật AI: o Không phù hợp (K): Kết luận kỹ thuật không phù hợp. o Cân nhắc (C): Không cộng điểm. o Phù hợp (P): Cộng 1 điểm.

- Độ phù hợp tổng thể của một kỹ thuật AI được xác định bằng tổng điểm các tiêu chí (chỉ tính nếu không có tiêu chí nào bị đánh giá là không phù hợp).

- Kỹ thuật có tổng điểm cao nhất được ưu tiên lựa chọn (phù hợp), các kỹ thuật có tổng điểm thấp hơn cần được cân nhắc và đánh giá kỹ lưỡng, có thể được áp dụng trong các trường hợp đặc biệt hoặc kết hợp với các kỹ thuật khác để khắc phục các điểm yếu cho kỹ thuật chính. Trong trường hợp có nhiều kỹ thuật có tổng điểm bằng nhau, cần ưu tiên theo thứ tự quan trọng của tiêu chí từ mục tiêu bài toán, loại dữ liệu, nhãn dữ liệu, số chiều dữ liệu, số lượng dữ liệu, cho đến yêu cầu khả năng giải thích hoặc cân nhắc kết hợp các kỹ thuật để tận dụng điểm mạnh của từng kỹ thuật.



- Căn cứ dựa trên đặc điểm6 của 14 bài toán AI phổ biến đã được phân loại, chiếu theo bộ tiêu chí đánh giá đã xây dựng để xác định mức độ phù hợp của các kỹ thuật AI cho từng bài toán. Cụ thể như sau:

Bảng 4. Bảng đánh giá mức độ phù hợp của các kỹ thuật AI theo từng bài toán phổ biến.

<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Tiêu chí</td>
      <td>Thuộc tính đánh giá</td>
      <td>Định nghĩa</td>
      <td>Đánh giá chi tiết</td>
      <td>ML</td>
      <td>DL</td>
      <td>Gen AI</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Khối lượng dữ liệu lớn</td>
      <td>Tập dữ liệu lớn</td>
      <td>- DL và GenAI phù hợp: Các kỹ thuật này có khả năng khai thác các mối quan hệ phức tạp từ dữ liệu lớn. - ML cân nhắc: ML có thể hoạt động nhưng thường kém hiệu quả hơn, đặc biệt khi dữ liệu có nhiều đặc trưng phức tạp.</td>
      <td>C</td>
      <td>P</td>
      <td>P</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Yêu cầu khả năng giải thích</td>
      <td>Yêu cầu khả năng giải thích rõ ràng, dễ kiểm tra</td>
      <td>Yêu cầu khả năng giải thích rõ ràng, dễ kiểm tra nguyên nhân mô hình đưa ra quyết định cụ thể.</td>
      <td>- ML phù hợp: Các thuật toán ML như Linear regression, Decision tree thường dễ giải thích, minh bạch và có thể kiểm tra các quyết định của mô hình. - DL và GenAI cân nhắc: Các kỹ thuật này dựa trên các mô hình mang tính chất hộp đen (black-box), rất khó để giải thích và truy vết nguyên nhân cụ thể. Tuy nhiên, có thể cân nhắc khi áp dụng kết hợp các kỹ thuật giải thích mô hình bổ sung hoặc đối với GenAI thì yêu cầu sinh phương pháp lý luận (tuy nhiên về bản chất mô hình vẫn không diễn giải được)</td>
      <td>P</td>
      <td>C</td>
      <td>C</td>
    </tr>
  </tbody>
</table>

<table>
  
  <tbody>
    <tr>
      <td>STT</td>
      <td>Bài toán AI</td>
      <td>Mô tả</td>
      <td>Ứng dụng cụ thể</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>1</td>
      <td>Tạo nội dung</td>
      <td>Tạo ra các sản phẩm, dữ liệu hoặc nội dung mới dựa trên các yêu cầu hoặc mục tiêu được xác định rõ ràng.</td>
      <td>Tạo phụ đề tự động cho video quảng cáo; sinh mã lập trình từ mô tả; tạo hình ảnh từ nội dung văn bản</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Tổng hợp nội dung</td>
      <td>Kết hợp, phân tích, tóm tắt các dữ liệu hoặc thông tin riêng lẻ để tạo ra một nội dung hoàn chỉnh, có cấu trúc và ý nghĩa rõ ràng.</td>
      <td>Tóm tắt báo cáo tài chính; chuyển đổi ghi chú y tế phi cấu trúc của bác sĩ thành hồ sơ bệnh án đầy đủ.</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Ra quyết định</td>
      <td>Hỗ trợ hoặc đề xuất quyết định tối ưu từ nhiều lựa chọn, dựa trên phân tích dữ liệu, dự đoán hoặc đánh giá rủi ro.</td>
      <td>Hỗ trợ quyết định mua bán cổ phiếu; hệ thống đề xuất phê duyệt khoản vay tự động dựa trên lịch sử tín dụng.</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Phát hiện</td>
      <td>Nhận diện và xác định sự hiện diện của các vấn đề, sự kiện hoặc nguy cơ tiềm ẩn thông qua phân tích dữ liệu.</td>
      <td>Phát hiện gian lận giao dịch ngân hàng; phát hiện tấn công mạng; nhận dạng sự cố kỹ thuật trong dây chuyền sản xuất.</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Trợ lý ảo</td>
      <td>Hỗ trợ người dùng bằng cách hiểu, phản hồi và thực hiện các yêu cầu hoặc tác vụ qua giao tiếp tự nhiên như một trợ lý cá nhân.</td>
      <td>Siri, Alexa hỗ trợ đặt lịch họp; trợ lý ảo giúp trả lời câu hỏi khách hàng trực tuyến tự động.</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Khám phá</td>
      <td>Khai phá, nhận dạng hoặc tìm ra thông tin, sản phẩm hoặc quy trình hoàn toàn mới mà con người chưa biết tới hoặc chưa tiếp cận được trước đó.</td>
      <td>Phát hiện phân tử mới trong dược phẩm; khám phá vật liệu pin tiên tiến; tối ưu công thức sản phẩm mới trong sản xuất.</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Phân tích hình ảnh</td>
      <td>Nhận diện và phân tích nội dung từ hình ảnh số để đưa ra thông tin hữu ích, hỗ trợ việc ra quyết định.</td>
      <td>Hệ thống nhận dạng ung thư sớm từ hình ảnh chẩn đoán y tế; phân tích sản phẩm lỗi từ hình ảnh trên dây chuyền sản xuất.</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Truy xuất thông tin</td>
      <td>Hỗ trợ người dùng tìm kiếm, tiếp cận nhanh chóng và chính xác các thông tin cần thiết từ nguồn dữ liệu lớn, đa dạng.</td>
      <td>Truy xuất tài liệu pháp lý theo từ khóa; tìm kiếm protein ổn định cho nghiên cứu thuốc nhanh hơn.</td>
    </tr>
    <tr>
      <td>9</td>
      <td>Giám sát</td>
      <td>Theo dõi, giám sát liên tục trạng thái, chất lượng hoặc hiệu suất của hệ thống để phát hiện bất thường hoặc cải tiến hoạt động.</td>
      <td>Giám sát tình trạng thiết bị công nghiệp theo thời gian thực; giám sát môi trường để phát hiện cháy rừng tự động.</td>
    </tr>
    <tr>
      <td>10</td>
      <td>Cải thiện hiệu suất</td>
      <td>Tối ưu hóa, nâng cao chất lượng, độ chính xác hoặc hiệu suất vận hành của quy trình hoặc hệ thống hiện có.</td>
      <td>Tối ưu thuật toán phân tích dữ liệu lớn; cải tiến độ chính xác mô hình dự báo thời tiết.</td>
    </tr>
  </tbody>
</table>



# Đánh giá chung:

- ML: phù hợp với các bài toán yêu cầu mô hình đơn giản, có khả năng giải thích tốt và dữ liệu có cấu trúc, điển hình như ra quyết định, giám sát, cải thiện hiệu suất, cá nhân hóa, dự báo, tự động hóa quy trình và khuyến nghị. Đây là những trường hợp mà dữ liệu đã được gán nhãn đầy đủ, số chiều không cao và yêu cầu giải thích thường được đặt ra rõ ràng. Tuy nhiên, ML không phù hợp với các bài toán có đặc điểm sinh nội dung, dữ liệu phi cấu trúc và không nhãn như tạo nội dung, tổng hợp nội dung, trợ lý số, khám phá, phân tích hình ảnh hay truy xuất thông tin. ML cũng gặp hạn chế trong bài toán phát hiện, nơi dữ liệu phi cấu trúc và nhãn phức tạp khiến hiệu quả suy giảm.

- DL: phù hợp với phần lớn các bài toán bao gồm cả sinh nội dung (tạo nội dung, tổng hợp nội dung, trợ lý số, khám phá), lẫn các tác vụ dự đoán như ra quyết định, phát hiện, phân tích hình ảnh, truy xuất thông tin, cải thiện hiệu suất, cá nhân hóa, dự báo, tự động hóa quy trình và khuyến nghị. DL cần được cân nhắc trong các trường hợp yêu cầu giải thích rõ như giám sát, hoặc dữ liệu nhỏ như tự động hóa quy trình, khi mà DL có thể áp dụng được nhưng không tối ưu nếu thiếu lượng dữ liệu lớn hoặc tài nguyên tính toán phù hợp.

<table>
  
  <tbody>
    <tr>
      <td>11</td>
      <td>Cá nhân hóa</td>
      <td>Điều chỉnh và cung cấp sản phẩm, dịch vụ, nội dung phù hợp nhất với từng cá nhân dựa trên hành vi, sở thích và đặc điểm riêng của họ.</td>
      <td>Cá nhân hóa nội dung quảng cáo theo hành vi mua sắm trực tuyến; cung cấp nội dung giáo dục phù hợp theo năng lực học viên.</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Dự báo</td>
      <td>Dự đoán khả năng xảy ra của các sự kiện hoặc kết quả trong tương lai, dựa trên phân tích dữ liệu lịch sử và mô hình thống kê.</td>
      <td>Dự báo doanh thu quý kế tiếp; dự báo khả năng hỏng hóc máy móc trong sản xuất; dự báo lưu lượng khách hàng để tối ưu dịch vụ.</td>
    </tr>
    <tr>
      <td>13</td>
      <td>Tự động hóa quy trình</td>
      <td>Thực hiện các tác vụ thường xuyên, lặp lại hoặc dễ xảy ra sai sót nhằm giảm thời gian, tiết kiệm nguồn lực và nâng cao hiệu quả hoạt động.</td>
      <td>Tự động hóa quản lý hóa đơn và thanh toán; xử lý, phân loại email nội bộ tự động.</td>
    </tr>
    <tr>
      <td>14</td>
      <td></td>
      <td>Khuyến nghị Đưa ra các gợi ý, lựa chọn hợp lý nhất cho người dùng nhằm hỗ trợ họ ra quyết định một cách hiệu quả.</td>
      <td>Đề xuất sản phẩm phù hợp cho khách hàng mua sắm trực tuyến; gợi ý phản hồi nhanh trong hệ thống chăm sóc khách hàng.</td>
    </tr>
  </tbody>
</table>

- GenAI: cho thấy hiệu quả vượt trội trong các bài toán sinh nội dung và tương tác ngôn ngữ tự nhiên như tạo nội dung, tổng hợp nội dung, trợ lý số và khám phá – tất cả đều đạt điểm đánh giá tối đa. GenAI cũng có thể cân nhắc áp dụng ở các bài toán như phân tích hình ảnh, phát hiện và truy xuất thông tin, đặc biệt khi cần hỗ trợ trực quan hóa hoặc mở rộng khả năng phân tích dữ liệu phi cấu trúc. Tuy nhiên, GenAI hiện không phù hợp cho các bài toán truyền thống thiên về dự đoán định lượng và yêu cầu tính giải thích cao như ra quyết định, giám sát, cải thiện hiệu suất, cá nhân hóa, dự báo, tự động hóa quy trình và khuyến nghị, do đặc điểm sinh mô hình không rõ ràng, chi phí huấn luyện lớn và khó kiểm soát logic suy luận
