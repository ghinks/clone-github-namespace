def keys_exists(dictionary, keys):
    keys_found = []
    nested_dict = dictionary

    for key in keys:
        try:
            nested_dict = nested_dict[key]
            keys_found.append(key)
        except KeyError:
            if len(keys_found):
                chain = ""
                for key in list(keys_found):
                    chain+=f"{key}."
            print(f"keys found were {chain}MISSING")
            return False
    return True


