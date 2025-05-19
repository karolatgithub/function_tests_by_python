from loguru import logger

logger.remove(0)
logger.add("function_tests_by_python.log",
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} {process} {level} {file} {function}({line}) {message}")
