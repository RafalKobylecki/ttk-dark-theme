[# ttk-dark-theme

<a href="#polski">🇵🇱 Polski</a> | <a href="#english">🇬🇧 English</a>

---

<a name="polski"></a>
## Polski

Centralny motyw kolorystyczny i inicjalizacja stylów widgetów dla aplikacji GUI opartych o `tkinter`/`ttk`. Jeden plik (`gui_app_theme_dark.py`) do zaimportowania w dowolnym projekcie GUI, aby zachować spójny, ciemny wygląd (tło `#1e1e1e`, akcent pomarańczowy `#ff8c00`).

### Zawartość repo

```
ttk-dark-theme/
├── gui_app_theme_dark.py     # biblioteka - motyw + fabryki widgetów
├── Examples/
│   └── theme_dark_demo_full.py   # pełny przykład użycia wszystkich stylów
├── LICENSE.txt                   # GNU GPL v3.0
└── README.md
```

### Wymagania

- Python 3.8+
- `tkinter` (standardowa biblioteka, w Windows/macOS dołączona domyślnie; na Linuksie doinstaluj pakiet `python3-tk`)

Brak dodatkowych zależności zewnętrznych (bez `pip install`).

### Instalacja / umiejscowienie biblioteki

Plik `gui_app_theme_dark.py` musi być widoczny dla interpretera Pythona przy imporcie w Twoim projekcie. Najprościej:

1. Skopiuj `gui_app_theme_dark.py` do katalogu głównego swojego projektu (obok pliku `main.py`), **lub**
2. Umieść go w podkatalogu i dodaj ten katalog do `PYTHONPATH`, **lub**
3. Sklonuj to repo jako submoduł/pakiet i zaimportuj po ścieżce.

### Użycie w projekcie

```python
from gui_app_theme_dark import T, apply_theme

root = tk.Tk()
apply_theme(root)   # stosuje styl ttk do całego okna
```

Słownik `T` zawiera wszystkie kolory i fonty motywu (`T["accent"]`, `T["font_mono"]`, itd.) do użycia przy tworzeniu własnych widgetów spoza `ttk`.

### Uruchomienie przykładu (`Examples/theme_dark_demo_full.py`)

Przykład wymaga, aby `gui_app_theme_dark.py` znajdował się **jeden katalog wyżej** niż `Examples/` (czyli w katalogu głównym repo) — plik importuje go jako `from gui_app_theme_dark import ...`.

Kroki:

1. Sklonuj repo:
   ```bash
   git clone <adres-repo>
   cd ttk-dark-theme
   ```
2. Uruchom przykład z katalogu głównego repo:
   ```bash
   python Examples/theme_dark_demo_full.py
   ```
   lub wejdź do `Examples/` i uruchom bezpośrednio — działa dopóki `gui_app_theme_dark.py` jest dostępny w `PYTHONPATH`:
   ```bash
   cd Examples
   PYTHONPATH=.. python theme_dark_demo_full.py
   ```

Otworzy się okno demonstracyjne z dwiema zakładkami prezentującymi wszystkie stylowane widgety: `Entry`, `Combobox`, `Spinbox`, `Checkbutton`, `Radiobutton`, przyciski (`TButton`, `Accent.TButton`, `tk.Button`), `Progressbar`, `Listbox`, `Text`, `ScrolledText` oraz `Treeview`.

### Licencja

Projekt jest objęty licencją **GNU General Public License v3.0 (GPL-3.0)**. Pełny tekst licencji znajduje się w pliku [`LICENSE.txt`](./LICENSE.txt) w głównym katalogu repozytorium.

<a href="#ttk-dark-theme">⬆ powrót na górę</a>

---

<a name="english"></a>
## English

A central color theme and widget style initializer for `tkinter`/`ttk`-based GUI applications. A single file (`gui_app_theme_dark.py`) to import into any GUI project to keep a consistent dark look (background `#1e1e1e`, orange accent `#ff8c00`).

### Repo layout

```
ttk-dark-theme/
├── gui_app_theme_dark.py     # library - theme + widget factories
├── Examples/
│   └── theme_dark_demo_full.py   # full usage example for all styles
├── LICENSE.txt                   # GNU GPL v3.0
└── README.md
```

### Requirements

- Python 3.8+
- `tkinter` (standard library; bundled by default on Windows/macOS; on Linux install the `python3-tk` package)

No external dependencies (no `pip install` needed).

### Installation / library placement

`gui_app_theme_dark.py` must be importable by your project's Python interpreter. Simplest options:

1. Copy `gui_app_theme_dark.py` into your project's root directory (next to `main.py`), **or**
2. Place it in a subdirectory and add that directory to `PYTHONPATH`, **or**
3. Add this repo as a submodule/package and import it by path.

### Usage in a project

```python
from gui_app_theme_dark import T, apply_theme

root = tk.Tk()
apply_theme(root)   # applies the ttk style to the whole window
```

The `T` dictionary holds all theme colors and fonts (`T["accent"]`, `T["font_mono"]`, etc.) for use when building custom non-`ttk` widgets.

### Running the example (`Examples/theme_dark_demo_full.py`)

The example expects `gui_app_theme_dark.py` to be located **one directory above** `Examples/` (i.e. in the repo root) — the file imports it as `from gui_app_theme_dark import ...`.

Steps:

1. Clone the repo:
   ```bash
   git clone <repo-url>
   cd ttk-dark-theme
   ```
2. Run the example from the repo root:
   ```bash
   python Examples/theme_dark_demo_full.py
   ```
   or `cd` into `Examples/` and run it directly — works as long as `gui_app_theme_dark.py` is on `PYTHONPATH`:
   ```bash
   cd Examples
   PYTHONPATH=.. python theme_dark_demo_full.py
   ```

A demo window opens with two tabs showcasing every styled widget: `Entry`, `Combobox`, `Spinbox`, `Checkbutton`, `Radiobutton`, buttons (`TButton`, `Accent.TButton`, `tk.Button`), `Progressbar`, `Listbox`, `Text`, `ScrolledText`, and `Treeview`.

### License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**. The full license text is available in [`LICENSE.txt`](./LICENSE.txt) in the repository root.

<a href="#ttk-dark-theme">⬆ back to top</a>
](https://github.com/RafalKobylecki/ttk-dark-theme.git)
