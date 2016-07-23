
def remove_dollar_sign(s):
    OLD_OID = "$oid"
    NEW_OID = "oid"
    return s.replace(OLD_OID, NEW_OID)