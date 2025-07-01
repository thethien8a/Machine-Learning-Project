# Tóm tắt Dự án: Phân tích Thị trường Lao động Ngành Dữ liệu & AI

## 1. Bối cảnh dự án
Dự án này phân tích thị trường lao động Khoa học Dữ liệu và Trí tuệ Nhân tạo (AI) toàn cầu trong giai đoạn 2024-2025, nhằm cung cấp cái nhìn tổng quan về xu hướng việc làm, mức lương và các kỹ năng quan trọng.

## 2. Mục tiêu phân tích
*   **Phân tích xu hướng thị trường:** Xác định các chức danh công việc, điểm nóng địa lý, ngành công nghiệp và quy mô công ty có nhu cầu tuyển dụng cao.
*   **Phân tích lương và phúc lợi:** Xây dựng benchmark lương theo vị trí, cấp độ kinh nghiệm, quốc gia và đánh giá tác động của làm việc từ xa đến mức lương.
*   **Phân tích kỹ năng yêu cầu:** Nhận diện các kỹ năng công nghệ và kỹ năng mềm được yêu cầu nhiều nhất, cũng như mối tương quan giữa kỹ năng chuyên biệt và mức lương.
*   **Mô hình dự báo:** Xây dựng mô hình Hồi quy Tuyến tính để dự báo mức lương tiềm năng.

## 3. Đối tượng và giá trị của báo cáo
Báo cáo này hữu ích cho:
*   **Người tìm việc và Sinh viên:** Định hướng nghề nghiệp, lộ trình phát triển kỹ năng.
*   **Chuyên gia Nhân sự (HR) và Nhà tuyển dụng:** Xây dựng chiến lược thu hút nhân tài, thiết kế thang bảng lương.
*   **Lãnh đạo doanh nghiệp:** Cái nhìn tổng quan chiến lược về thị trường nhân lực.
*   **Các cơ sở giáo dục:** Điều chỉnh chương trình đào tạo phù hợp với nhu cầu ngành.

## 4. Sản phẩm đầu ra dự kiến: Các Dashboards Phân tích
Dự án sẽ cung cấp 4 dashboards tương tác:
*   **Dashboard 1: Tổng quan Toàn cảnh Thị trường**
*   **Dashboard 2: Phân tích Chuyên sâu về Lương**
*   **Dashboard 3: Phân tích Kỹ năng và Yêu cầu**
*   **Dashboard 4: Công cụ Dự báo Lương Tương tác**

## 5. Thông tin về Tập dữ liệu "Global AI Job Market & Salary Trends 2025" (Kaggle)
*   **Nguồn:** https://www.kaggle.com/datasets/bismasajjad/global-ai-job-market-and-salary-trends-2025
*   **Tổng quan:** Chứa thông tin chi tiết về các vị trí công việc AI và học máy, mức lương và xu hướng thị trường trên toàn cầu. Bao gồm hơn 15.000 danh sách việc làm thực tế từ hơn 50 quốc gia, được thu thập từ tháng 1 năm 2024 đến tháng 5 năm 2025. Dữ liệu được cập nhật hàng tháng và đã được xác minh, chuẩn hóa thủ công.
*   **Các cột dữ liệu chính:**
    *   `job_id`: Mã định danh duy nhất.
    *   `job_title`: Chức danh công việc chuẩn hóa.
    *   `salary_usd`: Mức lương hàng năm bằng USD (đã chuẩn hóa).
    *   `salary_currency`: Tiền tệ gốc của mức lương.
    *   `experience_level`: Cấp độ kinh nghiệm (EN, MI, SE, EX).
    *   `employment_type`: Loại hình việc làm (FT, PT, CT, FL).
    *   `job_category`: Danh mục công việc.
    *   `company_location`: Quốc gia của công ty.
    *   `company_size`: Quy mô công ty (S, M, L).
    *   `employee_residence`: Quốc gia cư trú của nhân viên.
    *   `remote_ratio`: Tỷ lệ làm việc từ xa (0, 50, 100).
    *   `required_skills`: 5 kỹ năng bắt buộc hàng đầu (phân tách bằng dấu phẩy).
    *   `education_required`: Yêu cầu học vấn tối thiểu.
    *   `years_experience`: Số năm kinh nghiệm yêu cầu.
    *   `industry`: Lĩnh vực công nghiệp.
    *   `posting_date`: Ngày đăng việc làm.
    *   `application_deadline`: Hạn chót nộp đơn.
    *   `job_description_length`: Độ dài mô tả công việc.
    *   `benefits_score`: Điểm số gói phúc lợi (1-10).