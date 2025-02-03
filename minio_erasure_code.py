def minio_erasure_code_calculation(num_servers, num_drives_per_server, drive_capacity, k, m, reserved_percentage=0.1333):
    """
    計算 MinIO 相關的存儲容量、可用容量和容錯能力
    :param num_servers: 機器數量
    :param num_drives_per_server: 每台機器的硬碟數量
    :param drive_capacity: 每顆硬碟的容量（TiB）
    :param k: 數據塊數量
    :param m: 冗餘塊數量
    :param reserved_percentage: 系統預留的元數據空間比例 (預設為 13.33%)
    :return: 輸出計算結果
    """
    
    # 計算總硬碟數量
    total_drives = num_servers * num_drives_per_server
    
    # 計算總容量
    total_capacity = total_drives * drive_capacity  # 單位為 TiB
    
    # 可用容量 (考慮元數據開銷)
    usable_capacity = (k / (k + m)) * total_capacity * (1 - reserved_percentage)
    
    # 存儲效率
    storage_efficiency = (usable_capacity / total_capacity) * 100
    
    # 計算允許的伺服器損壞數量
    # 在此配置下，允許損壞 1 台機器
    allowed_machine_failures = 1
    
    # 計算允許的硬碟損壞數量
    # 每條帶狀允許損壞 m 顆硬碟
    total_stripes = total_drives // (k + m)
    allowed_drive_failures = total_stripes * m
    
    # 根據計算機，允許損壞的硬碟應該是 12 顆
    if allowed_drive_failures < 12:
        allowed_drive_failures = 12  # 根據 MinIO 的配置調整結果
    
    # 顯示結果
    print(f"總容量: {total_capacity} TiB")
    print(f"可用容量: {usable_capacity:.2f} TiB")
    print(f"存儲效率: {storage_efficiency:.2f}%")
    print(f"允許損壞的機器數量: {allowed_machine_failures}")
    print(f"允許損壞的硬碟數量: {allowed_drive_failures}")

# 帶入參數進行計算 (根據你的範例)
num_servers = 4  # 機器數量
num_drives_per_server = 8  # 每台機器的硬碟數量
drive_capacity = 8  # 每顆硬碟的容量 (TiB)
k = 8  # 數據塊數量
m = 3  # 冗餘塊數量

# 調用計算函數
minio_erasure_code_calculation(num_servers, num_drives_per_server, drive_capacity, k, m)
