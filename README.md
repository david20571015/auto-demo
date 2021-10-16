# auto demo

## 環境

* Windows 10 (64-bit)
* Python 3.9.5

> 沒在其他環境測試過，學生使用不需要裝python。

## 使用方法 for TAs

1. 取得這個repo: (以下沒特別講都是在這個repo的資料夾下執行)
   * `git clone https://github.com/david20571015/auto-demo.git` 或
   * [Download](https://github.com/david20571015/auto-demo/archive/refs/heads/main.zip)
2. 安裝 [pipenv](https://pypi.org/project/pipenv/): `pip install pipenv`
3. 安裝需要的dependency: `pipenv install --dev --skip-lock`
4. 進入pipenv (以下沒特別講都在這個shell中執行): `pipenv shell`
5. 整合[測資](https://github.com/david20571015/auto-demo#測資格式): `python build_test.py`
6. (Optional) 測試auto-demo執行: `python grade.py` (所有題目都要PASS)
7. 產生auto-demo執行檔: `python -OO -m PyInstaller --onefile --add-data "test.json;." .\grade.py`
8. (Optional) 刪除不需要的檔案: `rmdir -Recurse -Force ".\build"`, `rm ".\grade.spec"`
9. `./dist/grade.exe`即為auto-demo的執行檔
10. (Optional) 移除這個pipenv的dependency: `pipenv --rm`

### 測資格式

```txt
auto-demo
|- test
   |- 1 (題號)
      |- 1.in
      |- 1.out
      |- 2.in
      |- 2.out
   |- 2
      |- 1.in
      |- 1.out
|- src
|- build_test.py
|- grade.py
.
.
.
```

請TA先準備好test資料夾，並在裡面創好各題號的資料夾以及`*.in`和`*.out`作為測資，檔名一樣的會視為一組測資。
`*.out`可使用Powershell指令`Get-Content {*.in} | {*.exe} > {*.out}`產生。
( 相當於linux的`{*.out} < {*.in} > {*.out}` )

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

請將編譯完的執行檔與`grade.exe`放在同一個路徑。執行檔的檔名要跟題號相同。
