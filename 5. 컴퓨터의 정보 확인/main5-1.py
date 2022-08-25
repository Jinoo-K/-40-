# pip install psutil

import psutil

cpu = psutil.cpu_freq()     # CPU의 속도 출력
print(cpu)

cpu_core = psutil.cpu_count(logical=False)      # CPU의 물리코어 수 출력
print(cpu_core)

memory = psutil.virtual_memory()        # 메모리 정보 출력
print(memory)

disk = psutil.disk_partitions()     # 디스크 정보 출력
print(disk)

net = psutil.net_io_counters()      # 네트워크로 송수신 된 데이터량 출력
print(net)