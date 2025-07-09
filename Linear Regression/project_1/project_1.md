# Dự án 1: Phân tích Thị trường Lao động Ngành Dữ liệu & AI

## 1. Bối cảnh dự án (Project Context)

Trong bối cảnh cuộc cách mạng công nghiệp 4.0, lĩnh vực Khoa học Dữ liệu và Trí tuệ Nhân tạo (AI) đang phát triển với tốc độ vũ bão, trở thành động lực cốt lõi cho sự đổi mới ở mọi ngành nghề. Thị trường lao động cho các vị trí này không chỉ sôi động mà còn mang tính toàn cầu, với sự gia tăng của các mô hình làm việc từ xa và linh hoạt.

Dự án này thực hiện phân tích dựa trên một bộ dữ liệu tuyển dụng toàn cầu được thu thập trong giai đoạn 2024-2025, nhằm cung cấp một bức tranh toàn cảnh và chi tiết về xu hướng việc làm, mức lương, và các kỹ năng quan trọng đang định hình ngành công nghiệp này.

## 2. Mục tiêu phân tích (Objectives)

Báo cáo tập trung vào việc giải quyết các câu hỏi kinh doanh và nhân sự cốt lõi thông qua phân tích dữ liệu:

*   **Phân tích xu hướng thị trường:**
    *   Xác định các chức danh công việc (job titles) có nhu cầu tuyển dụng cao nhất.
    *   Phân tích các "điểm nóng" địa lý (geographic hotspots) và các ngành công nghiệp (industries) đang dẫn đầu trong việc tuyển dụng nhân tài dữ liệu.
    *   Đánh giá xu hướng tuyển dụng theo quy mô công ty (company size).

*   **Phân tích lương và phúc lợi:**
    *   Xây dựng benchmark lương (salary benchmarks) theo vị trí, cấp độ kinh nghiệm, và quốc gia.
    *   Đánh giá tác động của hình thức làm việc từ xa (remote work) đến mức lương.

*   **Phân tích kỹ năng yêu cầu:**
    *   Nhận diện các bộ kỹ năng công nghệ (tech skills) và kỹ năng mềm đang được yêu cầu nhiều nhất.
    *   Phân tích mối tương quan giữa việc sở hữu kỹ năng chuyên biệt và mức lương.

*   **Mô hình dự báo:**
    *   Xây dựng mô hình Hồi quy Tuyến tính (Linear Regression) để dự báo mức lương tiềm năng dựa trên các yếu tố chính như kinh nghiệm, kỹ năng, và vị trí địa lý, cung cấp một công cụ tham khảo giá trị.

## 3. Đối tượng và giá trị của báo cáo (Audience & Value)

Báo cáo này được thiết kế để mang lại giá trị thực tiễn cho nhiều đối tượng khác nhau:

*   **Người tìm việc và Sinh viên:** Cung cấp định hướng nghề nghiệp rõ ràng, lộ trình phát triển kỹ năng và thông tin cần thiết để tối ưu hóa cơ hội việc làm.
*   **Chuyên gia Nhân sự (HR) và Nhà tuyển dụng:** Trang bị dữ liệu để xây dựng chiến lược thu hút nhân tài, thiết kế thang bảng lương cạnh tranh và soạn thảo mô tả công việc hiệu quả.
*   **Lãnh đạo doanh nghiệp:** Cung cấp cái nhìn tổng quan chiến lược về thị trường nhân lực, hỗ trợ việc ra quyết định và đầu tư vào các sáng kiến dữ liệu.
*   **Các cơ sở giáo dục:** Cung cấp thông tin đầu vào để điều chỉnh và cập nhật chương trình đào tạo, đảm bảo phù hợp với nhu_cầu thực tế của ngành.

## 4. Sản phẩm đầu ra dự kiến: Các Dashboards Phân tích

Dự án sẽ cung cấp một bộ các dashboards tương tác, mỗi dashboard tập trung vào một khía cạnh phân tích riêng biệt:

### **Dashboard 1: Tổng quan Toàn cảnh Thị trường (Market Overview)**
- **Mục tiêu:** Cung cấp cái nhìn 360 độ về các xu hướng chính của thị trường.
- **Các Phân Tích Đã Thực Hiện:**
    - **Top 10 Chức danh "Hot" nhất:** Sử dụng biểu đồ cột để xếp hạng các vị trí có nhu cầu tuyển dụng cao nhất.
    - **Top 10 "Điểm nóng" Địa lý:** Phân tích và xếp hạng 10 quốc gia/khu vực có số lượng tin tuyển dụng nhiều nhất.
    - **Phân bổ theo Ngành và Quy mô Công ty:** Trực quan hóa số lượng tin đăng theo từng ngành (`industry`) và quy mô công ty (`S`, `M`, `L`).
- **So Sánh Với Kế Hoạch:**
    - **Hoàn thành:** Đã xác định được các chức danh, điểm nóng địa lý, và xu hướng theo ngành/quy mô.
    - **Điều chỉnh:** Thay vì bản đồ nhiệt, đã sử dụng biểu đồ cột để thể hiện các "điểm nóng" địa lý, tập trung vào top 10. Phân tích cấp độ kinh nghiệm được tích hợp trong các dashboard sau.

### **Dashboard 2: Phân tích Chuyên sâu về Lương & Kỹ năng (Salary & Skills Deep-Dive)**
- **Mục tiêu:** Cung cấp thông tin chi tiết về các yếu tố ảnh hưởng đến lương và các kỹ năng có giá trị cao.
- **Các Phân Tích Đã Thực Hiện:**
    - **Tương quan Lương và Kinh nghiệm:** Biểu đồ phân tán và hồi quy tuyến tính cho thấy mức lương tăng rõ rệt theo số năm kinh nghiệm.
    - **Benchmark Lương theo Chức danh:** Biểu đồ cột so sánh mức lương trung vị giữa các `job_title`.
    - **Tác động của Quy mô Công ty và Mô hình làm việc:** Phân tích lương trung bình theo `company_size` và `remote_ratio`.
    - **Phân tích Kỹ năng "Vàng":**
        - Xác định **Top 10 kỹ năng được yêu cầu nhiều nhất** cho từng chức danh.
        - Phân tích và xếp hạng **Top 10 kỹ năng được trả lương cao nhất**.
- **So Sánh Với Kế Hoạch:**
    - **Hoàn thành:** Đã thực hiện phần lớn các mục tiêu, bao gồm benchmark lương theo vị trí, kinh nghiệm, và tác động của remote work.
    - **Tích hợp:** Phân tích kỹ năng (vốn thuộc D3 trong kế hoạch gốc) đã được tích hợp vào đây để tạo một cái nhìn toàn diện hơn về "giá trị" của một ứng viên.

### **Dashboard 3: Phân Tích Vòng Đời Tuyển Dụng & Học Vấn (Recruitment Lifecycle & Education Analysis)**
- **Mục tiêu:** Cung cấp insight về hiệu quả quy trình tuyển dụng và giá trị của học vấn.
- **Các Phân Tích Đã Thực Hiện:**
  - **Phân tích Thời gian Tuyển dụng (Time-to-Fill):**
    - Tính toán và trực quan hóa thời gian từ lúc đăng tin đến hạn chót (`recruitment_days`).
    - Sử dụng Histogram và Heatmap để phân tích thời gian tuyển dụng trung bình theo ngành và quy mô công ty.
  - **Phân tích Xu hướng Tuyển dụng theo Mùa:** Biểu đồ cột tương tác thể hiện số lượng công việc đăng theo tháng/quý/năm, giúp xác định "thời điểm vàng" để ứng tuyển hoặc tuyển dụng.
  - **Phân tích Tỷ suất Hoàn vốn (ROI) của Bằng cấp:** So sánh phân phối lương theo các cấp độ học vấn (`education_required`) ở các cấp bậc kinh nghiệm khác nhau.
- **So Sánh Với Kế Hoạch:**
    - **Hoàn thành (với sự điều chỉnh):** Nội dung này được phát triển sâu hơn trong quá trình phân tích, thay thế cho kế hoạch ban đầu về Dashboard 3 (chỉ tập trung vào kỹ năng). Nó cung cấp những insight độc đáo về quy trình và giá trị học vấn.

### **Phần 4: Xây Dựng Mô Hình Dự Báo Lương (Salary Prediction Model)**

#### **1. Xây Dựng Mô Hình Hồi quy Tuyến tính**
- **Mục tiêu:** Xây dựng một mô hình Machine Learning có khả năng dự đoán mức lương (`salary_usd`) dựa trên các thuộc tính của công việc.
- **Phương pháp:**
  - **Tiền xử lý:** Sử dụng kỹ thuật One-Hot Encoding để chuyển đổi các biến phân loại (categorical) thành dạng số mà mô hình có thể hiểu được.
  - **Huấn luyện:** Chia dữ liệu thành tập huấn luyện và tập kiểm tra, sau đó huấn luyện mô hình Hồi quy Tuyến tính (`Linear Regression`).

#### **2. Đánh Giá Hiệu Suất Mô Hình**
- **Mục tiêu:** Đo lường độ chính xác và mức độ hiệu quả của mô hình dự báo.
- **Các chỉ số đánh giá:**
  - **R-squared (R²):** Tỷ lệ phương sai trong biến phụ thuộc (lương) có thể được dự đoán từ các biến độc lập.
  - **Mean Absolute Error (MAE):** Sai số tuyệt đối trung bình - cho biết trung bình mô hình dự đoán sai lệch bao nhiêu USD.
  - **Mean Squared Error (MSE) & Root Mean Squared Error (RMSE):** Đo lường sai số trung bình bình phương, với RMSE có cùng đơn vị với biến mục tiêu (USD).
- **Trực quan hóa:** Sử dụng biểu đồ Scatter Plot để so sánh mức lương thực tế và mức lương do mô hình dự đoán.
