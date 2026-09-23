"""!
@file theme_demo_full.py
@brief Single-window demo exercising every widget/style defined in gui_app_theme.py.

Import path assumes gui_app_theme.py is in the same directory or on PYTHONPATH.
"""
import tkinter as tk
from tkinter import ttk
from gui_app_theme_dark import T, apply_theme, make_listbox, make_text, \
    make_scrolled_text, make_header_frame, make_tk_button


def build_gui() -> tk.Tk:
    """!
    @brief Build and return the fully populated demo window.
    @return Configured tk.Tk root instance.
    """
    root = tk.Tk()
    root.title("gui_app_theme - full demo")
    root.geometry("780x640")
    apply_theme(root)

    # ── header (tk.Frame/Label factory) ────────────────────────
    hdr, _ = make_header_frame(root, "THEME DEMO")
    hdr.pack(fill=tk.X)

    # ── notebook with two tabs ─────────────────────────────────
    nb = ttk.Notebook(root)
    nb.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

    tab1 = ttk.Frame(nb)
    tab2 = ttk.Frame(nb)
    nb.add(tab1, text="Controls")
    nb.add(tab2, text="Text / Tree")

    # ── TAB 1: basic controls ──────────────────────────────────
    lf = ttk.Labelframe(tab1, text="Inputs")
    lf.pack(fill=tk.X, padx=8, pady=8)

    ttk.Label(lf, text="Label:").grid(row=0, column=0, sticky="w", padx=4, pady=4)
    ttk.Entry(lf).grid(row=0, column=1, sticky="ew", padx=4, pady=4)

    ttk.Label(lf, text="Combo:").grid(row=1, column=0, sticky="w", padx=4, pady=4)
    ttk.Combobox(lf, values=["A", "B", "C"], state="readonly") \
        .grid(row=1, column=1, sticky="ew", padx=4, pady=4)

    ttk.Label(lf, text="Spin:").grid(row=2, column=0, sticky="w", padx=4, pady=4)
    ttk.Spinbox(lf, from_=0, to=10).grid(row=2, column=1, sticky="ew", padx=4, pady=4)

    ttk.Label(lf, text="Dimmed hint", style="Dim.TLabel") \
        .grid(row=3, column=0, columnspan=2, sticky="w", padx=4, pady=4)

    lf.columnconfigure(1, weight=1)

    chk = ttk.Frame(tab1)
    chk.pack(fill=tk.X, padx=8, pady=4)
    ttk.Checkbutton(chk, text="Checkbox").pack(side=tk.LEFT, padx=4)
    ttk.Radiobutton(chk, text="Option 1", value=1).pack(side=tk.LEFT, padx=4)
    ttk.Radiobutton(chk, text="Option 2", value=2).pack(side=tk.LEFT, padx=4)

    btns = ttk.Frame(tab1)
    btns.pack(fill=tk.X, padx=8, pady=4)
    ttk.Button(btns, text="Normal").pack(side=tk.LEFT, padx=4)
    ttk.Button(btns, text="Accent", style="Accent.TButton").pack(side=tk.LEFT, padx=4)
    make_tk_button(btns, "tk.Button", accent=True).pack(side=tk.LEFT, padx=4)

    ttk.Separator(tab1).pack(fill=tk.X, padx=8, pady=8)

    pw = ttk.Progressbar(tab1, mode="determinate", value=60)
    pw.pack(fill=tk.X, padx=8, pady=4)

    # ── TAB 2: text widgets + treeview ─────────────────────────
    paned = ttk.Panedwindow(tab2, orient=tk.HORIZONTAL)
    paned.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

    left = ttk.Frame(paned)
    right = ttk.Frame(paned)
    paned.add(left, weight=1)
    paned.add(right, weight=1)

    lb = make_listbox(left)
    for item in ("Item 1", "Item 2", "Item 3"):
        lb.insert(tk.END, item)
    lb.pack(fill=tk.BOTH, expand=True, pady=(0, 4))

    txt = make_text(left, height=5)
    txt.insert("1.0", "make_text() sample content")
    txt.pack(fill=tk.BOTH, expand=True)

    sc = make_scrolled_text(right, height=6)
    sc.insert("1.0", "RX> make_scrolled_text() sample (terminal-style)")
    sc.pack(fill=tk.BOTH, expand=True, pady=(0, 4))

    tree = ttk.Treeview(right, columns=("val",), show="headings", height=4)
    tree.heading("val", text="Field")
    for i in range(3):
        tree.insert("", tk.END, values=(f"row {i}",))
    tree.pack(fill=tk.BOTH, expand=True)

    return root


if __name__ == "__main__":
    build_gui().mainloop()
