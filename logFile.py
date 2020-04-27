import logging

logging.basicConfig(filename="C:\\Users\\P2938214\\Documents\\Chemal\\QStack\\logFiles\\test.log",
    format='%(asctime)s: %(levelname)s: %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.DEBUG
)

#logger=logging.getLogger()
#logger.setLevel(logging.DEBUG)

#logging.debug("This is a debug message")
#logging.info("This is an info message")
#logging.warning("This is a warning message")
#logging.error("This is an error message")
#logging.critical("This is a critical message")

def logGitResponse(responseCode):
    logging.warning("The response was: " + responseCode)