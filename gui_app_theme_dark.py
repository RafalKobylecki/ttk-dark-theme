"""!
@file app_theme.py
@brief Central color theme and widget style initialization.

Import this module in all GUI projects to keep a consistent look.

@par Contrast rules
 - Dark background  -> light text  (#eeeeee / #ffffff)
 - Light background  -> dark text  (#1a1a1a / #333333)
 - Accent (#ff8c00)  -> black text (#000000)
"""
import tkinter as tk
from tkinter import ttk

# ──────────────────────────────────────────────────────────────────
#  COLOR PALETTE
# ──────────────────────────────────────────────────────────────────

## @brief Global theme dictionary: colors, fonts and palettes used across the app.
T = {
    # ── backgrounds ────────────────────────────────────────────
    "bg":           "#1e1e1e",   #!< main application background
    "bg2":          "#2d2d2d",   #!< panel / frame background
    "bg3":          "#3c3c3c",   #!< header / toolbar / button background
    "bg4":          "#8b8b8b",   #!< central panel background (e.g. Treeview, Text)
    "bg5":          "#5a5a5a",   #!< pressed / hover button background
    "bg_input":     "#2a2a2a",   #!< input field background (Entry, Combobox)
    "bg_input_sel": "#3a3a3a",   #!< input field background when focused

    # ── text ───────────────────────────────────────────────────
    "fg":           "#eeeeee",   #!< main text on dark background
    "fg_dim":       "#aaaaaa",   #!< secondary text / hints
    "fg_input":     "#ffffff",   #!< text in input fields (white - max contrast)
    "fg_on_accent": "#000000",   #!< text on accent-colored background
    "fg_on_light":  "#1a1a1a",   #!< text on light background

    # ── accents and states ────────────────────────────────────
    "accent":       "#ff8c00",   #!< primary accent - orange
    "accent_dark":  "#cc6e00",   #!< accent hover / active state
    "border":       "#555555",   #!< borders / separators

    # ── semantic terminal colors ──────────────────────────────
    "rx":           "#00ee77",   #!< received data (RX)
    "tx":           "#66aaff",   #!< transmitted data (TX)
    "proto":        "#ffcc44",   #!< decoded protocol
    "sys":          "#aaaaaa",   #!< system messages
    "err":          "#ff6666",   #!< errors
    "teal":         "#00bcd4",   #!< PORT2 - log console data (teal)

    # ── protocol field palette (cyclic) ───────────────────────
    "field_colors": [
        "#1a4a7a", "#1a5c1a", "#5c1a5c", "#7a4a00",
        "#1a4f5c", "#5c1a1a", "#1a5c3a", "#3a3a7a"
    ],

    # ── fonts ──────────────────────────────────────────────────
    "font_mono":    ("Courier New", 10),
    "font_ui":      ("Segoe UI", 9),
    "font_ui_bold": ("Segoe UI", 9, "bold"),
    "font_header":  ("Segoe UI", 10, "bold"),
}


# ──────────────────────────────────────────────────────────────────
#  ttk STYLE INITIALIZATION
# ──────────────────────────────────────────────────────────────────
def apply_theme(root: tk.Tk) -> None:
    """!
    @brief Apply the global theme to the main window and all ttk widgets.
    @param root Main Tk window (root) to configure.
    @return None
    """
    root.configure(bg=T["bg"])
    s = ttk.Style(root)
    s.theme_use("clam")

    # ── base ──────────────────────────────────────────────────
    s.configure(".",
        background=T["bg2"],
        foreground=T["fg"],
        font=T["font_ui"],
        bordercolor=T["border"],
        focuscolor=T["accent"],
        selectbackground=T["accent"],
        selectforeground=T["fg_on_accent"],
    )

    # ── Frame / LabelFrame ────────────────────────────────────
    s.configure("TFrame",          background=T["bg2"])
    s.configure("TLabelframe",     background=T["bg2"],
                                   foreground=T["accent"],
                                   bordercolor=T["border"])
    s.configure("TLabelframe.Label",
                background=T["bg2"],
                foreground=T["accent"],
                font=T["font_ui_bold"])

    # ── Label ─────────────────────────────────────────────────
    s.configure("TLabel",          background=T["bg2"], foreground=T["fg"])
    s.configure("Dim.TLabel",      background=T["bg2"], foreground=T["fg_dim"])

    # ── Button ────────────────────────────────────────────────
    s.configure("TButton",
        background=T["bg3"],
        foreground=T["fg"],          # light text on dark background
        padding=(6, 3),
        relief=tk.FLAT,
        borderwidth=1,
        bordercolor=T["border"],
    )
    s.map("TButton",
        background=[("active", T["accent"]), ("pressed", T["accent_dark"])],
        foreground=[("active", T["fg_on_accent"]), ("pressed", T["fg_on_accent"])],
    )
    s.configure("Accent.TButton",
        background=T["accent"],
        foreground=T["fg_on_accent"],  # black text on orange
        padding=(6, 3),
        font=T["font_ui_bold"],
    )
    s.map("Accent.TButton",
        background=[("active", T["accent_dark"]), ("pressed", T["accent_dark"])],
        foreground=[("active", T["fg_on_accent"])],
    )

    # ── Entry ─────────────────────────────────────────────────
    s.configure("TEntry",
        fieldbackground=T["bg_input"],   # dark field background
        foreground=T["fg_input"],         # white text
        insertcolor=T["fg_input"],        # caret
        selectbackground=T["accent"],
        selectforeground=T["fg_on_accent"],
        bordercolor=T["border"],
        lightcolor=T["bg_input"],
        darkcolor=T["bg_input"],
        padding=(4, 3),
    )
    s.map("TEntry",
        fieldbackground=[("focus", T["bg_input_sel"])],
        bordercolor=[("focus", T["accent"])],
    )

    # ── Combobox ──────────────────────────────────────────────
    s.configure("TCombobox",
        fieldbackground=T["bg_input"],
        background=T["bg3"],
        foreground=T["fg_input"],         # white text in field
        selectbackground=T["accent"],
        selectforeground=T["fg_on_accent"],
        arrowcolor=T["accent"],
        bordercolor=T["border"],
        padding=(4, 3),
    )
    s.map("TCombobox",
        fieldbackground=[("readonly", T["bg_input"]), ("focus", T["bg_input_sel"])],
        foreground=[("readonly", T["fg_input"])],
        bordercolor=[("focus", T["accent"])],
    )

    # ── Checkbutton ───────────────────────────────────────────
    s.configure("TCheckbutton",
        background=T["bg2"],
        foreground=T["fg"],
        indicatorcolor=T["bg_input"],
        indicatormargin=4,
    )
    s.map("TCheckbutton",
        background=[("active", T["bg2"])],
        foreground=[("active", T["fg"])],
        indicatorcolor=[("selected", T["accent"]), ("active", T["bg_input_sel"])],
    )

    # ── Radiobutton ───────────────────────────────────────────
    s.configure("TRadiobutton",
        background=T["bg2"],
        foreground=T["fg"],
    )
    s.map("TRadiobutton",
        background=[("active", T["bg2"])],
        foreground=[("active", T["fg"])],
        indicatorcolor=[("selected", T["accent"])],
    )

    # ── Scrollbar ─────────────────────────────────────────────
    s.configure("TScrollbar",
        background=T["bg3"],
        troughcolor=T["bg2"],
        arrowcolor=T["fg"],
        bordercolor=T["bg3"],
        lightcolor=T["bg3"],
        darkcolor=T["bg3"],
    )
    s.map("TScrollbar",
        background=[("active", T["accent"])],
        arrowcolor=[("active", T["fg_on_accent"])],
    )

    # ── Notebook / Tabs ───────────────────────────────────────
    s.configure("TNotebook",       background=T["bg"])
    s.configure("TNotebook.Tab",
        background=T["bg3"],
        foreground=T["fg"],
        padding=(10, 4),
    )
    s.map("TNotebook.Tab",
        background=[("selected", T["accent"])],
        foreground=[("selected", T["fg_on_accent"])],
    )

    # ── Treeview ──────────────────────────────────────────────
    s.configure("Treeview",
        background=T["bg2"],
        foreground=T["fg"],
        fieldbackground=T["bg2"],
        rowheight=22,
        bordercolor=T["border"],
    )
    s.configure("Treeview.Heading",
        background=T["bg3"],
        foreground=T["fg"],
        font=T["font_ui_bold"],
        relief=tk.FLAT,
    )
    s.map("Treeview",
        background=[("selected", T["accent"])],
        foreground=[("selected", T["fg_on_accent"])],
    )
    s.map("Treeview.Heading",
        background=[("active", T["accent_dark"])],
        foreground=[("active", T["fg"])],
    )

    # ── Separator ─────────────────────────────────────────────
    s.configure("TSeparator",      background=T["border"])

    # ── Progressbar ───────────────────────────────────────────
    s.configure("TProgressbar",
        background=T["accent"],
        troughcolor=T["bg3"],
        bordercolor=T["bg3"],
        lightcolor=T["accent"],
        darkcolor=T["accent_dark"],
    )

    # ── PanedWindow ───────────────────────────────────────────
    s.configure("TPanedwindow",    background=T["bg"])

    # ── Spinbox ───────────────────────────────────────────────
    s.configure("TSpinbox",
        fieldbackground=T["bg_input"],
        foreground=T["fg_input"],
        background=T["bg3"],
        arrowcolor=T["accent"],
        bordercolor=T["border"],
        insertcolor=T["fg_input"],
    )
    s.map("TSpinbox",
        fieldbackground=[("focus", T["bg_input_sel"])],
        bordercolor=[("focus", T["accent"])],
    )


# ──────────────────────────────────────────────────────────────────
#  WIDGET FACTORIES (helper, optional)
# ──────────────────────────────────────────────────────────────────
def make_listbox(parent, **kw) -> tk.Listbox:
    """!
    @brief Create a Listbox styled to match the theme.
    @param parent Parent widget.
    @param kw Extra keyword arguments overriding the default style.
    @return tk.Listbox instance.
    """
    defaults = dict(
        bg=T["bg_input"],
        fg=T["fg_input"],
        selectbackground=T["accent"],
        selectforeground=T["fg_on_accent"],
        activestyle="none",
        borderwidth=1,
        highlightthickness=1,
        highlightcolor=T["accent"],
        highlightbackground=T["border"],
        relief=tk.FLAT,
    )
    defaults.update(kw)
    return tk.Listbox(parent, **defaults)


def make_text(parent, **kw) -> tk.Text:
    """!
    @brief Create a multi-line Text field styled to match the theme.
    @param parent Parent widget.
    @param kw Extra keyword arguments overriding the default style.
    @return tk.Text instance.
    """
    defaults = dict(
        bg=T["bg_input"],
        fg=T["fg_input"],
        insertbackground=T["fg_input"],
        selectbackground=T["accent"],
        selectforeground=T["fg_on_accent"],
        relief=tk.FLAT,
        borderwidth=1,
        highlightthickness=1,
        highlightcolor=T["accent"],
        highlightbackground=T["border"],
        font=T["font_mono"],
    )
    defaults.update(kw)
    return tk.Text(parent, **defaults)


def make_scrolled_text(parent, **kw):
    """!
    @brief Create a ScrolledText widget styled to match the theme.
    @param parent Parent widget.
    @param kw Extra keyword arguments overriding the default style.
    @return scrolledtext.ScrolledText instance.
    """
    from tkinter import scrolledtext
    defaults = dict(
        bg="#0d0d0d",
        fg=T["rx"],
        insertbackground=T["fg_input"],
        selectbackground=T["accent"],
        selectforeground=T["fg_on_accent"],
        relief=tk.FLAT,
        borderwidth=1,
        font=T["font_mono"],
        wrap=tk.WORD,
    )
    defaults.update(kw)
    return scrolledtext.ScrolledText(parent, **defaults)


def make_header_frame(parent, title: str, bg=None) -> tuple:
    """!
    @brief Create a dark panel header.
    @param parent Parent widget.
    @param title Header label text.
    @param bg Optional background color override (defaults to T["bg3"]).
    @return Tuple (frame, title_label).
    """
    bg = bg or T["bg3"]
    frm = tk.Frame(parent, bg=bg, pady=4)
    lbl = tk.Label(frm, text=title, bg=bg, fg=T["accent"],
                   font=T["font_header"])
    lbl.pack(side=tk.LEFT, padx=6)
    return frm, lbl


def make_tk_button(parent, text: str, command=None, accent=False, **kw) -> tk.Button:
    """!
    @brief Create a plain tk.Button styled to match the theme (for places where ttk is insufficient).
    @param parent Parent widget.
    @param text Button label text.
    @param command Callback invoked on click.
    @param accent If True, use the accent (orange) style instead of the default one.
    @param kw Extra keyword arguments overriding the default style.
    @return tk.Button instance.
    """
    bg  = T["accent"] if accent else T["bg3"]
    fg  = T["fg_on_accent"] if accent else T["fg"]
    abg = T["accent_dark"] if accent else T["accent"]
    afg = T["fg_on_accent"]
    defaults = dict(
        bg=bg, fg=fg,
        activebackground=abg, activeforeground=afg,
        relief=tk.FLAT, padx=6, pady=3,
        font=T["font_ui"],
        cursor="hand2",
    )
    defaults.update(kw)
    return tk.Button(parent, text=text, command=command, **defaults)