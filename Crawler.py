#A R A N E A E
# WEB CRAWLER
#crawler 
def isStopWord(word):
    if len(word)<=3:
        return true
    stop_word_List=[]
    
def getPage(url):
    
    return page
def getUrlList(page):
    match_str='<a href="'
    url_pos_strt=page.find(match_str)
    new_url_list=[]
    while(url_pos_strt):
    			url_pos_end=page.find('"',len(match_str)+1)
       new_url_list.add(page[url_pos_strt:url_pos_end+1])
       url_pos_strt=page.find(match_str,url_pos_end)
			return new_url_list
def filterUrlList(new_url_list,crawled_url_list,url_list):
    for curr_url in new_url_list:
        if curr_url not in crawled_url_list:
            if curr_url not in url_list:
                url_list.add(curr_url)
            
    return
def run(seed_page):
    curr_page=seed_page
    url_list=[]
    crawled_url_list=[]
    control_counter=300
    while control_counter:
        try:
            new_url_list=getUrlList(curr_page)
            filterUrlList(new_url_list,crawled_url_list,url_list)    
            #now we have the filtered url list:url_list
            curr_url=url_list[0]
            url_list.remove(curr_url)
            curr_page=getPage(curr_url)
            control_counter-=1
        except E:
            print E
            break
