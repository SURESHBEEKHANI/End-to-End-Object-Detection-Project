import sys  # Importing the sys module for system-specific parameters and functions

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Fetching exception information using sys.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename  # Getting the filename where the exception occurred

    # Constructing the error message with filename, line number, and error description
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message  # Returning the formatted error message


class bhdException(Exception):
    def __init__(self, error_message, error_detail):
        """
        :param error_message: error message in string format
        :param error_detail: details of the error (expected to be an instance of sys)
        """
        super().__init__(error_message)  # Calling the parent constructor with the error message

        # Generating detailed error message using the provided error_message_detail function
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message  # Returning the detailed error message as a string
