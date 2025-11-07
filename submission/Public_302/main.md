# Public_302

# 1. Giới Thiệu

Observability (Khả Năng Quan Sát) là khả năng hiểu và chẩn đoán trạng thái nội tại của hệ thống thông qua dữ liệu được sinh ra như log, metrics và tracing. Trong Kubernetes, observability giúp phát hiện nhanh sự cố và giảm thời gian khắc phục (MTTR).

Observability khác với Monitoring ở chỗ Monitoring chỉ tập trung vào việc theo dõi các chỉ số đã biết, trong khi Observability cung cấp góc nhìn toàn diện để tìm ra nguyên nhân gốc.

# 2. Thành Phần Chính Của Observability

Các trụ cột chính của Observability trong Kubernetes gồm:

# 2.1 Metrics

- Thu thập dữ liệu số học về hiệu năng cluster, node, pod.   
- Giúp phát hiện các bất thường trong CPU, RAM, I/O.   
- Công cụ phổ biến: Prometheus.

# 2.2 Logging

- Ghi lại các sự kiện hệ thống và ứng dụng.   
- Hỗ trợ phân tích nguyên nhân sự cố.   
- Công cụ: ELK Stack, Loki.

# 2.3 Tracing

- Theo dõi luồng request xuyên suốt microservices.   
- Giúp phát hiện bottleneck.   
- Công cụ: Jaeger, OpenTelemetry.

# 3. Thách Thức Trong Kubernetes

- Hệ thống phân tán nhiều tầng.   
- Multi-cluster làm phức tạp việc giám sát.   
- Microservices tạo ra khối lượng log và dữ liệu khổng lồ.

# 4. Công Cụ Observability Thường Dùng

<table>
  
  <tbody>
    <tr>
      <td>Công Cụ</td>
      <td>Chức Năng</td>
      <td>Ghi Chú</td>
    </tr>
    <tr>
      <td>Prometheus</td>
      <td>Metrics</td>
      <td>Giám sát số liệu cluster.</td>
    </tr>
    <tr>
      <td>Grafana</td>
      <td>Visualization</td>
      <td>Biểu đồ, dashboard.</td>
    </tr>
    <tr>
      <td>Jaeger / OpenTelemetry</td>
      <td>Tracing</td>
      <td>Theo dõi request phân tán.</td>
    </tr>
  </tbody>
</table>



# 5. Quy Trình Troubleshooting Kubernetes

Quy trình thường áp dụng khi xử lý sự cố Kubernetes:

1. Kiểm tra cluster và node.   
2. Phân tích pod, container, network.   
3. Đọc log, metrics và tracing.   
4. Xác định nguyên nhân gốc (root cause).

# 6. Best Practices

- Chuẩn hóa log & metrics.   
- Thiết lập cảnh báo hợp lý.   
- Tích hợp observability vào CI/CD.   
- Tự động hóa khi có thể.

# 7. Observability vs Monitoring

<table>
  
  <tbody>
    <tr>
      <td>ELK / Loki</td>
      <td>Logging</td>
      <td>Thu thập & phân tích log.</td>
    </tr>
  </tbody>
</table>

# 8. Kết Luận

Observability là yếu tố then chốt để vận hành Kubernetes hiệu quả. Bằng cách kết hợp Metrics, Logging và Tracing cùng các công cụ hỗ trợ, doanh nghiệp có thể phát hiện sự cố nhanh hơn và tối ưu hiệu năng hệ thống.

# 9. Bảng Minh Họa Với Merge Cell

<table>
  
  <tbody>
    <tr>
      <td>Monitoring</td>
      <td>Observability</td>
    </tr>
    <tr>
      <td>Theo dõi chỉ số định sẵn.</td>
      <td>Khả năng phân tích sâu, tìm root cause.</td>
    </tr>
    <tr>
      <td>Giới hạn trong dữ liệu đã biết.</td>
      <td>Khai thác dữ liệu hệ thống để trả lời câu hỏi mới.</td>
    </tr>
  </tbody>
</table>

# 10. Bảng Pipeline Quan Sát (Phiên Bản Dài)

<table>
  
  <tbody>
    <tr>
      <td>Pipeline Observability Trong Kubernetes</td>
      <td></td>
    </tr>
    <tr>
      <td>Metrics Logging Tracing</td>
      <td>Ghi Chú</td>
    </tr>
    <tr>
      <td>Thu Thập Dữ Liệu</td>
      <td>Prometheus, ELK, Jaeger</td>
    </tr>
    <tr>
      <td>Phân Tích Quan Sát Tìm Root Cause</td>
      <td>Giảm MTTR</td>
    </tr>
  </tbody>
</table>

<table>
  
  <tbody>
    <tr>
      <td>Pipeline Observability Mở Rộng</td>
    </tr>
    <tr>
      <td>Bước Metrics Logging Tracing Ghi Chú</td>
    </tr>
  </tbody>
</table>



# 11. Phân Tích Chi Tiết Về Observability Trong Kubernetes

Observability trong Kubernetes không chỉ đơn thuần là giám sát (monitoring). Nó tập trung vào khả năng hiểu rõ trạng thái bên trong của hệ thống thông qua dữ liệu quan sát được từ bên ngoài. Điều này đặc biệt quan trọng đối với các hệ thống microservices, nơi hàng chục đến hàng trăm dịch vụ tương tác phức tạp với nhau.

Ba trụ cột chính của Observability gồm có Metrics, Logging và Tracing. Metrics cho phép thu thập các số liệu định lượng như CPU, bộ nhớ, số lượng request, độ trễ. Logging cung cấp ngữ cảnh chi tiết về sự kiện trong hệ thống. Tracing giúp theo dõi hành trình của một request qua nhiều dịch vụ khác nhau, nhờ đó phát hiện các điểm nghẽn hoặc nguyên nhân gây lỗi.

Khi triển khai Observability trong Kubernetes, tổ chức sẽ đối mặt với nhiều thách thức: 1) khối lượng dữ liệu khổng lồ; 2) chi phí lưu trữ và phân tích; 3) sự phức tạp trong tích hợp nhiều công cụ; 4) yêu cầu về kỹ năng của đội ngũ vận hành.

Để giải quyết các thách thức này, cần có kiến trúc Observability hiệu quả. Điển hình là sử dụng Prometheus để thu thập metrics, kết hợp Grafana để trực quan hóa, dùng ELK stack hoặc Loki để xử lý log, và Jaeger hoặc OpenTelemetry để thực hiện tracing. Khi các công cụ này hoạt động phối hợp, DevOps có thể nhanh chóng xác định nguyên nhân sự cố.

Một quy trình troubleshooting điển hình trong Kubernetes thường bắt đầu bằng việc kiểm tra cluster và node, sau đó đi sâu vào trạng thái pod và container. Nếu vấn đề không rõ ràng, nhóm vận hành sẽ phân tích log, metrics và tracing để tìm ra gốc rễ (root cause). Việc này giúp giảm MTTR (Mean Time To Repair) và nâng cao SLO/SLI cho dịch vụ.

Best Practices cho Observability trong Kubernetes bao $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m } ; 1$ 1) Chuẩn hóa log và metrics; 2) Sử dụng nhãn (label) thống nhất; 3) Tích hợp Observability vào

<table>
  
  <tbody>
    <tr>
      <td>Thu Thập Dữ Liệu</td>
      <td>Node Exporter</td>
      <td>Fluentd / Loki</td>
      <td>Jaeger Agent</td>
      <td>Các agent thu thập dữ liệu từ cluster</td>
    </tr>
    <tr>
      <td>Lưu Trữ</td>
      <td>Prometheus TSDB Elasticsearch / Loki</td>
      <td></td>
      <td>Jaeger Collector</td>
      <td>Kho dữ liệu trung tâm</td>
    </tr>
    <tr>
      <td>Phân Tích</td>
      <td>PromQL</td>
      <td>Kibana / Grafana Loki</td>
      <td>Jaeger Query</td>
      <td>Phân tích dữ liệu từ nhiều nguồn</td>
    </tr>
    <tr>
      <td>Trực Quan Hóa</td>
      <td>Grafana Dashboards</td>
      <td>Kibana Dashboard</td>
      <td>Jaeger UI</td>
      <td>Cung cấp dashboard cho DevOps</td>
    </tr>
    <tr>
      <td>Hành Động & Tối Ưu</td>
      <td>Alertmanager</td>
      <td>Cảnh báo log bất thường</td>
      <td>Trace-based alerts</td>
      <td>Giảm MTTR, cải thiện SLO</td>
    </tr>
  </tbody>
</table>

pipeline CI/CD; 4) Tự động hóa cảnh báo; 5) Liên tục đánh giá và tối ưu hóa chi phí lưu trữ dữ liệu.

Một ví dụ thực tế: khi ứng dụng microservice gặp lỗi 'Pod CrashLoopBackOff', metrics có thể cho thấy pod liên tục khởi động lại, log cung cấp thông tin về lỗi ứng dụng, trong khi tracing cho thấy request dừng lại ở một dịch vụ phụ thuộc. Nhờ quan sát đầy đủ, đội ngũ DevOps nhanh chóng sửa lỗi cấu hình và khôi phục dịch vụ.

# 12. So Sánh Observability và Monitoring
