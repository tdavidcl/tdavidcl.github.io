
function write_sidebar(page) {
        
    var srcsidebar = "<div id=\"sidebar-div\" class=\"wrapper\">  \
            <div class=\"section\">  \
                <div class=\"top_navbar\">  \
                    <div class=\"hamburger\">  \
                        <a href=\"#\">  \
                            <i class=\"fas fa-bars\"></i>  \
                        </a>  \
                    </div>  \
                </div>  \
            </div>  \
            <div class=\"sidebar\">  \
                <div class=\"profile\">  \
                    <img src=\"./files/profile.jpeg\" alt=\"profile_picture\">  \
                    <h3>Timothée David--Cléris</h3>  \
                    <p>PHD student</p>  \
                    <p>Astrophysics / Informatics</p>  \
                </div>  \
                <ul>  \
                    <li>  \
                        <a href=\"./index.html\"  ####rep_index>  \
                            <span class=\"icon\"><i class=\"fas fa-home\"></i></span>  \
                            <span class=\"item\">Home</span>  \
                        </a>  \
                    </li>  \
                    <li>  \
                        <a href=\"./cv.html\"  ####rep_cv>  \
                            <span class=\"icon\"><i class=\"fas fa-desktop\"></i></span>  \
                            <span class=\"item\">CV</span>  \
                        </a>  \
                    </li>  \
                    <li>  \
                        <a href=\"./publications.html\"  ####rep_publications>  \
                            <span class=\"icon\"><i class=\"fas fa-user-friends\"></i></span>  \
                            <span class=\"item\">Publications</span>  \
                        </a>  \
                    </li>  \
                    <li>  \
                        <a href=\"./research.html\"  ####rep_research>  \
                            <span class=\"icon\"><i class=\"fas fa-tachometer-alt\"></i></span>  \
                            <span class=\"item\">Research</span>  \
                        </a>  \
                    </li>  \
                    <li>  \
                        <a href=\"./posts.html\"  ####rep_posts>  \
                            <span class=\"icon\"><i class=\"fas fa-database\"></i></span>  \
                            <span class=\"item\">Posts</span>  \
                        </a>  \
                    </li>  \
                    <li>  \
                        <a href=\"./shamrock.html\"   ####rep_shamrock>  \
                            <span class=\"icon\"><i class=\"fas fa-chart-line\"></i></span>  \
                            <span class=\"item\">Shamrock code</span>  \
                        </a>  \
                    </li>  \
                    <li>  \
                        <a href=\"https://orcid.org/0000-0001-6696-7917\">  \
                            <span class=\"icon\"><i class=\"fas fa-circle\"></i></span>  \
                            <span class=\"item\">Orcid</span>  \
                        </a>  \
                    </li>  \
                </ul>  \
            </div>  \
            \
        </div>";


    if(page.match("index")){
        srcsidebar = srcsidebar.replace("####rep_index"," class=\"active\">");
    }else{
        srcsidebar = srcsidebar.replace("####rep_index","");
    }

    if(page.match("cv")){
        srcsidebar = srcsidebar.replace("####rep_cv"," class=\"active\">");
    }else{
        srcsidebar = srcsidebar.replace("####rep_cv","");
    }

    if(page.match("publications")){
        srcsidebar = srcsidebar.replace("####rep_publications"," class=\"active\">");
    }else{
        srcsidebar = srcsidebar.replace("####rep_publications","");
    }

    if(page.match("research")){
        srcsidebar = srcsidebar.replace("####rep_research"," class=\"active\">");
    }else{
        srcsidebar = srcsidebar.replace("####rep_research","");
    }

    if(page.match("posts")){
        srcsidebar = srcsidebar.replace("####rep_posts"," class=\"active\">");
    }else{
        srcsidebar = srcsidebar.replace("####rep_posts","");
    }
    
    if(page.match("shamrock")){
        srcsidebar = srcsidebar.replace("####rep_shamrock"," class=\"active\">");
    }else{
        srcsidebar = srcsidebar.replace("####rep_shamrock","");
    }

    document.writeln(srcsidebar);
}