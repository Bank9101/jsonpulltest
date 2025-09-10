# 🇹🇭 OTOP Thailand - ระบบค้นหาผลิตภัณฑ์ OTOP

> **แพลตฟอร์มเว็บแอปพลิเคชันสำหรับค้นหาและสำรวจผลิตภัณฑ์ OTOP (หนึ่งตำบลหนึ่งผลิตภัณฑ์) ทั่วประเทศไทย พร้อมระบบแผนที่แบบโต้ตอบ**

---

## 📖 เกี่ยวกับโครงการ

**OTOP Thailand** เป็นเว็บแอปพลิเคชันที่พัฒนาด้วย Django Framework เพื่อเป็นแพลตฟอร์มกลางในการค้นหา สำรวจ และเชื่อมต่อผู้บริโภคกับผลิตภัณฑ์ OTOP คุณภาพสูงจากทุกจังหวัดในประเทศไทย

โครงการนี้มุ่งเน้นการส่งเสริมผลิตภัณฑ์ชุมชนไทยและสนับสนุนเศรษฐกิจฐานรากผ่านเทคโนโลยีดิจิทัลที่ทันสมัยและใช้งานง่าย

---

## ✨ คุณสมบัติเด่น

### 🔍 **ระบบค้นหาอัจฉริยะ**
- 🎯 ค้นหาแบบ Full-text Search ตามชื่อผลิตภัณฑ์ ชื่อร้าน หรือที่อยู่
- 🗺️ กรองผลลัพธ์ตามจังหวัดและอำเภอ (ครอบคลุม 77 จังหวัด)
- 📍 ตัวกรองพิเศษสำหรับสินค้าที่มีพิกัด GPS
- 📄 ระบบแบ่งหน้าที่ปรับตัวได้ (Adaptive Pagination)

### 🗺️ **แผนที่แบบโต้ตอบ Google Maps**
- 📌 แสดงตำแหน่งร้านค้าด้วย Interactive Markers
- 💬 Pop-up แสดงข้อมูลผลิตภัณฑ์เมื่อคลิก
- 🔄 อัปเดตแผนที่แบบเรียลไทม์ตามผลการค้นหา
- 📱 รองรับการควบคุมด้วยการสัมผัสบนมือถือ
- 🎨 สไตล์แผนที่ที่กำหนดเองสำหรับประเทศไทย

### 📱 **ออกแบบตอบสนอง (Responsive Design)**
- 💻 ใช้งานได้อย่างสมบูรณ์บน Desktop, Tablet และ Mobile
- 🎨 UI/UX สไตล์ Modern Dark Theme พร้อม Glassmorphism Effect
- ⚡ ปรับแต่งประสิทธิภาพสำหรับมือถือ
- 👆 Touch-friendly Interface สำหรับ Touch Screen

### 📊 **แดชบอร์ดและสถิติ**
- 📈 แสดงสถิติผลิตภัณฑ์ทั้งหมดในระบบ
- 🌍 จำนวนสินค้าที่มีข้อมูลตำแหน่ง GPS
- 🏪 สถิติร้านค้าและการกระจายตัวตามจังหวัด
- 📱 Real-time Counter แบบ Animated

---

## 📊 ข้อมูลในระบบ

| หมวดหมู่ | จำนวน | รายละเอียด |
|----------|---------|-------------|
| 🛍️ **ผลิตภัณฑ์ทั้งหมด** | **6,387** รายการ | ครอบคลุมผลิตภัณฑ์ OTOP ทุกประเภท |
| 📍 **สินค้าที่มีพิกัด GPS** | **1,505** รายการ | พร้อมแสดงบนแผนที่ |
| 🗺️ **จังหวัดที่ครอบคลุม** | **77** จังหวัด | ทุกจังหวัดในประเทศไทย |
| 🏪 **ข้อมูลร้านค้า** | **Complete** | ชื่อร้าน, ที่อยู่, เบอร์โทร |

---

## 🛠️ เทคโนโลยีที่ใช้

### Backend
- 🐍 **Python 3.6+** - ภาษาหลักของระบบ
- 🚀 **Django Framework** - Web Framework สำหรับ Backend
- 📄 **JSON Data Storage** - จัดเก็บข้อมูลแบบ JSON
- 🔗 **RESTful API** - API สำหรับ Frontend Communication

### Frontend
- 🌐 **HTML5 + CSS3** - โครงสร้างและการตกแต่งหน้าเว็บ
- ⚡ **Vanilla JavaScript** - ฟังก์ชันการทำงานแบบ Interactive
- 🗺️ **Google Maps JavaScript API** - ระบบแผนที่
- 🎨 **Modern CSS (Glassmorphism + Dark Theme)** - การออกแบบทันสมัย

### การออกแบบ
- 📐 **Responsive Web Design** - รองรับทุกขนาดหน้าจอ
- 🌙 **Dark Theme UI** - ลดการเมื่อยล้าของสายตา
- ✨ **Glassmorphism Effects** - เอฟเฟกต์กระจกฝ้าทันสมัย
- 🎭 **Smooth Animations** - การเคลื่อนไหวที่ลื่นไหล

---

## 🚀 การติดตั้งและใช้งาน

### 📋 ความต้องการของระบบ
```
Python >= 3.6
Django >= 3.x
pip (Python Package Manager)
Google Maps API Key (สำหรับฟีเจอร์แผนที่)
Web Browser ที่รองรับ HTML5
```

### 🔧 วิธีการติดตั้ง

#### 1. **Clone โครงการ**
```bash
git clone <repository-url>
cd jsonpulltest
```

#### 2. **ติดตั้ง Dependencies**
```bash
pip install -r requirements.txt
```

#### 3. **ตั้งค่าฐานข้อมูล**
```bash
python manage.py migrate
```

#### 4. **เริ่มต้น Development Server**
```bash
python manage.py runserver
```

#### 5. **เข้าใช้งานเว็บไซต์**
- 🌐 **หน้าหลัก**: http://127.0.0.1:8000/
- ⚙️ **Admin Panel**: http://127.0.0.1:8000/admin/

### 🗂️ โหลดข้อมูล OTOP (ตัวเลือกเพิ่มเติม)
```bash
python manage.py load_otop_data
```

---

## 🗺️ การตั้งค่า Google Maps API

> **⚠️ สำคัญ**: ฟีเจอร์แผนที่จะไม่ทำงานหากไม่มี Google Maps API Key

### 📝 ขั้นตอนการตั้งค่า

#### 1. **สร้าง Google Cloud Project**
- เข้าไปที่ [Google Cloud Console](https://console.cloud.google.com/)
- สร้างโปรเจกต์ใหม่หรือเลือกโปรเจกต์ที่มีอยู่

#### 2. **เปิดใช้งาน APIs**
```
✅ Maps JavaScript API
✅ Places API (ตัวเลือก)
✅ Geocoding API (ตัวเลือก)
```

#### 3. **สร้างและคัดลอก API Key**
- ไปที่ "Credentials" → "Create Credentials" → "API Key"
- คัดลอก API Key ที่ได้

#### 4. **อัปเดต API Key ในโค้ด**
แก้ไขไฟล์ `templates/index.html` (บรรทัดที่ ~1550):
```html
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_ACTUAL_API_KEY&callback=initializeMap" async defer></script>
```

#### 5. **ตั้งค่า API Restrictions (แนะนำ)**
- จำกัด API Key ให้ใช้ได้เฉพาะ Domain ของคุณ
- จำกัดการใช้งาน API เฉพาะที่จำเป็น

---

## 🏗️ โครงสร้างโครงการ

```
jsonpulltest/
├── 📁 jsonpull/                     # Django Project Settings
│   ├── 📄 settings.py              # การตั้งค่าหลัก
│   ├── 📄 urls.py                  # URL Routing หลัก
│   └── 📄 wsgi.py                  # WSGI Configuration
│
├── 📁 jsonpullshow/                 # Main Django App
│   ├── 📄 models.py                # Data Models (สำหรับอนาคต)
│   ├── 📄 views.py                 # Business Logic & API Views
│   ├── 📄 urls.py                  # App URL Patterns
│   ├── 📄 admin.py                 # Admin Interface
│   └── 📁 management/              # Django Commands
│       └── 📁 commands/
│           └── 📄 load_otop_data.py # Data Loading Command
│
├── 📁 templates/                    # HTML Templates
│   └── 📄 index.html               # Main Web Interface
│
├── 📁 staticfiles_build/static/    # Static Files
│   └── 📁 data/
│       └── 📄 otop_data.json       # OTOP Products Database
│
├── 📄 convert_excel_to_json.py     # Data Conversion Utility
├── 📄 manage.py                    # Django Management Script
├── 📄 requirements.txt             # Python Dependencies
└── 📄 README.md                    # โดคิวเมนต์นี้
```

---

## 🔗 API Endpoints

### 🔍 **Search API**
```http
GET /api/search/
```
**Parameters:**
- `q` - คำค้นหา (ชื่อสินค้า, ร้าน, ที่อยู่)
- `province` - ชื่อจังหวัด
- `district` - ชื่ออำเภอ
- `coords` - กรองเฉพาะสินค้าที่มี GPS (`true`/`false`)
- `page` - หน้าที่ต้องการ
- `per_page` - จำนวนรายการต่อหน้า

**Response:**
```json
{
  "results": [...],
  "total": 1505,
  "page": 1,
  "per_page": 20,
  "total_pages": 76
}
```

### 🗺️ **Location APIs**
```http
GET /api/provinces/     # รายชื่อจังหวัดทั้งหมด
GET /api/districts/     # รายชื่ออำเภอตามจังหวัด
```

---

## 🎨 คุณสมบัติการออกแบบ

### 🌙 **ธีมสีเข้ม (Dark Theme)**
- การออกแบบที่ทันสมัยด้วยโทนสีเข้ม
- เอฟเฟกต์แก้วใส (Glassmorphism)
- แอนิเมชันที่นุ่มนวล

### 📱 **Mobile-First Design**
- เหมาะสำหรับการใช้งานบนมือถือ
- ปุ่มและฟิลด์ขนาดที่เหมาะสำหรับการสัมผัส
- การนำทางที่ใช้งานง่าย

### ⚡ **ประสิทธิภาพ**
- โหลดเร็ว
- แอนิเมชันที่ลื่นไหล
- การแสดงผลที่เหมาะสมกับอุปกรณ์

## 💡 วิธีการใช้งาน

1. **เปิดเว็บไซต์** และดูสถิติผลิตภัณฑ์ OTOP
2. **ค้นหาสินค้า** โดยพิมพ์ชื่อผลิตภัณฑ์หรือร้าน
3. **เลือกจังหวัด** จากดรอปดาวน์เพื่อกรองผลการค้นหา
4. **เลือกอำเภอ** เพื่อค้นหาที่แม่นยำยิ่งขึ้น
5. **ดูผลการค้นหา** ในรูปแบบการ์ดและบนแผนที่
6. **คลิกที่เครื่องหมายบนแผนที่** เพื่อดูรายละเอียดผลิตภัณฑ์

## 🛠️ เทคโนโลยีที่ใช้

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **แผนที่**: Google Maps JavaScript API
- **ฐานข้อมูล**: SQLite (สำหรับพัฒนา)
- **สไตล์**: CSS3 with Glassmorphism effects
- **Responsive**: Mobile-first design

## 🎯 สถานะการพัฒนา

- ✅ การแปลงข้อมูล Excel เป็น JSON
- ✅ โมเดล Django และ Admin interface
- ✅ ระบบค้นหาและกรองข้อมูล
- ✅ การผสานรวม Google Maps
- ✅ อินเทอร์เฟซเว็บที่ตอบสนอง
- ✅ การเพิ่มประสิทธิภาพสำหรับมือถือ
- ✅ ธีมสีเข้มที่ทันสมัย

## 📞 การสนับสนุน

หากมีปัญหาหรือข้อสงสัยในการใช้งาน สามารถตรวจสอบได้ที่:
- Console ของเบราว์เซอร์ (F12) สำหรับข้อความ debug
- ไฟล์ log ของ Django
- การตั้งค่า Google Maps API

---

**🇹🇭 OTOP Thailand** - แพลตฟอร์มค้นหาผลิตภัณฑ์ท้องถิ่นไทยที่ทันสมัยและใช้งานง่าย