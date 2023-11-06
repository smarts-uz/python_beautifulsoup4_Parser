import logging
import os
from datetime import datetime
import shutil

module_name = os.path.splitext(os.path.basename(__file__))[0]

logger2 = logging.getLogger(module_name)
logger2.setLevel(logging.INFO)

# настройка обработчика и форматировщика для logger2
handler2 = logging.FileHandler(f"{module_name}.log", mode='a')
formatter2 = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# добавление форматировщика к обработчику
handler2.setFormatter(formatter2)
# добавление обработчика к логгеру
logger2.addHandler(handler2)
logger2.info(f"Running module {module_name}...")
# Returns the current local date
year = datetime.now().year
month = datetime.now().month
day = datetime.now().day
current_path = os.path.dirname(os.path.realpath(__file__))
logger_path = f"0{year}/{month}/{day}/"
if not os.path.exists(logger_path):
    os.makedirs(logger_path)
# if not os.path.exists(f"{logger_path}/{module_name}.log"):
    shutil.move(f"{current_path}\\{module_name}.log", logger_path)

errors = (RuntimeError, TypeError, NameError,
          SyntaxError,Exception,ValueError,
          KeyboardInterrupt)
try:
    x = int(input("Please enter a number: "))
    logger2.info("Successful run")
except errors as err:
    logger2.exception("Some kind of error, check log file")





#save to specific folder
import logging
from datetime import datetime

# Specify log file name and path
log_file = '/path/to/logs/log_{}'.format(datetime.now().strftime('%Y%m%d'))

# Configure logging
logging.basicConfig(filename=log_file,
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Example log messages
logging.info('This message will be logged to the file')
logging.error('This is an error message')