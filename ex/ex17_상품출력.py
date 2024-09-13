import json

with open("ex/json_상품.json",'r',encoding="utf-8") as f:
    read = json.load(f)
    name = read['p_name']
    price = read['price']
    sp = read['sp']
    
    output = f"이름: {name}, 가격: {price}"
    
    for i, value in enumerate(sp):
        if i == 0:
            output += f", 평수: {value}"
        elif i == 1:
            output += f", 방/화장실: {value}"
    
    # 최종 출력
    print(output)
        # print(name,price,size,rooms)