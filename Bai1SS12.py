# Phân tích 
# Đề bài yêu cầu chúng ta cần tạo 1 menu gồm 5 chức năng 
# Để làm menu này thì chúng ta dùng 1 vòng lặp while và nó kết thúc khi người dùng ấn 5 để break ra khỏi vòng lặp
# Chức năng đầu tiên là xem chi tiết giỏ hàng và tính tổng tiền 
# Thì đầu tiên chúng ta cần duyệt vòng for để in ra tất cả các sản phẩm, tổng số lượng và tổng số tiền
# Ở ngoài vòng lặp thì chúng ta cần tạo 1 biến để đếm số lượng và tiền, sau đó mỗi vòng for thì chúng ta cộng dồn lên và in ra theo đúng định dạng 
# Chức năng thứ 2 là thêm sản phẩm mới, nếu sản phẩm đã tồn tại thì cộng thêm số lượng cho nó, còn nếu không có sản phẩm mà người dùng nhập thì in ra thông báo 
# Chức năng thứ 3 là cập nhật số lượng, yêu cầu người dùng nhập 1 mã sản phẩm 
# Từ đó duyệt qua vòng for xem nó có trong giỏ hàng không, nếu không có thì in ra thông báo, còn nếu có thì tiến hành cập nhật cộng thêm số lượng vừa nhập 
# Và chức năng cuối cùng là xóa sản phẩm, yêu cầu người dùng nhập mã sản phẩm, từ đó duyệt vòng for xem có sản phẩm trong giỏ hàng hay không 
# Nếu không có thì in ra thông báo còn nếu có thì tiến hành xóa sản phẩm khỏi giỏ 
# Nên nhớ check các Edge Cases đề bài đã yêu cầu 

# Viết code 
cart_items = [
    {
        "id": "P001", 
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
        "id": "P002",
        "name": "Op lung Silicon", 
        "number": 2, 
        "price": 150000
    }
]
while True:
    choose = input("""==========================================
    SHOPEE CART MANAGEMENT SYSTEM
==========================================
1. Xem chi tiết giỏ hàng và tính tổng tiền
2. Thêm sản phẩm mới / Cộng dồn số lượng
3. Cập nhật số lượng của một sản phẩm
4. Xóa sản phẩm khỏi giỏ hàng
5. Thoát chương trình
==========================================
Mời bạn chọn chức năng (1-5): """)
    if choose == "1":
        quantity_product = 0
        total_price = 0
        print("--- CHI TIẾT GIỎ HÀNG ---")
        print(f'{"STT": <5} | {"Mã SP": <5} | {"Tên sản phẩm": <20} | {"SL": <5} | {"Đơn giá": <10} | {"Thành tiền": <10}')
        for index, item in enumerate(cart_items):
            print(f'{index+1: <5} | {item.get("id"): <5} | {item.get("name"): <20} | {item.get("number"): <5} | {item.get("price"): <10} | {item.get("number")*item.get("price"): <10}')
            quantity_product += item.get("number")
            total_price += item.get("number")*item.get("price")
        print(f"=> Tổng số lượng sản phẩm trong giỏ: {quantity_product}")
        print(f"=> Tổng tiền thanh toán: {total_price}")
        print()
    elif choose == "2":
        add_item_quantity = input("Nhập mã sản phẩm cần thêm: ")
        valid = True 
        for index, item in enumerate(cart_items):
            if item.get("id") == add_item_quantity:
                quantity_add = int(input("Nhập số lượng sản phẩm cần thêm: "))
                if quantity_add <= 0:
                    valid = False
                    print("Số lượng không hợp lệ")
                    break
                valid = False
                item["number"] += quantity_add
                print("Thêm sản phẩm thành công")
                break 
        if valid == True:
            new_name_item = input("Nhập tên sản phẩm mới: ")
            new_quantity = int(input("Nhập số lượng sản phẩm mới: "))
            if new_quantity <= 0:
                print("Số lượng không hợp lệ")
                break
            new_price = int(input("Nhập giá của sản phẩm mới: "))
            if new_price < 0:
                print("Giá sản phẩm không hợp lệ")
                break
            new_item = {
                "id": add_item_quantity,
                "name": new_name_item,
                "number": new_quantity,
                "price": new_price
            }
            cart_items.append(new_item)
            print("Thêm sản phẩm thành công")
        print()
    elif choose == "3":
        update_item_quantity = input("Nhập mã sản phẩm cần cập nhật: ")
        valid = True 
        for index, item in enumerate(cart_items):
            if item.get("id") == update_item_quantity:
                quantity_update = int(input("Nhập số lượng sản phẩm cần sửa: "))
                if quantity_update <= 0:
                    valid = False
                    print("Số lượng không hợp lệ")
                    break
                valid = False
                item["number"] = quantity_update
                print("Thêm sản phẩm thành công")
                break 
        if valid == True:
            print("Không tìm thấy mã sản phẩm")
        print()
    elif choose == "4":
        delete_item_quantity = input("Nhập mã sản phẩm cần xóa: ")
        valid = True 
        for index, item in enumerate(cart_items):
            if item.get("id") == delete_item_quantity:
                cart_items.pop(index)
                valid = False
                print("Xóa sản phẩm thành công")
                break 
        if valid == True:
            print("Không tìm thấy mã sản phẩm")
        print()
    elif choose == "5":
        print("Chương trình kết thúc")
    else:
        print("Lựa chọn không hợp lệ")