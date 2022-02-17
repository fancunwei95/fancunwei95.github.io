---
layout: splash
permalink: /blogs/

title: "Cunwei's Blogs"
excerpt: "Aim for the moon. If you miss, you may hit a star."
classes: wide
author_profile: false

header:
  overlay_image: /assets/images/blog.jpg
  overlay_height: "800px"
  overlay_padding: "7em 0em"

feature_row:
  - image_path: /assets/images/techBlog.jpg
    alt: "Tech"
    title: "The Technical Nerds"
    excerpt: "If facts don’t fit the theory, change the facts."
    url: "/tech/"
  - image_path: /assets/images/lifeBlog_crop.jpg
    alt: "Life"
    title: "The Laughs and the Tears"
    excerpt: "Rocks in my path? I keep them all. With them I shall build my castle."
    url: "/life/"
---


<br/>

# Here is a glimpse of my daily experience
<br/> 

{% include feature_row %}



<h3 class="arhive__subtitle">Recent Posts</h3>
{% if paginator %}
  {% assign posts = paginator.posts %}
{% else %}
  {% assign posts = site.posts %}
{% endif %}


{% assign entries_layout = 'list' %}
<div class="entries-{{ entries_layout }}">
  {% for post in posts %}
    {% include archive-single.html type=entries_layout %}
  {% endfor %}
</div>

{% include paginator.html %}

