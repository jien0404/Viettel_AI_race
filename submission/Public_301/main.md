# Public_301

# 1. Mục lục

1. Giới Thiệu Và Mục Tiêu   
2. Kiến Trúc QoS Trên Catalyst 9400   
3. Thành Phần QoS: Classification, Marking, Shaping, Policing, Queuing   
4. Bảng Tra Cứu DSCP/PHB/CoS Và Mapping Queue (Bảng Phức Tạp)   
5. Triển Khai QoS Với MQC (Cisco IOS)   
6. Kịch Bản Thực Hành: Voice $^ +$ Video $^ +$ Data   
7. Giám Sát, Kiểm Chứng Và Xử Lý Sự Cố   
8. Lưu Ý, Hạn Chế, Best Practices   
9. Phụ Lục: Thuật Ngữ, Mẫu Cấu Hình

# 2. Giới Thiệu Và Mục Tiêu

Chất lượng dịch vụ (QoS) là tập hợp các cơ chế nhằm ưu tiên lưu lượng quan trọng, đảm bảo độ trễ, jitter và mất gói nằm trong ngưỡng chấp nhận. Giáo trình hướng đến khả năng thiết kế và cấu hình QoS theo chuẩn Cisco IOS, áp dụng cho môi trường doanh nghiệp.

# 3. Kiến Trúc QoS Trên Catalyst 9400

Catalyst 9400 sử dụng Modular QoS CLI (MQC) để định nghĩa class-map, policy-map và áp dụng service-policy vào interface/VLAN. Kiến trúc phần cứng hỗ trợ nhiều hàng đợi (queue) và thuật toán lập lịch.

Bảng 2.1 – Pipeline QoS (Heading Nằm Trong Bảng)   

<table>
  
  <tbody>
    <tr>
      <td>PIPELINE QOS TRÊN THIẾT BỊ (HEADING TRONG BẢNG)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bước</td>
      <td>Thành Phần</td>
      <td>Đầu Vào</td>
      <td>Hành Động</td>
      <td>Đầu Ra</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Classification Marking</td>
      <td>ACL/DSCP/CoS/NBAR Xác định</td>
      <td>lớp lưu lượng</td>
      <td>Lớp dịch vụ</td>
    </tr>
    <tr>
      <td>2</td>
      <td></td>
      <td>Gói đã phân loại</td>
      <td>Gán DSCP/CoS/IP Precedence</td>
      <td>Nhãn QoS</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Policing</td>
      <td>Nhãn + tốc độ vào</td>
      <td>Giới hạn/mark-down/drop Lưu lượng phù hợp ngưỡng</td>
      <td></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Shaping</td>
      <td>Hàng đợi đầu ra</td>
      <td>Điều chỉnh tốc độ, làm mượt</td>
      <td>Luồng ổn định</td>
    </tr>
  </tbody>
</table>

# 4. Thành Phần QoS

Các thành phần chính $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ : Classification & Marking (xác định và gắn nhãn), Policing & Shaping (giới hạn và làm mượt), Queuing & Scheduling (ưu tiên khi nghẽn).

Bảng 3.1 – So Sánh Thành Phần QoS (Merge Nhiều Ô)   

<table>
  
  <tbody>
    <tr>
      <td>SO SÁNH CÁC THÀNH PHẦN QOS</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Thành Phần</td>
      <td>Mục Đích</td>
      <td>Ưu Điểm</td>
      <td>Nhược Điểm</td>
      <td>Tình Huống Dùng</td>
      <td>Lưu Ý</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>Classification Nhận</td>
      <td>diện lưu lượng</td>
      <td>Chính xác theo ứng dụng Phụ thuộc match</td>
      <td></td>
      <td>Biên mạng</td>
      <td>Đồng bộ toàn mạng</td>
    </tr>
    <tr>
      <td>Marking</td>
      <td>Gán DSCP/CoS</td>
      <td>Ưu tiên xuyên miền</td>
      <td>Sai mark gây lệch</td>
      <td>Core/Distribution Tuân thủ chính sách</td>
      <td></td>
    </tr>
    <tr>
      <td>Policing</td>
      <td>Giới hạn tốc độ Bảo vệ tài nguyên Drop gói</td>
      <td></td>
      <td></td>
      <td>Biên, ràng buộc</td>
      <td>Kết hợp remark- down</td>
    </tr>
    <tr>
      <td>Shaping Làm mượt lưu lượng</td>
      <td></td>
      <td>Giảm burst</td>
      <td>Tăng trễ</td>
      <td>WAN/Metro Đặt</td>
      <td>tốc độ hợp lý</td>
    </tr>
    <tr>
      <td>Queuing</td>
      <td>Xếp hàng theo lớp</td>
      <td>Đảm bảo ưu tiên</td>
      <td>Cấu hình phức tạp</td>
      <td>Tại nơi nghẽn</td>
      <td>Kết hợp scheduling</td>
    </tr>
  </tbody>
</table>

# 5. Bảng Tra Cứu DSCP/PHB/CoS Và Mapping Queue

Bảng 4.1 – DSCP → PHB → CoS → Queue/Schedule (Bảng Vắt Trang)   

<table>
  
  <tbody>
    <tr>
      <td>ST T</td>
      <td>Lớp Dịch Vụ Ứng Dụng</td>
      <td></td>
      <td>DSC P</td>
      <td>PHB</td>
      <td>Co S</td>
      <td>Queu e</td>
      <td>Schedule</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Voice</td>
      <td>VoIP/SIP</td>
      <td>EF (46)</td>
      <td>Expedited Forwardin g</td>
      <td>5-7</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Video</td>
      <td>Conf/Streamin g</td>
      <td>AF41 (34)</td>
      <td>Assured Forwardin g</td>
      <td>4-5</td>
      <td>WFQ Q4</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Control</td>
      <td>OSPF/BGP</td>
      <td>CS6 (48)</td>
      <td>Network Control</td>
      <td>6</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Signaling</td>
      <td>SIP/H.323</td>
      <td>CS3 (24)</td>
      <td>Class Selector</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Transactiona l</td>
      <td>DB/ERP</td>
      <td>AF31 (26)</td>
      <td>Assured Forwardin g</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Bulk</td>
      <td>Backup/Sync</td>
      <td>AF11 (10)</td>
      <td>Assured Forwardin g</td>
      <td>1</td>
      <td>WFQ Q2</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>7</td>
      <td>BestEffort</td>
      <td>Web/Email</td>
      <td>BE (0)</td>
      <td>Best Effort</td>
      <td>0</td>
      <td>WFQ Q1</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Voice</td>
      <td>VoIP/SIP</td>
      <td>EF (46)</td>
      <td>Expedited Forwardin g</td>
      <td>5-7</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>9</td>
      <td>Video</td>
      <td>Conf/Streamin g</td>
      <td>AF41 (34)</td>
      <td>Assured Forwardin g</td>
      <td>4-5</td>
      <td>WFQ Q4</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td></td>
      <td>Control</td>
      <td>OSPF/BGP</td>
      <td>CS6 (48)</td>
      <td>Network Control</td>
      <td>6</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td></td>
      <td>Signaling</td>
      <td>SIP/H.323</td>
      <td>CS3 (24)</td>
      <td>Class Selector</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td></td>
      <td>Transactiona l</td>
      <td>DB/ERP</td>
      <td>AF31 (26)</td>
      <td>Assured Forwardin g</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td></td>
      <td>Bulk</td>
      <td>Backup/Sync</td>
      <td>AF11 (10)</td>
      <td>Assured Forwardin g</td>
      <td>1</td>
      <td>WFQ Q2</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td></td>
      <td>BestEffort</td>
      <td>Web/Email</td>
      <td>BE (0)</td>
      <td>Best Effort</td>
      <td>0</td>
      <td>WFQ Q1</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>10</td>
      <td>Voice</td>
      <td>VoIP/SIP</td>
      <td>EF (46)</td>
      <td>Expedited Forwardin g</td>
      <td>5-7</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>11</td>
      <td>Video</td>
      <td>Conf/Streamin g</td>
      <td>AF41 (34)</td>
      <td>Assured Forwardin g</td>
      <td>4-5</td>
      <td>WFQ Q4</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Control</td>
      <td>OSPF/BGP</td>
      <td>CS6 (48)</td>
      <td>Network Control</td>
      <td>6</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>13</td>
      <td>Signaling</td>
      <td>SIP/H.323</td>
      <td>CS3 (24)</td>
      <td>Class Selector</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>14</td>
      <td>Transactiona l</td>
      <td>DB/ERP</td>
      <td>AF31 (26)</td>
      <td>Assured Forwardin g</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>15</td>
      <td>Bulk</td>
      <td>Backup/Sync</td>
      <td>AF11 (10)</td>
      <td>Assured Forwardin g</td>
      <td>1</td>
      <td>WFQ Q2</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>16</td>
      <td>BestEffort</td>
      <td>Web/Email</td>
      <td>BE (0)</td>
      <td>Best Effort</td>
      <td>0</td>
      <td>WFQ Q1</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>17</td>
      <td>Voice</td>
      <td>VoIP/SIP</td>
      <td>EF (46)</td>
      <td>Expedited Forwardin g</td>
      <td>5-7</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>18</td>
      <td>Video</td>
      <td>Conf/Streamin g</td>
      <td>AF41 (34)</td>
      <td>Assured Forwardin g</td>
      <td>4-5</td>
      <td>WFQ Q4</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>19</td>
      <td>Control</td>
      <td>OSPF/BGP</td>
      <td>CS6 (48)</td>
      <td>Network Control</td>
      <td>6</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>20</td>
      <td>Signaling</td>
      <td>SIP/H.323</td>
      <td>CS3 (24)</td>
      <td>Class Selector</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>21</td>
      <td>Transactiona l</td>
      <td>DB/ERP</td>
      <td>AF31 (26)</td>
      <td>Assured Forwardin g</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>22</td>
      <td>Bulk</td>
      <td>Backup/Sync</td>
      <td>AF11 (10)</td>
      <td>Assured Forwardin g</td>
      <td>1</td>
      <td>WFQ Q2</td>
      <td>Weighte d</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>23</td>
      <td>BestEffort</td>
      <td>Web/Email</td>
      <td>BE (0)</td>
      <td>Best Effort</td>
      <td>0</td>
      <td>WFQ Q1</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>24</td>
      <td>Voice</td>
      <td>VoIP/SIP</td>
      <td>EF (46)</td>
      <td>Expedited Forwardin g</td>
      <td>5-7</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>25</td>
      <td>Video</td>
      <td>Conf/Streamin g</td>
      <td>AF41 (34)</td>
      <td>Assured Forwardin g</td>
      <td>4-5</td>
      <td>WFQ Q4</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>26</td>
      <td>Control</td>
      <td>OSPF/BGP</td>
      <td>CS6 (48)</td>
      <td>Network Control</td>
      <td>6</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>27</td>
      <td>Signaling</td>
      <td>SIP/H.323</td>
      <td>CS3 (24)</td>
      <td>Class Selector</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>28</td>
      <td>Transactiona l</td>
      <td>DB/ERP</td>
      <td>AF31 (26)</td>
      <td>Assured Forwardin g</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>29</td>
      <td>Bulk</td>
      <td>Backup/Sync</td>
      <td>AF11 (10)</td>
      <td>Assured Forwardin g</td>
      <td>1</td>
      <td>WFQ Q2</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>30</td>
      <td>BestEffort</td>
      <td>Web/Email</td>
      <td>BE (0)</td>
      <td>Best Effort</td>
      <td>0</td>
      <td>WFQ Q1</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>31</td>
      <td>Voice</td>
      <td>VoIP/SIP</td>
      <td>EF (46)</td>
      <td>Expedited Forwardin g</td>
      <td>5-7</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>32</td>
      <td>Video</td>
      <td>Conf/Streamin g</td>
      <td>AF41 (34)</td>
      <td>Assured Forwardin g</td>
      <td>4-5</td>
      <td>WFQ Q4</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>33</td>
      <td>Control</td>
      <td>OSPF/BGP</td>
      <td>CS6 (48)</td>
      <td>Network Control</td>
      <td>6</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>34</td>
      <td>Signaling</td>
      <td>SIP/H.323</td>
      <td>CS3 (24)</td>
      <td>Class Selector</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>35</td>
      <td>Transactiona l</td>
      <td>DB/ERP</td>
      <td>AF31 (26)</td>
      <td>Assured Forwardin g</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>36</td>
      <td>Bulk</td>
      <td>Backup/Sync</td>
      <td>AF11 (10)</td>
      <td>Assured Forwardin g</td>
      <td>1</td>
      <td>WFQ Q2</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>37</td>
      <td>BestEffort</td>
      <td>Web/Email</td>
      <td>BE (0)</td>
      <td>Best Effort</td>
      <td>0</td>
      <td>WFQ Q1</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>38</td>
      <td>Voice</td>
      <td>VoIP/SIP</td>
      <td>EF (46)</td>
      <td>Expedited Forwardin g</td>
      <td>5-7</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>39</td>
      <td>Video</td>
      <td>Conf/Streamin g</td>
      <td>AF41 (34)</td>
      <td>Assured Forwardin g</td>
      <td>4-5</td>
      <td>WFQ Q4</td>
      <td>Weighte d</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>40</td>
      <td>Control</td>
      <td>OSPF/BGP</td>
      <td>CS6 (48)</td>
      <td>Network Control</td>
      <td>6</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>41</td>
      <td>Signaling</td>
      <td>SIP/H.323</td>
      <td>CS3 (24)</td>
      <td>Class Selector</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>42</td>
      <td>Transactiona l</td>
      <td>DB/ERP</td>
      <td>AF31 (26)</td>
      <td>Assured Forwardin g</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>43</td>
      <td>Bulk</td>
      <td>Backup/Sync</td>
      <td>AF11 (10)</td>
      <td>Assured Forwardin g</td>
      <td>1</td>
      <td>WFQ Q2</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>44</td>
      <td>BestEffort</td>
      <td>Web/Email</td>
      <td>BE (0)</td>
      <td>Best Effort</td>
      <td>0</td>
      <td>WFQ Q1</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>45</td>
      <td>Voice</td>
      <td>VoIP/SIP</td>
      <td>EF (46)</td>
      <td>Expedited Forwardin g</td>
      <td>5-7</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>46</td>
      <td>Video</td>
      <td>Conf/Streamin g</td>
      <td>AF41 (34)</td>
      <td>Assured Forwardin g</td>
      <td>4-5</td>
      <td>WFQ Q4</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>47</td>
      <td>Control</td>
      <td>OSPF/BGP</td>
      <td>CS6 (48)</td>
      <td>Network Control</td>
      <td>6</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>48</td>
      <td>Signaling</td>
      <td>SIP/H.323</td>
      <td>CS3 (24)</td>
      <td>Class Selector</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>49</td>
      <td>Transactiona l</td>
      <td>DB/ERP</td>
      <td>AF31 (26)</td>
      <td>Assured Forwardin g</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>50</td>
      <td>Bulk</td>
      <td>Backup/Sync</td>
      <td>AF11 (10)</td>
      <td>Assured Forwardin g</td>
      <td>1</td>
      <td>WFQ Q2</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>51</td>
      <td>BestEffort</td>
      <td>Web/Email</td>
      <td>BE (0)</td>
      <td>Best Effort</td>
      <td>0</td>
      <td>WFQ Q1</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>52</td>
      <td>Voice</td>
      <td>VoIP/SIP</td>
      <td>EF (46)</td>
      <td>Expedited Forwardin g</td>
      <td>5-7</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>53</td>
      <td>Video</td>
      <td>Conf/Streamin g</td>
      <td>AF41 (34)</td>
      <td>Assured Forwardin g</td>
      <td>4-5</td>
      <td>WFQ Q4</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>54</td>
      <td>Control</td>
      <td>OSPF/BGP</td>
      <td>CS6 (48)</td>
      <td>Network Control</td>
      <td>6</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>55</td>
      <td>Signaling</td>
      <td>SIP/H.323</td>
      <td>CS3 (24)</td>
      <td>Class Selector</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>56</td>
      <td>Transactiona l</td>
      <td>DB/ERP</td>
      <td>AF31 (26)</td>
      <td>Assured Forwardin g</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>57</td>
      <td>Bulk</td>
      <td>Backup/Sync</td>
      <td>AF11 (10)</td>
      <td>Assured Forwardin g</td>
      <td>1</td>
      <td>WFQ Q2</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>58</td>
      <td>BestEffort</td>
      <td>Web/Email</td>
      <td>BE (0)</td>
      <td>Best Effort</td>
      <td>0</td>
      <td>WFQ Q1</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>59</td>
      <td>Voice</td>
      <td>VoIP/SIP</td>
      <td>EF (46)</td>
      <td>Expedited Forwardin g</td>
      <td>5-7</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>60</td>
      <td>Video</td>
      <td>Conf/Streamin g</td>
      <td>AF41 (34)</td>
      <td>Assured Forwardin g</td>
      <td>4-5</td>
      <td>WFQ Q4</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>61</td>
      <td>Control</td>
      <td>OSPF/BGP</td>
      <td>CS6 (48)</td>
      <td>Network Control</td>
      <td>6</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>62</td>
      <td>Signaling</td>
      <td>SIP/H.323</td>
      <td>CS3 (24)</td>
      <td>Class Selector</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>63</td>
      <td>Transactiona l</td>
      <td>DB/ERP</td>
      <td>AF31 (26)</td>
      <td>Assured Forwardin g</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>64</td>
      <td>Bulk</td>
      <td>Backup/Sync</td>
      <td>AF11 (10)</td>
      <td>Assured Forwardin g</td>
      <td>1</td>
      <td>WFQ Q2</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>65</td>
      <td>BestEffort</td>
      <td>Web/Email</td>
      <td>BE (0)</td>
      <td>Best Effort</td>
      <td>0</td>
      <td>WFQ Q1</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>66</td>
      <td>Voice</td>
      <td>VoIP/SIP</td>
      <td>EF (46)</td>
      <td>Expedited Forwardin g</td>
      <td>5-7</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>67</td>
      <td>Video</td>
      <td>Conf/Streamin g</td>
      <td>AF41 (34)</td>
      <td>Assured Forwardin g</td>
      <td>4-5</td>
      <td>WFQ Q4</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>68</td>
      <td>Control</td>
      <td>OSPF/BGP</td>
      <td>CS6 (48)</td>
      <td>Network Control</td>
      <td>6</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
    <tr>
      <td>69</td>
      <td>Signaling</td>
      <td>SIP/H.323</td>
      <td>CS3 (24)</td>
      <td>Class Selector</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>70</td>
      <td>Transactiona l</td>
      <td>DB/ERP</td>
      <td>AF31 (26)</td>
      <td>Assured Forwardin g</td>
      <td>3</td>
      <td>WFQ Q3</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>71</td>
      <td>Bulk</td>
      <td>Backup/Sync</td>
      <td>AF11 (10)</td>
      <td>Assured Forwardin g</td>
      <td>1</td>
      <td>WFQ Q2</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>72</td>
      <td>BestEffort</td>
      <td>Web/Email</td>
      <td>BE (0)</td>
      <td>Best Effort</td>
      <td>0</td>
      <td>WFQ Q1</td>
      <td>Weighte d</td>
    </tr>
    <tr>
      <td>73</td>
      <td>Voice</td>
      <td>VoIP/SIP</td>
      <td>EF (46)</td>
      <td>Expedited Forwardin g</td>
      <td>5-7</td>
      <td>PQ</td>
      <td>Strict Priority</td>
    </tr>
  </tbody>
</table>



<table>
  
  <tbody>
    <tr>
      <td>74</td>
      <td>Video</td>
      <td>Conf/Streamin g</td>
      <td>AF41 (34)</td>
      <td>Assured Forwardin g</td>
      <td>4-5</td>
      <td>WFQ Q4</td>
      <td>Weighte d</td>
    </tr>
  </tbody>
</table>
