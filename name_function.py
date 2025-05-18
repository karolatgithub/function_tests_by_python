def get_formattes_name(*names):
    """ Generuje elegancko sformatowane pelna nazwe uzytkownika """
    if names and len(names)>0:
        ret=''
        i=0
        for name in names:
            if name and name.strip():
                i+=1
                if i>1:
                    ret+=' '
                ret+=name.title()
        if ret:
            return ret;
    return None
