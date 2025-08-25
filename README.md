# 🍄 Ứng dụng Web Phân loại Nấm bằng ID3 và Flask

Trong dự án này, chúng ta sẽ xây dựng một ứng dụng web có khả năng phân loại nấm thành hai nhóm: **ăn được** và **không ăn được**. Ứng dụng sử dụng bộ dữ liệu Mushroom từ UCI Machine Learning Repository, áp dụng thuật toán **ID3 Decision Tree** để huấn luyện mô hình, và triển khai giao diện web bằng **Flask** để người dùng có thể nhập đặc điểm của cây nấm và nhận kết quả dự đoán.

## 1. Ý tưởng và mục tiêu
Nấm là một loại thực phẩm phổ biến nhưng cũng tiềm ẩn nguy cơ ngộ độc nếu ăn phải loại độc. Việc phân loại nấm dựa trên đặc điểm hình thái có thể giúp giảm rủi ro. Thay vì phải nhớ hàng loạt đặc điểm phức tạp, ứng dụng này cho phép người dùng chọn các đặc điểm từ danh sách và hệ thống sẽ dự đoán kết quả dựa trên mô hình đã học.

## 2. Dữ liệu và thuật toán
Bộ dữ liệu Mushroom chứa các mẫu nấm với nhiều thuộc tính như hình dạng mũ, màu mũ, mùi, màu phiến, môi trường sống… Mỗi mẫu được gán nhãn là **e** (edible – ăn được) hoặc **p** (poisonous – độc).

Thuật toán được sử dụng là **ID3** – một thuật toán xây dựng cây quyết định dựa trên:
- **Entropy**: đo độ hỗn loạn của tập dữ liệu.
- **Information Gain**: chọn thuộc tính giúp giảm entropy nhiều nhất để phân chia.
- **Đệ quy**: tiếp tục phân chia cho đến khi tất cả mẫu trong một nút thuộc cùng một lớp hoặc không còn thuộc tính để phân chia.

## 3. Huấn luyện mô hình
Quy trình huấn luyện gồm:
1. Đọc dữ liệu từ file `mushrooms.csv`.
2. Tách dữ liệu thành tập huấn luyện và tập kiểm tra.
3. Xây dựng cây quyết định bằng hàm `id3()` tự cài đặt.
4. Đánh giá mô hình bằng độ chính xác, ma trận nhầm lẫn và báo cáo phân loại.
5. Lưu cây quyết định đã huấn luyện vào file `mushroom_model.pkl` bằng `pickle` để tái sử dụng.

## 4. Xây dựng ứng dụng web với Flask
Ứng dụng Flask sẽ:
- Tải mô hình đã lưu từ file `.pkl`.
- Cung cấp một trang web với form gồm các trường `<select>` cho từng đặc điểm nấm.
- Khi người dùng chọn xong và bấm **Dự đoán**, dữ liệu sẽ được gửi lên server, chuyển thành dictionary và đưa vào hàm `predict()` để lấy kết quả.
- Kết quả hiển thị ngay trên trang, với màu xanh lá nếu nấm ăn được và màu đỏ nếu nấm độc.
- Form được thiết kế để **giữ nguyên lựa chọn** sau khi dự đoán, giúp người dùng chỉnh sửa nhanh. Ngoài ra có nút **Reset** để đưa form về trạng thái ban đầu.

## 5. Giao diện và trải nghiệm người dùng
Giao diện được thiết kế gọn gàng:
- Các trường chọn được bố trí ngang hàng khi màn hình rộng, tự xuống hàng khi màn hình hẹp.
- Nút **Dự đoán** màu xanh lá nổi bật, nút **Reset** màu xám nhạt.
- Kết quả hiển thị rõ ràng, dễ phân biệt bằng màu nền và biểu tượng.

## 6. Ảnh DEMO
<img width="1338" height="262" alt="image" src="https://github.com/user-attachments/assets/d7c5eb00-4571-46c4-92ce-0b5c6e88de3d" />
<img width="1346" height="339" alt="image" src="https://github.com/user-attachments/assets/d1794df6-64ff-4169-92cf-d6b528d13039" />
<img width="1348" height="341" alt="image" src="https://github.com/user-attachments/assets/9ec18335-1ae0-4ffc-afb1-97415052bce9" />
