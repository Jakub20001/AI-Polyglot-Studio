import logging
from datetime import datetime
from pathlib import Path

log_dir = Path("logs")
log_dir.mkdir(exist_ok = True)

logging.basicConfig(
    filename=log_dir / "user_activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_user_action(user_id: int, action: str, details: str = ""):
    """ 
    Logs user action to a log file.
    
    :param user_id: ID of the user
    :param action: Name of action (for example. "LOGIN", "QUIZ_ATTEMPT")
    :param details: Additional informations (for example. quiz result, langugage, etc.)
    """
    message = f"User {user_id} performed {action}. Details: {details}"
    logging.info(message)
    
def log_system_event(event: str, level: str = "INFO"):
    """
    Logs a system event, such as a server error or backend operation. 
    
    :param event: Description of the event
    :param level: Level of log (INFO, WARNING, ERROR)
    """
    level = level.upper()
    if level == "ERROR":
        logging.error(event)
    elif level == "WARNING":
        logging.warning(event)
    else:
        logging.info(event)
        

def get_current_timestamp() -> str:
    return datetime.utcnow().isoformat()
