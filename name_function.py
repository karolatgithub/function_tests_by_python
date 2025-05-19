from loguru import logger

def get_formattes_name(*names):
    """ Generuje elegancko sformatowane pelna nazwe uzytkownika """
    logger.debug("names={}", names)
    ret=''
    try:
        if names and len(names)>0:
            i=0
            for name in names:
                if name and name.strip():
                    i+=1
                    if i>1:
                        ret+=' '
                    ret+=name.title()
        if not ret:
            ret=None;
    finally:
        logger.debug("ret={}", ret)
    return ret
