# 🧾 Invoice Generator — Python Desktop App

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![ReportLab](https://img.shields.io/badge/PDF-ReportLab-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

A fully functional **desktop Invoice Generator** built with Python. Users fill in a clean GUI form with company and customer details, upload a logo, and generate a professionally styled **A4 PDF invoice** — all in one click.

> Built to demonstrate real-world Python skills: GUI development, PDF generation, layout design, and clean code architecture.

---

## 📸 Screenshot

<img width="1909" height="1006" alt="Screenshot 2026-04-30 025907" src="https://github.com/user-attachments/assets/6d0954d8-6d42-41ff-89a9-5672f8e465c4" />

---

## ✨ Key Features

- 📋 **Dynamic Form UI** — scrollable Tkinter form with 8 input fields
- 🖼️ **Logo Upload** — browse and embed a company logo directly into the PDF
- 📄 **Professional PDF Output** — A4-sized invoice with branded color scheme, table layout, header, and footer
- ✍️ **Authorized Signatory Section** — signature block auto-placed at the bottom right
- 💾 **Save As Dialog** — user chooses filename and save location at runtime
- 🎨 **Branded Design** — consistent color theming (`#B00857`) across UI and PDF
- 🔄 **Alternating Row Shading** — clean table design with zebra striping in the PDF

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3** | Core language |
| **Tkinter** | Desktop GUI framework |
| **ReportLab** | PDF generation engine |
| **filedialog** | Native OS file browser for logo & save path |
| **Canvas API** | Precise PDF layout and drawing |

---

## 🧠 Technical Strategy

### GUI Architecture
The form uses a **Tkinter Canvas + Scrollbar** pattern instead of a plain Frame — this makes the UI scrollable and responsive regardless of screen size. Layout is handled with `grid()` for clean alignment across all input fields.

### PDF Generation
ReportLab's `Canvas` is used directly (rather than high-level templates) for **precise control** over every element's position. All coordinates are calculated relative to `page_height` using the formula `page_h - offset`, correctly accounting for ReportLab's **bottom-left origin system**.

### Separation of Concerns
The app is structured as a single class (`InvoiceGenerator`) with clearly separated responsibilities — UI setup in `__init__`, scroll logic in helper methods, and PDF generation isolated in `generate_invoice()`. This makes the codebase easy to extend (e.g. adding line items, tax calculation, or database storage).

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install reportlab
```

### Run
```bash
python main.py
```

### Generate an Invoice
1. Fill in company name, address, city, GST number
2. Enter date, contact, customer name, and authorized signatory
3. (Optional) Upload a company logo via **Browse Files**
4. Click **Generate Invoice** → choose save location → done ✅

---

## 📁 Project Structure

```
invoice-generator-python/
│
├── main.py          # Main application (GUI + PDF logic)
         
└── screenshot.png  #screenshot
├── README.md
└── .gitignore
```

---

## 🔮 Future Improvements

- [ ] Add line items table (description, qty, rate, total)
- [ ] GST/tax auto-calculation
- [ ] Invoice number auto-increment
- [ ] Save customer data to SQLite database
- [ ] Export customer history as Excel report
- [ ] Dark mode UI

---

## 👨‍💻 Author

**Chinki Raj**  
[![GitHub](https://img.shields.io/badge/GitHub-ChinkirRaj-black?logo=github)](https://github.com/Chinki021)


---

*This project was built as part of my Python development portfolio to demonstrate desktop application development, PDF generation, and GUI design skills.*
