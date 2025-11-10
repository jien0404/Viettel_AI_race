# Public_447

<table>
  
  <tbody>
    <tr>
      <td>est case</td>
      <td>Mô tả</td>
      <td>Input</td>
      <td>Expected Output</td>
      <td>Phương pháp</td>
      <td>Ghi chú</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Manual test plan</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>ecurity scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống,</td>
      <td>network disconnect</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>bao gồm kịch bản thành công và thất bại.</td>
      <td></td>
      <td>sự cố</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Kịch bản Ansible</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Kịch bản Ansible</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>PI stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Automation Selenium</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>JMeter script</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Kịch bản Ansible</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản</td>
      <td>network disconnect</td>
      <td>User login thành công</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>thành công và thất bại.</td>
      <td></td>
      <td>trong <1s</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Automation Selenium</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>API stress</td>
      <td>Thực hiện API stress test để kiểm thử</td>
      <td>invalid</td>
      <td>User login</td>
      <td>JMeter</td>
      <td>Gửi báo cáo</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>est</td>
      <td>chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>data</td>
      <td>thành công trong <1s</td>
      <td>script</td>
      <td>PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Automation Selenium</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Manual test plan</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành</td>
      <td>invalid data</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>công và thất bại.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Manual test plan</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ</td>
      <td>network disconnect</td>
      <td>Hệ thống chịu tải 20k TPS không</td>
      <td>Kịch bản Ansible</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>thống, bao gồm kịch bản thành công và thất bại.</td>
      <td></td>
      <td>gián đoạn</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>JMeter script</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Database</td>
      <td>Thực hiện Database</td>
      <td>DB</td>
      <td>Hệ thống</td>
      <td>Automation</td>
      <td>So sánh</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>ecovery test</td>
      <td>recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>corruption</td>
      <td>chịu tải 20k TPS không gián đoạn</td>
      <td>Selenium</td>
      <td>benchmark với release trước</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Automation Selenium</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch</td>
      <td>invalid data</td>
      <td>User login thành công</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>bản thành công và thất bại.</td>
      <td></td>
      <td>trong <1s</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>JMeter script</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>JMeter script</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Manual test plan</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ</td>
      <td>network disconnect</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau</td>
      <td>Kịch bản Ansible</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>thống, bao gồm kịch bản thành công và thất bại.</td>
      <td></td>
      <td>sự cố</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress</td>
      <td>Thực hiện API stress</td>
      <td>network</td>
      <td>Không</td>
      <td>JMeter</td>
      <td>Theo chuẩn</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>est</td>
      <td>test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>disconnect</td>
      <td>phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>script</td>
      <td>ISTQB</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch</td>
      <td>invalid data</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>bản thành công và thất bại.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Kịch bản Ansible</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Data consistency</td>
      <td>Thực hiện Data consistency test để</td>
      <td>network</td>
      <td>Hệ thống chịu tải</td>
      <td>Manual test</td>
      <td>Phải log toàn</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>est</td>
      <td>kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>disconnect</td>
      <td>20k TPS không gián đoạn</td>
      <td>plan</td>
      <td>bộ kết quả</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>JMeter script</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Automation Selenium</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>oad test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất</td>
      <td>stress load > 10k TPS</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Kịch bản Ansible</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>bại.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>User login thành công trong <1s</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Automation Selenium</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>Kịch bản Ansible</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>JMeter script</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Security</td>
      <td>Thực hiện Security scan để kiểm thử</td>
      <td>valid data</td>
      <td>Dữ liệu được khôi</td>
      <td>Manual test</td>
      <td>Test môi trường Pre-</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>can</td>
      <td>chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td></td>
      <td>phục toàn vẹn sau sự cố</td>
      <td>plan</td>
      <td>Prod</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Kịch bản Ansible</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>ailover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Automation Selenium</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành</td>
      <td>invalid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau</td>
      <td>Manual test plan</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>công và thất bại.</td>
      <td></td>
      <td>sự cố</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Database recovery</td>
      <td>Thực hiện Database recovery test để</td>
      <td>valid data</td>
      <td>User login</td>
      <td>JMeter</td>
      <td>Theo chuẩn</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>est</td>
      <td>kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td></td>
      <td>thành công trong <1s</td>
      <td>script</td>
      <td>ISTQB</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>ailover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Automation Selenium</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống,</td>
      <td>valid data</td>
      <td>User login thành công</td>
      <td>Automation Selenium</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>bao gồm kịch bản thành công và thất bại.</td>
      <td></td>
      <td>trong <1s</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Kịch bản Ansible</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Data</td>
      <td>Thực hiện Data</td>
      <td>DB</td>
      <td>User</td>
      <td>Kịch bản</td>
      <td>Test môi</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>onsistency test</td>
      <td>consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>corruption</td>
      <td>login thành công trong <1s</td>
      <td>Ansible</td>
      <td>trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Automation Selenium</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Automation Selenium</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành</td>
      <td>network disconnect</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>công và thất bại.</td>
      <td></td>
      <td>Top 10</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành</td>
      <td>valid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>công và thất bại.</td>
      <td></td>
      <td>Top 10</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Kịch bản Ansible</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Automation Selenium</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công</td>
      <td>JMeter script</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>gồm kịch bản thành công và thất bại.</td>
      <td></td>
      <td>trong <1s</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>JMeter script</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>JMeter script</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>JMeter script</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng</td>
      <td>stress load > 10k</td>
      <td>Không phát hiện lỗ hổng</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>TPS</td>
      <td>bảo mật OWASP Top 10</td>
      <td></td>
      <td>release trước</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>Kịch bản Ansible</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Data</td>
      <td>Thực hiện Data</td>
      <td>invalid</td>
      <td>User</td>
      <td>Automation</td>
      <td>So sánh</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>onsistency test</td>
      <td>consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>data</td>
      <td>login thành công trong <1s</td>
      <td>Selenium</td>
      <td>benchmark với release trước</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Automation Selenium</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>công và thất bại.</td>
      <td></td>
      <td>Top 10</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Manual test plan</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>Kịch bản Ansible</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery</td>
      <td>Thực hiện Database recovery test để</td>
      <td>network</td>
      <td>Cluster failover</td>
      <td>Manual test</td>
      <td>So sánh benchmark với</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>est</td>
      <td>kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>disconnect</td>
      <td>tự động trong 5s</td>
      <td>plan</td>
      <td>release trước</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>JMeter script</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Kịch bản Ansible</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất</td>
      <td>API call batch 1000 request</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>bại.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Automation Selenium</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Kịch bản Ansible</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng</td>
      <td>invalid data</td>
      <td>Dữ liệu được khôi phục toàn</td>
      <td>JMeter script</td>
      <td>Test môi trường Pre-</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td></td>
      <td>vẹn sau sự cố</td>
      <td></td>
      <td>Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Manual test plan</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Kịch bản Ansible</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Automation Selenium</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Data consistency</td>
      <td>Thực hiện Data consistency test để</td>
      <td>API call batch</td>
      <td>Không phát hiện</td>
      <td>Kịch bản</td>
      <td>Theo chuẩn</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>est</td>
      <td>kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>1000 request</td>
      <td>lỗ hổng bảo mật OWASP Top 10</td>
      <td>Ansible</td>
      <td>ISTQB</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>ata consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch</td>
      <td>invalid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau</td>
      <td>JMeter script</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>bản thành công và thất bại.</td>
      <td></td>
      <td>sự cố</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>JMeter script</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Failover</td>
      <td>Thực hiện Failover test để kiểm thử</td>
      <td>DB</td>
      <td>Không phát hiện</td>
      <td>Automation Theo chuẩn</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>est</td>
      <td>chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>corruption</td>
      <td>lỗ hổng bảo mật OWASP Top 10</td>
      <td>Selenium</td>
      <td>ISTQB</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất</td>
      <td>network disconnect</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>bại.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Kịch bản Ansible</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Database recovery</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng</td>
      <td>network disconnect</td>
      <td>Dữ liệu được khôi phục toàn</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre-</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>est</td>
      <td>và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td></td>
      <td>vẹn sau sự cố</td>
      <td></td>
      <td>Prod</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Kịch bản Ansible</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>oad test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Automation Selenium</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>công và thất bại.</td>
      <td></td>
      <td>Top 10</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu</td>
      <td>network disconnect</td>
      <td>Cluster failover tự động</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td></td>
      <td>trong 5s</td>
      <td></td>
      <td>release trước</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Kịch bản Ansible</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Kịch bản Ansible</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và</td>
      <td>API call batch 1000 request</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>thất bại.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Automation Selenium</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>JMeter script</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Security</td>
      <td>Thực hiện Security scan để kiểm thử</td>
      <td>invalid</td>
      <td>Hệ thống chịu tải</td>
      <td>Kịch bản</td>
      <td>Test môi trường Pre-</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>can</td>
      <td>chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>data</td>
      <td>20k TPS không gián đoạn</td>
      <td>Ansible</td>
      <td>Prod</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>User login thành công trong <1s</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>JMeter script</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và</td>
      <td>network disconnect</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>thất bại.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ</td>
      <td>valid data</td>
      <td>User login thành công</td>
      <td>Manual test plan</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>thống, bao gồm kịch bản thành công và thất bại.</td>
      <td></td>
      <td>trong <1s</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Automation Selenium</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Kịch bản Ansible</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>ogin test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Automation Selenium</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành</td>
      <td>invalid data</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>công và thất bại.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng</td>
      <td>stress load > 10k</td>
      <td>User login thành</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>TPS</td>
      <td>công trong <1s</td>
      <td></td>
      <td>release trước</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Manual test plan</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>JMeter script</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Kịch bản Ansible</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>User login thành công trong <1s</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>oad test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>JMeter script</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Kịch bản Ansible</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và</td>
      <td>invalid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Automation Selenium</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>thất bại.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Kịch bản Ansible</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Kịch bản Ansible</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu</td>
      <td>API call batch 1000</td>
      <td>User login thành</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>request</td>
      <td>công trong <1s</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Automation Selenium</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Automation Selenium</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Automation Selenium</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>oad test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Manual test plan</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Kịch bản Ansible</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất</td>
      <td>invalid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>bại.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Automation Selenium</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức</td>
      <td>stress load > 10k</td>
      <td>Hệ thống chịu tải</td>
      <td>Automation</td>
      <td>Phải log toàn</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>TPS</td>
      <td>20k TPS không gián đoạn</td>
      <td>Selenium</td>
      <td>bộ kết quả</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Kịch bản Ansible</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>JMeter script</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Kịch bản Ansible</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>JMeter script</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>ogin test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>JMeter script</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Automation Selenium</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và</td>
      <td>invalid data</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>JMeter script</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>thất bại.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Manual test plan</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức</td>
      <td>invalid</td>
      <td>Hệ thống chịu tải</td>
      <td>Kịch bản</td>
      <td>Phải log toàn</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>data</td>
      <td>20k TPS không gián đoạn</td>
      <td>Ansible</td>
      <td>bộ kết quả</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>JMeter script</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Kịch bản Ansible</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>ogin test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Automation Selenium</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản</td>
      <td>invalid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP</td>
      <td>Kịch bản Ansible</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>thành công và thất bại.</td>
      <td></td>
      <td>Top 10</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>User login thành công trong <1s</td>
      <td>Kịch bản Ansible</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức</td>
      <td>API call batch</td>
      <td>Cluster failover</td>
      <td>Kịch bản</td>
      <td>So sánh benchmark với</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>1000 request</td>
      <td>tự động trong 5s</td>
      <td>Ansible</td>
      <td>release trước</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Kịch bản Ansible</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>JMeter script</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và</td>
      <td>network disconnect</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>thất bại.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>User login thành công trong <1s</td>
      <td>Kịch bản Ansible</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Kịch bản Ansible</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu</td>
      <td>valid data</td>
      <td>Không phát hiện lỗ hổng</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td></td>
      <td>bảo mật OWASP Top 10</td>
      <td></td>
      <td>release trước</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>JMeter script</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và</td>
      <td>network disconnect</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>thất bại.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>User login thành công trong <1s</td>
      <td>Kịch bản Ansible</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Security</td>
      <td>Thực hiện Security scan để kiểm thử</td>
      <td>API call batch</td>
      <td>Hệ thống chịu tải</td>
      <td>Manual test</td>
      <td>So sánh benchmark với</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>can</td>
      <td>chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>1000 request</td>
      <td>20k TPS không gián đoạn</td>
      <td>plan</td>
      <td>release trước</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Manual test plan</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>User login thành công trong <1s</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>API stress</td>
      <td>Thực hiện API stress</td>
      <td>invalid</td>
      <td>Không</td>
      <td>Kịch bản</td>
      <td>Gửi báo cáo</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>est</td>
      <td>test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>data</td>
      <td>phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Ansible</td>
      <td>PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Automation Selenium</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>User login thành công trong <1s</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Data consistency test</td>
      <td>Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và</td>
      <td>valid data</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>thất bại.</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>JMeter script</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>JMeter script</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Automation Selenium</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất</td>
      <td>invalid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP</td>
      <td>JMeter script</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>bại.</td>
      <td></td>
      <td>Top 10</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Security scan</td>
      <td>Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Kịch bản Ansible</td>
      <td>So sánh benchmark với release trước</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>DB corruption</td>
      <td>User login thành công trong <1s</td>
      <td>Manual test plan</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Cluster failover tự động trong 5s</td>
      <td>Automation Selenium</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
    <tr>
      <td>Database recovery</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng</td>
      <td>valid data</td>
      <td>Cluster failover tự động</td>
      <td>Kịch bản Ansible</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>est</td>
      <td>và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td></td>
      <td>trong 5s</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>API call batch 1000 request</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>Kịch bản Ansible</td>
      <td>Test môi trường Pre- Prod</td>
    </tr>
    <tr>
      <td>Database recovery test</td>
      <td>Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>User login thành công trong <1s</td>
      <td>Kịch bản Ansible</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Load test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>API stress test</td>
      <td>Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>stress load > 10k TPS</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Manual test plan</td>
      <td>Gửi báo cáo PDF hàng ngày</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>oad test</td>
      <td>Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>invalid data</td>
      <td>User login thành công trong <1s</td>
      <td>Kịch bản Ansible</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Hệ thống chịu tải 20k TPS không gián đoạn</td>
      <td>Kịch bản Ansible</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>valid data</td>
      <td>Không phát hiện lỗ hổng bảo mật OWASP Top 10</td>
      <td>Kịch bản Ansible</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
    <tr>
      <td>Failover test</td>
      <td>Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>Dữ liệu được khôi phục toàn vẹn sau sự cố</td>
      <td>JMeter script</td>
      <td>Phải log toàn bộ kết quả</td>
    </tr>
    <tr>
      <td>Login test</td>
      <td>Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.</td>
      <td>network disconnect</td>
      <td>User login thành công trong <1s</td>
      <td>Automation Selenium</td>
      <td>Theo chuẩn ISTQB</td>
    </tr>
  </tbody>
</table>
