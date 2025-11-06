# Public_363

# 1. Khái quát

Định vị di động có thể thực hiện bởi một số nguyên lý kỹ thuật, chẳng hạn như kỹ thuật tìm điểm giao thoa tín hiệu vô tuyến giữa (một số) tháp thu phát sóng di động của mạng và máy điện thoại hoặc đơn giản bằng cách sử dụng dữ liệu của hệ thống vệ tinh dẫn đường toàn cầu GNSS [23].

Để định vị điện thoại di động bằng cách tìm điểm giao thoa tín hiệu vô tuyến di động, điện thoại đó phải phát ra ít nhất tín hiệu nhàn rỗi (tín hiệu chờ - Idle) để liên lạc với các cột ăng ten gần đó và không yêu cầu kích hoạt một cuộc gọi. Hệ thống điện thoại di động toàn cầu GSM thực hiện kết nối điện thoại di động với mạng dựa trên cường độ tín hiệu của điện thoại tới các cột ăng ten gần đó [26].

Kỹ thuật định vị có thể được sử dụng cho các dịch vụ dựa trên vị trí (LBS) [30, 31] và khi đó sẽ tiết lộ tọa độ thực của điện thoại di động. Các công ty viễn thông di động sử dụng kỹ thuật này để xác định vị trí gần đúng của điện thoại di động và cả người dùng của nó.

# 2. Tổng quan các nguyên lý kỹ thuật định vị di động

Vị trí của thiết bị di động (điện thoại di động) có thể được xác định theo các nguyên lý kỹ thuật cụ thể sau đây [23 -33]:

# 2.1 Kỹ thuật định vị dựa trên mạng (Network-Based)

Vị trí của điện thoại di động có thể được xác định trên cơ sở hạ tầng mạng của nhà cung cấp dịch vụ. Ưu điểm của các kỹ thuật dựa trên mạng là chúng có thể được thực hiện mà không ảnh hưởng đến thiết bị cầm tay (tức không xâm phạm/ảnh hưởng đến người dùng). Các kỹ thuật dựa trên mạng đã được phát triển nhiều năm trước khi GPS trên thiết bị cầm tay được phổ biến rộng rãi.

Kỹ thuật định vị của một điện thoại di động dựa trên việc đo mức công suất và các phần tử ăng-ten, đồng thời sử dụng nguyên lý một điện thoại di động được cấp nguồn luôn giao tiếp vô tuyến với một trong những trạm gốc (BTS/eNB) gần nhất. Do đó, các hiểu biết về vị trí của trạm gốc gợi ý rằng điện thoại di động cần định vị đang ở gần trạm gốc đó.



Các hệ thống tiên tiến xác định khu vực mà điện thoại di động ở đó và ước tính gần đúng khoảng cách đến trạm gốc. Xác định khoảng cách gần đúng được tính toán bằng phép nội suy tín hiệu giữa các cột ăng ten liền $\mathrm { k } \dot { \hat { \mathbf { e } } }$ . Các dịch vụ đủ tiêu chuẩn có thể đạt được độ chính xác đến 50 mét ở các khu vực đô thị nơi lưu lượng truy cập di động và mật độ các cột ăng ten (trạm gốc) đủ cao. Tại các khu vực nông thôn và hoang vắng, do các trạm gốc có thể cách nhau hàng km nên việc xác định vị trí của điện thoại di động sẽ kém chính xác hơn. Định vị GSM sử dụng kỹ thuật giao thoa tín hiệu vô tuyến để xác định vị trí của điện thoại di động GSM hoặc sử dụng thiết bị theo dõi chuyên dụng.

Độ chính xác của các kỹ thuật dựa trên mạng là khác nhau. Trong đó kỹ thuật dựa trên nhận dạng tế bào (Cell-ID) là kém chính xác nhất (do có tín hiệu can nhiễu chuyển đổi giữa các tháp di động, hay còn gọi là "tín hiệu phản xạ/dội ngược"); kỹ thuật đo tam giác có độ chính xác vừa phải và kỹ thuật đo tam giác tín hiệu đường lên tiên tiến bằng định thời gian là mới hơn và có độ chính xác cao nhất. Độ chính xác của các kỹ thuật dựa trên mạng đều phụ thuộc vào mật độ của các trạm gốc tế bào. Trong đó, môi trường đô thị thường đạt được độ chính xác cao nhất có thể do có số lượng tháp phát sóng nhiều hơn và sử dụng kỹ thuật định vị bằng phương pháp định thời gian tiên tiến nhất.

Một trong những thách thức chính của các kỹ thuật dựa trên mạng là yêu cầu sự hợp tác chặt chẽ với nhà cung cấp dịch vụ (nhà mạng), nó đòi hỏi phải lắp đặt phần cứng và cài đặt phần mềm trong cơ sở hạ tầng của nhà điều hành mạng di động. Thông thường, việc đặt phần cứng và phần mềm trong cơ sở hạ tầng của nhà mạng phải được pháp luật của nước đó cho phép. Chẳng hạn như qui định của Mỹ trong bộ luật cho dịch vụ cấp cứu, cứu hộ, cứu nạn E911 buộc nhà mạng di động phải triển khai giải pháp kỹ thuật cung cấp khả năng định vị cho E911 trước khi cung cấp dịch vụ di động [25].

# 2.2 Kỹ thuật định vị dựa trên thiết bị cầm tay (Handset Based)

Vị trí của điện thoại di động có thể được xác định bằng cách sử dụng phần mềm khách được cài đặt trên máy điện thoại cầm tay. Kỹ thuật này xác định vị trí của thiết bị cầm tay bằng cách tính toán vị trí của tế bào di động và cường độ tín hiệu của các tế bào nhà và lân cận mà liên tục được gửi từ thiết bị cầm tay đến nhà cung cấp dịch vụ. Ngoài ra, nếu điện thoại cầm tay được trang bị GPS thì có thể lấy được thông tin vị trí chính xác hơn do vị trí GPS của máy cầm tay có thể được gửi đến nhà cung cấp dịch vụ. Một cách tiếp cận khác là sử dụng kỹ thuật dựa trên dấu vân tay, trong đó "chữ ký" của tế bào nhà và tế bào lân cận báo hiệu cường độ tín hiệu tại các điểm khác nhau trong khu vực quan tâm được ghi lại và khớp trong thời gian thực để xác định vị trí của thiết bị cầm tay. Kỹ thuật này thường được thực hiện độc lập với nhà cung cấp dịch vụ.



Nhược điểm chính của các kỹ thuật dựa trên thiết bị cầm tay là sự cần thiết phải cài đặt phần mềm trên thiết bị. Nó đòi hỏi sự hợp tác tích cực, chặt chẽ của người sử dụng thuê bao di động cũng như phần mềm cài đặt phải có khả năng xử lý các hệ điều hành khác nhau của thiết bị cầm tay mà nó liên tục được thay đổi. Nhưng điều này là khó khả thi vì đối tượng của CQAN thường là đối tượng giấu mặt, khó tiếp cận hoặc chúng ở nước ngoài. Thông thường, chẳng hạn như điện thoại thông minh sẽ có thể cài đặt và chạy phần mềm định vị đó cũng như cài đặt, chạy các phần mềm bản đồ số như Google Maps để phục vụ kỹ thuật định vị dựa trên máy cầm tay.

Một giải pháp được đề xuất là cài đặt phần cứng hoặc phần mềm nhúng trên thiết bị cầm tay, ví dụ phần mềm sử dụng kỹ thuật định vị bằng cách tính toán Chênh lệch thời gian quan sát nâng cao (E-OTD). Qua khảo sát, nghiên cứu, sẽ nhận thấy phương pháp này không đạt được bước tiến đáng $\mathrm { k } \mathring { \mathrm { e } }$ , do khó có thể thuyết phục các nhà sản xuất điện thoại di động khác nhau hợp tác trên một cơ chế chung và chi phí sản xuất điện thoại di động sẽ tăng cao. Một khó khăn khác là phải giải quyết vấn đề kỹ thuật của các thiết bị cầm tay nước ngoài đang chuyển vùng trong mạng của nhà cung

# 2.3 Kỹ thuật định vị dựa trên SIM

Sử dụng mô-đun nhận dạng thuê bao di động (SIM) trong thiết bị cầm tay GSM và UMTS, có thể thu được các phép đo vô tuyến thô từ thiết bị cầm tay. Các phép đo khả dụng bao $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ : Cell-ID đang phục vụ, thời gian phản hồi và cường độ



tín hiệu. Loại thông tin thu được qua SIM có thể khác với loại thông tin có sẵn từ điện thoại. Ví dụ: có thể không trực tiếp lấy được bất kỳ phép đo thô nào từ thiết bị cầm tay nhưng vẫn nhận được các phép đo thông qua SIM.

# 2.4 Kỹ thuật định vị dựa trên Wi-Fi

Dữ liệu Wi-Fi từ nguồn dữ liệu Wifi cộng đồng cũng có thể được sử dụng để xác định vị trí của thiết bị cầm tay. Hiệu suất kém của các kỹ thuật định vị dựa trên GPS trong môi trường trong nhà (do tín hiệu thu GPS từ vệ tinh sẽ yếu, không đủ cả ba vệ tinh cần thiết hoặc không thể thu được khi thiết bị cầm tay có gắn GPS ở trong nhà) và sự phổ biến ngày càng tăng của Wi-Fi đã khuyến khích các viện nghiên cứu, các công ty thiết kế các phương pháp mới và khả thi để thực hiện định vị điện thoại di động hoặc thiết bị di động trong nhà dựa trên Wi-Fi.

Hầu hết các điện thoại thông minh đều tích hợp modul lấy dữ liệu từ Hệ thống vệ tinh dẫn đường toàn cầu (GNSS), chẳng hạn như GPS của Mỹ, GLONASS của Nga, Galileo của Châu Âu, Beidou của Trung Quốc với hệ thống định vị Wifi.

# 2.5 Nguyên lý kỹ thuật lai ghép (hỗn hợp)

Hệ thống định vị lai ghép sử dụng kết hợp các kỹ thuật dựa trên mạng và dựa trên thiết bị cầm tay để xác định vị trí. Một ví dụ là phương pháp sử dụng một số chế độ của GPS có hỗ trợ (A-GPS), có thể sử dụng cả dữ liệu GPS và thông tin mạng để tính toán vị trí của thiết bị cầm tay. Cả hai loại dữ liệu này đều được điện thoại sử dụng để làm cho vị trí chính xác hơn (tức là kỹ thuật A-GPS). Ngoài ra, kỹ thuật định vị lai ghép bằng cách theo dõi cả hai hệ thống cũng có thể thực hiện bằng cách để điện thoại thu được vị trí GPS của nó trực tiếp từ vệ tinh, sau đó nó gửi thông tin qua mạng tới người đang muốn xác định vị trí của điện thoại.

Các hệ thống sử dụng kỹ thuật định vị lai ghép điển hình bao $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ : dịch vụ định vị của Google Maps, kỹ thuật OTDoA và E-CellID của mạng 4G-LTE. Ngoài ra còn có các hệ thống định vị kết hợp một số phương pháp tiếp cận/xác định vị trí khác nhau để định vị thiết bị di động bằng Wi-Fi, WiMAX, GSM, 4G-LTE, địa chỉ IP và dữ liệu môi trường mạng, trong đó có dữ liệu đa phương tiện mà thiết bị di động đã và đang sử dụng trên môi trường mạng đó.



Phương pháp định vị này có thể được gọi là phương pháp lai ghép tiên tiến, nó kết hợp được cả các dịch vụ định vị dựa trên vị trí thông thường (LBS) và dịch vụ định vị dựa trên đa phương tiện của vị trí (LBM).

# 2.6 Tổng hợp các kỹ thuật định vị

Trong bảng dưới đây, luận án tổng hợp một số nguyên lý kỹ thuật, thuật toán định vị khả dụng làm cơ sở tính toán, lựa chọn giải pháp kỹ thuật định vị theo mục tiêu đặt ra. Bảng tổng hợp này được tham khảo từ các nguồn tài liệu [23-45].

Bảng 1. 1. Tổng hợp các kỹ thuật định vị di động   

<table><tr><td rowspan=1 colspan=1>TT</td><td rowspan=1 colspan=1>Ky thuat</td><td rowspan=1 colspan=1>Mo ta/Dinh nghia/Khai niém</td><td rowspan=1 colspan=1>Thuat toan/ Cong thuctinh toan co ban</td></tr><tr><td rowspan=1 colspan=4>1.    Dura tren mang</td></tr><tr><td rowspan=1 colspan=4>Dinh vi dua tren thong tin tinh toan cua mang di dong</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Multilateration(MLAT)</td><td rowspan=1 colspan=1>Ky thuat do da phuong hay congoi la ky thuat dinh vi hyperbolic,la ky thuat tinh toan vi tri cua thiétbi trén co so do thoi gian dén(ToA) thiét bi cua sóng vo tuyénduoc phat tur nhiéu tram góc.Do da biét dang sóng, tóc do vadia diém cac tram góc, nén sé tinhduoc vi tri cua thiét bi can dinh vi.</td><td rowspan=1 colspan=1>ToAs (thoi diém dén) =ToFs (thoi gian bay) +ToT (thoi diém phat).</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>Triangulation</td><td rowspan=1 colspan=1>Ky thuat do tam giac dé tinh toanvi tri cua thiét bi bang cach ve cacduong cät thanh hinh tam giac turcac diém phat song da biet (cacBTS/eNB) dén thiét bi (con goi laky thuat do tam giac duong xuongtien tien).</td><td rowspan=1 colspan=1>Cac thuat toan tinh toantam giac dac.</td></tr></table>



<table><tr><td colspan="4">II. Dura trén may cam tay</td></tr><tr><td></td><td>dong).</td><td>Dinh vi dua trén phan mém khach cai dät trén may cam tay, vi du phän mém irng dung vi tri GPS trén may dien thoai thong minh Ky thuat nay xac dinh vi tri cua thiét bi cam tay boi cac tham só nhän dang té bao Cell-ID cua mang di dong phuc vu nó, cuong d  tin hiéu cua cac té bao nha va lan can, lien tuc duoc giri dén nha cung cap dich vu. Mot cach tiép cän khac la dua trén “däu van tay&quot;, trong dó “chur ky&quot; cua Cell nha va Cell lan cän bao hiéu cuong d@ tin hieu tai diém quan tam khac nhau, duoc ghi lai va khop voi thoi gian thuc dé tinh toan vi tri cua may cam tay. (Phuong phap nay doc lap voi nha cung cap dich vu, thuong duoc sur dung trong cac thiét bi dinh vi co</td><td>- Cac thuat toan tinh toan toa d@ dia ly tren co so tin hiéu GPS tir vé tinh dén may cam tay. - Thuat toan tinh chénh léch thoi gian quan sat nang cao E-OTD. Thuat toän tinh chénh léch thoi gian dén cua duong len U-TDoA.</td></tr></table>

# III. Dựa trên SIM



<table><tr><td rowspan=1 colspan=4>IV.Dua tren Wifi</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1> Xac dinh vi tri cua thiet bi cam taybang cach lay du lieu Wi-Finguon cong dong</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Signalstrengthbased(AP-RSSI)</td><td rowspan=1 colspan=1> Ky thuat ghi lai cuong d tin hieuRSSI tur mot só diém truy captrong pham vi may cam tay détinh toan vi tri may cam tay.</td><td rowspan=1 colspan=1>Su dung cac thuat toando tam giac nhu mó ta ótren.</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>Fingerprintingbased</td><td rowspan=1 colspan=1>Ky thuat ghi lai cuong do tin hieuRSSI tir mot só diém truy cap vaoco so du lieu, lay mot toa do dabiét cua thiét bi khach trong giaidoan ngoai tuyén, uoc tinh dugcvi tri gan dung nhat khi nó tructuyén.</td><td rowspan=1 colspan=1>Cac thuat toan do tam giac va cac thuat toanuoc luong.</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>Angle of arrivalbased (AoA)</td><td rowspan=1 colspan=1>Ky thuat uoc tinh goc dén(AoA) cua tin hieu da duongnhan duoc tai cac mang ang-ten trong cac diém truy cap va apdung phuong phap do tam giac détinh toan vi tri cüa cac thiét bikhach.</td><td rowspan=1 colspan=1>Thuat toan Music.</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>Time of flightbased (ToF)</td><td rowspan=1 colspan=1>Ky thuat lay dau thoi gian duoccung cap boi cac giao dien khongday dé tinh toan ToF cua tin hieu va sau dó sur dung thong tin naydé uóc tinh khoang cach va vi trituong doi cua mot thiét bi khachdoi voi cac diém truy cap.</td><td rowspan=1 colspan=1>- Thuat toan do tam giac- Thuat toan do thoi gian</td></tr><tr><td rowspan=1 colspan=4>V.Lai ghép tien tién</td></tr></table>



<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>A-GNSS(A-GPS)</td><td rowspan=1 colspan=1>Ky thuat dinh vi toan cäu có hótrg, dé tinh toan vi tri may cam taytr cä thong tin toa d@ GPS vathong tin mang (dien thoai c6dugc vi tri GPS cua nó truc tiéptr vé tinh va sau dó gii thong tinqua mang toi nguoi dang dinh vidien thoai do).</td><td rowspan=1 colspan=1>-Thuat toan cua GoogleMaps.-Thuat toan OTDoA vaE-CellID cua mang 4GLTE.</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>Két hop</td><td rowspan=1 colspan=1>Ky thuat két hop mót só phuongphap tiép cän vi tri khac nhau dédinh vi thiét bi di dong bang Wi-Fi, WiMAX,GSM,LTE,dia chiIP va du lieu moi truong mang.</td><td rowspan=1 colspan=1>Nhiéu thuat toan cua cacky thuat trén két hop voi nhau dé dinh vi hoac dungmoi thuat toan tuy theo durlieu vao kha dung.</td></tr></table>
