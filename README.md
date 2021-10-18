# auto demo

## 環境

* Windows 10 (64-bit)
* Python 3.9.5

> 沒在其他環境測試過，學生使用不需要裝python。

## 使用方法 for TAs

1. 取得這個repo: (以下沒特別講都是在這個repo的資料夾下執行)
   * `git clone --branch dev https://github.com/david20571015/auto-demo.git` 或
   * [Download](https://github.com/david20571015/auto-demo/archive/refs/heads/dev.zip)
2. 安裝 [pipenv](https://pypi.org/project/pipenv/): `pip install pipenv`
3. 安裝需要的dependency: `pipenv install --dev --skip-lock`
4. 進入pipenv (以下沒特別講都在這個shell中執行): `pipenv shell`
5. 整合測資:
   1. 將[測資](https://github.com/david20571015/auto-demo/tree/dev#%E6%B8%AC%E8%B3%87%E6%A0%BC%E5%BC%8F)放到`test.in`中
   2. 將各題編譯好的執行檔放到`.\exec`資料夾中
   3. 執行`python build_test.py`
6. (Optional) 將本次lab的執行檔放成[指定的格式](https://github.com/david20571015/auto-demo/tree/dev#%E5%9F%B7%E8%A1%8C%E6%AA%94%E6%A0%BC%E5%BC%8F)後測試auto-demo執行: `python grade.py --execution-dir .\exec` (所有題目都要PASS)
7. 產生auto-demo執行檔: `python -OO -m PyInstaller --onefile --add-data "test.json;." .\grade.py`
8. (Optional) 刪除編譯過程產生的檔案: `rmdir -Recurse -Force ".\build"; rm ".\grade.spec"`
9. `.\dist\grade.exe`即為auto-demo的執行檔
10. (Optional) 將`.\dist\grade.exe`移到`.\exec`中點兩下執行，檢查是否能正常使用
11. (Optional) 移除這個pipenv的dependency: `pipenv --rm`

### 測資格式 ([參考](https://github.com/david20571015/auto-demo/blob/dev/test.in))

同一筆測資請放在同一行，並以空白隔開。只需要input，對應的output由此程式產生。
編碼請使用UTF-8，目前還沒測試過其他編碼。

```txt
<題號> <Fail時顯示差異, 0為不顯示, 非0為顯示>
<測資數量>
<測資1>
<測資2>
.
.
.
<空行>
```

## 使用方法 for 學生

1. 將grade.exe與本次lab的執行檔放成[指定的格式](https://github.com/david20571015/auto-demo#執行檔格式)
2. 按兩下`grade.exe`即可看到結果

### 執行檔格式

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

請將編譯完的執行檔與`grade.exe`放在同一個路徑。執行檔的檔名要跟對應的題號相同。
