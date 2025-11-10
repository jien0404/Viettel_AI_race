# Public_444

<table>
  
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>IPCC- ContactCenter.</td>
      <td></td>
      <td>cho admin</td>
    </tr>
    <tr>
      <td>IVR-System</td>
      <td>Monitor ClusterNode</td>
      <td>/clusternode/monitor</td>
      <td>Monitor dữ liệu ClusterNode trong IVR-System.</td>
      <td>Thông báo qua email</td>
      <td>Chạy theo lịch cron</td>
    </tr>
    <tr>
      <td>Infra-Server</td>
      <td>Import Contact</td>
      <td>/contact/import</td>
      <td>Import dữ liệu Contact trong Infra- Server.</td>
      <td>Hiển thị báo cáo</td>
      <td>Có cơ chế rollback</td>
    </tr>
    <tr>
      <td>IPCC- ContactCenter</td>
      <td>Insert Blacklist</td>
      <td>/blacklist/insert</td>
      <td>Insert dữ liệu Blacklist trong IPCC- ContactCenter.</td>
      <td>Thông báo qua SMS</td>
      <td>Kết nối với hệ thống Billing</td>
    </tr>
    <tr>
      <td>Security- Firewall</td>
      <td>Import Blacklist</td>
      <td>/blacklist/import</td>
      <td>Import dữ liệu Blacklist trong Security-Firewall.</td>
      <td>Tự động retry</td>
      <td>Dữ liệu backup mỗi ngày</td>
    </tr>
    <tr>
      <td>QA- Automation</td>
      <td>Schedule PackagePlan</td>
      <td>/packageplan/schedule</td>
      <td>Schedule dữ liệu PackagePlan trong QA-Automation.</td>
      <td>Thông báo qua SMS</td>
      <td>Chạy theo lịch cron</td>
    </tr>
    <tr>
      <td>RPA-Engine</td>
      <td>Analyze Blacklist</td>
      <td>/blacklist/analyze</td>
      <td>Analyze dữ liệu Blacklist trong RPA- Engine.</td>
      <td>Ghi log đầy đủ</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>Infra-Server</td>
      <td>Analyze VPN</td>
      <td>/vpn/analyze</td>
      <td>Analyze dữ liệu VPN trong Infra- Server.</td>
      <td>Không lỗi</td>
      <td>Có cơ chế rollback</td>
    </tr>
    <tr>
      <td>Infra-Network Analyze</td>
      <td>FirewallPolicy</td>
      <td>/firewallpolicy/analyze</td>
      <td>Analyze dữ liệu FirewallPolicy trong Infra-Network.</td>
      <td>Thông báo</td>
      <td>Chạy theo</td>
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
      <td>qua SMS</td>
      <td>lịch cron</td>
    </tr>
    <tr>
      <td>BCCS2-Core</td>
      <td>Import Opportunity</td>
      <td>/opportunity/import</td>
      <td>Import dữ liệu Opportunity trong BCCS2-Core.</td>
      <td>Tự động retry</td>
      <td>Kết nối với hệ thống Billing</td>
    </tr>
    <tr>
      <td>IPCC- ContactCenter</td>
      <td>Analyze AgentStatus</td>
      <td>/agentstatus/analyze</td>
      <td>Analyze dữ liệu AgentStatus trong IPCC- ContactCenter.</td>
      <td>Cảnh báo</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
    <tr>
      <td>CRM- Platform</td>
      <td>Insert IVRPrompt</td>
      <td>/ivrprompt/insert</td>
      <td>Insert dữ liệu IVRPrompt trong CRM-Platform.</td>
      <td>Hiển thị báo cáo</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>BCCS2-Core</td>
      <td>Import CDRReport</td>
      <td>/cdrreport/import</td>
      <td>Import dữ liệu CDRReport trong BCCS2-Core.</td>
      <td>Cảnh báo</td>
      <td>Chỉ dùng cho admin</td>
    </tr>
    <tr>
      <td>CRM- Platform</td>
      <td>Analyze QoS</td>
      <td>/qos/analyze</td>
      <td>Analyze dữ liệu QoS trong CRM- Platform.</td>
      <td>Cảnh báo</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>BCCS2-Core</td>
      <td>Update Campaign</td>
      <td>/campaign/update</td>
      <td>Update dữ liệu Campaign trong BCCS2-Core.</td>
      <td>Lỗi nghiêm trọng</td>
      <td>Chạy theo lịch cron</td>
    </tr>
    <tr>
      <td>Infra-Network Export</td>
      <td>AccountLock</td>
      <td>/accountlock/export</td>
      <td>Export dữ liệu AccountLock trong Infra-Network.</td>
      <td>Hiển thị báo cáo</td>
      <td>Chạy theo lịch cron</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>CRM- Platform</td>
      <td>Analyze TransactionLog</td>
      <td>/transactionlog/analyze</td>
      <td>Analyze dữ liệu TransactionLog trong CRM- Platform.</td>
      <td>Không lỗi</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>CRM- Platform</td>
      <td>Config KPIReport</td>
      <td>/kpireport/config</td>
      <td>Config dữ liệu KPIReport trong CRM-Platform.</td>
      <td>Đồng bộ dữ liệu</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
    <tr>
      <td>RPA-Engine</td>
      <td>Optimize Campaign</td>
      <td>/campaign/optimize</td>
      <td>Optimize dữ liệu Campaign trong RPA-Engine.</td>
      <td>Thông báo qua email</td>
      <td>Chỉ dùng cho admin</td>
    </tr>
    <tr>
      <td>IVR-System</td>
      <td>Delete Queue</td>
      <td>/queue/delete</td>
      <td>Delete dữ liệu Queue trong IVR-System.</td>
      <td>Tự động retry</td>
      <td>Kết nối với hệ thống Billing</td>
    </tr>
    <tr>
      <td>RPA-Engine</td>
      <td>Delete AgentStatus</td>
      <td>/agentstatus/delete</td>
      <td>Delete dữ liệu AgentStatus trong RPA-Engine.</td>
      <td>Thông báo qua SMS</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>BCCS2- Billing</td>
      <td>Schedule AgentStatus</td>
      <td>/agentstatus/schedule</td>
      <td>Schedule dữ liệu AgentStatus trong BCCS2-Billing.</td>
      <td>Đồng bộ dữ liệu</td>
      <td>Dữ liệu backup mỗi ngày</td>
    </tr>
    <tr>
      <td>CRM- Platform</td>
      <td>Validate CustomerProfile</td>
      <td>/customerprofile/validate</td>
      <td>Validate dữ liệu CustomerProfile trong CRM- Platform.</td>
      <td>Lỗi nghiêm trọng</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>Security- Firewall</td>
      <td>Update VPN</td>
      <td>/vpn/update</td>
      <td>Update dữ liệu VPN trong Security- Firewall.</td>
      <td>Ghi log đầy đủ</td>
      <td>Tích hợp với CRM</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>IVR-System</td>
      <td>Schedule Invoice</td>
      <td>/invoice/schedule</td>
      <td>Schedule dữ liệu Invoice trong IVR- System.</td>
      <td>Không lỗi</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>BCCS2-Core</td>
      <td>Search Whitelist</td>
      <td>/whitelist/search</td>
      <td>Search dữ liệu Whitelist trong BCCS2-Core.</td>
      <td>Ghi log đầy đủ</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
    <tr>
      <td>BCCS2-Core</td>
      <td>Optimize PackagePlan</td>
      <td>/packageplan/optimize</td>
      <td>Optimize dữ liệu PackagePlan trong BCCS2-Core.</td>
      <td>Hiển thị báo cáo</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
    <tr>
      <td>Infra-Server</td>
      <td>Optimize VPN</td>
      <td>/vpn/optimize</td>
      <td>Optimize dữ liệu VPN trong Infra- Server.</td>
      <td>Thông báo qua email</td>
      <td>Dữ liệu backup mỗi ngày</td>
    </tr>
    <tr>
      <td>IVR-System</td>
      <td>Schedule QoS</td>
      <td>/qos/schedule</td>
      <td>Schedule dữ liệu QoS trong IVR- System.</td>
      <td>Hiển thị báo cáo</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>CRM- Platform</td>
      <td>Optimize IVRPrompt</td>
      <td>/ivrprompt/optimize</td>
      <td>Optimize dữ liệu IVRPrompt trong CRM-Platform.</td>
      <td>Thông báo qua email</td>
      <td>Bảo mật 2 lớp</td>
    </tr>
    <tr>
      <td>IPCC- ContactCenter</td>
      <td>Optimize KPIReport</td>
      <td>/kpireport/optimize</td>
      <td>Optimize dữ liệu KPIReport trong IPCC- ContactCenter.</td>
      <td>Lỗi nghiêm trọng</td>
      <td>Bảo mật 2 lớp</td>
    </tr>
    <tr>
      <td>Infra-Server</td>
      <td>Schedule FirewallPolicy</td>
      <td>/firewallpolicy/schedule</td>
      <td>Schedule dữ liệu FirewallPolicy trong Infra-Server.</td>
      <td>Tự động retry</td>
      <td>Có cơ chế rollback</td>
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
      <td>thống Billing</td>
    </tr>
    <tr>
      <td>QA- Automation</td>
      <td>Monitor Invoice</td>
      <td>/invoice/monitor</td>
      <td>Monitor dữ liệu Invoice trong QA- Automation.</td>
      <td>Cảnh báo</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
    <tr>
      <td>IVR-System</td>
      <td>Insert CustomerProfile</td>
      <td>/customerprofile/insert</td>
      <td>Insert dữ liệu CustomerProfile trong IVR-System.</td>
      <td>Hiển thị báo cáo</td>
      <td>Bảo mật 2 lớp</td>
    </tr>
    <tr>
      <td>IVR-System</td>
      <td>Optimize QoS</td>
      <td>/qos/optimize</td>
      <td>Optimize dữ liệu QoS trong IVR- System.</td>
      <td>Hiển thị báo cáo</td>
      <td>Chỉ dùng cho admin</td>
    </tr>
    <tr>
      <td>BCCS2- Billing</td>
      <td>Schedule Invoice</td>
      <td>/invoice/schedule</td>
      <td>Schedule dữ liệu Invoice trong BCCS2-Billing.</td>
      <td>Đồng bộ dữ liệu</td>
      <td>Dữ liệu backup mỗi ngày</td>
    </tr>
    <tr>
      <td>BCCS2- Billing</td>
      <td>Search DebtControl</td>
      <td>/debtcontrol/search</td>
      <td>Search dữ liệu DebtControl trong BCCS2-Billing.</td>
      <td>Cảnh báo</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>IVR-System</td>
      <td>Optimize Lead</td>
      <td>/lead/optimize</td>
      <td>Optimize dữ liệu Lead trong IVR- System.</td>
      <td>Không lỗi</td>
      <td>Chỉ dùng cho admin</td>
    </tr>
    <tr>
      <td>RPA-Engine</td>
      <td>Config Lead</td>
      <td>/lead/config</td>
      <td>Config dữ liệu Lead trong RPA-Engine.</td>
      <td>Cảnh báo</td>
      <td>Chỉ dùng cho admin</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>Security- Firewall</td>
      <td>Monitor ClusterNode</td>
      <td>/clusternode/monitor</td>
      <td>Monitor dữ liệu ClusterNode trong Security-Firewall.</td>
      <td>Thông báo qua SMS</td>
      <td>Chạy theo lịch cron</td>
    </tr>
    <tr>
      <td>Security- Firewall</td>
      <td>Update QoS</td>
      <td>/qos/update</td>
      <td>Update dữ liệu QoS trong Security- Firewall.</td>
      <td>Ghi log đầy đủ</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
    <tr>
      <td>RPA-Engine</td>
      <td>Import Blacklist</td>
      <td>/blacklist/import</td>
      <td>Import dữ liệu Blacklist trong RPA- Engine.</td>
      <td>Ghi log đầy đủ</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>RPA-Engine</td>
      <td>Delete StorageVolume</td>
      <td>/storagevolume/delete</td>
      <td>Delete dữ liệu StorageVolume trong RPA-Engine.</td>
      <td>Tự động retry</td>
      <td>Bảo mật 2 lớp</td>
    </tr>
    <tr>
      <td>RPA-Engine</td>
      <td>Generate Invoice</td>
      <td>/invoice/generate</td>
      <td>Generate dữ liệu Invoice trong RPA- Engine.</td>
      <td>Không lỗi</td>
      <td>Chỉ dùng cho admin</td>
    </tr>
    <tr>
      <td>Infra-Network</td>
      <td>Search CDRReport</td>
      <td>/cdrreport/search</td>
      <td>Search dữ liệu CDRReport trong Infra-Network.</td>
      <td>Đồng bộ dữ liệu</td>
      <td>Chạy theo lịch cron</td>
    </tr>
    <tr>
      <td>BCCS2-Core</td>
      <td>Optimize DebtControl</td>
      <td>/debtcontrol/optimize</td>
      <td>Optimize dữ liệu DebtControl trong BCCS2-Core.</td>
      <td>Thông báo qua email</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>Infra-Network Delete</td>
      <td>Campaign</td>
      <td>/campaign/delete</td>
      <td>Delete dữ liệu Campaign trong Infra-Network.</td>
      <td>Thành công</td>
      <td>Kết nối với hệ thống Billing</td>
    </tr>
  </tbody>
</table>







<table>
  
  <tbody>
    <tr>
      <td>QA- Automation</td>
      <td>Optimize TransactionLog</td>
      <td>/transactionlog/optimize</td>
      <td>Optimize dữ liệu TransactionLog trong QA- Automation.</td>
      <td>Thành công</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>Infra-Network Optimize</td>
      <td>Opportunity</td>
      <td>/opportunity/optimize</td>
      <td>Optimize dữ liệu Opportunity trong Infra-Network.</td>
      <td>Không lỗi</td>
      <td>Kết nối với hệ thống Billing</td>
    </tr>
    <tr>
      <td>RPA-Engine</td>
      <td>Update PackagePlan</td>
      <td>/packageplan/update</td>
      <td>Update dữ liệu PackagePlan trong RPA-Engine.</td>
      <td>Lỗi nghiêm trọng</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
    <tr>
      <td>BCCS2-Core</td>
      <td>Generate Invoice</td>
      <td>/invoice/generate</td>
      <td>Generate dữ liệu Invoice trong BCCS2-Core.</td>
      <td>Thông báo qua email</td>
      <td>Kết nối với hệ thống Billing</td>
    </tr>
    <tr>
      <td>BCCS2-Core</td>
      <td>Import SwitchConfig</td>
      <td>/switchconfig/import</td>
      <td>Import dữ liệu SwitchConfig trong BCCS2-Core.</td>
      <td>Không lỗi</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
    <tr>
      <td>Security- Firewall</td>
      <td>Schedule Campaign</td>
      <td>/campaign/schedule</td>
      <td>Schedule dữ liệu Campaign trong Security-Firewall.</td>
      <td>Tự động retry</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>BCCS2- Billing</td>
      <td>Update Whitelist</td>
      <td>/whitelist/update</td>
      <td>Update dữ liệu Whitelist trong BCCS2-Billing.</td>
      <td>Tự động retry</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>QA- Automation</td>
      <td>Insert DataLake</td>
      <td>/datalake/insert</td>
      <td>Insert dữ liệu DataLake trong QA- Automation.</td>
      <td>Ghi log đầy đủ</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>CRM- Platform</td>
      <td>Import CDRReport</td>
      <td>/cdrreport/import</td>
      <td>Import dữ liệu CDRReport trong CRM-Platform.</td>
      <td>Tự động retry</td>
      <td>Chạy theo lịch cron</td>
    </tr>
    <tr>
      <td>QA- Automation</td>
      <td>Config AgentStatus</td>
      <td>/agentstatus/config</td>
      <td>Config dữ liệu AgentStatus trong QA-Automation.</td>
      <td>Hiển thị báo cáo</td>
      <td>Kết nối với hệ thống Billing</td>
    </tr>
    <tr>
      <td>IVR-System</td>
      <td>Search CDRReport</td>
      <td>/cdrreport/search</td>
      <td>Search dữ liệu CDRReport trong IVR-System.</td>
      <td>Lỗi nghiêm trọng</td>
      <td>Dữ liệu backup mỗi ngày</td>
    </tr>
    <tr>
      <td>Infra-Network Validate</td>
      <td>SwitchConfig</td>
      <td>/switchconfig/validate</td>
      <td>Validate dữ liệu SwitchConfig trong Infra-Network.</td>
      <td>Thông báo qua SMS</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>BCCS2- Billing</td>
      <td>Monitor ClusterNode</td>
      <td>/clusternode/monitor</td>
      <td>Monitor dữ liệu ClusterNode trong BCCS2-Billing.</td>
      <td>Thông báo qua SMS</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>Security- Firewall</td>
      <td>Validate Opportunity</td>
      <td>/opportunity/validate</td>
      <td>Validate dữ liệu Opportunity trong Security-Firewall.</td>
      <td>Thông báo qua SMS</td>
      <td>Chỉ dùng cho admin</td>
    </tr>
  </tbody>
</table>



















<table>
  
  <tbody>
    <tr>
      <td>QA- Automation</td>
      <td>Delete IVRPrompt</td>
      <td>/ivrprompt/delete</td>
      <td>Delete dữ liệu IVRPrompt trong QA-Automation.</td>
      <td>Cảnh báo</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
    <tr>
      <td>QA- Automation</td>
      <td>Import Opportunity</td>
      <td>/opportunity/import</td>
      <td>Import dữ liệu Opportunity trong QA-Automation.</td>
      <td>Ghi log đầy đủ</td>
      <td>Dữ liệu backup mỗi ngày</td>
    </tr>
    <tr>
      <td>RPA-Engine</td>
      <td>Delete Promotion</td>
      <td>/promotion/delete</td>
      <td>Delete dữ liệu Promotion trong RPA-Engine.</td>
      <td>Cảnh báo</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>IVR-System</td>
      <td>Update Campaign</td>
      <td>/campaign/update</td>
      <td>Update dữ liệu Campaign trong IVR-System.</td>
      <td>Không lỗi</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>IPCC- ContactCenter</td>
      <td>Optimize CDRReport</td>
      <td>/cdrreport/optimize</td>
      <td>Optimize dữ liệu CDRReport trong IPCC- ContactCenter.</td>
      <td>Thông báo qua email</td>
      <td>Kết nối với hệ thống Billing</td>
    </tr>
    <tr>
      <td>Infra-Network Monitor VPN</td>
      <td></td>
      <td>/vpn/monitor</td>
      <td>Monitor dữ liệu VPN trong Infra- Network.</td>
      <td>Thành công</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>RPA-Engine</td>
      <td>Import IVRPrompt</td>
      <td>/ivrprompt/import</td>
      <td>Import dữ liệu IVRPrompt trong RPA-Engine.</td>
      <td>Không lỗi</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
    <tr>
      <td>BCCS2- Billing</td>
      <td>Validate StorageVolume</td>
      <td>/storagevolume/validate</td>
      <td>Validate dữ liệu StorageVolume trong BCCS2- Billing.</td>
      <td>Đồng bộ dữ liệu</td>
      <td>Chỉ dùng cho admin</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>QA- Automation</td>
      <td>Delete Invoice</td>
      <td>/invoice/delete</td>
      <td>Delete dữ liệu Invoice trong QA- Automation.</td>
      <td>Ghi log đầy đủ</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>BCCS2-Core</td>
      <td>Update PackagePlan</td>
      <td>/packageplan/update</td>
      <td>Update dữ liệu PackagePlan trong BCCS2-Core.</td>
      <td>Tự động retry</td>
      <td>Chỉ dùng cho admin</td>
    </tr>
    <tr>
      <td>CRM- Platform</td>
      <td>Search Campaign</td>
      <td>/campaign/search</td>
      <td>Search dữ liệu Campaign trong CRM-Platform.</td>
      <td>Đồng bộ dữ liệu</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>BCCS2- Billing</td>
      <td>Insert VPN</td>
      <td>/vpn/insert</td>
      <td>Insert dữ liệu VPN trong BCCS2- Billing.</td>
      <td>Lỗi nghiêm trọng</td>
      <td>Dữ liệu backup mỗi ngày</td>
    </tr>
    <tr>
      <td>IVR-System</td>
      <td>Schedule ClusterNode</td>
      <td>/clusternode/schedule</td>
      <td>Schedule dữ liệu ClusterNode trong IVR-System.</td>
      <td>Thông báo qua email</td>
      <td>Kết nối với hệ thống Billing</td>
    </tr>
    <tr>
      <td>Security- Firewall</td>
      <td>Optimize KPIReport</td>
      <td>/kpireport/optimize</td>
      <td>Optimize dữ liệu KPIReport trong Security-Firewall.</td>
      <td>Cảnh báo</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>Infra-Server</td>
      <td>Analyze Promotion</td>
      <td>/promotion/analyze</td>
      <td>Analyze dữ liệu Promotion trong Infra-Server.</td>
      <td>Tự động retry</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
    <tr>
      <td>BCCS2- Billing</td>
      <td>Export IVRPrompt</td>
      <td>/ivrprompt/export</td>
      <td>Export dữ liệu IVRPrompt trong BCCS2-Billing.</td>
      <td>Thành công</td>
      <td>Chạy theo lịch cron</td>
    </tr>
  </tbody>
</table>











<table>
  
  <tbody>
    <tr>
      <td>BCCS2- Billing</td>
      <td>Delete CustomerProfile</td>
      <td>/customerprofile/delete</td>
      <td>Delete dữ liệu CustomerProfile trong BCCS2- Billing.</td>
      <td>Hiển thị báo cáo</td>
      <td>Có cơ chế rollback</td>
    </tr>
    <tr>
      <td>BCCS2- Billing</td>
      <td>Generate AccountLock</td>
      <td>/accountlock/generate</td>
      <td>Generate dữ liệu AccountLock trong BCCS2-Billing.</td>
      <td>Thành công</td>
      <td>Kết nối với hệ thống Billing</td>
    </tr>
    <tr>
      <td>CRM- Platform</td>
      <td>Delete PackagePlan</td>
      <td>/packageplan/delete</td>
      <td>Delete dữ liệu PackagePlan trong CRM-Platform.</td>
      <td>Ghi log đầy đủ</td>
      <td>Chạy theo lịch cron</td>
    </tr>
    <tr>
      <td>CRM- Platform</td>
      <td>Validate Opportunity</td>
      <td>/opportunity/validate</td>
      <td>Validate dữ liệu Opportunity trong CRM-Platform.</td>
      <td>Ghi log đầy đủ</td>
      <td>Có cơ chế rollback</td>
    </tr>
    <tr>
      <td>Infra-Network Optimize</td>
      <td>Promotion</td>
      <td>/promotion/optimize</td>
      <td>Optimize dữ liệu Promotion trong Infra-Network.</td>
      <td>Không lỗi</td>
      <td>Bảo mật 2 lớp</td>
    </tr>
    <tr>
      <td>IPCC- ContactCenter</td>
      <td>Search DebtControl</td>
      <td>/debtcontrol/search</td>
      <td>Search dữ liệu DebtControl trong IPCC- ContactCenter.</td>
      <td>Ghi log đầy đủ</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>RPA-Engine</td>
      <td>Generate AgentStatus</td>
      <td>/agentstatus/generate</td>
      <td>Generate dữ liệu AgentStatus trong RPA-Engine.</td>
      <td>Không lỗi</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>Infra-Server</td>
      <td>Config VPN</td>
      <td>/vpn/config</td>
      <td>Config dữ liệu VPN trong Infra-Server.</td>
      <td>Đồng bộ dữ liệu</td>
      <td>Chỉ dùng cho admin</td>
    </tr>
  </tbody>
</table>







<table>
  
  <tbody>
    <tr>
      <td>CRM- Platform</td>
      <td>Generate ClusterNode</td>
      <td>/clusternode/generate</td>
      <td>Generate dữ liệu ClusterNode trong CRM-Platform.</td>
      <td>Không lỗi</td>
      <td>Bảo mật 2 lớp</td>
    </tr>
    <tr>
      <td>BCCS2-Core</td>
      <td>Optimize Lead</td>
      <td>/lead/optimize</td>
      <td>Optimize dữ liệu Lead trong BCCS2- Core.</td>
      <td>Lỗi nghiêm trọng</td>
      <td>Kết nối với hệ thống Billing</td>
    </tr>
    <tr>
      <td>IVR-System</td>
      <td>Update CustomerProfile</td>
      <td>/customerprofile/update</td>
      <td>Update dữ liệu CustomerProfile trong IVR-System.</td>
      <td>Thông báo qua email</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
    <tr>
      <td>Infra-Network</td>
      <td>Schedule AccountLock</td>
      <td>/accountlock/schedule</td>
      <td>Schedule dữ liệu AccountLock trong Infra-Network.</td>
      <td>Lỗi nghiêm trọng</td>
      <td>Chỉ dùng cho admin</td>
    </tr>
    <tr>
      <td>BCCS2-Core</td>
      <td>Search ClusterNode</td>
      <td>/clusternode/search</td>
      <td>Search dữ liệu ClusterNode trong BCCS2-Core.</td>
      <td>Đồng bộ dữ liệu</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>BCCS2- Billing</td>
      <td>Monitor Opportunity</td>
      <td>/opportunity/monitor</td>
      <td>Monitor dữ liệu Opportunity trong BCCS2-Billing.</td>
      <td>Thông báo qua SMS</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>RPA-Engine</td>
      <td>Import Campaign</td>
      <td>/campaign/import</td>
      <td>Import dữ liệu Campaign trong RPA-Engine.</td>
      <td>Lỗi nghiêm trọng</td>
      <td>Có cơ chế rollback</td>
    </tr>
    <tr>
      <td>QA- Automation</td>
      <td>Search SwitchConfig</td>
      <td>/switchconfig/search</td>
      <td>Search dữ liệu SwitchConfig trong QA-Automation.</td>
      <td>Tự động retry</td>
      <td>Có cơ chế rollback</td>
    </tr>
  </tbody>
</table>















<table>
  
  <tbody>
    <tr>
      <td>IPCC- ContactCenter</td>
      <td>Search PackagePlan</td>
      <td>/packageplan/search</td>
      <td>Search dữ liệu PackagePlan trong IPCC- ContactCenter.</td>
      <td>Tự động retry</td>
      <td>Chỉ dùng cho admin</td>
    </tr>
    <tr>
      <td>IPCC- ContactCenter</td>
      <td>Delete Promotion</td>
      <td>/promotion/delete</td>
      <td>Delete dữ liệu Promotion trong IPCC- ContactCenter.</td>
      <td>Thông báo qua SMS</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>BCCS2-Core</td>
      <td>Monitor SwitchConfig</td>
      <td>/switchconfig/monitor</td>
      <td>Monitor dữ liệu SwitchConfig trong BCCS2-Core.</td>
      <td>Tự động retry</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>IPCC- ContactCenter</td>
      <td>Schedule DataLake</td>
      <td>/datalake/schedule</td>
      <td>Schedule dữ liệu DataLake trong IPCC- ContactCenter.</td>
      <td>Ghi log đầy đủ</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
    <tr>
      <td>IPCC- ContactCenter</td>
      <td>Insert Queue</td>
      <td>/queue/insert</td>
      <td>Insert dữ liệu Queue trong IPCC- ContactCenter.</td>
      <td>Thông báo qua email</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>RPA-Engine</td>
      <td>Validate APIGateway</td>
      <td>/apigateway/validate</td>
      <td>Validate dữ liệu APIGateway trong RPA-Engine.</td>
      <td>Thông báo qua SMS</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
    <tr>
      <td>Infra-Server</td>
      <td>Schedule AgentStatus</td>
      <td>/agentstatus/schedule</td>
      <td>Schedule dữ liệu AgentStatus trong Infra-Server.</td>
      <td>Đồng bộ dữ liệu</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
  </tbody>
</table>























<table>
  
  <tbody>
    <tr>
      <td>BCCS2-Core</td>
      <td>Delete DataLake</td>
      <td>/datalake/delete</td>
      <td>Delete dữ liệu DataLake trong BCCS2-Core.</td>
      <td>Ghi log đầy đủ</td>
      <td>Dữ liệu backup mỗi ngày</td>
    </tr>
    <tr>
      <td>Infra-Server</td>
      <td>Validate DataLake</td>
      <td>/datalake/validate</td>
      <td>Validate dữ liệu DataLake trong Infra-Server.</td>
      <td>Không lỗi</td>
      <td>Chạy theo lịch cron</td>
    </tr>
    <tr>
      <td>Infra-Server</td>
      <td>Schedule QoS</td>
      <td>/qos/schedule</td>
      <td>Schedule dữ liệu QoS trong Infra- Server.</td>
      <td>Tự động retry</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>RPA-Engine</td>
      <td>Search CustomerProfile</td>
      <td>/customerprofile/search</td>
      <td>Search dữ liệu CustomerProfile trong RPA-Engine.</td>
      <td>Hiển thị báo cáo</td>
      <td>Dữ liệu backup mỗi ngày</td>
    </tr>
    <tr>
      <td>Infra-Server</td>
      <td>Update Lead</td>
      <td>/lead/update</td>
      <td>Update dữ liệu Lead trong Infra-Server.</td>
      <td>Không lỗi</td>
      <td>Có cơ chế rollback</td>
    </tr>
    <tr>
      <td>Security- Firewall</td>
      <td>Generate CDRReport</td>
      <td>/cdrreport/generate</td>
      <td>Generate dữ liệu CDRReport trong Security-Firewall.</td>
      <td>Đồng bộ dữ liệu</td>
      <td>Chỉ dùng cho admin</td>
    </tr>
    <tr>
      <td>Security- Firewall</td>
      <td>Monitor PackagePlan</td>
      <td>/packageplan/monitor</td>
      <td>Monitor dữ liệu PackagePlan trong Security-Firewall.</td>
      <td>Cảnh báo</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>IPCC- ContactCenter</td>
      <td>Export FirewallPolicy</td>
      <td>/firewallpolicy/export</td>
      <td>Export dữ liệu FirewallPolicy trong</td>
      <td>Thông báo</td>
      <td>Theo chuẩn</td>
    </tr>
  </tbody>
</table>











<table>
  
  <tbody>
    <tr>
      <td>BCCS2- Billing</td>
      <td>Analyze Whitelist</td>
      <td>/whitelist/analyze</td>
      <td>Analyze dữ liệu Whitelist trong BCCS2-Billing.</td>
      <td>Thông báo qua SMS</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>Security- Firewall</td>
      <td>Generate CDRReport</td>
      <td>/cdrreport/generate</td>
      <td>Generate dữ liệu CDRReport trong Security-Firewall.</td>
      <td>Thành công</td>
      <td>Có cơ chế rollback</td>
    </tr>
    <tr>
      <td>IPCC- ContactCenter</td>
      <td>Analyze Whitelist</td>
      <td>/whitelist/analyze</td>
      <td>Analyze dữ liệu Whitelist trong IPCC- ContactCenter.</td>
      <td>Không lỗi</td>
      <td>Dữ liệu backup mỗi ngày</td>
    </tr>
    <tr>
      <td>QA- Automation</td>
      <td>Export Invoice</td>
      <td>/invoice/export</td>
      <td>Export dữ liệu Invoice trong QA- Automation.</td>
      <td>Hiển thị báo cáo</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
    <tr>
      <td>IPCC- ContactCenter</td>
      <td>Export QoS</td>
      <td>/qos/export</td>
      <td>Export dữ liệu QoS trong IPCC- ContactCenter.</td>
      <td>Cảnh báo</td>
      <td>Dữ liệu backup mỗi ngày</td>
    </tr>
    <tr>
      <td>BCCS2-Core</td>
      <td>Insert CDRReport</td>
      <td>/cdrreport/insert</td>
      <td>Insert dữ liệu CDRReport trong BCCS2-Core.</td>
      <td>Lỗi nghiêm trọng</td>
      <td>Kết nối với hệ thống Billing</td>
    </tr>
    <tr>
      <td>BCCS2-Core</td>
      <td>Update APIGateway</td>
      <td>/apigateway/update</td>
      <td>Update dữ liệu APIGateway trong BCCS2-Core.</td>
      <td>Tự động retry</td>
      <td>Chỉ dùng cho admin</td>
    </tr>
    <tr>
      <td>Infra-Server</td>
      <td>Export TransactionLog</td>
      <td>/transactionlog/export</td>
      <td>Export dữ liệu TransactionLog trong Infra-Server.</td>
      <td>Cảnh báo</td>
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
      <td></td>
      <td></td>
      <td>thống Billing</td>
    </tr>
    <tr>
      <td>CRM- Platform</td>
      <td>Monitor Promotion</td>
      <td>/promotion/monitor</td>
      <td>Monitor dữ liệu Promotion trong CRM-Platform.</td>
      <td>Cảnh báo</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>Security- Firewall</td>
      <td>Monitor Whitelist</td>
      <td>/whitelist/monitor</td>
      <td>Monitor dữ liệu Whitelist trong Security-Firewall.</td>
      <td>Thông báo qua SMS</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
    <tr>
      <td>IPCC- ContactCenter</td>
      <td>Delete PackagePlan</td>
      <td>/packageplan/delete</td>
      <td>Delete dữ liệu PackagePlan trong IPCC- ContactCenter.</td>
      <td>Thành công</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>IVR-System</td>
      <td>Insert DebtControl</td>
      <td>/debtcontrol/insert</td>
      <td>Insert dữ liệu DebtControl trong IVR-System.</td>
      <td>Lỗi nghiêm trọng</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>Infra-Server</td>
      <td>Optimize Whitelist</td>
      <td>/whitelist/optimize</td>
      <td>Optimize dữ liệu Whitelist trong Infra-Server.</td>
      <td>Tự động retry</td>
      <td>Dữ liệu backup mỗi ngày</td>
    </tr>
    <tr>
      <td>Infra-Network Monitor</td>
      <td>Promotion</td>
      <td>/promotion/monitor</td>
      <td>Monitor dữ liệu Promotion trong Infra-Network.</td>
      <td>Hiển thị báo cáo</td>
      <td>Kết nối với hệ thống Billing</td>
    </tr>
    <tr>
      <td>BCCS2-Core</td>
      <td>Import IVRPrompt</td>
      <td>/ivrprompt/import</td>
      <td>Import dữ liệu IVRPrompt trong BCCS2-Core.</td>
      <td>Không lỗi</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
  </tbody>
</table>







<table>
  
  <tbody>
    <tr>
      <td>Infra-Server</td>
      <td>Update KPIReport</td>
      <td>/kpireport/update</td>
      <td>Update dữ liệu KPIReport trong Infra-Server.</td>
      <td>Tự động retry</td>
      <td>Có cơ chế rollback</td>
    </tr>
    <tr>
      <td>BCCS2- Billing</td>
      <td>Config Lead</td>
      <td>/lead/config</td>
      <td>Config dữ liệu Lead trong BCCS2- Billing.</td>
      <td>Đồng bộ dữ liệu</td>
      <td>Có cơ chế rollback</td>
    </tr>
    <tr>
      <td>CRM- Platform</td>
      <td>Analyze Blacklist</td>
      <td>/blacklist/analyze</td>
      <td>Analyze dữ liệu Blacklist trong CRM-Platform.</td>
      <td>Cảnh báo</td>
      <td>Chạy theo lịch cron</td>
    </tr>
    <tr>
      <td>QA- Automation</td>
      <td>Update Whitelist</td>
      <td>/whitelist/update</td>
      <td>Update dữ liệu Whitelist trong QA- Automation.</td>
      <td>Thông báo qua SMS</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>IPCC- ContactCenter</td>
      <td>Monitor Invoice</td>
      <td>/invoice/monitor</td>
      <td>Monitor dữ liệu Invoice trong IPCC- ContactCenter.</td>
      <td>Ghi log đầy đủ</td>
      <td>Bảo mật 2 lớp</td>
    </tr>
    <tr>
      <td>CRM- Platform</td>
      <td>Export Invoice</td>
      <td>/invoice/export</td>
      <td>Export dữ liệu Invoice trong CRM- Platform.</td>
      <td>Lỗi nghiêm trọng</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>Infra-Server</td>
      <td>Import KPIReport</td>
      <td>/kpireport/import</td>
      <td>Import dữ liệu KPIReport trong Infra-Server.</td>
      <td>Tự động retry</td>
      <td>Chạy theo lịch cron</td>
    </tr>
    <tr>
      <td>QA- Automation</td>
      <td>Validate Lead</td>
      <td>/lead/validate</td>
      <td>Validate dữ liệu Lead trong QA- Automation.</td>
      <td>Thành công</td>
      <td>Chỉ dùng cho admin</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>Infra-Server</td>
      <td>Update VPN</td>
      <td>/vpn/update</td>
      <td>Update dữ liệu VPN trong Infra-Server.</td>
      <td>Thông báo qua email</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>Infra-Network</td>
      <td>Search VPN</td>
      <td>/vpn/search</td>
      <td>Search dữ liệu VPN trong Infra-Network.</td>
      <td>Thông báo qua email</td>
      <td>Chạy theo lịch cron</td>
    </tr>
    <tr>
      <td>BCCS2- Billing</td>
      <td>Export APIGateway</td>
      <td>/apigateway/export</td>
      <td>Export dữ liệu APIGateway trong BCCS2-Billing.</td>
      <td>Đồng bộ dữ liệu</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>Infra-Network</td>
      <td>Import KPIReport</td>
      <td>/kpireport/import</td>
      <td>Import dữ liệu KPIReport trong Infra-Network.</td>
      <td>Thông báo qua email</td>
      <td>Kết nối với hệ thống Billing</td>
    </tr>
    <tr>
      <td>Security- Firewall</td>
      <td>Export APIGateway</td>
      <td>/apigateway/export</td>
      <td>Export dữ liệu APIGateway trong Security-Firewall.</td>
      <td>Tự động retry</td>
      <td>Theo chuẩn ISO 27001</td>
    </tr>
    <tr>
      <td>Infra-Server</td>
      <td>Schedule Blacklist</td>
      <td>/blacklist/schedule</td>
      <td>Schedule dữ liệu Blacklist trong Infra- Server.</td>
      <td>Hiển thị báo cáo</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>QA- Automation</td>
      <td>Schedule Blacklist</td>
      <td>/blacklist/schedule</td>
      <td>Schedule dữ liệu Blacklist trong QA- Automation.</td>
      <td>Tự động retry</td>
      <td>Tích hợp với CRM</td>
    </tr>
  </tbody>
</table>







<table>
  
  <tbody>
    <tr>
      <td>RPA-Engine</td>
      <td>Analyze CDRReport</td>
      <td>/cdrreport/analyze</td>
      <td>Analyze dữ liệu CDRReport trong RPA-Engine.</td>
      <td>Hiển thị báo cáo</td>
      <td>Tích hợp với CRM</td>
    </tr>
    <tr>
      <td>IPCC- ContactCenter</td>
      <td>Search Contact</td>
      <td>/contact/search</td>
      <td>Search dữ liệu Contact trong IPCC- ContactCenter.</td>
      <td>Thành công</td>
      <td>Chỉ dùng cho admin</td>
    </tr>
    <tr>
      <td>IVR-System</td>
      <td>Analyze FirewallPolicy</td>
      <td>/firewallpolicy/analyze</td>
      <td>Analyze dữ liệu FirewallPolicy trong IVR-System.</td>
      <td>Không lỗi</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>Infra-Network</td>
      <td>Search IVRPrompt</td>
      <td>/ivrprompt/search</td>
      <td>Search dữ liệu IVRPrompt trong Infra-Network.</td>
      <td>Thông báo qua email</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>Infra-Network</td>
      <td>Schedule VPN</td>
      <td>/vpn/schedule</td>
      <td>Schedule dữ liệu VPN trong Infra- Network.</td>
      <td>Hiển thị báo cáo</td>
      <td>Chỉ dùng cho admin</td>
    </tr>
    <tr>
      <td>IVR-System</td>
      <td>Monitor TransactionLog</td>
      <td>/transactionlog/monitor</td>
      <td>Monitor dữ liệu TransactionLog trong IVR-System.</td>
      <td>Tự động retry</td>
      <td>Yêu cầu xác thực người dùng</td>
    </tr>
    <tr>
      <td>QA- Automation</td>
      <td>Monitor StorageVolume</td>
      <td>/storagevolume/monitor</td>
      <td>Monitor dữ liệu StorageVolume trong QA- Automation.</td>
      <td>Thông báo qua email</td>
      <td>Tích hợp với CRM</td>
    </tr>
  </tbody>
</table>
