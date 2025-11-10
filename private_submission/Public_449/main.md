# Public_449

<table>
  
  <tbody>
    <tr>
      <td>Module</td>
      <td>Loại log</td>
      <td>Mức độ</td>
      <td>Hành động</td>
      <td>Mô tả chi tiết</td>
      <td>Kết quả</td>
      <td>Ghi chú</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Xuất log</td>
      <td>Hệ thống RPA Xuất log loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống CRM Nén và lưu trữ log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>PerformanceLog Error</td>
      <td></td>
      <td>Phân tích log</td>
      <td>Hệ thống Billing Phân tích log loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>Hệ thống Infra Xóa log loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Warning Xuất</td>
      <td></td>
      <td>Hệ thống QA Xuất</td>
      <td>Không</td>
      <td>Có dashboard</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>log</td>
      <td>log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>mất mát dữ liệu</td>
      <td>Grafana</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống IPCC Nén và lưu trữ log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>Hệ thống IPCC Xóa log loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Warning Xóa</td>
      <td>log</td>
      <td>Hệ thống Billing Xóa log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống CRM Gửi log sang SIEM loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Gửi log</td>
      <td>Hệ thống Infra Gửi log sang SIEM loại</td>
      <td>Không mất mát</td>
      <td>Theo chuẩn syslog</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>sang SIEM</td>
      <td>AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>dữ liệu</td>
      <td>RFC5424</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Xuất log</td>
      <td>Hệ thống RPA Xuất log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống QA Nén và lưu trữ log loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Xuất log</td>
      <td>Hệ thống Billing Xuất log loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống IVR Xóa log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>PerformanceLog Error</td>
      <td></td>
      <td>Xóa log</td>
      <td>Hệ thống IVR Xóa log loại PerformanceLog</td>
      <td>Có chỉ số thống</td>
      <td>Gửi log sang ELK</td>
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
      <td>với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>kê</td>
      <td></td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống IPCC Nén và lưu trữ log loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Warning Xuất</td>
      <td>log</td>
      <td>Hệ thống Infra Xuất log loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AccessLog</td>
      <td>Warning Nén</td>
      <td>và lưu trữ log</td>
      <td>Hệ thống QA Nén và lưu trữ log loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Xuất log</td>
      <td>Hệ thống Infra Xuất log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>Hệ thống QA Xóa log loại AuditLog với mức Error, dữ liệu lưu trữ tối</td>
      <td>Tích hợp cảnh báo</td>
      <td>Phân quyền chi tiết</td>
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
      <td>thiểu 90 ngày.</td>
      <td>realtime</td>
      <td></td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AuditLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống CRM Xóa log loại AuditLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td></td>
      <td>PerformanceLog Warning Xuất</td>
      <td>log</td>
      <td>Hệ thống CRM Xuất log loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Xuất log</td>
      <td>Hệ thống Infra Xuất log loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống IPCC Nén và lưu trữ log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống IPCC Xóa log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối</td>
      <td>Có chỉ số thống kê</td>
      <td>Phân quyền chi tiết</td>
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
      <td>thiểu 90 ngày.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Phân tích log</td>
      <td>Hệ thống Billing Phân tích log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống RPA Xóa log loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Xuất log</td>
      <td>Hệ thống Infra Xuất log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Warning Xuất</td>
      <td>log</td>
      <td>Hệ thống IVR Xuất log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Warning Gửi</td>
      <td>log sang SIEM</td>
      <td>Hệ thống QA Gửi log sang SIEM loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog Critical</td>
      <td></td>
      <td>Phân</td>
      <td>Hệ thống Infra</td>
      <td>Có chỉ</td>
      <td>Theo chuẩn</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>tích log</td>
      <td>Phân tích log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>số thống kê</td>
      <td>syslog RFC5424</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Xuất log</td>
      <td>Hệ thống QA Xuất log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống IPCC Nén và lưu trữ log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>PerformanceLog Critical</td>
      <td></td>
      <td>Phân tích log</td>
      <td>Hệ thống RPA Phân tích log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>Hệ thống Infra Xóa log loại AuditLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống RPA Xóa log loại ErrorLog với mức Fatal, dữ</td>
      <td>Tích hợp cảnh</td>
      <td>Phân quyền chi tiết</td>
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
      <td>liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>báo realtime</td>
      <td></td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống Billing Gửi log sang SIEM loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>PerformanceLog Critical</td>
      <td></td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống CRM Gửi log sang SIEM loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống Billing Nén và lưu trữ log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Phân tích log</td>
      <td>Hệ thống CRM Phân tích log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Xuất log</td>
      <td>Hệ thống IVR Xuất log loại AuditLog với mức Critical,</td>
      <td>Không mất mát</td>
      <td>Gửi log sang ELK</td>
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
      <td>dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>dữ liệu</td>
      <td></td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Xuất log</td>
      <td>Hệ thống CRM Xuất log loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Phân tích log</td>
      <td>Hệ thống IPCC Phân tích log loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống QA Nén và lưu trữ log loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống CRM Gửi log sang SIEM loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Warning Nén</td>
      <td>và lưu trữ</td>
      <td>Hệ thống Infra Nén và lưu trữ log loại ErrorLog với mức Warning, dữ liệu</td>
      <td>Log được mã hóa AES-</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>log</td>
      <td>lưu trữ tối thiểu 90 ngày.</td>
      <td>256</td>
      <td></td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống RPA Gửi log sang SIEM loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Xuất log</td>
      <td>Hệ thống QA Xuất log loại ErrorLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Xuất log</td>
      <td>Hệ thống QA Xuất log loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống CRM Gửi log sang SIEM loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td></td>
      <td>PerformanceLog Warning Nén</td>
      <td>và lưu trữ log</td>
      <td>Hệ thống Billing Nén và lưu trữ log loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Có dashboard Grafana</td>
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
      <td>thiểu 90 ngày.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống IPCC Gửi log sang SIEM loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AuditLog</td>
      <td>Warning Xuất</td>
      <td>log</td>
      <td>Hệ thống Billing Xuất log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Xuất log</td>
      <td>Hệ thống Billing Xuất log loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống Billing Nén và lưu trữ log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AccessLog</td>
      <td>Warning Nén</td>
      <td>và lưu trữ log</td>
      <td>Hệ thống CRM Nén và lưu trữ log loại AccessLog với mức Warning, dữ liệu lưu trữ tối</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Tự động xóa log sau 180 ngày</td>
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
      <td>thiểu 90 ngày.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Phân tích log</td>
      <td>Hệ thống Infra Phân tích log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>Hệ thống IPCC Xóa log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống QA Nén và lưu trữ log loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Phân tích log</td>
      <td>Hệ thống IPCC Phân tích log loại ErrorLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>Hệ thống Infra Phân tích log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90</td>
      <td>Không mất mát dữ liệu</td>
      <td>Phân quyền chi tiết</td>
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
      <td>ngày.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AccessLog</td>
      <td>Warning</td>
      <td>Phân tích log</td>
      <td>Hệ thống IVR Phân tích log loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống IVR Nén và lưu trữ log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống QA Gửi log sang SIEM loại ErrorLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Phân tích log</td>
      <td>Hệ thống RPA Phân tích log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống Billing Gửi log sang SIEM loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90</td>
      <td>Không mất mát dữ liệu</td>
      <td>Tự động xóa log sau 180 ngày</td>
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
      <td>ngày.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Phân tích log</td>
      <td>Hệ thống CRM Phân tích log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống Billing Nén và lưu trữ log loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống RPA Nén và lưu trữ log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>Hệ thống Infra Xóa log loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống IVR Nén và lưu trữ log loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>IPCC</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống IPCC Gửi log sang SIEM loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống QA Gửi log sang SIEM loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Warning Xóa</td>
      <td>log</td>
      <td>Hệ thống Infra Xóa log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Warning Gửi</td>
      <td>log sang SIEM</td>
      <td>Hệ thống IVR Gửi log sang SIEM loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AuditLog</td>
      <td>Fatal</td>
      <td>Xuất log</td>
      <td>Hệ thống IVR Xuất log loại AuditLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog</td>
      <td>Info</td>
      <td>Nén và lưu</td>
      <td>Hệ thống Infra Nén và lưu trữ log loại PerformanceLog</td>
      <td>Không mất mát</td>
      <td>Phân quyền chi tiết</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>trữ log</td>
      <td>với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>dữ liệu</td>
      <td></td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>PerformanceLog Error</td>
      <td></td>
      <td>Xuất log</td>
      <td>Hệ thống Billing Xuất log loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống CRM Nén và lưu trữ log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Xuất log</td>
      <td>Hệ thống QA Xuất log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống RPA Gửi log sang SIEM loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Phân tích</td>
      <td>Hệ thống QA Phân tích log loại TransactionLog</td>
      <td>Có chỉ số thống</td>
      <td>Theo chuẩn syslog</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>log</td>
      <td>với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>kê</td>
      <td>RFC5424</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống CRM Gửi log sang SIEM loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>PerformanceLog Critical</td>
      <td></td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống Billing Nén và lưu trữ log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Xuất log</td>
      <td>Hệ thống QA Xuất log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>Hệ thống Billing Xóa log loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AuditLog</td>
      <td>Warning Nén</td>
      <td>và lưu</td>
      <td>Hệ thống CRM Nén và lưu trữ log loại AuditLog với</td>
      <td>Có chỉ số thống</td>
      <td>Phân quyền chi tiết</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>trữ log</td>
      <td>mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>kê</td>
      <td></td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>Hệ thống Billing Xóa log loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>Hệ thống IVR Xóa log loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>Hệ thống IVR Xóa log loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống Billing Nén và lưu trữ log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>Hệ thống Billing Xóa log loại TransactionLog với mức Error, dữ liệu lưu trữ tối</td>
      <td>Log được mã hóa AES-</td>
      <td>Phân quyền chi tiết</td>
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
      <td>thiểu 90 ngày.</td>
      <td>256</td>
      <td></td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>Hệ thống Infra Xóa log loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>Hệ thống RPA Xóa log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Warning Nén</td>
      <td>và lưu trữ log</td>
      <td>Hệ thống Billing Nén và lưu trữ log loại TransactionLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống Infra Xóa log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Warning Gửi</td>
      <td>log sang SIEM</td>
      <td>Hệ thống Infra Gửi log sang SIEM loại TransactionLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Phân quyền chi tiết</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog Critical</td>
      <td></td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống IPCC Nén và lưu trữ log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống IPCC Gửi log sang SIEM loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống RPA Gửi log sang SIEM loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AccessLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>Hệ thống IVR Phân tích log loại AccessLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>Hệ thống Billing Xóa log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
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
      <td>ngày.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống QA Gửi log sang SIEM loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống Billing Gửi log sang SIEM loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Warning Nén</td>
      <td>và lưu trữ log</td>
      <td>Hệ thống Billing Nén và lưu trữ log loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>Hệ thống IPCC Xóa log loại ErrorLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>Hệ thống RPA Phân tích log loại TransactionLog với mức Critical, dữ liệu lưu trữ tối</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Gửi log sang ELK</td>
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
      <td>thiểu 90 ngày.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Phân tích log</td>
      <td>Hệ thống Billing Phân tích log loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống QA Nén và lưu trữ log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AuditLog</td>
      <td>Info</td>
      <td>Phân tích log</td>
      <td>Hệ thống CRM Phân tích log loại AuditLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Warning</td>
      <td>Phân tích log</td>
      <td>Hệ thống QA Phân tích log loại TransactionLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Xuất log</td>
      <td>Hệ thống Billing Xuất log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Gửi log sang ELK</td>
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
      <td>thiểu 90 ngày.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Warning Xóa</td>
      <td>log</td>
      <td>Hệ thống Infra Xóa log loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống Billing Gửi log sang SIEM loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AccessLog</td>
      <td>Critical</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống CRM Nén và lưu trữ log loại AccessLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>ErrorLog</td>
      <td>Warning Xóa</td>
      <td>log</td>
      <td>Hệ thống QA Xóa log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống Infra Nén và lưu trữ log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>IPCC</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống IPCC Nén và lưu trữ log loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống QA Nén và lưu trữ log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>PerformanceLog Error</td>
      <td></td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống CRM Gửi log sang SIEM loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống RPA Nén và lưu trữ log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AuditLog</td>
      <td>Warning</td>
      <td>Phân tích log</td>
      <td>Hệ thống CRM Phân tích log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống Infra Nén và lưu trữ log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>PerformanceLog Critical</td>
      <td></td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống RPA Nén và lưu trữ log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>AuditLog</td>
      <td>Warning</td>
      <td>Phân tích log</td>
      <td>Hệ thống IPCC Phân tích log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Xuất log</td>
      <td>Hệ thống Billing Xuất log loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Warning Xuất</td>
      <td>log</td>
      <td>Hệ thống Billing Xuất log loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Warning Xuất</td>
      <td>log</td>
      <td>Hệ thống QA Xuất log loại TransactionLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AccessLog</td>
      <td>Warning Gửi</td>
      <td>log sang SIEM</td>
      <td>Hệ thống IVR Gửi log sang SIEM loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Warning Xóa</td>
      <td>log</td>
      <td>Hệ thống IVR Xóa log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>AuditLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống IPCC Xóa log loại AuditLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống Infra Nén và lưu trữ log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Nén và</td>
      <td>Hệ thống Infra Nén và lưu trữ log loại</td>
      <td>Tích hợp</td>
      <td>Theo chuẩn syslog</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>lưu trữ log</td>
      <td>AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>cảnh báo realtime</td>
      <td>RFC5424</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog Critical</td>
      <td></td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống IPCC Gửi log sang SIEM loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td></td>
      <td>PerformanceLog Warning</td>
      <td>Phân tích log</td>
      <td>Hệ thống Infra Phân tích log loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống Infra Xóa log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>PerformanceLog Critical</td>
      <td></td>
      <td>Phân tích log</td>
      <td>Hệ thống QA Phân tích log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog Critical</td>
      <td></td>
      <td>Xóa log</td>
      <td>Hệ thống Infra Xóa log loại PerformanceLog</td>
      <td>Có thể truy xuất khi</td>
      <td>Theo chuẩn syslog</td>
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
      <td>với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>cần</td>
      <td>RFC5424</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống QA Nén và lưu trữ log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Warning Nén</td>
      <td>và lưu trữ log</td>
      <td>Hệ thống RPA Nén và lưu trữ log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>Hệ thống IPCC Xóa log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống QA Xóa log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AuditLog</td>
      <td>Warning Nén</td>
      <td>và lưu trữ</td>
      <td>Hệ thống RPA Nén và lưu trữ log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90</td>
      <td>Log được mã hóa AES-</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>log</td>
      <td>ngày.</td>
      <td>256</td>
      <td></td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Fatal</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống QA Gửi log sang SIEM loại AuditLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td></td>
      <td>PerformanceLog Warning Gửi</td>
      <td>log sang SIEM</td>
      <td>Hệ thống CRM Gửi log sang SIEM loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống RPA Gửi log sang SIEM loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AuditLog</td>
      <td>Warning Nén</td>
      <td>và lưu trữ log</td>
      <td>Hệ thống Billing Nén và lưu trữ log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Nén và lưu trữ</td>
      <td>Hệ thống IPCC Nén và lưu trữ log loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90</td>
      <td>Log được mã hóa AES-</td>
      <td>Gửi log sang ELK</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>log</td>
      <td>ngày.</td>
      <td>256</td>
      <td></td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td></td>
      <td>PerformanceLog Warning Nén</td>
      <td>và lưu trữ log</td>
      <td>Hệ thống IPCC Nén và lưu trữ log loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>TransactionLog</td>
      <td>Warning Gửi</td>
      <td>log sang SIEM</td>
      <td>Hệ thống IPCC Gửi log sang SIEM loại TransactionLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td></td>
      <td>PerformanceLog Warning</td>
      <td>Phân tích log</td>
      <td>Hệ thống IVR Phân tích log loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>Hệ thống Infra Phân tích log loại AccessLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td></td>
      <td>PerformanceLog Warning Nén</td>
      <td>và lưu trữ</td>
      <td>Hệ thống Billing Nén và lưu trữ log loại PerformanceLog</td>
      <td>Có thể truy xuất khi</td>
      <td>Phân quyền chi tiết</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>log</td>
      <td>với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>cần</td>
      <td></td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AccessLog</td>
      <td>Warning Gửi</td>
      <td>log sang SIEM</td>
      <td>Hệ thống QA Gửi log sang SIEM loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>QA</td>
      <td></td>
      <td>PerformanceLog Warning Gửi</td>
      <td>log sang SIEM</td>
      <td>Hệ thống QA Gửi log sang SIEM loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Xuất log</td>
      <td>Hệ thống IPCC Xuất log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống Infra Gửi log sang SIEM loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Gửi log sang</td>
      <td>Hệ thống IPCC Gửi log sang SIEM loại ErrorLog với mức Error, dữ liệu</td>
      <td>Có thể truy xuất khi</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>SIEM</td>
      <td>lưu trữ tối thiểu 90 ngày.</td>
      <td>cần</td>
      <td></td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống IVR Nén và lưu trữ log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống Billing Gửi log sang SIEM loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>PerformanceLog Critical</td>
      <td></td>
      <td>Phân tích log</td>
      <td>Hệ thống RPA Phân tích log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống IPCC Gửi log sang SIEM loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Nén và lưu trữ</td>
      <td>Hệ thống Infra Nén và lưu trữ log loại AuditLog với mức Critical, dữ liệu lưu</td>
      <td>Tích hợp cảnh báo</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>log</td>
      <td>trữ tối thiểu 90 ngày.</td>
      <td>realtime</td>
      <td></td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>Hệ thống Billing Xóa log loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Xuất log</td>
      <td>Hệ thống QA Xuất log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>QA</td>
      <td></td>
      <td>PerformanceLog Warning Gửi</td>
      <td>log sang SIEM</td>
      <td>Hệ thống QA Gửi log sang SIEM loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>Hệ thống Infra Xóa log loại ErrorLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>Hệ thống CRM Xóa log loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>IPCC</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống IPCC Gửi log sang SIEM loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Fatal</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống QA Nén và lưu trữ log loại AuditLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống RPA Xóa log loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Xuất log</td>
      <td>Hệ thống CRM Xuất log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog</td>
      <td>Info</td>
      <td>Xuất log</td>
      <td>Hệ thống Infra Xuất log loại PerformanceLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Warning Gửi</td>
      <td>log</td>
      <td>Hệ thống Infra Gửi log sang SIEM loại</td>
      <td>Tích hợp</td>
      <td>Theo chuẩn syslog</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>sang SIEM</td>
      <td>TransactionLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>cảnh báo realtime</td>
      <td>RFC5424</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AuditLog</td>
      <td>Warning Xuất</td>
      <td>log</td>
      <td>Hệ thống IVR Xuất log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Warning Xóa</td>
      <td>log</td>
      <td>Hệ thống Billing Xóa log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog Critical</td>
      <td></td>
      <td>Phân tích log</td>
      <td>Hệ thống IPCC Phân tích log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống RPA Nén và lưu trữ log loại ErrorLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Xuất log</td>
      <td>Hệ thống RPA Xuất log loại TransactionLog với mức Critical,</td>
      <td>Không mất mát dữ liệu</td>
      <td>Có dashboard Grafana</td>
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
      <td>dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống RPA Nén và lưu trữ log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Phân tích log</td>
      <td>Hệ thống QA Phân tích log loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống RPA Gửi log sang SIEM loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Warning</td>
      <td>Phân tích log</td>
      <td>Hệ thống RPA Phân tích log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>PerformanceLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>Hệ thống CRM Xóa log loại PerformanceLog với mức Info, dữ liệu lưu trữ tối</td>
      <td>Có chỉ số thống kê</td>
      <td>Phân quyền chi tiết</td>
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
      <td>thiểu 90 ngày.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống Infra Nén và lưu trữ log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>Hệ thống IVR Phân tích log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog Error</td>
      <td></td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống Infra Nén và lưu trữ log loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống IPCC Gửi log sang SIEM loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Nén và lưu trữ</td>
      <td>Hệ thống IPCC Nén và lưu trữ log loại ErrorLog với mức Error, dữ liệu lưu trữ tối thiểu 90</td>
      <td>Có chỉ số thống kê</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>log</td>
      <td>ngày.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>PerformanceLog Error</td>
      <td></td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống RPA Gửi log sang SIEM loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>Hệ thống Infra Xóa log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>PerformanceLog Critical</td>
      <td></td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống IVR Gửi log sang SIEM loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống Infra Gửi log sang SIEM loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>Hệ thống IVR Xóa log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Nén</td>
      <td>Hệ thống QA Nén</td>
      <td>Có thể</td>
      <td>Tự động xóa</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>và lưu trữ log</td>
      <td>và lưu trữ log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>truy xuất khi cần</td>
      <td>log sau 180 ngày</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>Hệ thống RPA Phân tích log loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống RPA Xóa log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống Billing Xóa log loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống RPA Xóa log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AccessLog</td>
      <td>Warning Xuất</td>
      <td>log</td>
      <td>Hệ thống CRM Xuất log loại AccessLog với</td>
      <td>Có thể truy xuất khi</td>
      <td>Gửi log sang ELK</td>
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
      <td>mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>cần</td>
      <td></td>
    </tr>
    <tr>
      <td>IVR</td>
      <td></td>
      <td>PerformanceLog Warning Gửi</td>
      <td>log sang SIEM</td>
      <td>Hệ thống IVR Gửi log sang SIEM loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog Error</td>
      <td></td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống IPCC Nén và lưu trữ log loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống QA Nén và lưu trữ log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Phân tích log</td>
      <td>Hệ thống QA Phân tích log loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AuditLog</td>
      <td>Info</td>
      <td>Phân tích</td>
      <td>Hệ thống RPA Phân tích log loại AuditLog với mức</td>
      <td>Có thể truy xuất khi</td>
      <td>Phân quyền chi tiết</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>log</td>
      <td>Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>cần</td>
      <td></td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống Billing Nén và lưu trữ log loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống CRM Nén và lưu trữ log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống Billing Xóa log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Xuất log</td>
      <td>Hệ thống CRM Xuất log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Warning Gửi</td>
      <td>log sang</td>
      <td>Hệ thống Infra Gửi log sang SIEM loại AccessLog với</td>
      <td>Có chỉ số thống</td>
      <td>Có dashboard Grafana</td>
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
      <td>SIEM mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>kê</td>
      <td></td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>AuditLog</td>
      <td>Fatal</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống IPCC Gửi log sang SIEM loại AuditLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Warning Nén</td>
      <td>và lưu trữ log</td>
      <td>Hệ thống CRM Nén và lưu trữ log loại TransactionLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Xuất log</td>
      <td>Hệ thống IVR Xuất log loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>Hệ thống CRM Xóa log loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Nén và lưu trữ</td>
      <td>Hệ thống Infra Nén và lưu trữ log loại TransactionLog với mức Fatal, dữ</td>
      <td>Không mất mát dữ liệu</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>log</td>
      <td>liệu lưu trữ tối thiểu 90 ngày.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog Critical</td>
      <td></td>
      <td>Xuất log</td>
      <td>Hệ thống IPCC Xuất log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống Billing Xóa log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống Infra Xóa log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống IPCC Gửi log sang SIEM loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Phân tích log</td>
      <td>Hệ thống IPCC Phân tích log loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
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
      <td>ngày.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Infra</td>
      <td></td>
      <td>PerformanceLog Warning Gửi</td>
      <td>log sang SIEM</td>
      <td>Hệ thống Infra Gửi log sang SIEM loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td></td>
      <td>PerformanceLog Warning Gửi</td>
      <td>log sang SIEM</td>
      <td>Hệ thống IPCC Gửi log sang SIEM loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống Billing Nén và lưu trữ log loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>PerformanceLog</td>
      <td>Info</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống Billing Gửi log sang SIEM loại PerformanceLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Xuất log</td>
      <td>Hệ thống CRM Xuất log loại ErrorLog với mức Fatal, dữ liệu lưu</td>
      <td>Có chỉ số thống</td>
      <td>Theo chuẩn syslog RFC5424</td>
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
      <td>trữ tối thiểu 90 ngày.</td>
      <td>kê</td>
      <td></td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống Billing Nén và lưu trữ log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>Hệ thống CRM Phân tích log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Fatal</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống QA Gửi log sang SIEM loại AuditLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Phân tích log</td>
      <td>Hệ thống QA Phân tích log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Xuất log</td>
      <td>Hệ thống Infra Xuất log loại TransactionLog với mức Critical, dữ liệu lưu trữ tối</td>
      <td>Có chỉ số thống kê</td>
      <td>Tự động xóa log sau 180 ngày</td>
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
      <td>thiểu 90 ngày.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>Hệ thống CRM Phân tích log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AuditLog</td>
      <td>Warning Xuất</td>
      <td>log</td>
      <td>Hệ thống Billing Xuất log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>AccessLog</td>
      <td>Warning</td>
      <td>Phân tích log</td>
      <td>Hệ thống IPCC Phân tích log loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>PerformanceLog Critical</td>
      <td></td>
      <td>Xuất log</td>
      <td>Hệ thống Billing Xuất log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Xuất log</td>
      <td>Hệ thống RPA Xuất log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Có dashboard Grafana</td>
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
      <td>ngày.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống CRM Nén và lưu trữ log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AuditLog</td>
      <td>Info</td>
      <td>Xuất log</td>
      <td>Hệ thống RPA Xuất log loại AuditLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Xuất log</td>
      <td>Hệ thống RPA Xuất log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Xuất log</td>
      <td>Hệ thống RPA Xuất log loại ErrorLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>Hệ thống QA Xóa log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>IVR</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống IVR Gửi log sang SIEM loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Warning Gửi</td>
      <td>log sang SIEM</td>
      <td>Hệ thống QA Gửi log sang SIEM loại TransactionLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>Hệ thống Infra Phân tích log loại AccessLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống RPA Gửi log sang SIEM loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AccessLog</td>
      <td>Warning Gửi</td>
      <td>log sang SIEM</td>
      <td>Hệ thống CRM Gửi log sang SIEM loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Có dashboard Grafana</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>RPA</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>Hệ thống RPA Xóa log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống RPA Gửi log sang SIEM loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>Hệ thống RPA Xóa log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>ErrorLog</td>
      <td>Warning Nén</td>
      <td>và lưu trữ log</td>
      <td>Hệ thống CRM Nén và lưu trữ log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>Hệ thống Infra Xóa log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>PerformanceLog</td>
      <td>Info</td>
      <td>Nén và</td>
      <td>Hệ thống Billing Nén và lưu trữ log</td>
      <td>Không mất mát</td>
      <td>Gửi log sang</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>lưu trữ log</td>
      <td>loại PerformanceLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>dữ liệu</td>
      <td>ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Phân tích log</td>
      <td>Hệ thống Infra Phân tích log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>Hệ thống IPCC Xóa log loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog Error</td>
      <td></td>
      <td>Xóa log</td>
      <td>Hệ thống IPCC Xóa log loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Warning Xóa</td>
      <td>log</td>
      <td>Hệ thống Billing Xóa log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Gửi log</td>
      <td>Hệ thống IVR Gửi log sang SIEM loại</td>
      <td>Log được</td>
      <td>Có dashboard</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>sang SIEM</td>
      <td>ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>mã hóa AES- 256</td>
      <td>Grafana</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>PerformanceLog Error</td>
      <td></td>
      <td>Xuất log</td>
      <td>Hệ thống CRM Xuất log loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Xóa log</td>
      <td>Hệ thống Billing Xóa log loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Phân tích log</td>
      <td>Hệ thống QA Phân tích log loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Fatal</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống Infra Gửi log sang SIEM loại AuditLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Xuất log</td>
      <td>Hệ thống QA Xuất log loại AuditLog với mức Critical,</td>
      <td>Có chỉ số thống</td>
      <td>Theo chuẩn syslog</td>
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
      <td>dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>kê</td>
      <td>RFC5424</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>PerformanceLog Error</td>
      <td></td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống QA Gửi log sang SIEM loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>Hệ thống Infra Xóa log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống IVR Nén và lưu trữ log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>TransactionLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>Hệ thống CRM Xóa log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AccessLog</td>
      <td>Critical</td>
      <td>Phân tích log</td>
      <td>Hệ thống CRM Phân tích log loại AccessLog với mức Critical, dữ liệu lưu trữ tối</td>
      <td>Log được mã hóa AES-</td>
      <td>Theo chuẩn syslog RFC5424</td>
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
      <td>thiểu 90 ngày.</td>
      <td>256</td>
      <td></td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Xóa log</td>
      <td>Hệ thống RPA Xóa log loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AuditLog</td>
      <td>Info</td>
      <td>Xuất log</td>
      <td>Hệ thống RPA Xuất log loại AuditLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Warning</td>
      <td>Phân tích log</td>
      <td>Hệ thống Infra Phân tích log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>PerformanceLog</td>
      <td>Info</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống CRM Nén và lưu trữ log loại PerformanceLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống Billing Nén và lưu trữ log loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Phân quyền chi tiết</td>
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
      <td>ngày.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Phân tích log</td>
      <td>Hệ thống IVR Phân tích log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống QA Nén và lưu trữ log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Warning Xuất</td>
      <td>log</td>
      <td>Hệ thống Infra Xuất log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>PerformanceLog</td>
      <td>Info</td>
      <td>Phân tích log</td>
      <td>Hệ thống IPCC Phân tích log loại PerformanceLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>PerformanceLog Critical</td>
      <td></td>
      <td>Phân tích log</td>
      <td>Hệ thống IVR Phân tích log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối</td>
      <td>Có chỉ số thống kê</td>
      <td>Theo chuẩn syslog RFC5424</td>
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
      <td>thiểu 90 ngày.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống Infra Nén và lưu trữ log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống QA Gửi log sang SIEM loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống IVR Xóa log loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống Billing Gửi log sang SIEM loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống Infra Xóa log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Phân quyền chi tiết</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Xuất log</td>
      <td>Hệ thống Billing Xuất log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Warning Xóa</td>
      <td>log</td>
      <td>Hệ thống IPCC Xóa log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AccessLog</td>
      <td>Error</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống IVR Gửi log sang SIEM loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Phân tích log</td>
      <td>Hệ thống Infra Phân tích log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AuditLog</td>
      <td>Error</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống Infra Gửi log sang SIEM loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Phân quyền chi tiết</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Warning Xóa</td>
      <td>log</td>
      <td>Hệ thống Infra Xóa log loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống IVR Gửi log sang SIEM loại ErrorLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống Infra Nén và lưu trữ log loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>QA</td>
      <td>TransactionLog</td>
      <td>Fatal</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống QA Nén và lưu trữ log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Xóa log</td>
      <td>Hệ thống RPA Xóa log loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Error</td>
      <td>Xuất log</td>
      <td>Hệ thống RPA Xuất log loại ErrorLog với mức</td>
      <td>Có chỉ số thống</td>
      <td>Theo chuẩn syslog</td>
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
      <td>Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>kê</td>
      <td>RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống Infra Nén và lưu trữ log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>TransactionLog</td>
      <td>Critical</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống IPCC Gửi log sang SIEM loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>PerformanceLog</td>
      <td>Info</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống Infra Gửi log sang SIEM loại PerformanceLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống RPA Nén và lưu trữ log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>AuditLog</td>
      <td>Critical</td>
      <td>Xuất log</td>
      <td>Hệ thống Billing Xuất log loại AuditLog với mức</td>
      <td>Có chỉ số thống</td>
      <td>Phân quyền chi tiết</td>
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
      <td>Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>kê</td>
      <td></td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AuditLog</td>
      <td>Info</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống IVR Gửi log sang SIEM loại AuditLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AuditLog</td>
      <td>Warning Xuất</td>
      <td>log</td>
      <td>Hệ thống RPA Xuất log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Có dashboard Grafana</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>AuditLog</td>
      <td>Info</td>
      <td>Phân tích log</td>
      <td>Hệ thống IPCC Phân tích log loại AuditLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Xuất log</td>
      <td>Hệ thống IVR Xuất log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>ErrorLog</td>
      <td>Warning Nén</td>
      <td>và lưu trữ</td>
      <td>Hệ thống RPA Nén và lưu trữ log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90</td>
      <td>Tích hợp cảnh báo</td>
      <td>Gửi log sang ELK</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>log</td>
      <td>ngày.</td>
      <td>realtime</td>
      <td></td>
    </tr>
    <tr>
      <td>QA</td>
      <td>AuditLog</td>
      <td>Warning Xóa</td>
      <td>log</td>
      <td>Hệ thống QA Xóa log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Info</td>
      <td>Phân tích log</td>
      <td>Hệ thống IPCC Phân tích log loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>IVR</td>
      <td>ErrorLog</td>
      <td>Warning</td>
      <td>Phân tích log</td>
      <td>Hệ thống IVR Phân tích log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Phân quyền chi tiết</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>TransactionLog</td>
      <td>Warning Xuất</td>
      <td>log</td>
      <td>Hệ thống Infra Xuất log loại TransactionLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AccessLog</td>
      <td>Fatal</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống RPA Gửi log sang SIEM loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Gửi log sang ELK</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>CRM</td>
      <td>ErrorLog</td>
      <td>Fatal</td>
      <td>Xóa log</td>
      <td>Hệ thống CRM Xóa log loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>IPCC</td>
      <td>ErrorLog</td>
      <td>Critical</td>
      <td>Xuất log</td>
      <td>Hệ thống IPCC Xuất log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>RPA</td>
      <td>AuditLog</td>
      <td>Info</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống RPA Nén và lưu trữ log loại AuditLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có thể truy xuất khi cần</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>PerformanceLog Critical</td>
      <td></td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống Billing Nén và lưu trữ log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Infra</td>
      <td>AccessLog</td>
      <td>Critical</td>
      <td>Xuất log</td>
      <td>Hệ thống Infra Xuất log loại AccessLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Phân quyền chi tiết</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>IVR</td>
      <td>AccessLog</td>
      <td>Critical</td>
      <td>Xuất log</td>
      <td>Hệ thống IVR Xuất log loại AccessLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Không mất mát dữ liệu</td>
      <td>Gửi log sang ELK</td>
    </tr>
    <tr>
      <td>Billing</td>
      <td>TransactionLog</td>
      <td>Error</td>
      <td>Gửi log sang SIEM</td>
      <td>Hệ thống Billing Gửi log sang SIEM loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Log được mã hóa AES- 256</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>AccessLog</td>
      <td>Info</td>
      <td>Xuất log</td>
      <td>Hệ thống CRM Xuất log loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>PerformanceLog Critical</td>
      <td></td>
      <td>Xóa log</td>
      <td>Hệ thống CRM Xóa log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Tích hợp cảnh báo realtime</td>
      <td>Theo chuẩn syslog RFC5424</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>PerformanceLog</td>
      <td>Fatal</td>
      <td>Nén và lưu trữ log</td>
      <td>Hệ thống CRM Nén và lưu trữ log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.</td>
      <td>Có chỉ số thống kê</td>
      <td>Tự động xóa log sau 180 ngày</td>
    </tr>
  </tbody>
</table>
