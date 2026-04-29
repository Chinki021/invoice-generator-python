import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


class InvoiceGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Invoice Generator – Developed by Chinki Raj")
        self.root.geometry("750x700")
        self.root.configure(bg="white")

        self.file_name = ""

        
        self.canvas_widget = tk.Canvas(self.root, bg="white", highlightthickness=0)
        self.scrollbar = Scrollbar(self.root, orient="vertical",
                                   command=self.canvas_widget.yview)
        self.canvas_widget.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas_widget.pack(side="left", fill="both", expand=True)

        self.frame = Frame(self.canvas_widget, bg="white")
        self.frame_window = self.canvas_widget.create_window(
            (0, 0), window=self.frame, anchor="nw"
        )

        self.frame.bind("<Configure>", self._on_frame_configure)
        self.canvas_widget.bind("<Configure>", self._on_canvas_configure)
        self.canvas_widget.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas_widget.bind_all("<Button-4>", self._on_mousewheel)
        self.canvas_widget.bind_all("<Button-5>", self._on_mousewheel)

        
        Label(self.frame, text="Enter your company details",
              font=("times new roman", 28, "bold"),
              bg="white", fg="green").grid(
                  row=0, column=0, columnspan=2,
                  padx=50, pady=(20, 10), sticky="w")

        fields = [
            ("Company Name",        "company_name"),
            ("Address",             "address"),
            ("City",                "city"),
            ("GST Number",          "gst"),
            ("Date",                "date"),
            ("Contact",             "contact"),
            ("Customer Name",       "c_name"),
            ("Authorized Signatory","aus"),
        ]

        for i, (label_text, attr) in enumerate(fields, start=1):
            Label(self.frame, text=label_text,
                  font=("times new roman", 15, "bold"),
                  bg="white", fg="gray").grid(
                      row=i, column=0, padx=50, pady=10, sticky="w")
            entry = Entry(self.frame,
                          font=("times new roman", 15),
                          bg="light grey", width=30)
            entry.grid(row=i, column=1, padx=10, pady=10, sticky="w")
            setattr(self, attr, entry)

        
        Label(self.frame, text="Company Image",
              font=("times new roman", 15, "bold"),
              bg="white", fg="gray").grid(
                  row=len(fields)+1, column=0,
                  padx=50, pady=10, sticky="w")

        img_frame = Frame(self.frame, bg="white")
        img_frame.grid(row=len(fields)+1, column=1,
                       padx=10, pady=10, sticky="w")

        Button(img_frame, text="Browse Files",
               font=("times new roman", 14),
               command=self.browse).pack(side="left")

        self.image_label = Label(img_frame, bg="white",
                                 font=("times new roman", 12))
        self.image_label.pack(side="left", padx=10)

        Button(self.frame, text="Generate Invoice",
               command=self.generate_invoice,
               font=("times new roman", 14, "bold"),
               fg="white", cursor="hand2",
               bg="#B00857", width=20, height=2).grid(
                   row=len(fields)+2, column=0, columnspan=2,
                   padx=50, pady=30, sticky="w")

    def _on_frame_configure(self, event=None):
        self.canvas_widget.configure(scrollregion=self.canvas_widget.bbox("all"))

    def _on_canvas_configure(self, event):
        self.canvas_widget.itemconfig(self.frame_window, width=event.width)

    def _on_mousewheel(self, event):
        if event.num == 4:
            self.canvas_widget.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas_widget.yview_scroll(1, "units")
        else:
            self.canvas_widget.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def browse(self):
        self.file_name = filedialog.askopenfilename(title="Select Image")
        if self.file_name:
            self.image_label.config(text=os.path.basename(self.file_name))

    def generate_invoice(self):
        try:
            
            page_w, page_h = A4
            margin = 50

            c = canvas.Canvas("Invoice.pdf", pagesize=A4)

            
            if self.file_name:
                c.drawImage(self.file_name,
                            margin, page_h - 100,
                            width=80, height=60,
                            preserveAspectRatio=True, mask='auto')

            
            c.setFont("Helvetica-Bold", 16)
            c.setFillColor(colors.HexColor("#B00857"))
            c.drawString(margin + 100, page_h - 60,  self.company_name.get())

            c.setFont("Helvetica", 10)
            c.setFillColor(colors.black)
            c.drawString(margin + 100, page_h - 78,  self.address.get())
            c.drawString(margin + 100, page_h - 92,  self.city.get() + ", India")
            c.drawString(margin + 100, page_h - 106, "GST No: " + self.gst.get())

            
            c.setStrokeColor(colors.HexColor("#B00857"))
            c.setLineWidth(1.5)
            c.line(margin, page_h - 120, page_w - margin, page_h - 120)

            
            c.setFont("Helvetica-Bold", 22)
            c.setFillColor(colors.HexColor("#B00857"))
            c.drawString(margin, page_h - 160, "INVOICE")

            
            c.setFont("Helvetica-Bold", 10)
            c.setFillColor(colors.black)
            c.drawString(margin, page_h - 190, "Date:")
            c.drawString(margin, page_h - 208, "Bill To:")
            c.drawString(margin, page_h - 226, "Contact:")

            c.setFont("Helvetica", 10)
            c.drawString(margin + 80, page_h - 190, self.date.get())
            c.drawString(margin + 80, page_h - 208, self.c_name.get())
            c.drawString(margin + 80, page_h - 226, self.contact.get())

            
            table_top = page_h - 270
            col_widths = [250, 80, 100, 115]
            col_x = [margin]
            for w in col_widths[:-1]:
                col_x.append(col_x[-1] + w)

            
            c.setFillColor(colors.HexColor("#B00857"))
            c.rect(margin, table_top - 4, page_w - 2*margin, 20, fill=1, stroke=0)

            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 10)
            for i, h in enumerate(["Description", "Qty", "Unit Price", "Total"]):
                c.drawString(col_x[i] + 5, table_top + 3, h)

            
            row_h = 22
            for row in range(5):
                y = table_top - (row + 1) * row_h
                bg = colors.HexColor("#F5F5F5") if row % 2 == 0 else colors.white
                c.setFillColor(bg)
                c.rect(margin, y - 4, page_w - 2*margin, row_h, fill=1, stroke=0)
                c.setFillColor(colors.black)
                c.setFont("Helvetica", 10)
                c.drawString(margin + 5, y + 4, "—")

            
            bottom_y = table_top - 6 * row_h - 10
            c.setStrokeColor(colors.HexColor("#B00857"))
            c.line(margin, bottom_y, page_w - margin, bottom_y)

            
            sig_x = page_w - margin - 180
            c.setFont("Helvetica-Bold", 10)
            c.setFillColor(colors.black)
            c.drawString(sig_x, bottom_y - 40, "Authorized Signatory:")
            c.setFont("Helvetica", 10)
            c.drawString(sig_x, bottom_y - 58, self.aus.get())
            c.setStrokeColor(colors.black)
            c.line(sig_x, bottom_y - 62, page_w - margin, bottom_y - 62)

            
            c.setFont("Helvetica-Oblique", 8)
            c.setFillColor(colors.grey)
            c.drawCentredString(page_w / 2, 25, "Developed by Chinki Raj")

            c.save()
            messagebox.showinfo("Success", "Invoice.pdf generated successfully!\nSaved in the same folder as this script.")

        except Exception as e:
            messagebox.showerror("Error", str(e))


def main():
    root = Tk()
    app = InvoiceGenerator(root)
    root.mainloop()


if __name__ == "__main__":
    main()