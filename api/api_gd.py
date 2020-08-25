from requests import post


def api_gd(address, city=None):
    """获取地址详细信息"""
    url = 'https://restapi.amap.com/geocode/geo?parameters'
    data = {
        'key': 'cf4ef08a9d3771617dd2bd6db345c990',
        'address': address,
        'city': city
    }
    r = post(url, data)
    return r.json()


if __name__ == '__main__':
    r = api_gd('北京市海淀区上地街道金隅嘉华大厦', city='010')
    print(r)

