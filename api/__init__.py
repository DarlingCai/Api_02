from common.log_config import init_log_config
from config import BASE_DIR

# 配置日志的调用
print('==============日志调用========================')
init_log_config(BASE_DIR + '/log/ihrm.log')