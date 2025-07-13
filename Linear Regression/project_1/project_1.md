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

---

## 4. Mô hình Dự báo và Ứng dụng Web

### Giới thiệu dự án

Thay vì chỉ dừng lại ở việc phân tích, dự án đã được phát triển thành một sản phẩm hoàn chỉnh: một **ứng dụng web dự đoán lương**. Mục tiêu là cung cấp một công cụ tương tác, cho phép người dùng nhập thông tin chi tiết về một công việc và nhận lại mức lương dự đoán gần như ngay lập tức.

Sản phẩm cuối cùng bao gồm hai thành phần chính:
-   **Backend API:** Một dịch vụ web mạnh mẽ được xây dựng bằng **FastAPI**, chịu trách nhiệm thực hiện các dự đoán.
-   **Frontend:** Một giao diện người dùng đơn giản, trực quan được xây dựng bằng **HTML, CSS, và JavaScript**.

### Miêu tả dự án

Kiến trúc của dự án đã được tái cấu trúc hoàn toàn để phục vụ cho việc triển khai và sử dụng trong thực tế.

#### **A. Pipeline Xử lý Dữ liệu và Huấn luyện (Backend)**

Trái tim của dự án là một **`scikit-learn Pipeline`** được đóng gói và lưu vào tệp `salary_prediction_pipeline.joblib`. Pipeline này là một dây chuyền tự động, thực hiện toàn bộ các bước từ xử lý dữ liệu thô đến đưa ra dự đoán.

**Các bước chính trong Pipeline:**
1.  **Xử lý Ngày tháng (`DateFeatureExtractor`):** Tự động tách cột `posting_date` thành các đặc trưng ngày, tháng, năm và xử lý các giá trị thiếu bằng `KNNImputer`.
2.  **Kỹ thuật Đặc trưng Kỹ năng (`SkillFeatureTransformer`):** Phân tích chuỗi `required_skills`, đếm số lượng kỹ năng nằm trong top phổ biến và top lương cao (đã học được từ dữ liệu huấn luyện).
3.  **Tiền xử lý song song (`ColumnTransformer`):** Áp dụng các phép biến đổi phù hợp cho từng nhóm cột:
    -   **Encoding:** Sử dụng `TargetEncoder` cho các cột có nhiều danh mục (như `job_title`), `OneHotEncoder` và `OrdinalEncoder` cho các cột còn lại.
    -   **Imputation:** Điền các giá trị thiếu bằng `SimpleImputer` (chiến lược `median` hoặc `most_frequent`).
    -   **Scaling:** Chuẩn hóa các đặc trưng số bằng `StandardScaler`.
4.  **Mô hình Dự báo:** Sử dụng một mô hình `XGBRegressor` đã được tinh chỉnh để đưa ra dự đoán cuối cùng.

Toàn bộ logic này được định nghĩa trong `build_pipeline.py` và `feature_engineering.py`.

#### **B. API Server (Backend)**

Dịch vụ API được xây dựng bằng **FastAPI** trong tệp `api.py`.
-   **Xác thực đầu vào:** Sử dụng **Pydantic** để định nghĩa một `schema` nghiêm ngặt, đảm bảo dữ liệu người dùng gửi lên luôn đúng định dạng. API cũng được thiết kế để chấp nhận một vài trường có thể để trống (ví dụ: `required_skills`, `industry`).
-   **Endpoint `/predict`:** Nhận dữ liệu JSON từ người dùng, chuyển đổi nó thành một `DataFrame`, đưa vào pipeline đã tải và trả về kết quả dự đoán.
-   **Hiệu năng:** Pipeline `.joblib` chỉ được tải một lần duy nhất khi API khởi động, đảm bảo thời gian phản hồi cho các dự đoán là nhanh nhất.

#### **C. Giao diện Người dùng (Frontend)**

Một giao diện web đơn giản được đặt trong thư mục `/frontend`, bao gồm:
-   `index.html`: Cung cấp form nhập liệu cho người dùng.
-   `styles.css`: Tạo kiểu dáng hiện đại, dễ sử dụng.
-   `script.js`: "Bộ não" của frontend, chịu trách nhiệm thu thập dữ liệu từ form, gọi đến Backend API bằng `fetch`, nhận kết quả và hiển thị cho người dùng.

### Cách sử dụng

Để chạy toàn bộ ứng dụng, bạn cần thực hiện các bước sau:

#### **1. Chuẩn bị Môi trường**
Mở terminal và cài đặt tất cả các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

#### **2. Xây dựng "Bộ não" (Chỉ chạy một lần)**
Nếu tệp `salary_prediction_pipeline.joblib` chưa tồn tại, hãy chạy kịch bản sau để huấn luyện và lưu lại pipeline:
```bash
python build_pipeline.py
```
*Lưu ý: Bước này có thể mất một vài phút.*

#### **3. Chạy Backend API**
Trong terminal, khởi động máy chủ API:
```bash
uvicorn api:app --reload
```
Để cửa sổ terminal này chạy. API của bạn giờ đang hoạt động tại `http://127.0.0.1:8000`.

#### **4. Chạy Frontend**
1.  Mở File Explorer và điều hướng đến thư mục `frontend` của dự án.
2.  Nháy đúp chuột vào tệp `index.html` để mở nó bằng trình duyệt web.

Bây giờ bạn có thể nhập thông tin vào form trên trang web và nhấn "Predict Salary" để nhận kết quả từ mô hình của mình.
