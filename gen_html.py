import glob
import os
import re



for fpath in glob.glob("build/posts/*.html"):
    os.system("rm "+fpath)

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


for fpath in glob.glob("src/posts/*.md"):
    os.system("pandoc "+fpath+" -t html --no-highlight -o "+fpath+".html")

for fpath in glob.glob("src/posts/*.html"):
    print("gen ->",fpath)

    f = open(fpath,'r')
    html_src = f.read()
    f.close()

    html_src_splt = html_src.splitlines()

    


    name = html_src[html_src.find(">")+1:html_src.find("</h1>")].replace("\n", " ")
    html_src = html_src[html_src.find("</h1>")+5:]

    date = html_src[html_src.find(">")+1:html_src.find("</p>")].replace("\n", " ")
    html_src = html_src[html_src.find("</p>")+4:]

    desc = html_src[html_src.find(">")+1:html_src.find("</p>")].replace("\n", " ")
    html_src = html_src[html_src.find("</p>")+4:]


    tmp_html_src = ""

    name = "<h1 class=\"post-title\">" +name+"</h1>"
    date = "<h4 class=\"post-date\">" +date+"</h4>"
    desc = "<h5 class=\"post-desc\">" +desc+"</h5>"

    print(name)
    print(date)
    print(desc)

    tmp_html_src += name + "\n"
    tmp_html_src += date + "\n<br/>\n"
    tmp_html_src += desc + "\n<br/><hr/><br/>\n"

    
    html_src = tmp_html_src + html_src


    article_html_path.append((fpath).replace("src", "build"))

    articles_html.append(html_src)

    article_name.append(name)
    article_date.append(date)
    article_desc.append(desc)



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

    
    f = open(fname,'x')
    f.write(html)
    f.close()

f = open("posts.html",'w')
f.write(src_posts_list.replace("###ctn", html_lst))
f.close()

for fpath in glob.glob("src/posts/*.html"):
    os.system("rm "+fpath)
