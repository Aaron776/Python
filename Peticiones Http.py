import requests
def peticionesHttp():
    if __name__ == '__main__':
        url="https://jsonplaceholder.typicode.com/comments"
        r=requests.get(url)
        print(r)
        if r.status_code==200:
            data=r.json()
            print(data)
            for item in data:
                print(item["postId"])


peticionesHttp()