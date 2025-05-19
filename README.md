# function_tests_by_python_demo

## zainstalowac python3

## zainstalowac modul pytest

```
python -m pip install --upgrade pip
```

```
python -m pip install pytest
```

## zainstalowac modul loguru

```
python -m pip install loguru
```

## uruchomienie

bedac w katalogu zrodel wykonac polecenie z linii komend

```
python -m pytest test_name_function.py
```

powinny sie wyswietlic napisy w konsoli

```
================================================= test session starts =================================================
platform win32 -- Python 3.13.0a5, pytest-8.3.5, pluggy-1.6.0
rootdir: e:\pets_by_python\function_tests_by_python
collected 7 items

test_name_function.py .......                                                                                    [100%]

================================================== 7 passed in 0.01s ==================================================
```

## tresc logowania testowanej funkcji w logu function_tests_by_python.log

```
2025-05-19 13:38:47.983 6768 DEBUG name_function.py get_formattes_name(10) names=('abcde', 'efghijklm')
2025-05-19 13:38:47.983 6768 DEBUG name_function.py get_formattes_name(24) ret=Abcde Efghijklm
2025-05-19 13:38:47.984 6768 DEBUG name_function.py get_formattes_name(10) names=('abcde', 'xyz', 'efghijklm')
2025-05-19 13:38:47.985 6768 DEBUG name_function.py get_formattes_name(24) ret=Abcde Xyz Efghijklm
2025-05-19 13:38:47.985 6768 DEBUG name_function.py get_formattes_name(10) names=(None, '', 'efghijklm')
2025-05-19 13:38:47.985 6768 DEBUG name_function.py get_formattes_name(24) ret=Efghijklm
2025-05-19 13:38:47.986 6768 DEBUG name_function.py get_formattes_name(10) names=()
2025-05-19 13:38:47.986 6768 DEBUG name_function.py get_formattes_name(24) ret=None
2025-05-19 13:38:47.987 6768 DEBUG name_function.py get_formattes_name(10) names=(None,)
2025-05-19 13:38:47.987 6768 DEBUG name_function.py get_formattes_name(24) ret=None
2025-05-19 13:38:47.987 6768 DEBUG name_function.py get_formattes_name(10) names=(None, None)
2025-05-19 13:38:47.988 6768 DEBUG name_function.py get_formattes_name(24) ret=None
2025-05-19 13:38:47.988 6768 DEBUG name_function.py get_formattes_name(10) names=(None, None, None)
2025-05-19 13:38:47.988 6768 DEBUG name_function.py get_formattes_name(24) ret=None
```
