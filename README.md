## 2. Консольные операции

![img.svg](img%2Fimg.svg)

Добро пожаловать на вторую тему, где вы освоите навыки работы с консолью!

Здесь вы узнаете, как выполнять базовые операции языка, такие как арифметические операции,
как выводить информацию в консоль, научитесь использовать встроенную функцию `print()` и изучите различные
разделители и символы, которые помогут вам форматировать вывод в консоль.

---

- [Арифметические операторы](#арифметические-операторы)
- [Вывод в консоль с `print()`](#вывод-в-консоль-с-print)
- [Разделители и концы строк](#разделители-и-концы-строк)
- [Управляющие символы](#управляющие-символы)
- [Задания по теме](#задания)

---

### Арифметические операторы

Арифметические операторы - это незаменимый инструмент в программировании, который позволяет нам проводить 
математические вычисления. Они позволяют выполнять базовые арифметические операции, как сложение, вычитание, 
умножение, деление и т.д.

Чтобы убедиться, как работают арифметические операторы, можем использовать интерактивный режим. 
Просто запустите консоль Python и введите выражение, которое хотите вычислить.
Например, вы можете проверить результаты следующих выражений:

```shell
>>> 2 + 3
5
>>> 6 * 4
24
```

Кроме базовых арифметических операций, также доступны другие операторы.

* Оператор возведения в степень `**` позволяет возводить число в указанную степень.
* Оператор целочисленного деления `//` возвращает результат деления, округленный до целого числа вниз.
* Оператор остатка от деления `%` возвращает остаток от деления двух чисел.

Например, чтобы возвести число `2` в степень `3`, можно использовать оператор возведения в степень:

```shell
>>> 2 ** 3
8
>>> 7 ** 4
2401
```

Для выполнения целочисленного деления числа `15` на `2`, можно использовать оператор целочисленного деления:

```shell
>>> 15 // 2
7
>>> 99 // 6
16
```

Оператор остатка от деления может быть полезен, например, для проверки, является ли число четным или нечетным:

```shell
>>> 7 % 2
1
>>> 10 % 2
0
>>> 45 % 9
0
```

| Оператор |       Название        | Объяснение                                                                             | Примеры                                                 |
|:--------:|:---------------------:|:---------------------------------------------------------------------------------------|---------------------------------------------------------|
|   `+`    |       Сложение        | Суммирует два объекта                                                                  | `3 + 5` даст `8`; `'a' + 'b'` даст `'ab'`               |
|   `-`    |       Вычитание       | Даёт разность двух чисел; если первый операнд  отсутствует, он считается  равным нулю  | `-5.2` даст отрицательное  число, а `50 - 24` даст `26` |
|   `*`    |       Умножение       | Даёт произведение двух  чисел или возвращает  строку, повторённую  заданное число раз. | `2 * 3` даст `6`. `'la'` * `3` даст `'lalala'`          |
|   `/`    |        Деление        | Возвращает частное от  деления `x` на `y`                                              | `4 / 3` даст  `1.3333333333333333`                      |
|   `**`   | Возведение в степень  | Возводит `x` в степень `y`                                                             | `3 ** 4` даст `81` (т.е. `3 * 3 * 3 * 3`)               |
|   `//`   | Целочисленное деление | Возвращает неполное частное от деления                                                 | `4 // 3` даст `1`.                                      |
|   `%`    |   Деление по модулю   | Возвращает остаток от деления                                                          | `8 % 3` даст `2`. `-25.5 % 2.25` даст `1.5`             |

Также можно использовать скобки для изменения порядка выполнения операций, как в математических выражениях.

Попробуйте сами, используя различные операторы и числа, чтобы увидеть, как они работают в Python.

---

### Вывод в консоль с `print()`

Для вывода данных в консоль в Python используется встроенная функция `print()`. Она может принимать различные типы
значений в качестве аргументов, как строки, числа, булевы значения и т.д.

Вот примеры использования функции `print()`:

```shell
>>> print("Привет, мир!")
Привет, мир!

>>> x = 42
>>> print("Значение x =", x)
Значение x = 42

>>> y = 3.14
>>> print("Значение y =", y)
Значение y = 3.14
```

Функция `print()` также может принимать несколько аргументов. Например:

```shell
>>> name = "Иван"
>>> age = 25
>>> print("Меня зовут", name, "и мне", age, "лет.")
Меня зовут Иван и мне 25 лет.
```

---

### Разделители и концы строк

Когда используете функцию `print()` для вывода данных в консоль, можете указать, какие символы будут использоваться
в качестве разделителя между значениями, а также какой символ должен использоваться в конце каждой строки.

По умолчанию, `print()` выводит значения через пробел и добавляет символ перевода строки `\n` в конце.
Это поведение можно изменить с помощью параметров функции `sep` и `end`

Например, использование запятую в качестве разделителя и точку с запятой в качестве символа конца строки, выглдит так:

```python
print("Hello", "world", sep=", ", end=";")
```

Вывод: `"Hello, world;"`.

---

### Управляющие символы

Управляющие символы - это специальные символы, которые позволяют вставлять различные управляющие последовательности в
строку.

Одним из наиболее часто используемых управляющих символов является символ перевода строки `\n`. Он используется для
создания новой строки в консоли. Например:

```python
print("Привет,\nмир!")
```

_Вывод:_

```commandline
Привет,
мир!
```

Другой управляющий символ - это символ возврата каретки `\r`. Он используется для перемещения каретки в начало строки.
Например:

```python
print("Привет, мир\rPython")
```

_Вывод:_

```commandline
Python
```

Обратите внимание, что символы после `\r` перезаписывают начало строки. Это может быть полезно, например, для создания
прогресс-бара или для вывода анимации.

Символ `\b` обозначает управляющий символ `backspace` (возврат на одну позицию назад) и используется для
удаления предыдущего символа в строке.

Когда символ `\b` встречается в строке, он перемещает курсор на одну позицию назад, не удаляя символ на этой позиции.
Это позволяет перезаписать или удалить предыдущий символ в строке.

Например, следующий код удаляет последний символ из строки:

```python
s = "Hello world\b"
print(s)
```

_Вывод:_

```commandline
Hello worl
```

В данном примере, после вывода строки `Hello world`, символ `\b` перемещает курсор назад на одну позицию, в результате
чего выводится строка `Hello worl`, без последней буквы `d`.

Важно отметить, что символ `\b` работает только в тех окружениях, где присутствует возможность перемещения курсора
влево и вправо, это консоль или терминал. А в других типах вывода, как файлы или сетевые
соединения, он не имеет эффекта.

Если необходимо вставить в строку специальные символы, такие как кавычки `"` или `'`, символы новой строки `\n` или
символы табуляции `\t`, можно использовать экранирующий символ `\` перед этими символами. Например:

```python
print("Это \\nсимвол \\ в \\tстроке")
print("Это \"строка\"")
```

_Вывод:_

```commandline
Это \nсимвол \ в \tстроке
Это "строка"
```

Некоторые из наиболее распространенных управляющих и экранирующих символов в Python:

| Символ | Описание                    |
|:------:|-----------------------------|
|  `\n`  | символ новой строки         |
|  `\r`  | возврат каретки             |           
|  `\t`  | горизонтальная табуляция    |  
|  `'`   | одинарная кавычка           |
|  `"`   | двойная кавычка             |
|  `\b`  | забой                       |
|  `\f`  | перевод страницы            |
|  `\v`  | вертикальная табуляция      |
|  `\`   | символ обратной косой черты |

---

В этой теме мы изучили базовые операции в консоли, такие как арифметические операторы и вывод данных
с помощью функции `print()`. Также рассмотрели разделители и управляющие символы для форматирования вывода.

В следующей теме `Переменные и объекты` познакомимся с объявлением и использованием переменных.
Также разберемся, что такое объекты и как они связаны с переменными.

Это будет интересное введение в основы работы с данными!

---

### [Задания](./tasks/TASKS.md)
