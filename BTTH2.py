# Khởi tạo dữ liệu danh sách sổ tiết kiệm ban đầu
saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")
    
    choice = input("> Nhập lựa chọn của bạn (1-7): ").strip()

    match choice:
        
        # Chức năng 1: Xem danh sách sổ tiết kiệm
        case "1":
            print()
            if len(saving_accounts) == 0:
                print("Danh sách sổ tiết kiệm hiện đang trống.")
            else:
                print("Danh sách sổ tiết kiệm:")
                for i in range(len(saving_accounts)):
                    acc = saving_accounts[i]
                    print(f"{i + 1}. Mã sổ: {acc['account_id']} | Khách hàng: {acc['customer_name']} | Số tiền gửi: {acc['balance']} | Kỳ hạn: {acc['term_months']} tháng | Lãi suất: {acc['interest_rate']}%/năm | Trạng thái: {acc['status']}")

        # Chức năng 2: Mở sổ tiết kiệm mới
        case "2":
            print()
            raw_id = input("- Nhập mã sổ tiết kiệm: ")
            new_id = raw_id.strip().upper()
            
            # Bẫy 1: Kiểm tra mã sổ trùng lặp
            is_duplicate = False
            for acc in saving_accounts:
                if acc["account_id"] == new_id:
                    is_duplicate = True
                    break
            
            if is_duplicate:
                print("[!] Mã sổ tiết kiệm đã tồn tại!")
            else:
                new_name = input("- Nhập tên khách hàng: ").strip()
                # Bẫy 2: Kiểm tra tên khách hàng
                if new_name == "":
                    print("[!] Tên khách hàng không được để trống!")
                else:
                    try:
                        # Bẫy 3: Kiểm tra tiền gửi và kỳ hạn
                        new_balance = int(input("- Nhập số tiền gửi: "))
                        new_term = int(input("- Nhập kỳ hạn gửi theo tháng: "))
                        
                        if new_balance <= 0 or new_term <= 0:
                            print("[!] Số tiền gửi hoặc kỳ hạn không hợp lệ!")
                        else:
                            try:
                                # Bẫy 4: Kiểm tra lãi suất
                                new_rate = float(input("- Nhập lãi suất năm (%): "))
                                if new_rate <= 0:
                                    print("[!] Lãi suất không hợp lệ!")
                                else:
                                    # Thêm sổ mới vào danh sách
                                    new_account = {
                                        "account_id": new_id,
                                        "customer_name": new_name,
                                        "balance": new_balance,
                                        "term_months": new_term,
                                        "interest_rate": new_rate,
                                        "status": "active"
                                    }
                                    saving_accounts.append(new_account)
                                    print(f"=> Mở sổ tiết kiệm mới {new_id} thành công!")
                            except ValueError:
                                print("[!] Lãi suất không hợp lệ!")
                    except ValueError:
                        print("[!] Số tiền gửi hoặc kỳ hạn không hợp lệ!")

        # Chức năng 3: Cập nhật thông tin sổ tiết kiệm
        case "3":
            print()
            raw_id = input("- Nhập mã sổ tiết kiệm cần cập nhật: ")
            update_id = raw_id.strip().upper()
            
            found_index = -1
            for i in range(len(saving_accounts)):
                if saving_accounts[i]["account_id"] == update_id:
                    found_index = i
                    break
            
            # Bẫy 5: Mã sổ không tồn tại
            if found_index == -1:
                print("[!] Không tìm thấy mã sổ tiết kiệm!")
            else:
                acc = saving_accounts[found_index]
                # Bẫy 6: Sổ đã tất toán
                if acc["status"] == "closed":
                    print("[!] Không thể thao tác với sổ tiết kiệm đã tất toán!")
                else:
                    upd_name = input(f"- Nhập tên khách hàng mới (hiện tại: {acc['customer_name']}): ").strip()
                    if upd_name == "":
                        print("[!] Tên khách hàng không được để trống!")
                    else:
                        try:
                            upd_balance = int(input(f"- Nhập số tiền gửi mới (hiện tại: {acc['balance']}): "))
                            upd_term = int(input(f"- Nhập kỳ hạn mới theo tháng (hiện tại: {acc['term_months']}): "))
                            
                            if upd_balance <= 0 or upd_term <= 0:
                                print("[!] Số tiền gửi hoặc kỳ hạn không hợp lệ!")
                            else:
                                try:
                                    upd_rate = float(input(f"- Nhập lãi suất năm mới (hiện tại: {acc['interest_rate']}%): "))
                                    if upd_rate <= 0:
                                        print("[!] Lãi suất không hợp lệ!")
                                    else:
                                        # Tiến hành cập nhật
                                        acc["customer_name"] = upd_name
                                        acc["balance"] = upd_balance
                                        acc["term_months"] = upd_term
                                        acc["interest_rate"] = upd_rate
                                        print("=> Cập nhật thông tin sổ tiết kiệm thành công!")
                                except ValueError:
                                    print("[!] Lãi suất không hợp lệ!")
                        except ValueError:
                            print("[!] Số tiền gửi hoặc kỳ hạn không hợp lệ!")

        # Chức năng 4: Tất toán hoặc xóa sổ tiết kiệm
        case "4":
            print()
            raw_id = input("- Nhập mã sổ tiết kiệm cần tất toán: ")
            close_id = raw_id.strip().upper()
            
            found_index = -1
            for i in range(len(saving_accounts)):
                if saving_accounts[i]["account_id"] == close_id:
                    found_index = i
                    break
            
            if found_index == -1:
                print("[!] Không tìm thấy mã sổ tiết kiệm!")
            else:
                if saving_accounts[found_index]["status"] == "closed":
                    print("[!] Sổ tiết kiệm này đã được tất toán từ trước!")
                else:
                    saving_accounts[found_index]["status"] = "closed"
                    print(f"=> Đã tất toán thành công sổ tiết kiệm {close_id}.")

        # Chức năng 5: Tính lãi dự kiến khi đến hạn
        case "5":
            print()
            raw_id = input("- Nhập mã sổ tiết kiệm cần tính lãi: ")
            calc_id = raw_id.strip().upper()
            
            found_index = -1
            for i in range(len(saving_accounts)):
                if saving_accounts[i]["account_id"] == calc_id:
                    found_index = i
                    break
            
            if found_index == -1:
                print("[!] Không tìm thấy mã sổ tiết kiệm!")
            else:
                acc = saving_accounts[found_index]
                if acc["status"] == "closed":
                    print("[!] Không thể thao tác với sổ tiết kiệm đã tất toán!")
                else:
                    interest = acc["balance"] * acc["interest_rate"] / 100 * acc["term_months"] / 12
                    total_amount = acc["balance"] + interest
                    print("--- KẾT QUẢ TÍNH LÃI DỰ KIẾN ---")
                    print(f"Tiền lãi dự kiến: {interest:,.0f} VNĐ")
                    print(f"Tổng tiền nhận khi đến hạn: {total_amount:,.0f} VNĐ")

        # Chức năng 6: Kiểm tra điều kiện rút trước hạn
        case "6":
            print()
            raw_id = input("- Nhập mã sổ tiết kiệm cần kiểm tra: ")
            check_id = raw_id.strip().upper()
            
            found_index = -1
            for i in range(len(saving_accounts)):
                if saving_accounts[i]["account_id"] == check_id:
                    found_index = i
                    break
            
            if found_index == -1:
                print("[!] Không tìm thấy mã sổ tiết kiệm!")
            else:
                acc = saving_accounts[found_index]
                if acc["status"] == "closed":
                    print("[!] Không thể thao tác với sổ tiết kiệm đã tất toán!")
                else:
                    try:
                        actual_months = int(input("- Nhập số tháng thực gửi: "))
                        # Bẫy 7: Số tháng thực gửi không hợp lệ
                        if actual_months <= 0:
                            print("[!] Số tháng thực gửi không hợp lệ!")
                        else:
                            # Kiểm tra điều kiện tính lãi
                            if actual_months < acc["term_months"]:
                                applied_rate = 0.5
                                print("=> Khách hàng rút trước hạn. Áp dụng lãi suất không kỳ hạn: 0.5%/năm.")
                            else:
                                applied_rate = acc["interest_rate"]
                                print(f"=> Khách hàng đủ kỳ hạn. Áp dụng lãi suất ban đầu: {applied_rate}%/năm.")
                            
                            # Tính toán tiền thực nhận
                            actual_interest = acc["balance"] * applied_rate / 100 * actual_months / 12
                            actual_total = acc["balance"] + actual_interest
                            print(f"Tiền lãi thực nhận: {actual_interest:,.0f} VNĐ")
                            print(f"Tổng tiền thực nhận: {actual_total:,.0f} VNĐ")
                    except ValueError:
                        print("[!] Số tháng thực gửi không hợp lệ!")

        # Chức năng 7: Thoát chương trình
        case "7":
            print("\nThoát chương trình. Cảm ơn bạn đã sử dụng hệ thống TechBank!")
            break

        # Bẫy 8: Menu Validation
        case _:
            print("\n[!] Lựa chọn không hợp lệ, vui lòng nhập lại!")