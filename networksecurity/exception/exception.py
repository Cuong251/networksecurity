import sys
import traceback
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message

        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

        super().__init__(self.__str__())

    def __str__(self):
        return (
            f"Error occurred in python script [{self.file_name}] "
            f"at line number [{self.lineno}]: {self.error_message}"
        )

# Test block
if __name__ == '__main__':
    try:
        logger.logging.info("Enter the try block")
        a = 1 / 0
        print("This will not be printed", a)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
