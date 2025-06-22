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

#### **Dashboard 1: Tổng quan Toàn cảnh Thị trường (Market Overview)**
*   **Mục tiêu:** Cung cấp cái nhìn 360 độ về thị trường cho các nhà quản lý và lãnh đạo.
*   **Các thành phần chính:**
    *   **Bản đồ nhiệt tuyển dụng toàn cầu:** Hiển thị các quốc gia "điểm nóng" về nhu cầu nhân lực AI/Data.
    *   **Biểu đồ Top 10 chức danh "hot" nhất:** Xếp hạng các vai trò được tìm kiếm nhiều nhất.
    *   **Phân bổ cấp độ kinh nghiệm:** Tỷ lệ tuyển dụng theo các cấp bậc (Entry, Mid, Senior, Executive).
    *   **Biểu đồ xu hướng tuyển dụng theo thời gian:** Theo dõi sự phát triển của thị trường qua các tháng/quý.

#### **Dashboard 2: Phân tích Chuyên sâu về Lương (Salary Deep-Dive)**
*   **Mục tiêu:** Cung cấp thông tin chi tiết về các yếu tố ảnh hưởng đến lương cho người lao động và bộ phận nhân sự.
*   **Các thành phần chính:**
    *   **Biểu đồ hộp (Box Plot) so sánh lương:** Theo chức danh, cấp độ kinh nghiệm và quốc gia.
    *   **Phân tích tác động của làm việc từ xa (remote work) đến lương.**
    *   **So sánh mức lương trung bình giữa các ngành (industries).**

#### **Dashboard 3: Phân tích Kỹ năng và Yêu cầu (Skills & Requirements)**
*   **Mục tiêu:** Hướng dẫn sinh viên và người đi làm về các kỹ năng cần thiết để phát triển sự nghiệp.
*   **Các thành phần chính:**
    *   **Đám mây từ (Word Cloud) về các kỹ năng hàng đầu:** Hiển thị các công nghệ và kỹ năng được yêu cầu nhiều nhất.
    *   **Biểu đồ phân tán (Scatter Plot) về tương quan giữa số năm kinh nghiệm và lương.**
    *   **Phân tích yêu cầu về học vấn (education) cho các vị trí khác nhau.**

#### **Dashboard 4: Công cụ Dự báo Lương Tương tác (Interactive Salary Predictor)**
*   **Mục tiêu:** Tích hợp mô hình hồi quy tuyến tính để cung cấp một công cụ tham khảo thực tiễn.
*   **Các thành phần chính:**
    *   **Các bộ lọc tương tác:** Cho phép người dùng tùy chọn quốc gia, ngành, cấp độ kinh nghiệm.
    *   **Giao diện nhập liệu:** Người dùng nhập thông tin cá nhân (kinh nghiệm, kỹ năng, v.v.).
    *   **Kết quả dự báo:** Hiển thị mức lương ước tính dựa trên mô hình đã xây dựng.
