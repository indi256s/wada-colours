# wada-colours

A Claude Code skill built on Sanzo Wada's 1933 "Dictionary of Colour Combinations." 159 named colours. 348 hand-composed palettes. No algorithmic generation, no colour wheel math. Every combination was picked by a colour theorist who spent his career studying what looks right together.

The dataset comes from [mattdesl/dictionary-of-colour-combinations](https://github.com/mattdesl/dictionary-of-colour-combinations), with CMYK-to-RGB conversion done through professional ICC profiles (U.S. Web Coated SWOP v2 for CMYK, sRGB IEC61966-2.1 for RGB). The hex values are accurate to the original printed swatches.

## What's inside

```
wada-colours/
├── SKILL.md              # Skill instructions, mood collections, integration examples
├── references/
│   └── colors.json       # Full 159-colour dataset
└── scripts/
    └── palette_tool.py   # Search, filter, export (8 commands)
```

## The palette tool

Search colours by name:

```bash
python scripts/palette_tool.py search "blue"
```

Get a palette by ID (1-348):

```bash
python scripts/palette_tool.py palette 42
python scripts/palette_tool.py palette 42 --css        # CSS custom properties
python scripts/palette_tool.py palette 42 --tailwind   # Tailwind v4 @theme
python scripts/palette_tool.py palette 42 --echarts    # ECharts colour array
```

Browse by mood:

```bash
python scripts/palette_tool.py mood warm       # warm, cool, bold, pastel, earthy
python scripts/palette_tool.py mood dramatic   # nature, tropical, dramatic, ui
```

Filter by palette size:

```bash
python scripts/palette_tool.py size 2    # 120 two-colour palettes
python scripts/palette_tool.py size 3    # 120 three-colour palettes
python scripts/palette_tool.py size 4    # 108 four-colour palettes
```

Find palettes that include a colour:

```bash
python scripts/palette_tool.py with "Cerulian Blue"
```

Check WCAG contrast between two colours:

```bash
python scripts/palette_tool.py contrast "#0093a5" "#ffffff"
```

Get random palettes:

```bash
python scripts/palette_tool.py random 3 --size 4
```

## Example output

```
$ python scripts/palette_tool.py palette 1 --css

Palette #1
==========
  #d96629  English Red
  #0093a5  Cerulian Blue

/* CSS Custom Properties */
:root {
  --color-primary: #d96629;  /* English Red */
  --color-secondary: #0093a5;  /* Cerulian Blue */
}
```

## 9 mood collections

| Mood | What it looks like | Good for |
|------|--------------------|----------|
| warm | Ochres, siennas, cinnamons | Restaurant brands, craft products |
| cool | Slate blues, sage greens | SaaS dashboards, corporate UI |
| bold | Saturated primaries | Hero sections, campaigns |
| pastel | Pale pinks, buffs | Onboarding, empty states |
| floral | Roses, violets, mauves | Editorial, beauty |
| nature | Deep greens, olive, moss | Sustainability, outdoor |
| tropical | Teal, coral, golden | Playful apps, food |
| dramatic | Dark indigos, burgundy | Luxury, dark mode |
| ui | Balanced contrast | Dashboards, data tables, charts |

## Install as a Claude Code skill

Copy the `wada-colours` folder to your skills directory:

```bash
cp -r wada-colours ~/.claude/skills/
```

The skill auto-triggers when you ask Claude to pick colours, set up a theme, or choose a palette.

## About the source

Sanzo Wada (1883-1967) was a Japanese artist and colour researcher. His dictionary, published by Seigensha Art Publishing, catalogues 159 colours organized into 348 combinations across six chapters. The original data was digitized by Dain M. Blodorn Kim and improved by Matt DesLauriers with better colour profile conversions.

No npm install needed. The full dataset is bundled in `references/colors.json`.

---

# wada-colours (RU)

Скилл для Claude Code на основе книги Санзо Вада "Dictionary of Colour Combinations" 1933 года. 159 именованных цветов. 348 палитр, собранных вручную. Никакой алгоритмической генерации -- каждую комбинацию подбирал исследователь цвета, посвятивший этому карьеру.

Датасет взят из [mattdesl/dictionary-of-colour-combinations](https://github.com/mattdesl/dictionary-of-colour-combinations). Конвертация CMYK в RGB сделана через профессиональные ICC-профили (U.S. Web Coated SWOP v2 для CMYK, sRGB IEC61966-2.1 для RGB). Hex-значения точно соответствуют оригинальным печатным образцам.

## Что внутри

```
wada-colours/
├── SKILL.md              # Инструкции, коллекции по настроению, примеры интеграции
├── references/
│   └── colors.json       # Полный датасет из 159 цветов
└── scripts/
    └── palette_tool.py   # Поиск, фильтрация, экспорт (8 команд)
```

## Инструмент палитр

Поиск цветов по названию:

```bash
python scripts/palette_tool.py search "blue"
```

Получить палитру по ID (1-348):

```bash
python scripts/palette_tool.py palette 42
python scripts/palette_tool.py palette 42 --css        # CSS custom properties
python scripts/palette_tool.py palette 42 --tailwind   # Tailwind v4 @theme
python scripts/palette_tool.py palette 42 --echarts    # Массив цветов для ECharts
```

Подбор по настроению:

```bash
python scripts/palette_tool.py mood warm       # warm, cool, bold, pastel, earthy
python scripts/palette_tool.py mood dramatic   # nature, tropical, dramatic, ui
```

Фильтр по размеру палитры:

```bash
python scripts/palette_tool.py size 2    # 120 двухцветных палитр
python scripts/palette_tool.py size 3    # 120 трёхцветных палитр
python scripts/palette_tool.py size 4    # 108 четырёхцветных палитр
```

Найти палитры с конкретным цветом:

```bash
python scripts/palette_tool.py with "Cerulian Blue"
```

Проверить контрастность по WCAG:

```bash
python scripts/palette_tool.py contrast "#0093a5" "#ffffff"
```

Случайные палитры:

```bash
python scripts/palette_tool.py random 3 --size 4
```

## Пример вывода

```
$ python scripts/palette_tool.py palette 1 --css

Palette #1
==========
  #d96629  English Red
  #0093a5  Cerulian Blue

/* CSS Custom Properties */
:root {
  --color-primary: #d96629;  /* English Red */
  --color-secondary: #0093a5;  /* Cerulian Blue */
}
```

## 9 коллекций по настроению

| Настроение | Как выглядит | Для чего |
|------------|-------------|----------|
| warm | Охра, сиена, корица | Ресторанные бренды, крафт |
| cool | Сланцевый синий, шалфейный зелёный | SaaS-дашборды, корпоративный UI |
| bold | Насыщенные основные цвета | Герой-секции, рекламные кампании |
| pastel | Бледно-розовый, палевый | Онбординг, пустые состояния |
| floral | Розы, фиалки, мовеин | Редакционный дизайн, бьюти |
| nature | Тёмная зелень, олива, мох | Эко-бренды, outdoor |
| tropical | Бирюза, коралл, золотой | Игривые приложения, фуд |
| dramatic | Тёмный индиго, бордо | Люкс, тёмная тема |
| ui | Сбалансированный контраст | Дашборды, таблицы, графики |

## Установка как скилл Claude Code

Скопируйте папку `wada-colours` в директорию скиллов:

```bash
cp -r wada-colours ~/.claude/skills/
```

Скилл срабатывает автоматически, когда вы просите Claude подобрать цвета, настроить тему или выбрать палитру.

## Об источнике

Санзо Вада (1883-1967) -- японский художник и исследователь цвета. Его словарь, изданный Seigensha Art Publishing, содержит 159 цветов, организованных в 348 комбинаций по шести главам. Данные оцифровал Dain M. Blodorn Kim, конвертацию цветовых профилей улучшил Matt DesLauriers.

npm не нужен. Полный датасет уже лежит в `references/colors.json`.
