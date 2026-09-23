# ttk-dark-theme

Centralny motyw kolorystyczny i inicjalizacja stylów widgetów dla aplikacji GUI opartych o `tkinter`/`ttk`. Jeden plik (`gui_app_theme_dark.py`) do zaimportowania w dowolnym projekcie GUI, aby zachować spójny, ciemny wygląd (tło `#1e1e1e`, akcent pomarańczowy `#ff8c00`).

## Zawartość repo

```
ttk-dark-theme/
├── gui_app_theme_dark.py     # biblioteka - motyw + fabryki widgetów
├── Examples/
│   └── theme_dark_demo_full.py   # pełny przykład użycia wszystkich stylów
└── README.md
```

## Wymagania

- Python 3.8+
- `tkinter` (standardowa biblioteka, w Windows/macOS dołączona domyślnie; na Linuksie doinstaluj pakiet `python3-tk`)

Brak dodatkowych zależności zewnętrznych (bez `pip install`).

## Instalacja / umiejscowienie biblioteki

Plik `gui_app_theme_dark.py` musi być widoczny dla interpretera Pythona przy imporcie w Twoim projekcie. Najprościej:

1. Skopiuj `gui_app_theme_dark.py` do katalogu głównego swojego projektu (obok pliku `main.py`), **lub**
2. Umieść go w podkatalogu i dodaj ten katalog do `PYTHONPATH`, **lub**
3. Sklonuj to repo jako submoduł/pakiet i zaimportuj po ścieżce.

## Użycie w projekcie

```python
from gui_app_theme_dark import T, apply_theme

root = tk.Tk()
apply_theme(root)   # stosuje styl ttk do całego okna
```

Słownik `T` zawiera wszystkie kolory i fonty motywu (`T["accent"]`, `T["font_mono"]`, itd.) do użycia przy tworzeniu własnych widgetów spoza `ttk`.

## Uruchomienie przykładu (`Examples/theme_dark_demo_full.py`)

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
   lub wejdź do `Examples/` i uruchom bezpośrednio — działa dopóki `gui_app_theme_dark.py` jest dostępny w `PYTHONPATH` (np. przez ustawienie zmiennej środowiskowej):
   ```bash
   cd Examples
   PYTHONPATH=.. python theme_dark_demo_full.py
   ```

Otworzy się okno demonstracyjne z dwiema zakładkami prezentującymi wszystkie stylowane widgety: `Entry`, `Combobox`, `Spinbox`, `Checkbutton`, `Radiobutton`, przyciski (`TButton`, `Accent.TButton`, `tk.Button`), `Progressbar`, `Listbox`, `Text`, `ScrolledText` oraz `Treeview`.

## Licencja

Do uzupełnienia (np. MIT).
