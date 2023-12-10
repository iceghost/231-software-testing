== Selenium

Selenium là một công cụ tự động hóa trình duyệt web, được sử dụng để thực hiện
các tác vụ tự động trên các trang web. Nó giúp tự động hóa các thao tác như điều
khiển trình duyệt, nhập liệu, click, kiểm tra và xác nhận dữ liệu trên trang
web.

Selenium có thể thực hiện một số chức năng đáng chú ý sau::

+ `open`: Mở một trang web bằng cách cung cấp URL.

  Ví dụ: `open | https://www.example.com`

+ `click`: Click vào một phần tử trên trang web.

  Ví dụ: `click | id=buttonId`

+ `type`: Nhập liệu vào một trường văn bản hoặc ô nhập liệu.

  Ví dụ: `type | id=username | your_username`

+ `assert`: Kiểm tra xem một điều kiện có đúng hay không. Nếu điều kiện sai, sẽ
  tạo ra một lỗi và dừng quá trình chạy.

  Ví dụ: `assert | id=pageTitle | Expected Page Title`

+ `waitFor`: Chờ đợi cho đến khi một điều kiện cụ thể trở thành đúng trước khi
  tiếp tục thực hiện các bước tiếp theo.

  Ví dụ: `waitFor | id=elementId | 5000`

Selenium thường được sử dụng ở hai dạng:

+ _Selenium IDE_: Người dùng tương tác trực tiếp để tạo ra mã thực thi. Ưu điểm là
  dễ tạo, tạo nhanh hơn, nhưng mức độ kiểm soát kém hơn.
+ _Selenium với Webdriver_: Sử dụng script để mô tả quá trình thực thi. Nhược điểm
  là tạo phức tạp hơn, nhưng mức độ kiểm soát cao.

== Quy trình tạo testcase

Trong bài tập lớn này, nhóm thực hiện các bước sau:

+ Tạo testcase thông qua Selenium IDE (*mức 1*).
+ Lưu file `.side`.
+ Xuất testcase qua các ngôn ngữ scripting.
+ Dọn dẹp script, refactor và tách riêng data ra khỏi code (*mức 2*).

== Kết quả

Source code cho bài tập lớn nằm ở đường link: #link("https://github.com/iceghost/231-software-testing/tree/assignment-3").