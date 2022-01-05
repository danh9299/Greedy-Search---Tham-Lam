#Đồ thị cây của chương trình
graph ={
    'S' : ['A','B'],
    'A' : ['B','C','D','G'],
    'B' : ['C'],
    'C' : ['G'],
    'D' : ['G'],
    'G' : []
}
#Hàm đánh giá heuristic tại mỗi nút
heuristic = {
    'S' : 6,
    'A' : 3,
    'B' : 4,
    'C' : 2,
    'D' : 2,
    'G' : 0
}
#Thuật toán tham lam GreedySearch
def greedySearch(start,end,graph,heuristic):
    #Tạo một list open để lưu giá trị các nút con của nút đang xét
    open = []
    #Tạo list path để lưu đường đi
    path = []
    open.append(start)
    currentNode=open[0]
    #Tìm kiếm tới nút cuối cùng
    while open != []:
        #Lấy nút đầu (tức nút có heuristic nhỏ nhất) trong open
        currentNode = open.pop(0)
        print("Duyệt: ",currentNode)
        #Đặt nút được thăm vào path
        path.append(currentNode)
        #Kết thúc chương trình nếu tìm thấy nút cần tìm
        if currentNode == end:
            print("Đã tìm thấy đường")
            print("Đường đi: ",end="")
            return path
        #Xóa hết dữ liệu trong open vì chỉ xét đi tiếp các nút con của nút đang xét, không quay lui
        open = []
        #Cho hết các nút con của nút đang xét vào open
        for child in graph[currentNode]:
            open.append(child)
        #Sắp xếp các nút con trong open theo hướng tăng dần
        for i in range(0,len(open)-1):
            for j in range(i+1,len(open)):
                if(heuristic[open[i]] > heuristic[open[j]]):
                    tmp = open[i]
                    open[i] = open[j]
                    open[j] = tmp
    #Nếu đã duyệt tới nút cuối cùng mà vẫn không tìm thấy nút cần tìm
    path = ["Không tìm thấy đường đi"]
    return path

#Phần main của bài
#Người dùng nhập vào dữ liệu cho điểm bắt đầu và điểm kết thúc
start = (input("Nhập điểm bắt đầu: "))
start = start.upper()
while start not in graph:
    print("Điểm bắt đầu phải có trong cây!")
    start = input("Nhập lại điểm bắt đầu: ")
    start = start.upper()
end = input("Nhập điểm cần đến: ")
end = end.upper()
while end not in graph:
    print("Điểm đến phải có trong cây!")
    end = input("Nhập lại điểm cần đến: ")
    end = end.upper()


#Thực hiện thuật toán
for x in greedySearch(start,end,graph,heuristic):
    if x == "Không tìm thấy đường đi":
        print(x)
    elif x == start:
        print(x,end="")
    else:
        print("->",x,end="")
