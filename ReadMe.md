# ImageGen 

이 README는 `ImageGen` 클래스, 메서드 및 사용 예시에 대한 개요를 제공합니다. `ImageGen` 클래스는 지정된 텍스트를 포함하는 이미지를 생성하고 이를 JPEG 파일로 저장하는 기능을 가지고 있습니다. 또한, 엑셀 파일에서 데이터를 읽어 이미지 생성 과정을 자동화하는 기능도 포함되어 있습니다.

## Method

### `__init__()`

ImageGen 클래스를 초기화합니다:

- 흰색 배경의 새로운 이미지를 생성합니다.
- 드로잉 컨텍스트를 초기화합니다.

### `code(word)`

지정된 word를 이미지에 추가합니다:

- NanumGothicBold.ttf 폰트를 크기 150으로 설정합니다.
- 단어를 이미지 중앙에 위치시키기 위해 위치를 계산합니다.
- 단어를 이미지에 그립니다.

### `number(level)`

지정된 level을 이미지에 추가합니다:

- NanumGothicBold.ttf 폰트를 크기 150으로 설정합니다.
- 레벨을 이미지 중앙에 위치시키기 위해 위치를 계산합니다.
- 레벨을 이미지에 그립니다.

### `saveToFile(filename)`

현재 이미지를 지정된 filename으로 JPEG 형식으로 파일에 저장합니다.

### `getSize(text, font)`

지정된 text와 font의 너비와 높이를 계산합니다.

### makeImage(word, number)

지정된 word와 number로 이미지를 생성합니다:

- 이미지를 초기화합니다.
- code(word)를 호출하여 단어를 이미지에 추가합니다.
- number(level)를 호출하여 레벨을 이미지에 추가합니다.
- `./result` 디렉토리에 word와 number를 조합한 파일명으로 이미지를 저장합니다.

### `read_excel_to_lists(filename)`

엑셀 파일에서 데이터를 읽어 리스트 형태로 반환합니다:

- 워크북을 로드합니다.
- 활성 워크시트를 선택합니다.
- 행을 반복하여 각 행의 데이터를 리스트에 추가합니다.
- 워크북을 닫고 데이터 리스트를 반환합니다.

## 사용예시

```python
if __name__ == "__main__":
    a = ImageGen()
    list = a.read_excel_to_lists("code.xlsx")
    print(list)
    for i in list:
        a.makeImage(i[0], i[1])
```

- 결과는 `./result/` 디렉토리에 자동으로 저장됩니다.