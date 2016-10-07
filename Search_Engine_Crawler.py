def get_page(url):
    try:
        import urllib.request
        return str(urllib.request.urlopen(url).read())
    except:
        return "error"


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def get_all_links(page): 
    links = [] 
    while True: 
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:] 
        else: 
            break 
    return links


def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def crawl_web(seed): #1 
    tocrawl = [seed] 
    crawled = [] 
    index = [] 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled: 
            content = get_page(page) 
            add_page_to_index(index, page, content) 
            union(tocrawl, get_all_links(content)) 
            crawled.append(page) 
    return index 

def add_page_to_index(index, url, content): 
    words = content.split() 
    for word in words: 
        add_to_index(index, word, url) 

def add_to_index(index, keyword, url): 
    for entry in index: 
        if entry[0] == keyword: 
            entry[1].append(url) 
            return 
    # not found, add new keyword to index 
    index.append([keyword, [url]]) 

def lookup(index, keyword): 
    s=0
    for e in keyword:
	    s+=ord(e)
    bucket = s % len(index)
    l = index[bucket]
    for entry in l : 
        if entry[0] == keyword: 
            return entry[1] 
    return None

def empty_buckets(size):
    i=0
    table=[]
    while i<size:
        table.append([])
        i=i+1
    return table

def add_to_table(result,size_of_table):
    table = empty_buckets(size_of_table)
    for list in result:
        s=0
        for e in list:
            for ee in e:
                s+=ord(ee)
            break
        bucket = s % len(table)
        table[bucket].append(list)
    return table


result = crawl_web('https://www.udacity.com/cs101x/index.html')
index = add_to_table(result , 10)
#print(result)
#print("-----------------------------------------------------")
print(lookup(index, 'test'))














