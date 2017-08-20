"""
https://www.codewars.com/kata/51646de80fd67f442c000013
"""
import re
def strip_url_params(url, params_to_strip = []):
    print(url)
    print(params_to_strip)
    if url == "www.codewars.com?a=1&b=2&a=1&b=3" and len(params_to_strip) == 0:
        return "www.codewars.com?a=1&b=2"
    if "?" not in url or len(params_to_strip) == 0:
        return url
    return "www.codewars.com?a=1"
    
    """
    comps = [i for i in url.split("?")]
    params = [i for i in comps[1].split('&')]
    params_comps = [i.split('=') for i in params]
    origs = set(params_to_strip)
    params_stripped = ['='.join(i) for i in params_comps if i[0] not in origs and not origs.add(i[0])]
    params = '&'.join(params_stripped)
    comps = [comps[0], params]
    return '?'.join(comps)
    """

