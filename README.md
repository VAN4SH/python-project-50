### Hexlet tests and linter status:
[![Actions Status](https://github.com/VAN4SH/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/VAN4SH/python-project-50/actions)

## О программе
Gendiff - программа, которая выводит различия между двумя файлами. Поддерживаемые форматы: json, yaml.

## Установка программы
Для установки необходимо воспользоваться командой ```pip install gendiff-dmitriev```

[![asciicast](https://asciinema.org/a/fjAxFqqX8dgrdPfLIWZDUJSdO.svg)](https://asciinema.org/a/fjAxFqqX8dgrdPfLIWZDUJSdO)

## Вывод справочной информации
Для вывода справочной информации о программе используем команду ```gendiff -h```

[![asciicast](https://asciinema.org/a/RLWKUHl3vyIXd6LzBOzWyX4ch.svg)](https://asciinema.org/a/RLWKUHl3vyIXd6LzBOzWyX4ch)

## Сравнение плоских файлов (JSON)
```gendiff tests/file1.json tests/file2.json```, tests/file1.json и tests/file2.json меняем на свои пути к файлам

[![asciicast](https://asciinema.org/a/CFbKKnaDtuPad2J9ojhXOHp0v.svg)](https://asciinema.org/a/CFbKKnaDtuPad2J9ojhXOHp0v)

## Сравнение плоских файлов (YAML)
```gendiff tests/file1.yaml tests/file2.yml```

[![asciicast](https://asciinema.org/a/xAzCeNBwS8sJu8Umuiw3VY5YM.svg)](https://asciinema.org/a/xAzCeNBwS8sJu8Umuiw3VY5YM)

## Рекурсивное сравнение
```gendiff tests/file1_nested.json tests/file2_nested.yaml```

[![asciicast](https://asciinema.org/a/yy2b1cve3WyrNyNnLlqCsavVL.svg)](https://asciinema.org/a/yy2b1cve3WyrNyNnLlqCsavVL)

## Сравнение в плоском формате
```gendiff -f plain tests/file1.json tests/file2.json```

[![asciicast](https://asciinema.org/a/DBFmb0a4uokLZ8cm1NM4aLSw6.svg)](https://asciinema.org/a/DBFmb0a4uokLZ8cm1NM4aLSw6)

## Сравнение в формате JSON
```gendiff -f json tests/file1.json tests/file2.json```

[![asciicast](https://asciinema.org/a/UOEPlkalgRyO5NFW1O13SYK9c.svg)](https://asciinema.org/a/UOEPlkalgRyO5NFW1O13SYK9c)
