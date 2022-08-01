import glob

src_posts = ""
f = open("src/template_post.html",'r')
src_posts += f.read()
f.close()



src_posts_list = ""
f = open("src/template_posts_list.html",'r')
src_posts_list += f.read()
f.close()


article_name = []
article_date = []
article_html_path = []
articles_html = []
article_desc = []

for fpath in glob.glob("src/posts/*.html"):
    print("gen ->",fpath)

    f = open(fpath,'r')
    html_src = f.read()
    f.close()

    article_html_path.append((fpath).replace("src", "build"))

    articles_html.append(html_src)

    article_name.append(html_src.splitlines()[0])
    article_date.append(html_src.splitlines()[1])
    article_desc.append(html_src.splitlines()[3])



html_lst = ""

for (name,dt,desc,fname,a) in zip(article_name,article_date,article_desc,article_html_path,articles_html):
    
    print("writing : ",name,"to",fname)

    html_lst += ("<a href=\"./" + fname + "\">"+name+"</a>"+dt)
    html_lst += "<br/>"
    html_lst += desc
    html_lst += "<hr/>"


    html = "\n"
    html += "<div class=\"post\">\n\n"
    html += a
    html += "\n</div>\n\n"


    html = src_posts.replace("###ctn", html)

    
    f = open(fname,'w')
    f.write(html)
    f.close()

f = open("posts.html",'w')
f.write(src_posts_list.replace("###ctn", html_lst))
f.close()