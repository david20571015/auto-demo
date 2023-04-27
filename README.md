# auto demo

## 使用結果範例

* PASS

![PASS](https://i.imgur.com/6bCuMxV.png)

* FAIL

![FAIL](https://i.imgur.com/OWzRIvC.png)

## 環境

* Windows 10 (64-bit)
* Python 3.10.3

* Ubuntu 20.04.3 LTS (WSL)
* Python 3.9.5

> 沒在其他環境測試過，學生使用不需要裝python。

## 使用方法 for TAs

安裝 [poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)
> 請注意path有沒有設好

### Windows

1. 取得這個repo: (以下沒特別講都是在這個repo的資料夾下執行)
   * `git clone --branch main https://github.com/david20571015/auto-demo.git` 或
   * [Download](https://github.com/david20571015/auto-demo/archive/refs/heads/main.zip)
2. 安裝需要的dependency: `poetry install`
3. 進入pipenv (以下沒特別講都在這個shell中執行): `poetry shell`
4. 整合測資:
   1. 將[測資](https://github.com/david20571015/auto-demo#%E6%B8%AC%E8%B3%87%E6%A0%BC%E5%BC%8F-%E5%8F%83%E8%80%83)放到`test.in`中
   2. 將各題編譯好的執行檔放到`.\exec`資料夾中
   3. 執行`python build_test.py`或用`python build_test.py --output-dir output`將程式的輸出存到./output
5. (Optional) 將本次lab的執行檔放成[指定的格式](https://github.com/david20571015/auto-demo#%E5%9F%B7%E8%A1%8C%E6%AA%94%E6%A0%BC%E5%BC%8F)後測試auto-demo執行: `python grade.py --execution-dir .\exec` (所有題目都要PASS)
6. 產生auto-demo執行檔: `python -OO -m PyInstaller --onefile --add-data "test.json;." .\grade.py`
7. (Optional) 刪除編譯過程產生的檔案: `rmdir -Recurse -Force ".\build"; rm ".\grade.spec"`
8. `.\dist\grade.exe`即為auto-demo的執行檔
9. (Optional) 將`.\dist\grade.exe`移到`.\exec`中點兩下執行，檢查是否能正常使用
10. (Optional) 移除這個pipenv的dependency: `poetry env remove --all`

### Linux (out-of-dated)

1. 取得這個repo: (以下沒特別講都是在這個repo的資料夾下執行)
   * `git clone --branch main https://github.com/david20571015/auto-demo.git` 或
   * [Download](https://github.com/david20571015/auto-demo/archive/refs/heads/main.zip)
2. 安裝 [pipenv](https://pypi.org/project/pipenv/): `pip3 install pipenv`
3. 安裝需要的dependency: `pipenv install --dev --skip-lock`
4. 進入pipenv (以下沒特別講都在這個shell中執行): `pipenv shell`
5. 整合測資:
   1. 將[測資](https://github.com/david20571015/auto-demo#%E6%B8%AC%E8%B3%87%E6%A0%BC%E5%BC%8F-%E5%8F%83%E8%80%83)放到`test.in`中
   2. 將各題編譯好的執行檔放到`./exec`資料夾中
   3. 執行`python3 build_test.py`或用`python3 build_test.py --output-dir output`將程式的輸出存到./output
6. (Optional) 將本次lab的執行檔放成[指定的格式](https://github.com/david20571015/auto-demo#%E5%9F%B7%E8%A1%8C%E6%AA%94%E6%A0%BC%E5%BC%8F)後測試auto-demo執行: `python3 grade.py --execution-dir ./exec` (所有題目都要PASS)
7. 產生auto-demo執行檔: `python3 -OO -m PyInstaller --onefile --add-data "test.json:." ./grade.py`
8. (Optional) 刪除編譯過程產生的檔案: `rm -rf ./build ./grade.spec`
9. `./dist/grade.exe`即為auto-demo的執行檔
10. (Optional) 將`./dist/grade.exe`移到`./exec`中點兩下執行，檢查是否能正常使用
11. (Optional) 移除這個pipenv的dependency: `pipenv --rm`

### 測資格式 ([參考](https://github.com/david20571015/auto-demo/blob/main/test.in))

* 同一筆測資請放在同一行，並以空白隔開。
* 只需要input，對應的output由此程式產生。
* 如果沒有input，該行請直接留空。
* 編碼請使用UTF-8，目前還沒測試過其他編碼。

```txt
<題號> <Fail時顯示差異, 0為不顯示, 非0為顯示> <隱藏答案的行數 (1 5為隱藏第1~5行)>
<測資數量>
<測資1>
<測資2>
.
.
.
<空行>
```

## 使用方法 for 學生

1. 將grade.exe與本次lab的執行檔放成[指定的格式](https://github.com/david20571015/auto-demo#%E5%9F%B7%E8%A1%8C%E6%AA%94%E6%A0%BC%E5%BC%8F)
2. 按兩下`grade.exe`即可看到結果

### 執行檔格式

* 請將編譯完的執行檔與`grade.exe`放在同一個路徑。執行檔的檔名要跟對應的題號相同。

```txt
(dir)
|- grade.exe
|- 1.exe
|- 2.exe
|- 3.exe
.
.
.
```

## 錯誤回報

這個工具是課餘時間寫的，使用上可能會遇到我沒注意到的bug，請利用[issue](https://github.com/david20571015/auto-demo/issues)回報，或直接用[pull requests](https://github.com/david20571015/auto-demo/pulls)協助修正問題。謝謝。
