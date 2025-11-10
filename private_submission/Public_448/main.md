# Public_448

<table>
  
  <tbody>
    <tr>
      <td>API</td>
      <td>Phương thức</td>
      <td>Hành động</td>
      <td>Mô tả chi tiết</td>
      <td>Kết quả</td>
      <td>Ghi chú</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PATCH</td>
      <td>Thêm bản ghi</td>
      <td>API /customer/update sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /invoice/export sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/security/firewall/config GET</td>
      <td></td>
      <td>Xóa thông tin</td>
      <td>API /security/firewall/config sử dụng phương thức GET để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /ivr/callflow sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Export dữ liệu</td>
      <td>API /crm/lead/import sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>/rpa/task/execute</td>
      <td>POST</td>
      <td>Cập nhật cấu hình</td>
      <td>API /rpa/task/execute sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>GET</td>
      <td>Thêm bản ghi</td>
      <td>API /customer/update sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /network/qos/monitor sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>Cập nhật cấu hình</td>
      <td>API /invoice/export sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>Export dữ liệu</td>
      <td>API /network/qos/monitor sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>/rpa/task/execute</td>
      <td>POST</td>
      <td>Export dữ liệu</td>
      <td>API /rpa/task/execute sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Export dữ liệu</td>
      <td>API /crm/lead/import sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>Cập nhật cấu hình</td>
      <td>API /invoice/export sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>GET</td>
      <td>Xóa thông tin</td>
      <td>API /ivr/callflow sử dụng phương thức GET để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td></td>
      <td>/security/firewall/config DELETE Kiểm</td>
      <td>tra trạng thái</td>
      <td>API /security/firewall/config sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Xóa thông tin</td>
      <td>API /ivr/callflow sử dụng phương thức POST để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /security/firewall/config sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Thêm bản ghi</td>
      <td>API /invoice/export sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PATCH</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /invoice/export sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Cập nhật cấu hình</td>
      <td>API /crm/lead/import sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PUT</td>
      <td>Thêm bản</td>
      <td>API /ivr/callflow sử dụng phương thức PUT</td>
      <td>Log đầy</td>
      <td>Tích hợp với API</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>ghi</td>
      <td>để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>đủ</td>
      <td>Gateway</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>POST</td>
      <td>Thêm bản ghi</td>
      <td>API /rpa/task/execute sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE Kiểm</td>
      <td>tra trạng thái</td>
      <td>API /rpa/task/execute sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /crm/lead/import sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>DELETE Cập</td>
      <td>nhật cấu hình</td>
      <td>API /crm/lead/import sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>DELETE Thêm</td>
      <td>bản ghi</td>
      <td>API /network/qos/monitor sử dụng phương thức DELETE để Thêm bản</td>
      <td>Thành công <1s</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>DELETE Thêm</td>
      <td>bản ghi</td>
      <td>API /crm/lead/import sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Cập nhật cấu hình</td>
      <td>API /rpa/task/execute sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Export dữ liệu</td>
      <td>API /invoice/export sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /security/firewall/config sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>POST</td>
      <td>Kiểm tra trạng</td>
      <td>API /rpa/task/execute sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực</td>
      <td>Log đầy đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>thái</td>
      <td>OAuth2 và log giao dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/security/firewall/config GET</td>
      <td></td>
      <td>Kiểm tra trạng thái</td>
      <td>API /security/firewall/config sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>GET</td>
      <td>Thêm bản ghi</td>
      <td>API /rpa/task/execute sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>Cập nhật cấu hình</td>
      <td>API /crm/lead/import sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>GET</td>
      <td>Export dữ liệu</td>
      <td>API /ivr/callflow sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE Thêm</td>
      <td>bản ghi</td>
      <td>API /ivr/callflow sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Export dữ liệu</td>
      <td>API /invoice/export sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PATCH</td>
      <td>Export dữ liệu</td>
      <td>API /ivr/callflow sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Export dữ liệu</td>
      <td>API /invoice/export sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>DELETE Kiểm</td>
      <td>tra trạng thái</td>
      <td>API /customer/update sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE Cập</td>
      <td>nhật cấu hình</td>
      <td>API /rpa/task/execute sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PUT</td>
      <td>Export API</td>
      <td></td>
      <td>Rollback Tích hợp</td>
      <td></td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>dữ liệu</td>
      <td>/security/firewall/config sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>khi lỗi</td>
      <td>với API Gateway</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PUT</td>
      <td>Export dữ liệu</td>
      <td>API /rpa/task/execute sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PUT</td>
      <td>Thêm bản ghi</td>
      <td>API /security/firewall/config sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td></td>
      <td>DELETE Export dữ liệu</td>
      <td>API /network/qos/monitor sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Thêm bản ghi</td>
      <td>API /rpa/task/execute sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Xóa thông</td>
      <td>API /invoice/export sử dụng phương thức GET</td>
      <td>Rollback Giới hạn</td>
      <td>rate-limit</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>tin</td>
      <td>để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>khi lỗi</td>
      <td>1000 req/min</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Cập nhật cấu hình</td>
      <td>API /rpa/task/execute sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE Kiểm</td>
      <td>tra trạng thái</td>
      <td>API /ivr/callflow sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE Thêm</td>
      <td>bản ghi</td>
      <td>API /invoice/export sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>GET</td>
      <td>Cập nhật cấu hình</td>
      <td>API /rpa/task/execute sử dụng phương thức GET để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE Cập</td>
      <td>nhật cấu</td>
      <td>API /ivr/callflow sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực</td>
      <td>Thành công <1s</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>hình</td>
      <td>OAuth2 và log giao dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Xóa thông tin</td>
      <td>API /crm/lead/import sử dụng phương thức PUT để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>Thêm bản ghi</td>
      <td>API /crm/lead/import sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PATCH</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /network/qos/monitor sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>Export dữ liệu</td>
      <td>API /crm/lead/import sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao</td>
      <td>Log đầy đủ</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PUT</td>
      <td>Thêm bản ghi</td>
      <td>API /security/firewall/config sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Export dữ liệu</td>
      <td>API /invoice/export sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /security/firewall/config sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>GET</td>
      <td>Cập nhật cấu hình</td>
      <td>API /customer/update sử dụng phương thức GET để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>POST</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update sử dụng phương thức POST để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PUT</td>
      <td>Thêm bản ghi</td>
      <td>API /network/qos/monitor sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td></td>
      <td>DELETE Export dữ liệu</td>
      <td>API /ivr/callflow sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Xóa thông tin</td>
      <td>API /invoice/export sử dụng phương thức GET để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/security/firewall/config GET</td>
      <td></td>
      <td>Export dữ liệu</td>
      <td>API /security/firewall/config sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Xóa thông tin</td>
      <td>API /ivr/callflow sử dụng phương thức POST để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>DELETE Xóa</td>
      <td>thông</td>
      <td>API /customer/update sử dụng phương thức DELETE để Xóa thông</td>
      <td>Rollback khi lỗi</td>
      <td>Giới hạn rate-limit 1000</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>tin</td>
      <td>tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td></td>
      <td>req/min</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Thêm bản ghi</td>
      <td>API /security/firewall/config sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Thêm bản ghi</td>
      <td>API /invoice/export sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /customer/update sử dụng phương thức PUT để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /customer/update sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Export dữ liệu</td>
      <td>API /ivr/callflow sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td></td>
      <td>DELETE Export dữ liệu</td>
      <td>API /invoice/export sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/security/firewall/config GET</td>
      <td></td>
      <td>Export dữ liệu</td>
      <td>API /security/firewall/config sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /crm/lead/import sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /network/qos/monitor sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>DELETE Thêm</td>
      <td>bản ghi</td>
      <td>API /crm/lead/import sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao</td>
      <td>Log đầy đủ</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Export dữ liệu</td>
      <td>API /crm/lead/import sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /crm/lead/import sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>GET</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /customer/update sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PUT</td>
      <td>Cập nhật cấu hình</td>
      <td>API /network/qos/monitor sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PUT</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /network/qos/monitor sử dụng phương thức PUT để Kiểm tra trạng thái, có xác thực OAuth2 và log giao</td>
      <td>Thành công <1s</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/security/firewall/config GET</td>
      <td></td>
      <td>Kiểm tra trạng thái</td>
      <td>API /security/firewall/config sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/security/firewall/config GET</td>
      <td></td>
      <td>Cập nhật cấu hình</td>
      <td>API /security/firewall/config sử dụng phương thức GET để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>Thêm bản ghi</td>
      <td>API /invoice/export sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td></td>
      <td>/security/firewall/config DELETE Kiểm</td>
      <td>tra trạng thái</td>
      <td>API /security/firewall/config sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>Cập nhật cấu</td>
      <td>API /network/qos/monitor sử dụng phương thức</td>
      <td>Retry tối đa 3 lần</td>
      <td>Tích hợp với API</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>hình</td>
      <td>GET để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td></td>
      <td>Gateway</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Export dữ liệu</td>
      <td>API /rpa/task/execute sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update sử dụng phương thức PUT để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Thêm bản ghi</td>
      <td>API /customer/update sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>GET</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /ivr/callflow sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Export dữ liệu</td>
      <td>API /invoice/export sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>/security/firewall/config DELETE Xóa</td>
      <td>thông tin</td>
      <td>API /security/firewall/config sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td></td>
      <td>DELETE Export dữ liệu</td>
      <td>API /network/qos/monitor sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /crm/lead/import sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>Thêm bản ghi</td>
      <td>API /invoice/export sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>POST</td>
      <td>Cập nhật cấu hình</td>
      <td>API /rpa/task/execute sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>GET</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /crm/lead/import sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PUT</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /network/qos/monitor sử dụng phương thức PUT để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>POST</td>
      <td>Cập nhật cấu hình</td>
      <td>API /customer/update sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Thêm bản ghi</td>
      <td>API /crm/lead/import sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /ivr/callflow sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>/customer/update</td>
      <td>PATCH</td>
      <td>Cập nhật cấu hình</td>
      <td>API /customer/update sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /invoice/export sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Cập nhật cấu hình</td>
      <td>API /crm/lead/import sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>GET</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /customer/update sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Cập nhật cấu hình</td>
      <td>API /crm/lead/import sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>GET</td>
      <td>Thêm bản ghi</td>
      <td>API /crm/lead/import sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/security/firewall/config GET</td>
      <td></td>
      <td>Kiểm tra trạng thái</td>
      <td>API /security/firewall/config sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Export dữ liệu</td>
      <td>API /crm/lead/import sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /network/qos/monitor sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /security/firewall/config sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao</td>
      <td>Retry tối đa 3 lần</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>POST</td>
      <td>Export dữ liệu</td>
      <td>API /customer/update sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE Kiểm</td>
      <td>tra trạng thái</td>
      <td>API /ivr/callflow sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>Cập nhật cấu hình</td>
      <td>API /network/qos/monitor sử dụng phương thức GET để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PUT</td>
      <td>Export dữ liệu</td>
      <td>API /network/qos/monitor sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PATCH</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /ivr/callflow sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao</td>
      <td>Rollback khi lỗi</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Cập nhật cấu hình</td>
      <td>API /crm/lead/import sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>Xóa thông tin</td>
      <td>API /crm/lead/import sử dụng phương thức POST để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PATCH</td>
      <td>Export dữ liệu</td>
      <td>API /network/qos/monitor sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PUT</td>
      <td>Cập nhật cấu hình</td>
      <td>API /ivr/callflow sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>GET</td>
      <td>Cập nhật cấu hình</td>
      <td>API /ivr/callflow sử dụng phương thức GET để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Thêm</td>
      <td>API /crm/lead/import</td>
      <td>Thông</td>
      <td>Theo</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>bản ghi</td>
      <td>sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>báo sự kiện qua Kafka</td>
      <td>chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Thêm bản ghi</td>
      <td>API /rpa/task/execute sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PATCH</td>
      <td>Export dữ liệu</td>
      <td>API /ivr/callflow sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Cập nhật cấu hình</td>
      <td>API /invoice/export sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td></td>
      <td>DELETE Export dữ liệu</td>
      <td>API /network/qos/monitor sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Cập nhật</td>
      <td>API /crm/lead/import sử dụng phương thức</td>
      <td>Rollback Theo</td>
      <td>chuẩn</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>cấu hình</td>
      <td>PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>khi lỗi</td>
      <td>RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>POST</td>
      <td>Cập nhật cấu hình</td>
      <td>API /rpa/task/execute sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE Kiểm</td>
      <td>tra trạng thái</td>
      <td>API /rpa/task/execute sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /network/qos/monitor sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>GET</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update sử dụng phương thức GET để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>POST</td>
      <td>Kiểm tra trạng</td>
      <td>API /rpa/task/execute sử dụng phương thức POST để Kiểm tra</td>
      <td>Thành công</td>
      <td>Giới hạn rate-limit 1000</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>thái</td>
      <td>trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td><1s</td>
      <td>req/min</td>
    </tr>
    <tr>
      <td></td>
      <td>/security/firewall/config DELETE Thêm</td>
      <td>bản ghi</td>
      <td>API /security/firewall/config sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td></td>
      <td>/security/firewall/config DELETE Xóa</td>
      <td>thông tin</td>
      <td>API /security/firewall/config sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PATCH</td>
      <td>Cập nhật cấu hình</td>
      <td>API /security/firewall/config sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>Cập nhật cấu</td>
      <td>API /network/qos/monitor sử dụng phương thức</td>
      <td>Rollback khi lỗi</td>
      <td>Tích hợp với API</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>hình</td>
      <td>GET để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td></td>
      <td>Gateway</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /customer/update sử dụng phương thức PUT để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Cập nhật cấu hình</td>
      <td>API /ivr/callflow sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /security/firewall/config sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>Export dữ liệu</td>
      <td>API /invoice/export sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Xóa thông</td>
      <td>API /security/firewall/config</td>
      <td>Retry tối Hỗ trợ</td>
      <td>JSON và</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>tin</td>
      <td>sử dụng phương thức POST để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>đa 3 lần</td>
      <td>XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>Thêm bản ghi</td>
      <td>API /crm/lead/import sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>DELETE Thêm</td>
      <td>bản ghi</td>
      <td>API /network/qos/monitor sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE Kiểm</td>
      <td>tra trạng thái</td>
      <td>API /ivr/callflow sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PATCH</td>
      <td>Export dữ liệu</td>
      <td>API /network/qos/monitor sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Cập nhật cấu hình</td>
      <td>API /rpa/task/execute sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>GET</td>
      <td>Thêm bản ghi</td>
      <td>API /crm/lead/import sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE Xóa</td>
      <td>thông tin</td>
      <td>API /invoice/export sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>GET</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /customer/update sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /rpa/task/execute sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>Xóa thông</td>
      <td>API /crm/lead/import sử dụng phương thức POST để Xóa thông tin,</td>
      <td>Thành công</td>
      <td>Tích hợp với API</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>tin</td>
      <td>có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td><1s</td>
      <td>Gateway</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PATCH</td>
      <td>Thêm bản ghi</td>
      <td>API /network/qos/monitor sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>GET</td>
      <td>Xóa thông tin</td>
      <td>API /ivr/callflow sử dụng phương thức GET để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PATCH</td>
      <td>Export dữ liệu</td>
      <td>API /customer/update sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>Export dữ liệu</td>
      <td>API /invoice/export sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Xóa thông tin</td>
      <td>API /invoice/export sử dụng phương thức PUT để Xóa thông tin, có xác thực OAuth2 và log</td>
      <td>Log đầy đủ</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>giao dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PATCH</td>
      <td>Thêm bản ghi</td>
      <td>API /network/qos/monitor sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>GET</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /rpa/task/execute sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE Kiểm</td>
      <td>tra trạng thái</td>
      <td>API /invoice/export sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PUT</td>
      <td>Thêm bản ghi</td>
      <td>API /rpa/task/execute sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Có versioning v1/v2</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>/invoice/export</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /invoice/export sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE Thêm</td>
      <td>bản ghi</td>
      <td>API /ivr/callflow sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>GET</td>
      <td>Cập nhật cấu hình</td>
      <td>API /crm/lead/import sử dụng phương thức GET để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE Kiểm</td>
      <td>tra trạng thái</td>
      <td>API /rpa/task/execute sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PATCH</td>
      <td>Cập nhật cấu hình</td>
      <td>API /network/qos/monitor sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Export dữ liệu</td>
      <td>API /ivr/callflow sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE Cập</td>
      <td>nhật cấu hình</td>
      <td>API /ivr/callflow sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>GET</td>
      <td>Xóa thông tin</td>
      <td>API /crm/lead/import sử dụng phương thức GET để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PUT</td>
      <td>Xóa thông tin</td>
      <td>API /rpa/task/execute sử dụng phương thức PUT để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Thêm bản ghi</td>
      <td>API /crm/lead/import sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Kiểm tra trạng</td>
      <td>API /invoice/export sử dụng phương thức PUT để Kiểm tra trạng thái,</td>
      <td>Retry tối đa 3 lần</td>
      <td>Theo chuẩn</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>thái</td>
      <td>có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td></td>
      <td>RESTful</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PATCH</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /ivr/callflow sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /invoice/export sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Cập nhật cấu hình</td>
      <td>API /rpa/task/execute sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>Xóa thông tin</td>
      <td>API /network/qos/monitor sử dụng phương thức GET để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>POST</td>
      <td>Export dữ liệu</td>
      <td>API /network/qos/monitor sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Xóa thông tin</td>
      <td>API /invoice/export sử dụng phương thức PUT để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td></td>
      <td>/security/firewall/config DELETE Thêm</td>
      <td>bản ghi</td>
      <td>API /security/firewall/config sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PATCH</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /invoice/export sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td></td>
      <td>DELETE Export dữ liệu</td>
      <td>API /network/qos/monitor sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PATCH</td>
      <td>Export dữ liệu</td>
      <td>API /ivr/callflow sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Cập nhật cấu hình</td>
      <td>API /crm/lead/import sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /ivr/callflow sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /ivr/callflow sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>DELETE Xóa</td>
      <td>thông tin</td>
      <td>API /network/qos/monitor sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td></td>
      <td>/security/firewall/config DELETE Kiểm</td>
      <td>tra trạng thái</td>
      <td>API /security/firewall/config sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao</td>
      <td>Rollback khi lỗi</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>DELETE Xóa</td>
      <td>thông tin</td>
      <td>API /customer/update sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>Thêm bản ghi</td>
      <td>API /network/qos/monitor sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td></td>
      <td>DELETE Export dữ liệu</td>
      <td>API /crm/lead/import sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>Cập nhật cấu hình</td>
      <td>API /invoice/export sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/security/firewall/config GET</td>
      <td></td>
      <td>Export dữ liệu</td>
      <td>API /security/firewall/config sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>/security/firewall/config</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /security/firewall/config sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>POST</td>
      <td>Export dữ liệu</td>
      <td>API /network/qos/monitor sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE Thêm</td>
      <td>bản ghi</td>
      <td>API /rpa/task/execute sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /crm/lead/import sử dụng phương thức PUT để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Thêm bản ghi</td>
      <td>API /invoice/export sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>/ivr/callflow</td>
      <td>PATCH</td>
      <td>Cập nhật cấu hình</td>
      <td>API /ivr/callflow sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td></td>
      <td>DELETE Export dữ liệu</td>
      <td>API /network/qos/monitor sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update sử dụng phương thức PUT để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /network/qos/monitor sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>POST</td>
      <td>Xóa thông tin</td>
      <td>API /rpa/task/execute sử dụng phương thức POST để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Xóa thông</td>
      <td>API /crm/lead/import sử dụng phương thức</td>
      <td>Thông báo sự</td>
      <td>Theo chuẩn</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>tin</td>
      <td>PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>kiện qua Kafka</td>
      <td>RESTful</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Cập nhật cấu hình</td>
      <td>API /crm/lead/import sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update sử dụng phương thức PUT để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>Export dữ liệu</td>
      <td>API /crm/lead/import sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PATCH</td>
      <td>Cập nhật cấu hình</td>
      <td>API /security/firewall/config sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>GET</td>
      <td>Thêm bản ghi</td>
      <td>API /rpa/task/execute sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và</td>
      <td>Log đầy đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>log giao dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>POST</td>
      <td>Xóa thông tin</td>
      <td>API /network/qos/monitor sử dụng phương thức POST để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /customer/update sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Cập nhật cấu hình</td>
      <td>API /rpa/task/execute sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Thêm bản ghi</td>
      <td>API /crm/lead/import sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Xóa thông tin</td>
      <td>API /invoice/export sử dụng phương thức GET để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PUT</td>
      <td>Export API /ivr/callflow sử</td>
      <td></td>
      <td>Thông</td>
      <td>Hỗ trợ</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>dữ liệu</td>
      <td>dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>báo sự kiện qua Kafka</td>
      <td>JSON và XML</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>POST</td>
      <td>Xóa thông tin</td>
      <td>API /rpa/task/execute sử dụng phương thức POST để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>DELETE Cập</td>
      <td>nhật cấu hình</td>
      <td>API /crm/lead/import sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PATCH</td>
      <td>Thêm bản ghi</td>
      <td>API /invoice/export sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PUT</td>
      <td>Cập nhật cấu hình</td>
      <td>API /security/firewall/config sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>Cập nhật cấu</td>
      <td>API /invoice/export sử dụng phương thức POST để Cập nhật cấu</td>
      <td>Thông báo sự kiện qua</td>
      <td>Theo chuẩn</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>hình</td>
      <td>hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Kafka</td>
      <td>RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PUT</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /rpa/task/execute sử dụng phương thức PUT để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PUT</td>
      <td>Thêm bản ghi</td>
      <td>API /network/qos/monitor sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PUT</td>
      <td>Thêm bản ghi</td>
      <td>API /security/firewall/config sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Cập nhật cấu hình</td>
      <td>API /crm/lead/import sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/security/firewall/config GET</td>
      <td></td>
      <td>Export dữ liệu</td>
      <td>API /security/firewall/config sử dụng phương thức GET để Export dữ liệu,</td>
      <td>Rollback khi lỗi</td>
      <td>Có versioning v1/v2</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE Kiểm</td>
      <td>tra trạng thái</td>
      <td>API /rpa/task/execute sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Thêm bản ghi</td>
      <td>API /ivr/callflow sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE Cập</td>
      <td>nhật cấu hình</td>
      <td>API /ivr/callflow sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td></td>
      <td>DELETE Export dữ liệu</td>
      <td>API /rpa/task/execute sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PUT</td>
      <td>Export dữ liệu</td>
      <td>API /security/firewall/config sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>log giao dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>Cập nhật cấu hình</td>
      <td>API /crm/lead/import sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /rpa/task/execute sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PATCH</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /invoice/export sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>GET</td>
      <td>Cập nhật cấu hình</td>
      <td>API /crm/lead/import sử dụng phương thức GET để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>GET</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /customer/update sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>/rpa/task/execute</td>
      <td>GET</td>
      <td>Thêm bản ghi</td>
      <td>API /rpa/task/execute sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /invoice/export sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PATCH</td>
      <td>Thêm bản ghi</td>
      <td>API /invoice/export sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE Thêm</td>
      <td>bản ghi</td>
      <td>API /invoice/export sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td></td>
      <td>/security/firewall/config DELETE Cập</td>
      <td>nhật cấu hình</td>
      <td>API /security/firewall/config sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Xóa thông</td>
      <td>API /invoice/export sử dụng phương thức PUT</td>
      <td>Retry tối</td>
      <td>Theo chuẩn</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>tin</td>
      <td>để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>đa 3 lần</td>
      <td>RESTful</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>POST</td>
      <td>Thêm bản ghi</td>
      <td>API /crm/lead/import sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>Thêm bản ghi</td>
      <td>API /network/qos/monitor sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PUT</td>
      <td>Cập nhật cấu hình</td>
      <td>API /ivr/callflow sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE Kiểm</td>
      <td>tra trạng thái</td>
      <td>API /rpa/task/execute sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PUT</td>
      <td>Thêm bản ghi</td>
      <td>API /rpa/task/execute sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và</td>
      <td>Thành công <1s</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>log giao dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /crm/lead/import sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /customer/update sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /ivr/callflow sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>Xóa thông tin</td>
      <td>API /network/qos/monitor sử dụng phương thức GET để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>DELETE Xóa</td>
      <td>thông tin</td>
      <td>API /crm/lead/import sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PUT</td>
      <td>Export API /ivr/callflow sử</td>
      <td></td>
      <td>Retry tối</td>
      <td>Theo</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>dữ liệu</td>
      <td>dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>đa 3 lần</td>
      <td>chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /rpa/task/execute sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Export dữ liệu</td>
      <td>API /rpa/task/execute sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Xóa thông tin</td>
      <td>API /crm/lead/import sử dụng phương thức PUT để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /rpa/task/execute sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>GET</td>
      <td>Export dữ liệu</td>
      <td>API /crm/lead/import sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và</td>
      <td>Log đầy đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>log giao dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td></td>
      <td>DELETE Export dữ liệu</td>
      <td>API /rpa/task/execute sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PATCH</td>
      <td>Thêm bản ghi</td>
      <td>API /network/qos/monitor sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Export dữ liệu</td>
      <td>API /invoice/export sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td></td>
      <td>DELETE Export dữ liệu</td>
      <td>API /rpa/task/execute sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PATCH</td>
      <td>Xóa thông tin</td>
      <td>API /security/firewall/config sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>và log giao dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Cập nhật cấu hình</td>
      <td>API /customer/update sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE Xóa</td>
      <td>thông tin</td>
      <td>API /invoice/export sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Export dữ liệu</td>
      <td>API /customer/update sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /network/qos/monitor sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Xóa thông tin</td>
      <td>API /invoice/export sử dụng phương thức PUT để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>GET</td>
      <td>Export API</td>
      <td></td>
      <td>Retry tối</td>
      <td>Tích hợp</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>dữ liệu</td>
      <td>/network/qos/monitor sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>đa 3 lần</td>
      <td>với API Gateway</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>GET</td>
      <td>Thêm bản ghi</td>
      <td>API /ivr/callflow sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /security/firewall/config sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Export dữ liệu</td>
      <td>API /security/firewall/config sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>Export dữ liệu</td>
      <td>API /invoice/export sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /crm/lead/import sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PUT</td>
      <td>Cập nhật cấu hình</td>
      <td>API /rpa/task/execute sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PUT</td>
      <td>Thêm bản ghi</td>
      <td>API /invoice/export sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>DELETE Thêm</td>
      <td>bản ghi</td>
      <td>API /crm/lead/import sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PUT</td>
      <td>Cập nhật cấu hình</td>
      <td>API /ivr/callflow sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>PATCH</td>
      <td>Thêm bản</td>
      <td>API /invoice/export sử dụng phương thức PATCH để Thêm bản</td>
      <td>Thành công</td>
      <td>Có versioning</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>ghi</td>
      <td>ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td><1s</td>
      <td>v1/v2</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PUT</td>
      <td>Export dữ liệu</td>
      <td>API /rpa/task/execute sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE Thêm</td>
      <td>bản ghi</td>
      <td>API /invoice/export sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /invoice/export sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Thêm bản ghi</td>
      <td>API /customer/update sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>PATCH</td>
      <td>Thêm bản ghi</td>
      <td>API /rpa/task/execute sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>dịch chi tiết.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>PUT</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /network/qos/monitor sử dụng phương thức PUT để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE Kiểm</td>
      <td>tra trạng thái</td>
      <td>API /invoice/export sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PATCH</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /ivr/callflow sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Thêm bản ghi</td>
      <td>API /customer/update sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/rpa/task/execute</td>
      <td>DELETE Xóa</td>
      <td>thông tin</td>
      <td>API /rpa/task/execute sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>DELETE Thêm</td>
      <td>bản ghi</td>
      <td>API /crm/lead/import sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PUT</td>
      <td>Export dữ liệu</td>
      <td>API /crm/lead/import sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>POST</td>
      <td>Export dữ liệu</td>
      <td>API /network/qos/monitor sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /security/firewall/config sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PUT</td>
      <td>Cập nhật cấu hình</td>
      <td>API /ivr/callflow sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>/crm/lead/import</td>
      <td>DELETE Cập</td>
      <td>nhật cấu hình</td>
      <td>API /crm/lead/import sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>DELETE Cập</td>
      <td>nhật cấu hình</td>
      <td>API /ivr/callflow sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>GET</td>
      <td>Thêm bản ghi</td>
      <td>API /crm/lead/import sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>PATCH</td>
      <td>Export dữ liệu</td>
      <td>API /security/firewall/config sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>PUT</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /ivr/callflow sử dụng phương thức PUT để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Rollback khi lỗi</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>DELETE Kiểm</td>
      <td>tra</td>
      <td>API /network/qos/monitor</td>
      <td>Rollback Hỗ trợ</td>
      <td>JSON và</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>trạng thái</td>
      <td>sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>khi lỗi</td>
      <td>XML</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE Xóa</td>
      <td>thông tin</td>
      <td>API /invoice/export sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/network/qos/monitor</td>
      <td>POST</td>
      <td>Thêm bản ghi</td>
      <td>API /network/qos/monitor sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td></td>
      <td>/security/firewall/config DELETE Xóa</td>
      <td>thông tin</td>
      <td>API /security/firewall/config sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>DELETE Cập</td>
      <td>nhật cấu hình</td>
      <td>API /invoice/export sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thành công <1s</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PATCH</td>
      <td>Xóa thông</td>
      <td>API /customer/update sử dụng phương thức</td>
      <td>Rollback Tích hợp</td>
      <td>với API</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>tin</td>
      <td>PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>khi lỗi</td>
      <td>Gateway</td>
    </tr>
    <tr>
      <td>/ivr/callflow</td>
      <td>POST</td>
      <td>Cập nhật cấu hình</td>
      <td>API /ivr/callflow sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td></td>
      <td>/security/firewall/config DELETE Cập</td>
      <td>nhật cấu hình</td>
      <td>API /security/firewall/config sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>DELETE Kiểm</td>
      <td>tra trạng thái</td>
      <td>API /customer/update sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PATCH</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /customer/update sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Theo chuẩn RESTful</td>
    </tr>
    <tr>
      <td>/security/firewall/config</td>
      <td>POST</td>
      <td>Export dữ</td>
      <td>API /security/firewall/config sử dụng phương thức</td>
      <td>Log đầy đủ</td>
      <td>Tích hợp với API</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>liệu</td>
      <td>POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td></td>
      <td>Gateway</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>DELETE Kiểm</td>
      <td>tra trạng thái</td>
      <td>API /crm/lead/import sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Retry tối đa 3 lần</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
    <tr>
      <td>/crm/lead/import</td>
      <td>PATCH</td>
      <td>Kiểm tra trạng thái</td>
      <td>API /crm/lead/import sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Log đầy đủ</td>
      <td>Có versioning v1/v2</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>PUT</td>
      <td>Export dữ liệu</td>
      <td>API /customer/update sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Tích hợp với API Gateway</td>
    </tr>
    <tr>
      <td>/invoice/export</td>
      <td>GET</td>
      <td>Export dữ liệu</td>
      <td>API /invoice/export sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.</td>
      <td>Thông báo sự kiện qua Kafka</td>
      <td>Giới hạn rate-limit 1000 req/min</td>
    </tr>
    <tr>
      <td>/customer/update</td>
      <td>POST</td>
      <td>Thêm bản ghi</td>
      <td>API /customer/update sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao</td>
      <td>Retry tối đa 3 lần</td>
      <td>Hỗ trợ JSON và XML</td>
    </tr>
  </tbody>
</table>
