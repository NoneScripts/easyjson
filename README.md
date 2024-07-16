# easyjson
## библиотека которая упрощает работу с json файлами

Это моя первая библиотека - я только учусь. Тут пока-что мало методов и классов. Если мне не будет лень, то может быть добавлю ещё.

**Установка библиотеки** `pip install easyjson`

**1. Как создать файл json?**
```python
from easyjson import JsonDC

create = JsonDC('filejs.json')
create.jsoncreate()
```
**2. Как создать файл json добавляя словарь?**
```python
from easyjson import JsonDC

dictjs = {
    "key1": 1,
    "key2": 2,
    "key3": 3
}

create = JsonDC('filejs.json')
create.jsoncreate(dictjs)
```
```json
{
    "key1": 1,
    "key2": 2,
    "key3": 3
}
```
**Кстати повторно файл не получиться создать, т.к. будет ошибка**

**3. Чтобы записать другой словарь в тот же файл**
```python
from easyjson import JsonMaster

dictjs = {
    "key4": 8,
    "key5": 7,
    "key6": 6
}

write = JsonMaster('filejs.json')
write.jsonwrite(dictjs)
```
```json
{
    "key4": 8,
    "key5": 7,
    "key6": 6
}
```
**4. Добавление ключа и значение в json файл**
```python
from easyjson import JsonMaster

addjs = JsonMaster('filejs.json')
addjs.jsonadd('key', 3)
```
```json
{
    "key4": 8,
    "key5": 7,
    "key6": 6,
    "key": 3
}
```
**5. Удаление ключа в json**
```python
from easyjson import JsonMaster

deletejs = JsonMaster('filejs.json')
deletejs.jsondelete('key')
deletejs.jsondelete('key6')
```
```json
{
    "key4": 8,
    "key5": 7
}
```
