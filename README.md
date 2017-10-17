
[![Build Status](https://travis-ci.org/trallard/Modules-template.svg?branch=master)](https://travis-ci.org/trallard/Modules-template)

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Modules template](#modules-template)
- [About the website](#about-the-website)
	- [Configuration and setup](#configuration-and-setup)
		- [Site settings](#site-settings)
- [Site settings](#site-settings)
		- [Generating the pages for the lecture modules or projects](#generating-the-pages-for-the-lecture-modules-or-projects)
		- [Theme colors](#theme-colors)
		- [Layouts](#layouts)
- [How to use Jekyll to build this site](#how-to-use-jekyll-to-build-this-site)
	- [Editing pages online with GitHub](#editing-pages-online-with-github)
	- [Working locally](#working-locally)
- [Generating posts/pages from Jupyter notebooks](#generating-postspages-from-jupyter-notebooks)

<!-- /TOC -->

# Modules template
This Jekyll template is intended to be used to by academics and researchers wanting to generate a _literate programming_ and _hassle free_ static website.
This can be used as a scientific blog template or as a webpage to host/display projects information, scientific outputs or as a site for academic modules.

It provides validation of Jupyter notebooks as well as automatic rendering, support for Latex via MathJax, code highlighting, and  support for [reveal.js](https://github.com/hakimel/reveal.js/) slides.
On top of the various Jekyll capabilities.

# About the website
This website is hosted as a GitHub page (github-pages). In short, it is built statically from Markdown source files and/or Jupyter notebooks using [Jekyll](http://jekyllrb.com). To update a page, just modify the corresponding source and push. The website will then be built and deployed using gh-pages.

This site uses the [Bootstrap framework](http://getbootstrap.com) along with [Material Design for Boostrap](https://mdbootstrap.com/material-design-for-bootstrap/).

Below you will find a description of the various files and directories within this repository:
- `_config.yml`: main configuration file, this **must** set accordingly for your own website/blog
- `Gemfile`: list of the various gems used in the website
- `index.md`: landing page content
- `_includes/*`: diverse components of the website, reusable html components
- `_layouts/*`: local style files
- `_sass/*`: css/sass style sheets
- `js/*:` various JavaScript scripts used in this website
- `pages/*`: pages markdown files
- `posts/*`: containing folder for posts
- `images/*`: images used across the website
- `notebooks/*`: this contains both the original Jupyter notebooks and the converted versions for the website
- `basic_style.scss`: this stylesheet contains the default colour scheme and fonts used in this site

## Configuration and setup
The main configuration for the Jekyll website is declared in the `config.yml` file. Such a file contains the site specific variables, which are accessed at various points within the website.

### Site settings

```yaml
# Site settings
title: Module template
description: Lorem ipsum dolor sit amet understanding yourself in the universe tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
baseurl: "/Module_template"
url: "" # the base hostname & protocol for your site
```

These are the basic configuration setups for the site, this **must** be set accordingly.

The title and description are used in the landing page as well as to generate canonical urls for the website.

The variable
`baseurl` is the name of your repository which is **/Module_template** by default. If you setup your instance using another method than forking like duplication/mirroring, or you changed the name of your repository, you will need to change this accordingly.


If you have trouble understanding what the `baseurl` and `url` variables are visit <https://byparker.com/blog/2014/clearing-up-confusion-around-baseurl/>.

### Generating the pages for the lecture modules or projects

Each of your lecture modules/projects should be declared as a collection in the `_config.yml` file so that Jekyll knows where to read:
~~~ yaml
collections:
  - module1
    output: true
  - module2
    output: true
~~~
(leaving the output as `true` ensures the generation of an html page for each of the files contained in the directory)

You will then need to generate a folder for each module (using the exact same name you used in the configuration file) adding an underscore to the folder's name e.g. `_module1`

These are automatically added to the landing page in the form of a card as well as to the main navigation menu on the website. The urls and redirects to the files within the collections folders are generated automatically and added to the front page of each module/project.


### Theme colors
The color scheme follows [Google's material design](https://material.io/guidelines/style/color.html#color-color-palette) style and is specified in terms of a primary and a secondary color, which can be modified in the `basic_style.scss` file in the root directory.

If you want to modify the color scheme or the fonts used you only need to modify this file and they will be automatically updated as the site is built.

 Alternatively, a guide for the MDB colour aliases can be found [here](https://mdbootstrap.com/css/colors/).

 Note that depending on color scheme you use for your website you might need to change the color of some components to ensure appropriate contrast and readability.

### Layouts
This template includes basic layouts for posts, pages, and presentations intended for the casual user.
Advanced layouts are included for the coding scientist providing a robust publication framework.

Basic templates containing the required `.yml` front matter can be located in the `templates` directory.

All of your content **must** have a Title and a layout. The rest of the variables are optional.

In the case of pages generated using the module template, the subtitle variable will be displayed along with the title in the landing page as a short description of the lecture module/project.


### Adding a logo
If you need to add a logo to your website you can do it by saving the image to the 'images' folder and modify the name of the image in the `config.yml` file:
```yaml
logo: "./images/logo-sheffield.png"
```

# How to use Jekyll to build this site

## Editing pages online with GitHub

You can edit any page by following the "Edit this page" link in the Quick links nav bar. Alternatively, you can directly navigate to the corresponding .md (Markdown) file in GitHub.

This will drop you in GitHub's file editing interface, where you can modify the source code, preview it, and save your changes, by giving a short description of what you modified. If you have write access to the repository (hint: you do), your modifications will be published right-away. If you do not have right access, you will be asked to fork the repository and make a pull request.

Most of the pages are written in Markdown, which is a textual format for generating formatted text. Markdown syntax is very intuitive, you can get a quick review here or here.

CAVEATS: The Markdown engine used by this site is Kramdown. Its syntax definitions are slightly different form GitHub Flavored Markdown, thus the preview feature in GitHub might not render source as in the final result.

Other reasons why GitHub's preview may not correspond to the final results are:

- Use of Liquid templates in the source. This is seldom used, but some pages use them to access site-wide configuration variables.
- Use of special purpose markup, HTML, and scripts, such as mathematical excerpts written in MathJax.


## Working locally

If you want to do more than the occasional editing, you'll soon
realise GitHub's editor and preview are too limited. It's better to
work locally on your computer.

All you need to work locally is a [Git client](http://git-scm.com/).
[Clone the repository](https://help.github.com/articles/fork-a-repo/#step-2-create-a-local-clone-of-your-fork)
and start coding right away.

At some point, you will need to preview your work, but pushing to
GitHub each time you want to preview is clumsy.  😕
Your best option is to
[install Jekyll and the required dependencies](https://help.github.com/articles/using-jekyll-with-pages/#installing-jekyll)
on your machine. It is recommended to install the
[GitHub pages gem](https://github.com/github/pages-gem) which provides
you with the exact same versions used by GitHub to compile your site. By not doing so you might risk your website not building properly when being pushed to your GitHub repository.

If you already have Ruby, the install part should be as easy as

~~~
gem install github-pages -V
~~~

Note that you will need Ruby headers (`ruby-dev` package on Ubuntu) in
order to compile C dependencies.

On OS X, you can just type `sudo gem install github-pages -V`.

Now you can `cd` into your local clone of the repository and launch
the compilation by

~~~
jekyll serve -w -b
~~~

Your site will be generated in a `_site` sub-directory, and served
live at <http://localhost:4000/>. Any changes to the sources will
trigger an automatic recompilation!

# Generating posts/pages from Jupyter notebooks

The main content of this website is generated from [Jupyter notebooks](http://jupyter.org).  The notebooks are converted to .md files using [nbconvert](https://github.com/jupyter/nbconvert) and a custom generated python script and jinja template (jekyll.py and jekyll.tpl).  For more information on using nbconvert and custom generated templates visit https://github.com/jupyter/nbconvert

All the Jupyter notebooks used to generate this site can be found in the [Notebooks directory](https://github.com/trallard/BAD_days/tree/gh-pages/notebooks).

The conversion from `*.ipynb` is done via the `jekyll.py` script. This can be used to convert all the notebooks within the notebooks directory (you can change the location of the notebooks directly on the script), or one at a time.

The usage is as follows:

* For one notebook at a time

~~~
jupyter nbconvert --config jekyll.py <notebook>
~~~

* For all the notebooks contained within a given directory

~~~
jupyter nbconvert --config jekyll.py
~~~

The custom converter creates a `*.md` file by extending the default `markdown.tpl` template from nbconvert. This adds the required jekyll front matter and ensures consistency between the static version of the notebook and the website.

In order for the generated `*.md` files to be correctly rendered in Jekyll, some scoped text needs to be parsed this is done using the `replace.py` script.

~~~
python replace.py
~~~

If the notebooks have images (e.g. plots) these are saved as `.png` files within the notebook directory. The path can be modified directly within the script.
