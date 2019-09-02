import sys
from raygun4py import raygunprovider

def handle_exception(exc_type, exc_value, exc_traceback):
  cl = raygunprovider.RaygunSender("k9topkdx3xKf7LT3IH6fNw")
  cl.send_exception(exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception
