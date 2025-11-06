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



<table><tr><td rowspan=1 colspan=1>8.</td><td rowspan=1 colspan=1>Don vi VHKT</td><td rowspan=1 colspan=1>B@ phan Van hanh khai thac</td></tr><tr><td rowspan=1 colspan=1>9.</td><td rowspan=1 colspan=1>GNOC</td><td rowspan=1 colspan=1>Global Network OperationsCenter: Hé thong quan ly vadieu hanh mang luoi toan cau</td></tr><tr><td rowspan=1 colspan=1>10.</td><td rowspan=1 colspan=1>BM</td><td rowspan=1 colspan=1>Biéu mau</td></tr><tr><td rowspan=1 colspan=1>11.</td><td rowspan=1 colspan=1>SR</td><td rowspan=1 colspan=1>Service Request - Yéu câudich vu can dap ung</td></tr><tr><td rowspan=1 colspan=1>12.</td><td rowspan=1 colspan=1>CR</td><td rowspan=1 colspan=1>Change Request: Phiéu yéucau tac dong mang luoi</td></tr><tr><td rowspan=1 colspan=1>13.</td><td rowspan=1 colspan=1>PYC</td><td rowspan=1 colspan=1>Phieu yéu cau</td></tr><tr><td rowspan=1 colspan=1>14.</td><td rowspan=1 colspan=1>PAKD</td><td rowspan=1 colspan=1>Phuong án kinh doanh</td></tr></table>

# 5. Trách nhiệm các bên liên quan

- Đơn vị cấp phát: Chịu trách nhiệm cấp phát, quản lý tài nguyên cấp 1: Bộ phận quản lý, cấp phát trực thuộc Bộ phận Cấp phát tài nguyên (cấp phòng); cấp phê duyệt lãnh đạo TT   
- Đơn vị VHKT chịu trách nhiệm sử dụng, cấp phát, quản lý cấp 2.



- ĐVCP: Chịu trách nhiệm cấp phát đúng tài nguyên yêu cầu, không bị trùng lặp.

ĐVSD: Chịu trách nhiệm trong việc sử dụng tài nguyên: Dùng đúng mục đích, không lãng phí, thất thoát.

6. Nội dung hướng dẫn quản lý cấp phát, thu hồi tài nguyên IP

6.1 Hướng dẫn cấp phát tài nguyên IP   

<table><tr><td rowspan=1 colspan=1>STT</td><td rowspan=1 colspan=1>Hoat dongchinh</td><td rowspan=1 colspan=1>Cong viec thurc hien</td><td rowspan=1 colspan=1>DV thurchien</td><td rowspan=1 colspan=1>Phihop</td><td rowspan=1 colspan=1>Cong cuthurc hien</td><td rowspan=1 colspan=1>Dau vao</td><td rowspan=1 colspan=1>Dau ra</td><td rowspan=1 colspan=1>Thoi gian thurc hien</td></tr><tr><td rowspan=1 colspan=1>1.</td><td rowspan=1 colspan=1>Trinh kyphieu yeu caucap phat tainguyen</td><td rowspan=1 colspan=1>- Thuc hien theo biéu mauBM01 (tai nguyen IP c6 2 loai IP public va IP private) khi thuc hien phai ghi royeu cau.</td><td rowspan=1 colspan=1>DVSD</td><td rowspan=1 colspan=1>DVCP</td><td rowspan=1 colspan=1>Voffice</td><td rowspan=1 colspan=1>Nhu cau tainguyen choviec trienkhai moi</td><td rowspan=1 colspan=1>PYCcapphat tainguyenduoctrinh ky</td><td rowspan=1 colspan=1>Theo thoi gian thuc té</td></tr><tr><td rowspan=1 colspan=1>2.</td><td rowspan=1 colspan=1>Phe duyet phiéu yeu caucap phat tainguyen</td><td rowspan=1 colspan=1>- Thuc hien phé duyét yéucau cua don vi yeu cau cap phat tai nguyen tren heth6ng VOFFICE.</td><td rowspan=1 colspan=1>Lanh daophongDVSD</td><td rowspan=1 colspan=1>DVCP</td><td rowspan=1 colspan=1>Voffice</td><td rowspan=1 colspan=1>PYC,PAKD/hopdong/totrinhde xuat cungcaptai nguyen duocphe duyet</td><td rowspan=1 colspan=1>PYCduocpheduyet</td><td rowspan=1 colspan=1>Theo thoi gian thuc té</td></tr><tr><td rowspan=1 colspan=1>3.</td><td rowspan=1 colspan=1>Tao SR capphat</td><td rowspan=1 colspan=1>- DVSD tao SR dinh kem PYC da duoc phe duyet.</td><td rowspan=1 colspan=1>DVSD</td><td rowspan=1 colspan=1>DVCP</td><td rowspan=1 colspan=1>GNOC</td><td rowspan=1 colspan=1>PYC duocphé duyet, socur lien quan</td><td rowspan=1 colspan=1>SR duoctao trenGNOC</td><td rowspan=1 colspan=1>Theo thoi gian thuc té</td></tr></table>



<table><tr><td rowspan=1 colspan=1>STT</td><td rowspan=1 colspan=1>Hoat dongchinh</td><td rowspan=1 colspan=1> Cong viec thurc hien</td><td rowspan=1 colspan=1>DV thurchien</td><td rowspan=1 colspan=1>Phoihop</td><td rowspan=1 colspan=1>Cong cuthuc hien</td><td rowspan=1 colspan=1>Dau vao</td><td rowspan=1 colspan=1>Dau ra</td><td rowspan=1 colspan=1>Thoi gian thurc hien</td></tr><tr><td rowspan=1 colspan=1>4.</td><td rowspan=1 colspan=1>Tiep nhan SRcap phat</td><td rowspan=1 colspan=1>DV CPTN tiep nhan vadanh gia SR:- Truong hop SR dam bao theo yeu cau: Chuyén sangBuoc 5 - Truong hop SR khong dam bao theo yeu cau: Turchói SR, yéu cau DVYC bó sung thong tin con thiéu vaquay lai Buroc 3.Thoi gian tiép nhan: 01ngay lam viec tinh tur thoidiem SR duoc tao.</td><td rowspan=1 colspan=1>DVCP</td><td rowspan=1 colspan=1>DVSD</td><td rowspan=1 colspan=1>GNOC</td><td rowspan=1 colspan=1>SR trenGNOC</td><td rowspan=1 colspan=1>SR duoctiepnhan</td><td rowspan=1 colspan=1>10 ngay lam viec</td></tr><tr><td rowspan=1 colspan=1>5.</td><td rowspan=1 colspan=1>Cap phat tainguyen</td><td rowspan=1 colspan=1>BP CPTN thuc hien: - Cap phat tai nguyen theo PYC tu dong thuc hien tren phan mém. - C6 thé bó sung cac ghi chu vao phan muc tai nguyencap phat tren he thong.</td><td rowspan=1 colspan=1>DVCP</td><td rowspan=1 colspan=1>DVSD</td><td rowspan=1 colspan=1>Trangquan tri tainguyen</td><td rowspan=1 colspan=1>Yeu cau vétai nguyentren SR datiép nhan</td><td rowspan=1 colspan=1>Ket quathurchien capphat</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>5.1</td><td rowspan=1 colspan=1>Cap nhat coso dur lieu</td><td rowspan=1 colspan=1> Cap nhat co so du lieu quanly tai nguyen IP</td><td rowspan=1 colspan=1>He thong,DVCP</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Ngay khi cap phat xong</td></tr></table>



<table><tr><td rowspan=1 colspan=1>STT</td><td rowspan=1 colspan=1>Hoat dongchinh</td><td rowspan=1 colspan=1>Cong viec thurc hien</td><td rowspan=1 colspan=1>DV thurchien</td><td rowspan=1 colspan=1>Phoihop</td><td rowspan=1 colspan=1>Cong cuthuc hien</td><td rowspan=1 colspan=1>Dau vao</td><td rowspan=1 colspan=1>Dau ra</td><td rowspan=1 colspan=1> Thoi gian thurc hien</td></tr><tr><td rowspan=1 colspan=1>6.</td><td rowspan=1 colspan=1>D6ng SR capphat trenGNOC</td><td rowspan=1 colspan=1>DVSD thuc hien kiem trathong tin tai nguyen duoccap phat va thuc hien dongSR. Thoi gian dong SR la 01 ngay lam viec.</td><td rowspan=1 colspan=1>DVSD</td><td rowspan=1 colspan=1>DVCP</td><td rowspan=1 colspan=1>GNOC</td><td rowspan=1 colspan=1>Ket qua thuchien cap phat</td><td rowspan=1 colspan=1>SRotrangthaiClosed</td><td rowspan=1 colspan=1></td></tr></table>

# 6.2 Hướng dẫn thu hồi tài nguyên IP

<table><tr><td rowspan=1 colspan=1> STT</td><td rowspan=1 colspan=1>Hoat dongchinh</td><td rowspan=1 colspan=1>Cong viec thurc hien</td><td rowspan=1 colspan=1>DVthurchien</td><td rowspan=1 colspan=1>Phoi hop</td><td rowspan=1 colspan=1>Cong cu thurchien</td><td rowspan=1 colspan=1>Dau vao</td><td rowspan=1 colspan=1>Dau ra</td><td rowspan=1 colspan=1>Thoi gian thuc hien</td></tr><tr><td rowspan=2 colspan=1>1.</td><td rowspan=2 colspan=1>Trinh ky phiéu yeu cauthu hoi tainguyen</td><td rowspan=1 colspan=1>Can cu vao nhu cau su dungtai nguyen, DVCP tao PYC(theo biéu mau BM02) thu</td><td rowspan=2 colspan=1>DVCP</td><td rowspan=2 colspan=1>DVSD</td><td rowspan=2 colspan=1>Voffice</td><td rowspan=2 colspan=1>Nhu cauthu hoi tainguyencua DVCP</td><td rowspan=2 colspan=1>PYC thuc,hien thu hoitai nguyenkhong sudung</td><td rowspan=2 colspan=1>Theo thoi gian thuc té</td></tr><tr><td rowspan=1 colspan=1>hoi tai nguyen IP trong cac truong hop sau:- Tai nguyen IP duoc cap phat nhung khong c6 CRkhai bao tren mang luoi(trong thoi han mot quy, cacdon vi sur dung c6 trachnhiem cap nhat CR khai bao dai IP moi va thong bao chodon vi cap phat hang quy). - Hieu suat sur dung tainguyen IP (dai IP) duoc capthap (0% trong mot quy). Khong tinh dai IP khai bao</td></tr></table>



<table><tr><td rowspan=1 colspan=1>STT</td><td rowspan=1 colspan=1>Hoat dongchinh</td><td rowspan=1 colspan=1> Cong viec thurc hien</td><td rowspan=1 colspan=1>DVthurchien</td><td rowspan=1 colspan=1>Phoi hop</td><td rowspan=1 colspan=1>Cong cu thurchien</td><td rowspan=1 colspan=1>Dau vao</td><td rowspan=1 colspan=1>Dau ra</td><td rowspan=1 colspan=1>Thoi gian thuc hien</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>du phong hoac quy hoachcho cac trrong hop dac bietkhac. - Don vi sur dung (DVSD)thong bao khong con nhucau.</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>2.</td><td rowspan=1 colspan=1>Phe duyetphiéu yéu cauthu hoi tainguyen</td><td rowspan=1 colspan=1>Phe duyet phieu yéu cau</td><td rowspan=1 colspan=1>LanhdaophongDVSD,DV CP</td><td rowspan=1 colspan=1>Vofice</td><td rowspan=1 colspan=1>PYCthu hoitainguyen</td><td rowspan=1 colspan=1>PYC duocphe duyet</td><td rowspan=1 colspan=1>Theo thoi gian thuc té</td><td rowspan=1 colspan=1>Theo thoi gian thuc té</td></tr><tr><td rowspan=1 colspan=1>3.</td><td rowspan=1 colspan=1>Tao SR thuhi</td><td rowspan=1 colspan=1>DVCP thuc hien tao SRdinh kem PYC duoc pheduyét veé viec thu hoi tainguyen.</td><td rowspan=1 colspan=1>DVCP</td><td rowspan=1 colspan=1>DVSD</td><td rowspan=1 colspan=1>GNOC</td><td rowspan=1 colspan=1>PYC duoc phé duyet</td><td rowspan=1 colspan=1>SR duoc taotren GNOC</td><td rowspan=1 colspan=1>01 ngay lam viec (tinh tur thoidiem PYC duoc phe duyet)</td></tr><tr><td rowspan=1 colspan=1>4.</td><td rowspan=1 colspan=1>Tiep nhan SRthu hoi</td><td rowspan=1 colspan=1>DVSD tiep nhan SR, kiemtra cac tai liéu dinh kem va thong tin lien quan vé viecthu hoi tai nguyen. Thoi gian thuc hien cong viec:- Tiep nhan SR: 01 ngaylam viec tinh tr thoi diemDVCP tao SR. - Thuc hien SR: Lap kéhoach dé thu hoi tra lai tai nguyen don vi cáp phat.</td><td rowspan=1 colspan=1>BPCPTN</td><td rowspan=1 colspan=1>DVCP</td><td rowspan=1 colspan=1>GNOC</td><td rowspan=1 colspan=1>SR trenGNOC</td><td rowspan=1 colspan=1>SR dugc tiepnhan</td><td rowspan=1 colspan=1>Tiep nhan SR: 01 ngay lamviec.Thuc hien SR: Theo thoi gian thuc té thuchien ké hoach, toi da O1 thang</td></tr></table>



<table><tr><td rowspan=1 colspan=1>STT</td><td rowspan=1 colspan=1>Hoat dongchinh</td><td rowspan=1 colspan=1>Cong viec thurc hien</td><td rowspan=1 colspan=1>DVthurchien</td><td rowspan=1 colspan=1>Phoi hop</td><td rowspan=1 colspan=1>Congcu thrchien</td><td rowspan=1 colspan=1>Dau vao</td><td rowspan=1 colspan=1>Dau ra</td><td rowspan=1 colspan=1>Thoi gian thurc hien</td></tr><tr><td rowspan=1 colspan=1>5.</td><td rowspan=1 colspan=1>Lap, thuchien ke hoachthu hoi</td><td rowspan=1 colspan=1>DVSD lap ke hoach de thuhoi tai nguyen</td><td rowspan=1 colspan=1>DVSD</td><td rowspan=1 colspan=1>Cac don vi lien quan</td><td rowspan=1 colspan=1>Email</td><td rowspan=1 colspan=1>Thong tinyeu cau tainguyen</td><td rowspan=1 colspan=1>Tai nguyenduoc thu hoi(x6a khai baodai IP trencac he thóng)</td><td rowspan=1 colspan=1>Ngay sau khi tiep nhan thongtin, thoi gian thuc hien theo tinh hinh thuc té</td></tr><tr><td rowspan=1 colspan=1>6.</td><td rowspan=1 colspan=1>Cap nhatthong tin dathu hoi lenSR</td><td rowspan=1 colspan=1> DVSD thuc hien cap nhat SR sau khi hoan thanh kéhoach thu hoi tai nguyen IP</td><td rowspan=1 colspan=1>BPCPTN</td><td rowspan=1 colspan=1>GNOC</td><td rowspan=1 colspan=1>Kéhoachthu hoi,dai IPthu hoi</td><td rowspan=1 colspan=1>SR duroccap nhat</td><td rowspan=1 colspan=1>01 ngay lamviec</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>7.</td><td rowspan=1 colspan=1>D6ng SR capphat trenGNOC</td><td rowspan=1 colspan=1>DVCP thuc hien dong SR sau khi nhan thong tin hoanthanh thu hoi tai nguyen theo yéu cau</td><td rowspan=1 colspan=1>DVCP</td><td rowspan=1 colspan=1>DVSD</td><td rowspan=1 colspan=1>GNOC</td><td rowspan=1 colspan=1>Ket quathuc hienké hoach(Ke hoach,CR)</td><td rowspan=1 colspan=1>SRotrangthai Closed</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>8.</td><td rowspan=1 colspan=1>Cap nhat coso dur lieu</td><td rowspan=1 colspan=1>Cap nhat co so du lieu quanly tai nguyen IP</td><td rowspan=1 colspan=1>Hethong，DVCP,DVSD</td><td rowspan=1 colspan=1>Ngay khi thuhoi xong</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>
