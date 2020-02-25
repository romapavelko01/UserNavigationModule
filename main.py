"""
Module for helping the user navigate through the
json object.
"""
import urllib.request
import urllib.parse
import urllib.error
import json
import ssl
import twurl


# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE


def get_dict(inp_acc):
    """
    (str) -> (dict)
    Returns a dictionary out of a json object.
    """
    url_main = twurl.augment(TWITTER_URL,
                             {'screen_name': inp_acc, 'count': '100'})
    # print('Retrieving', url)
    connection_var = urllib.request.urlopen(url_main, context=CTX)
    data = connection_var.read().decode()

    js_open = json.loads(data)
    # dr = json.dumps(js_open, indent=2)
    return js_open


def collect_acc():
    """
    (None) -> (str)
    Collects account name from a user.
    """
    res_acc = input("Enter an account: ")
    return res_acc


def info_main():
    """
    (None) -> (str)
    Returns a helping information to the user.
    """
    help_info = """\nType 'help' to get help information.\n
        In order to go one step up in the json object structure,
        type 'back'.\n
        In order to get the keys of a dictionary, type 'keys'.\n
        In order to quit the process, type 'exit'.
        """
    print(help_info)


def main_func():
    """
    (None) -> (None)
    Main function. Navigates over a dictionary received
    as a twitter'sjson object.
    """
    navig_acct = collect_acc()
    navig_dict = get_dict(navig_acct)
    th_mess = "Thanks for choosing our service!"
    ans_lst = ["y", "yeah", "yes"]
    oper_lst = []
    start_inp = input("Do you want to navigate?[yes/no] ")
    list_strs = ["exit", "back", "help", "keys"]
    if start_inp in ans_lst:
        oper_lst.append(navig_dict)
        info_main()
        while True:
            try:
                data = oper_lst[-1]
                try:
                    if isinstance(data, list):
                        if len(data) == 0:
                            new_str = input("Empty list. Want to return back?")
                            if new_str in ans_lst:
                                oper_lst = oper_lst[:-1]
                            elif new_str == "help":
                                info_main()
                            elif new_str == "exit":
                                print(th_mess)
                                break
                        else:
                            len_h = str(len(oper_lst[-1]))
                            new_str = input("What element out of " +
                                            len_h +
                                            "would you like to check?")
                            if new_str not in list_strs:
                                data = oper_lst[-1][int(new_str) - 1]
                                oper_lst.append(data)
                            elif new_str == "back":
                                oper_lst = oper_lst[:-1]
                            elif new_str == "help":
                                info_main()
                            elif new_str == "exit":
                                print(th_mess)
                                break
                    elif isinstance(data, dict):
                        data_keys = [key for key in data.keys()]
                        print('    '.join(data_keys))
                        new_str = input("What key would you like to check?")
                        list_strs = ["exit", "back", "help", "keys"]
                        if new_str not in list_strs:
                            data = data[new_str]
                            oper_lst.append(data)
                        elif new_str == "back":
                            oper_lst = oper_lst[:-1]
                        elif new_str == "help":
                            info_main()
                        elif new_str == "exit":
                            print(th_mess)
                            break
                    else:
                        new_str = input("Would you like to see the element?")
                        if new_str not in list_strs and new_str in ans_lst:
                            print(data)
                        elif new_str == "back":
                            oper_lst = oper_lst[:-1]
                        elif new_str == "help":
                            info_main()
                        elif new_str == "exit":
                            print(th_mess)
                            break
                        new_str = input("Want to return back? ")
                        if new_str in ans_lst:
                            oper_lst = oper_lst[:-1]
                        elif new_str == "help":
                            info_main()
                        elif new_str == "exit":
                            print(th_mess)
                            break
                except (KeyError, IndexError):
                    print("Please, make sure you have given valid input.")
            except IndexError:
                print("You are out of elements")
                print(th_mess)
                break

    else:
        print(th_mess)


if __name__ == "__main__":
    main_func()
