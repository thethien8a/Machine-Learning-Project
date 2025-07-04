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
*   **Mục tiêu:** Cung cấp cái nhìn 360 độ về thị trường cho các nhà quản lý và lãnh đạo.
*   **Các thành phần chính:**
    *   **Bản đồ nhiệt tuyển dụng toàn cầu:** Hiển thị các quốc gia "điểm nóng" về nhu cầu nhân lực AI/Data.
    *   **Biểu đồ Top 10 chức danh "hot" nhất:** Xếp hạng các vai trò được tìm kiếm nhiều nhất.
    *   **Phân bổ cấp độ kinh nghiệm:** Tỷ lệ tuyển dụng theo các cấp bậc (Entry, Mid, Senior, Executive).

**Tóm tắt các phân tích đã thực hiện & Insights:**

Dựa trên các mục tiêu trên, các phân tích sau đã được thực hiện trong notebook để cung cấp insight cho ban lãnh đạo:
- **Phân tích Lương & Cấp bậc:** Đã trực quan hóa mối quan hệ giữa cấp bậc kinh nghiệm và mức lương trung bình, cho thấy sự tăng trưởng rõ rệt qua từng cấp bậc, làm cơ sở cho việc xây dựng thang bảng lương.
- **Phân tích Kỹ năng Chuyên sâu:** 
    - Xây dựng bộ lọc tương tác để xem top 10 kỹ năng yêu cầu cho từng chức danh công việc.
    - Xác định top 10 kỹ năng được thị trường trả lương cao nhất, cung cấp insight về "bộ kỹ năng vàng" để định hướng đào tạo.
- **Phân tích Phúc lợi:** Tạo card KPI tương tác để xem nhanh điểm phúc lợi trung bình, có thể lọc theo ngành, vị trí, và cấp bậc.
- **Phân tích Địa lý & Nhân tài:**
    - Xác định top 10 "điểm nóng" nhân tài và phân tích kết hợp giữa số lượng và chi phí lương trung bình tại các điểm đó.
    - Xây dựng bộ lọc để tìm kiếm các chuyên gia theo cấp bậc tại các quốc gia khác nhau.
- **Phân tích Mô hình làm việc (Remote/Hybrid/On-site):**
    - Tạo biểu đồ tương tác để phân tích sự phổ biến của các mô hình làm việc, có thể lọc theo ngành và quy mô công ty.
    - Phân tích chi phí lương trung bình cho từng mô hình làm việc để hỗ trợ ra quyết định về chính sách làm việc.

### **Dashboard 2: Phân tích Chuyên sâu về Lương (Salary Deep-Dive)**
*   **Mục tiêu:** Cung cấp thông tin chi tiết về các yếu tố ảnh hưởng đến lương cho người lao động và bộ phận nhân sự.
*   **Các thành phần chính (đã điều chỉnh theo thực tế triển khai):**
    *   **Biểu đồ phân tán (Scatter Plot) và Hồi quy tuyến tính:** Trực quan hóa mối quan hệ giữa kinh nghiệm và lương.
    *   **Biểu đồ cột tương tác (Interactive Bar Chart):** So sánh lương trung vị theo chức danh, có bộ lọc theo quốc gia.
    *   **Biểu đồ tròn (Pie Chart):** Phân tích tỷ lệ tuyển dụng giữa thị trường trong nước và quốc tế.
    *   **Biểu đồ cột (Bar Chart):** So sánh mức lương trung bình theo quy mô công ty.

**Tóm tắt các phân tích đã thực hiện & Insights:**

Dựa trên các mục tiêu trên, các phân tích sau đã được thực hiện trong notebook để cung cấp insight cho người lao động và bộ phận nhân sự:
- **Phân tích Tương quan Lương và Kinh nghiệm:** Đã trực quan hóa mối quan hệ tuyến tính giữa số năm kinh nghiệm và mức lương, khẳng định kinh nghiệm là yếu tố then chốt quyết định thu nhập. Insight này giúp người lao động đặt mục tiêu thăng tiến và HR xây dựng khung lương dựa trên kinh nghiệm.
- **So sánh Lương theo Chức danh:** Sử dụng biểu đồ cột tương tác để so sánh mức lương trung vị giữa các chức danh khác nhau. Người dùng có thể lọc theo quốc gia, giúp người lao động hiểu rõ giá trị của từng vai trò trên thị trường và HR định giá vị trí chính xác.
- **Phân tích Thị trường Lao động Nội địa vs. Quốc tế:** Biểu đồ tròn đã cho thấy tỷ lệ tuyển dụng giữa các công ty trong nước và quốc tế. Insight này giúp người lao động định vị chiến lược tìm việc (tập trung vào thị trường nào) và giúp các công ty trong nước hiểu rõ mức độ cạnh tranh từ các công ty nước ngoài.
- **Tác động của Quy mô Công ty đến Lương:** Phân tích mức lương trung bình theo quy mô công ty, cung cấp cho người tìm việc cái nhìn về việc nên chọn công ty lớn hay nhỏ để tối ưu hóa thu nhập.

### **Dashboard 3: Phân Tích Vòng Đời Tuyển Dụng & Học Vấn (Recruitment Lifecycle & Education Analysis)**
*   **Mục tiêu:** Cung cấp insight cho bộ phận nhân sự về hiệu quả quy trình tuyển dụng và cho người lao động/sinh viên về giá trị của học vấn.
*   **Các thành phần chính:**
    *   **Phân tích thời gian tuyển dụng (Time-to-Fill):**
        *   Tính toán khoảng thời gian từ `posting_date` đến `application_deadline`.
        *   Trực quan hóa thời gian tuyển dụng trung bình theo ngành (`industry`) và quy mô công ty (`company_size`) để HR xác định các "điểm nghẽn" trong quy trình.
    *   **Phân tích xu hướng tuyển dụng theo mùa:**
        *   Biểu đồ thể hiện số lượng công việc được đăng tuyển theo từng tháng/quý, giúp doanh nghiệp lên kế hoạch nhân sự và người tìm việc chọn "thời điểm vàng" để ứng tuyển.
    *   **Phân tích ROI của Bằng Cấp (Education ROI):**
        *   So sánh mức lương trung vị (`salary_usd`) giữa các cấp độ học vấn (`education_required`: Bachelor, Master, PhD) cho cùng một cấp bậc kinh nghiệm (`experience_level`).
        *   Phân tích mức độ yêu cầu học vấn phổ biến cho từng chức danh (`job_title`).
