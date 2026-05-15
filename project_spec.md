# Project Name
JAPANI

# Concept
AI-powered Japanese communication assistant

# Technical Requirements

TR-01
Platform:
- Website
- Không yêu cầu cài app

TR-02
AI Integration:
- OpenAI GPT-4 API
- Google Gemini Pro API

TR-03
Database:
- PostgreSQL
- MongoDB
- Lưu tài khoản + search history

TR-04
Speed:
- AI phản hồi 5-10s

TR-05
Security:
- Bảo mật thông tin cá nhân

# Sitemap

SN-01 Home
- Công cụ phân tích AI
- Nhập liệu
- Hiển thị kết quả

SN-02 Search History
- Lưu lịch sử
- Lọc
- Xem lại phân tích cũ

SN-03 About Website
- Hero section
- Sứ mệnh
- Giải pháp

SN-04 Language Switcher
- EN/JP

SN-05 User Account
- Đăng nhập Google/Email

# Style Design

SD-01 Logo
- Speech Bubble

SD-02 Visual Theme
- Nhật Bản
- Tối giản hiện đại
- Nhiều khoảng trắng

SD-03 Color Palette
- Navy
- Blue pastel
- White
- Light grey

SD-04 Font
- JP: Noto Sans JP
- EN: Inter

# Content Management

## CM-01 Hệ thống đa ngôn ngữ
- Cho phép thay đổi ngôn ngữ toàn trang ngay lập tức khi người dùng nhấn nút chuyển đổi trên Header

---

## CM-02 Kho dữ liệu 1 Day 1 Fact
- Lưu trữ danh sách các kiến thức văn hóa Nhật Bản ngắn gọn
- Dữ liệu được truy xuất theo lịch trình để hiển thị tại widget trang chủ mỗi ngày
- Tất cả người dùng sẽ nhìn thấy cùng một nội dung trong ngày

---

## CM-03 Kết quả phân tích AI
Quản lý cách định dạng và hiển thị dữ liệu trả về từ AI bao gồm:
- Chỉ số phân tích của 3 tiêu chí
- Đoạn văn giải thích sắc thái
- Danh sách các câu gợi ý viết lại

---

## CM-04 Lưu trữ Search History
Quản lý dữ liệu người dùng đã thực hiện phân tích.

Mỗi bản ghi bao gồm:
- ID người dùng
- Câu gốc
- Bối cảnh đã chọn
- Chỉ số phân tích
- Thời gian thực hiện

Giới hạn:
- Chỉ lưu dữ liệu trong 30 ngày

---

## CM-05 Cấu trúc thông báo lỗi
Quản lý nội dung thông báo khi có lỗi xảy ra.

Ví dụ:
- "Vượt quá 1000 từ"
- "Vui lòng nhập tiếng Nhật"
- "Lỗi kết nối AI"

# Visitor Interaction

---

# 1. Home Section

## VI-01 Văn hóa
Vị trí:
- Left Side

Mặc định:
- Japanese Workplace

---

## VI-02 Lựa chọn quan hệ
Các lựa chọn:
- Boss
- Colleague
- Client
- Friend

---

## VI-03 Lựa chọn mục đích
Sử dụng:
- Radio Buttons

Các mục:
- Convey politely
- Give opinion / proposal
- Make a request
- Say thank you
- Apologize
- Decline

---

## VI-04 1 Day 1 Fact
Chức năng phụ:
- Widget hiển thị kiến thức văn hóa Nhật Bản hằng ngày
- Tự động cập nhật mỗi 24h

---

## VI-05 Input Box
Vị trí:
- Middle

Yêu cầu:
- Nhập văn bản tiếng Nhật
- Giới hạn 1000 từ

---

## VI-06 Analyze Click Button
Chức năng:
- Kích hoạt gọi AI API để xử lý dữ liệu
- Hiển thị hiệu ứng Loading trong lúc chờ phản hồi

---

## VI-07 AI Results Display
Hiển thị:
- Circle Indicator hoặc Progress Bar

Các chỉ số:
- Formality level: 0 - 100%
- Natural level: 0 - 100%
- Relevance in communication context:
  - High
  - Medium
  - Low

---

## VI-08 Overall Evaluation
- Đánh giá tổng thể câu giao tiếp

---

## VI-09 Culture Explanation
- Giải thích văn hóa giao tiếp Nhật Bản
- Chỉ ra lý do câu nói chưa tự nhiên hoặc chưa phù hợp bối cảnh

---

## VI-10 Rewrite Suggestions
- Đề xuất cách viết lại câu tiếng Nhật phù hợp hơn với bối cảnh người dùng đã chọn

---

## VI-11 Learn Related Expressions
Chức năng phụ:
- Đưa ra các cách diễn đạt liên quan khác

---

# 2. Search History Section

## VI-12 Search Keywords
Vị trí:
- Middle

Yêu cầu:
- Mini input box
- Giới hạn 100 chữ

---

## VI-13 Filter by Context
Sử dụng:
- Dropdown menu

Các lựa chọn:
- Boss / Senior
- Colleague / Teammate
- Client / Business Partner
- Friend

---

## VI-14 Sort by Date
Sử dụng:
- Dropdown menu

---

## VI-15 Analysis Cards
Mỗi card hiển thị:
- Câu gốc
- Context
- Analysis Results

---

## VI-16 Card Actions
Các nút:
- View Detail
- Delete

Chi tiết:
- View Detail dẫn tới kết quả phân tích chi tiết của câu đó

---

# 3. About Website Section

## VI-17 Hero Section
Headline:
- "Master Japanese, Use JAPANI now"

Sub-text:
- "Our mission is to help you build true, natural communication through in-depth analysis of culture nuance"

---

## VI-18 Our Solution

### Advanced Context Analysis
- AI phân tích quan hệ, môi trường và sắc thái cảm xúc
- Không chỉ dịch, mà còn hiểu ngữ cảnh

### Unspoken Cultural Rules
- Phân tích quy tắc ngầm trong giao tiếp Nhật Bản
- Bao gồm:
  - Keigo
  - Tone
  - Social protocols

### Smart Learning History
- Lưu trữ và phân tích lịch sử tương tác
- Đưa ra gợi ý học tập cá nhân hóa

---

## VI-19 CTA
Nội dung:
- "Ready to master Japanese?"
- Nút "GET STARTED NOW"

Chức năng:
- Điều hướng trực tiếp về trang Home