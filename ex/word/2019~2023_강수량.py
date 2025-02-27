from matplotlib import font_manager, rc,pyplot as plt
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
import csv
colors = ['b','g','r','c','m','y','k']
labels = ['2024년도 강수량','2023년도 강수량','2022년도 강수량','2021년도 강수량','2020년도 강수량','2019년도 강수량']
try :
    file = open("ex/word/2019_2024강수량.csv",'r',encoding="utf-8")
        
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
else:
    header = next(file)
    # 자동으로 , 찍어주지만 다른 형식으로 끊어와야할 땐
    # delimiter -사용한다. 
    reader = csv.reader(file,delimiter=",")
    x=[]
    y=[]
    for line in reader:
        year,month = line[0].split("-") 
        x.append(month)
        y.append(float(line[2]))
        if month in "12":
            plt.plot(x,y,linestyle = "-",color = colors.pop(),label = labels.pop())
            x=[]
            y=[]
    if year in "2024":
        plt.plot(x,y,linestyle = "-",color = colors.pop(),label = labels.pop())


    plt.legend()
    plt.show()
    # 파일 닫아줌,,
finally :
    if 'file' in locals() and not file.closed:
        file.close()
        print("파일 닫음")
print("프로그램 종료")